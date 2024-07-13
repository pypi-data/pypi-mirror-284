import React, { useState, useCallback, useEffect } from 'react';
import ReactFlow, {
  MiniMap,
  Background,
  Node,
  Edge,
  applyEdgeChanges,
  applyNodeChanges,
  MarkerType,
  Connection,
  ReactFlowInstance,
  NodeChange,
  EdgeChange,
  getConnectedEdges
} from 'reactflow';

import PullingNode, { PullingNodeData } from './pulling/PullingNode';
import SystemNode, { SystemNodeData } from './SystemNode';
import {
  ConnectionEdge,
  ConnEdgeData,
  PullEdgeData,
  PullingEdge
} from './MovingLabelEdge';
import CustomControls from './CustomControls';

import { connSysPortInfos, BaseFlowProps } from './SystemFlowProvider';
import { kwargsPropsType } from './KwargsPopUp';
import {
  systemType,
  connectionType,
  systemClassType,
  pullingType,
  pullingPortInfos,
  portVariableType,
  sysPullType,
  ClientPosition
} from '../../tools/customTypes';
import {
  addPortPulling,
  getMousePosInGraph,
  getPortTypePack,
  getPortVar,
  getSysType,
  getPullingEdgeInfos,
  getUniqueSysName,
  isNotPort,
  getSystem
} from '../../tools/genericFunctions';

const nodeTypes = { SystemNode, PullingNode };

const nodeColor = (node: Node) => {
  switch (node.type) {
    case 'SystemNode':
      return 'var(--nodeBackgroundColor)';
    case 'PullingNode':
      return 'var(--pullingBackgroundColor)';
    default:
      return 'black';
  }
};

const markerEnd = { type: MarkerType.ArrowClosed, width: 20, height: 20 };

type isPullingProps = { source: string | null; target: string | null };
/**
 * Returns wether `obj` is a pulling edge/connection or not.
 * @param obj edge or connection to check
 * @returns boolean
 */
const isPulling = ({ source, target }: isPullingProps) =>
  source === 'pullingsIn' || target === 'pullingsOut';
const isConn = (obj: isPullingProps) => !isPulling(obj);

const areConns = (props: isPullingProps[] | isPullingProps) => {
  const testList = props instanceof Array ? props : [props];
  return testList.every(isConn);
};

const arePulls = (props: isPullingProps[] | isPullingProps) => {
  const testList = props instanceof Array ? props : [props];
  return testList.every(isPulling);
};

type SysNode = Node<SystemNodeData>;
type PullNode = Node<PullingNodeData>;
type CustomNode = SysNode | PullNode;

function isSystemNode(node: Node): node is SysNode {
  return node.type === 'SystemNode';
}

const edgeTypes = { ConnectionEdge, PullingEdge };

type ConnEdge = Edge<ConnEdgeData>;
type PullEdge = Edge<PullEdgeData>;
type CustomEdge = ConnEdge | PullEdge;

function isPullEdge(edge: Edge): edge is PullEdge {
  return edge.type === 'PullingEdge';
}

/** Separate nodes based on wether they are pulling nodes or systems */
const separateNodes = (nodes: CustomNode[]) => {
  const pullingNodes: PullNode[] = [];
  const systemNodes: SysNode[] = [];

  nodes.forEach(node => {
    if (isSystemNode(node)) systemNodes.push(node);
    else pullingNodes.push(node);
  });

  return { pullingNodes, systemNodes };
};

/** Separate edges based on wether they are pullings or connections */
const separateEdges = (edges: CustomEdge[]) => {
  const connEdges: ConnEdge[] = [];
  const pullEdges: PullEdge[] = [];

  edges.forEach(edge => {
    if (isPullEdge(edge)) pullEdges.push(edge);
    else connEdges.push(edge);
  });

  return { connEdges, pullEdges };
};

/** Return id for a connection */
const getConnEdgeId = (conn: connectionType) =>
  `${conn.systems.from}.${conn.ports.from}-${conn.systems.to}.${conn.ports.to}`;

/**
 * Sets the stroke of `edge` to `color`.
 *
 * Removes it if no color is provided
 * @param edge edge to change
 * @param color color for stroke (optional)
 */
const setStroke = (edge: Edge, color?: string) => {
  // eslint-disable-next-line no-param-reassign
  edge.style = {
    ...edge.style,
    stroke: color
  };
};

/** Returns a copy of `edges` without strokes */
const getNoStrokeEdges = (edges: Edge[]) => {
  const newEdges = [...edges];
  newEdges.forEach(edge => {
    setStroke(edge);
  });
  return newEdges;
};

/** Set all edges in `wrongEdges` to have a red stroke.
 *
 * DO NOT copy `wrongEdges`, changes the edges directly. */
const setWrongStroke = (wrongEdges: Edge[] | Edge) => {
  const newEdges = wrongEdges instanceof Array ? wrongEdges : [wrongEdges];
  newEdges.forEach(edge => {
    setStroke(edge, 'red');
  });
  return newEdges;
};

type SysClassUndefined = systemClassType | undefined;
type portTypePackNamesType = { name: string; pack: string } | undefined;

interface SystemFlowProps {
  setShowConnPopUp: (val: boolean, options?: any) => void;
  setSysConn: (val: connSysPortInfos, options?: any) => void;
  setPortsConn: (val: connSysPortInfos, options?: any) => void;
  setIndexConn: (val: number, options?: any) => void;

  setShowPullingVariablePopUp: (val: boolean, options?: any) => void;
  setPortPullName: (val: string, options?: any) => void;
  setSysNamePull: (val: string, options?: any) => void;
  setPortVarPull: (val: portVariableType[], options?: any) => void;

  setShowPullingPortPopUp: (val: boolean, options?: any) => void;
  setPortPullnfos: (val: pullingPortInfos, options?: any) => void;
  setPosition: (val: ClientPosition, options?: any) => void;

  setShowKwargs: (val: boolean, options?: any) => void;
  setKwargsProps: (val: kwargsPropsType, options?: any) => void;

  reactFlowWrapper: React.RefObject<HTMLDivElement>;
  flowInstance: ReactFlowInstance<any, any> | undefined;
  setFlowInstance: (
    val: ReactFlowInstance<any, any> | undefined,
    options?: any
  ) => void;

  setShowResetPopUp: (val: boolean, options?: any) => void;
}

/** Flow to add children systems and create connections */
function SystemFlow(props: BaseFlowProps & SystemFlowProps) {
  const {
    packages,
    systemList,
    setSystemList,
    connectionList,
    sysPullsDict,
    getConnErrors,
    setIndexConn,
    setPosition,
    flowInstance,
    reactFlowWrapper,
    wrongConns,
    wrongPulls
  } = props;

  const initNode: Node[] = [
    {
      id: 'pullingsIn',
      type: 'PullingNode',
      position: { x: 400, y: 10 },
      deletable: false,
      data: {
        boolInOut: true,
        systemList,
        sysPullsDict,
        packages
      }
    },
    {
      id: 'pullingsOut',
      type: 'PullingNode',
      position: { x: 400, y: 500 },
      deletable: false,
      data: {
        boolInOut: false,
        systemList,
        sysPullsDict,
        packages
      }
    }
  ];
  const initEdge: Edge[] = [];

  const [nodes, setNodes] = useState<CustomNode[]>(initNode);
  const [edges, setEdges] = useState<CustomEdge[]>(initEdge);

  // rename system
  const [renameSys, setRenameSys] = useState({ oldName: '', newName: '' });
  useEffect(() => {
    const { oldName, newName } = renameSys;
    if (oldName !== '' && newName !== '') {
      const newUniqueName = getUniqueSysName(newName, systemList); // enforce unique name
      const newSystemList = systemList.map(system => ({
        ...system,
        name: system.name === oldName ? newUniqueName : system.name
      }));

      let connSame = true;
      const provConnectionList = connectionList.map(conn => {
        // connectionList
        const systems = { ...conn.systems };
        if (systems.from === oldName) {
          systems.from = newUniqueName;
          connSame = false;
        }
        if (systems.to === oldName) {
          systems.to = newUniqueName;
          connSame = false;
        }
        return { ...conn, systems };
      });
      const newConnectionList = connSame ? connectionList : provConnectionList;

      const provSysPullsDict: sysPullType = {}; // sysPullsDict
      let pullingSame = true;
      Object.entries(sysPullsDict).forEach(([sysName, sysPulls]) => {
        if (sysName !== oldName) {
          provSysPullsDict[sysName] = sysPulls;
        } else {
          provSysPullsDict[newUniqueName] = sysPulls;
          pullingSame = false;
        }
      });
      const newSysPullsDict = pullingSame ? sysPullsDict : provSysPullsDict;

      getConnErrors({
        newSystemList,
        newConnectionList,
        newSysPullsDict
      });
    }
  }, [renameSys]);

  /**
   * Get the port type of the source and the target of `obj`.
   * @param obj edge or connection
   * @returns type of the source and type of the target
   */
  const setSourceTargetType = useCallback(
    (obj: Edge | Connection) => {
      let srcSysType: SysClassUndefined;
      let tgtSysType: SysClassUndefined;
      let srcPortType: portTypePackNamesType;
      let tgtPortType: portTypePackNamesType;
      const { source, target, sourceHandle, targetHandle } = obj;
      if (source && target && sourceHandle && targetHandle) {
        const srcSys = getSystem(source, systemList);
        srcSysType = getSysType(srcSys.type, srcSys.pack, packages);
        srcPortType = getPortTypePack(sourceHandle, srcSysType);

        const tgtSys = getSystem(target, systemList);
        tgtSysType = getSysType(tgtSys.type, tgtSys.pack, packages);
        tgtPortType = getPortTypePack(targetHandle, tgtSysType);

        props.setSysConn({
          from: { name: source, type: srcSysType.name, pack: srcSysType.pack },
          to: { name: target, type: tgtSysType.name, pack: tgtSysType.pack }
        });

        props.setPortsConn({
          from: {
            name: sourceHandle,
            type: srcPortType.name,
            pack: srcPortType.pack
          },
          to: {
            name: targetHandle,
            type: tgtPortType.name,
            pack: tgtPortType.pack
          }
        });
      }
      return { src: srcPortType, tgt: tgtPortType };
    },
    [systemList, packages]
  );

  /**
   * Set the states for the partial connection pop up and show it
   * @param obj edge or connection that needs the pop up
   */
  const setAndShowConnPopUp = useCallback(
    (obj: Edge | Connection) => {
      const index = connectionList.findIndex(
        ({ systems, ports }) =>
          systems.from === obj.source &&
          systems.to === obj.target &&
          ports.from === obj.sourceHandle &&
          ports.to === obj.targetHandle
      );
      setIndexConn(index);
      props.setShowConnPopUp(true);
    },
    [connectionList]
  );

  /**
   * Create data for pulling pop up
   * @param obj edge or connection
   * @returns system and port data
   */
  const getPullData = useCallback(
    (obj: Edge | Connection) => {
      const { source, target, sourceHandle, targetHandle } = obj;
      const isSource = target === 'pullingsOut';
      const systemName = (isSource ? source : target) || '';
      const portName = (isSource ? sourceHandle : targetHandle) || '';

      const isHandleNew =
        (isSource ? targetHandle : sourceHandle) === 'newPulling';
      const provPortMapping = isSource ? targetHandle : sourceHandle;
      const portMapping =
        !isHandleNew && provPortMapping ? provPortMapping : undefined;

      const system = getSystem(systemName, systemList);
      const sysType = getSysType(system.type, system.pack, packages);
      const portType = getPortTypePack(portName, sysType);

      return {
        system: {
          name: systemName,
          type: sysType.name,
          pack: sysType.pack
        },
        port: {
          name: portName,
          type: portType.name,
          pack: portType.pack,
          nameMapping: portMapping
        }
      };
    },
    [systemList, packages]
  );

  /**
   * Set the states for the partial pulling pop up and show it
   * @param port port for the pulling
   * @param system system to which `port` belongs to
   */
  const setAndShowPullVarPopUp = useCallback(
    (
      port: { name: string; type: string; pack: string },
      system: { name: string; type: string; pack: string }
    ) => {
      const portVar = getPortVar(port, system, packages);
      props.setPortPullName(port.name);
      props.setSysNamePull(system.name);
      props.setPortVarPull(portVar);
      props.setShowPullingVariablePopUp(true);
    },
    [packages]
  );

  /** Unselect all nodes and edges */
  const unselectAll = useCallback(() => {
    setNodes(nodes.map(node => ({ ...node, selected: false })));
    setEdges(edges.map(edge => ({ ...edge, selected: false })));
  }, [nodes, edges]);

  /**
   * Delete obsolete connections and pullings when a system is deleted.
   *
   * Set the new list of systems, connections and pullings
   * @param newSystemList
   */
  const deleteObsConnPull = useCallback(
    (newSystemList: systemType[]) => {
      const newConnectionList = connectionList.filter(conn => {
        // connections
        const { from, to } = conn.systems;
        const connSys = newSystemList.filter(
          ({ name }) => name === from || name === to
        );
        return connSys.length === 2;
      });

      const newSysPullsDict: sysPullType = {}; // pullings
      newSystemList.forEach(({ name }) => {
        const pullings = sysPullsDict[name];
        if (pullings) {
          newSysPullsDict[name] = pullings;
        }
      });

      getConnErrors({ newSystemList, newConnectionList, newSysPullsDict });
    },
    [connectionList, sysPullsDict, getConnErrors]
  );

  // updates when systemList changes
  useEffect(() => {
    const { pullingNodes: oldPullNodes, systemNodes: oldSysNodes } =
      separateNodes(nodes);

    const pullingNodes = oldPullNodes.map(
      (node): PullNode => ({
        ...node,
        data: {
          ...node.data,
          systemList
        }
      })
    );

    const systemNodes = systemList.map(
      ({
        // system nodes
        name,
        position,
        kwargs,
        type,
        pack
      }): SysNode => {
        const existingNode = oldSysNodes.find(node => node.id === name);
        if (existingNode) {
          if (existingNode.position !== position) {
            existingNode.position = position;
          }
          if (existingNode.data.kwargs !== kwargs) {
            existingNode.data.kwargs = kwargs;
          }
        }
        return (
          existingNode || {
            id: name,
            type: 'SystemNode',
            position,
            data: {
              type,
              pack,
              kwargs,
              packages,
              setRenameSys
            }
          }
        );
      }
    );

    setNodes([...pullingNodes, ...systemNodes]);
  }, [systemList]);

  // updates when connectionList changes
  useEffect(() => {
    const { pullEdges, connEdges } = separateEdges(edges);

    const newConnEdges = connectionList.map((connection): ConnEdge => {
      const id = getConnEdgeId(connection);
      const existingEdge = connEdges.find(({ id: existId }) => existId === id);
      if (
        existingEdge &&
        existingEdge.data &&
        existingEdge.data.connection !== connection
      ) {
        // update edge data if needed
        existingEdge.data.connection = connection;
        setStroke(existingEdge);
      }
      return (
        existingEdge || {
          id,
          source: connection.systems.from,
          sourceHandle: connection.ports.from,
          target: connection.systems.to,
          targetHandle: connection.ports.to,
          type: 'ConnectionEdge',
          markerEnd,
          data: { connection }
        }
      );
    });

    setEdges([...newConnEdges, ...pullEdges]);
  }, [connectionList]);

  // updates when sysPullsDict changes
  useEffect(() => {
    // update nodes
    // at the begining for the pulling nodes to have the right handles
    const newNodes: Node[] = [...nodes];
    for (let i = 0; i < 2; i += 1) {
      // pulling nodes
      newNodes[i].data = {
        ...nodes[i].data,
        sysPullsDict
      };
    }
    setNodes(newNodes);

    const { connEdges, pullEdges } = separateEdges(edges);

    const newPullEdges = Object.entries(sysPullsDict)
      .map(([sysName, sysPulls]) =>
        sysPulls.map((pulling): Edge<PullEdgeData> => {
          const edgeInfos = getPullingEdgeInfos(
            sysName,
            pulling,
            systemList,
            packages
          );
          const edgeId = edgeInfos.id;
          const existingEdge = pullEdges.find(({ id }) => id === edgeId);
          if (existingEdge) {
            const { data } = existingEdge;
            if (data && data.pulling !== pulling) {
              data.pulling = pulling;
              setStroke(existingEdge);
            }
          }
          return (
            existingEdge || {
              ...edgeInfos,
              markerEnd,
              data: { pulling }
            }
          );
        })
      )
      .reduce((prevVals, nextVal) => prevVals.concat(nextVal), []);

    setEdges([...connEdges, ...newPullEdges]);
  }, [sysPullsDict]);

  // update wrong edges
  useEffect(() => {
    const { connEdges, pullEdges } = separateEdges(edges);

    // connections
    const newConnEdges = getNoStrokeEdges(connEdges);
    const wrongConnEdges = newConnEdges.filter(({ id }) => {
      const isEdgeWrong = wrongConns.some(conn => getConnEdgeId(conn) === id);
      return isEdgeWrong;
    });
    setWrongStroke(wrongConnEdges);

    // pullings
    const newPullEdges = getNoStrokeEdges(pullEdges);
    const wrongPullEdges = newPullEdges.filter(edge => {
      const { variables, port, portMapping }: pullingType = edge.data.pulling;
      const mapList = variables || [{ name: port, mapping: portMapping }];
      return mapList.some(({ mapping, name }) =>
        wrongPulls.includes(mapping || name)
      );
    });
    setWrongStroke(wrongPullEdges);

    setEdges([...newConnEdges, ...newPullEdges]);
  }, [wrongConns, wrongPulls]);

  // update node.data.packages
  useEffect(() => {
    const updatePackages = (node: Node) => ({
      ...node,
      data: { ...node.data, packages }
    });
    const newNodes = nodes.map(updatePackages);
    setNodes(newNodes);
  }, [packages]);

  // nodes related functions
  const handleNodesChange = useCallback(
    (changes: NodeChange[]) =>
      setNodes(nds => applyNodeChanges<any>(changes, nds)),
    []
  );

  /** Update node position when a node is dragged */
  const handleNodeDragStop = useCallback(
    (_: React.MouseEvent, node: Node) => {
      const newSystemList = systemList.map(system => ({
        ...system,
        position: node.id === system.name ? node.position : system.position
      }));

      setSystemList(newSystemList);
    },
    [systemList]
  );

  /** Update `systemList` when a node is deleted */
  const deleteNodes = useCallback(
    (deletedNds: Node[]) => {
      const newSystemList = systemList.filter(({ name }) => {
        const isSysDelted = deletedNds.some(({ id }) => id === name);
        return !isSysDelted;
      });

      deleteObsConnPull(newSystemList);
    },
    [systemList, getConnErrors]
  );

  /** Set kwargs pop up states and show the pop up */
  const showKwargsPopUp = useCallback((event: React.MouseEvent, node: Node) => {
    props.setKwargsProps({
      name: node.id,
      mousePos: event,
      kwargs: node.data.kwargs
    });
    props.setShowKwargs(true);
  }, []);

  // edges related functions
  const handleEdgesChange = useCallback(
    (changes: EdgeChange[]) =>
      setEdges(eds => applyEdgeChanges<any>(changes, eds)),
    []
  );

  /** Delete connection/pulling related to an edge when an edge is deleted */
  const deleteEdges = useCallback(
    (delEds: Edge[]) => {
      if (areConns(delEds)) {
        // for connection edges
        const newConnectionList = connectionList.filter(
          ({ ports, systems }) => {
            const doesEdgeEqualConn = ({
              source,
              target,
              sourceHandle,
              targetHandle
            }: Edge) =>
              source === systems.from &&
              sourceHandle === ports.from &&
              target === systems.to &&
              targetHandle === ports.to;
            return !delEds.some(doesEdgeEqualConn);
          }
        );
        getConnErrors({ newConnectionList });
      } else if (arePulls(delEds)) {
        // for pulling edges
        const newSysPullsDict: sysPullType = {};
        Object.entries(sysPullsDict).forEach(([sys, pullings]) => {
          const sysEdges = delEds.filter(
            ({ source, target }) => source === sys || target === sys
          );
          if (sysEdges.length > 0) {
            const delPulls = sysEdges.map(({ sourceHandle, targetHandle }) =>
              sourceHandle === 'pullingsIn' ? targetHandle : sourceHandle
            );
            // eslint-disable-next-line max-len
            const isNotDel = ({ port, portMapping }: pullingType) =>
              !delPulls.includes(portMapping || port);
            const newPullList = pullings.filter(isNotDel);
            if (newPullList.length > 0) newSysPullsDict[sys] = newPullList;
          } else newSysPullsDict[sys] = pullings;
        });
        getConnErrors({ newSysPullsDict });
      }
    },
    [connectionList, sysPullsDict, packages, getConnErrors]
  );

  const changeShowEdgeLabel = useCallback(
    ({ id }: Edge, show: boolean) => {
      const eds = edges.map(edge => {
        const newEdge = { ...edge };
        if (newEdge.id === id) {
          if (newEdge.data) newEdge.data.showLabel = show;
          newEdge.animated = show;
        }
        return newEdge;
      });
      setEdges(eds);
    },
    [edges]
  );

  const showEdgeLabel = useCallback(
    (_: React.MouseEvent, labelEdge: Edge) => {
      changeShowEdgeLabel(labelEdge, true);
    },
    [edges]
  );

  const hideEdgeLabel = useCallback(
    (_: React.MouseEvent, labelEdge: Edge) => {
      changeShowEdgeLabel(labelEdge, false);
    },
    [edges]
  );

  const moveEdgeLabel = useCallback(
    (e: React.MouseEvent, labelEdge: Edge) => {
      const { x, y } = getMousePosInGraph(
        e,
        reactFlowWrapper.current,
        flowInstance
      );
      const updateEdgePosition = (edge: Edge) => ({
        ...edge,
        data: edge.data
          ? {
              ...edge.data,
              labelPosition:
                edge.id === labelEdge.id
                  ? { left: x + 3, top: y - 8 }
                  : edge.data?.labelPosition
            }
          : undefined
      });

      const newEdges = (eds: CustomEdge[]) => eds.map(updateEdgePosition);

      setEdges(newEdges);
    },
    [edges]
  );

  /** Show connection/pulling pop up */
  const handleEdgeDoubleClick = useCallback(
    (event: React.MouseEvent, edge: Edge) => {
      unselectAll();
      if (isPulling(edge)) {
        // pulling pop up
        const { port, system } = getPullData(edge);

        if (system.type && system.pack && port.type && port.pack) {
          setPosition(event);

          if (isNotPort(port.type)) setAndShowPullVarPopUp(port, system);
          else {
            props.setPortPullnfos({
              portName: port.name,
              systemName: system.name,
              mapping: port.nameMapping
            });
            props.setShowPullingPortPopUp(true);
          }
        }
      } else {
        // partial connection pop up
        setSourceTargetType(edge);
        setAndShowConnPopUp(edge);
      }
    },
    [nodes, edges, connectionList]
  );

  /**
   * Connect two systems by pushing a new connection to `connectionList`.
   *
   * Connect assembly and a child system by pushing a new pulling to `sysPullsDict`.
   */
  const handleConnect = useCallback(
    (conn: Connection) => {
      if (
        conn.source &&
        conn.sourceHandle &&
        conn.target &&
        conn.targetHandle &&
        conn.source !== conn.target
      ) {
        if (!isPulling(conn)) {
          // sibling system connection
          const portTypes = setSourceTargetType(conn);
          const haveDiffTypes =
            portTypes.src?.name !== portTypes.tgt?.name ||
            portTypes.src?.pack !== portTypes.tgt?.pack ||
            (portTypes.src && isNotPort(portTypes.src.name)) ||
            (portTypes.tgt && isNotPort(portTypes.tgt.name));
          const nodesToConn = nodes.filter(
            ({ id }) => id === conn.source || conn.target
          );
          const nodeEdges = getConnectedEdges(nodesToConn, edges);
          const portEdges = nodeEdges.filter(
            ({ target, source, sourceHandle, targetHandle }) =>
              (target === conn.source && targetHandle === conn.sourceHandle) ||
              (target === conn.target && targetHandle === conn.targetHandle) ||
              (source === conn.source && sourceHandle === conn.sourceHandle) ||
              (source === conn.target && sourceHandle === conn.targetHandle)
          );
          if (haveDiffTypes || portEdges.length > 0) {
            // partial connection
            setAndShowConnPopUp(conn);
          } else {
            // full connection
            const newConn = {
              systems: { from: conn.source, to: conn.target },
              ports: { from: conn.sourceHandle, to: conn.targetHandle }
            };

            const newConnectionList = [...connectionList];
            const connExists = newConnectionList.some(
              ({ systems, ports }) =>
                systems.from === newConn.systems.from &&
                systems.to === newConn.systems.to &&
                ports.from === newConn.ports.from &&
                ports.to === newConn.ports.to
            );
            if (!connExists) {
              newConnectionList.push(newConn);
              getConnErrors({ newConnectionList });
            }
          }
        } else {
          // pullings
          const { system, port } = getPullData(conn);

          if (system.type && system.pack && port.type && port.pack) {
            if (isNotPort(port.type)) {
              // chose variables if the port is an extensible port
              setAndShowPullVarPopUp(port, system);
            } else {
              const sysPullings = sysPullsDict[system.name];
              const pullExists = (sysPullings || []).some(
                pulling => pulling.port === port.name
              );
              if (!pullExists) {
                addPortPulling(
                  {
                    port: port.name,
                    portMapping: port.nameMapping || port.name
                  },
                  system.name,
                  sysPullsDict,
                  getConnErrors
                );
              }
            }
          }
        }
      }
    },
    [connectionList, sysPullsDict, systemList, getConnErrors, edges]
  );

  /** Set position for the pop up */
  const handleConnectEnd = useCallback((event: MouseEvent | TouchEvent) => {
    if (event instanceof MouseEvent) {
      setPosition(event);
    }
  }, []);

  /** Drag and drop of a system from the sidebar to the flow */
  const onDragOver = useCallback((event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    // eslint-disable-next-line no-param-reassign
    event.dataTransfer.dropEffect = 'move';
  }, []);

  const onDrop = useCallback(
    (event: React.DragEvent) => {
      event.preventDefault();

      const jsonType: {
        name: string;
        className: string;
        pack: string;
        kwargs: any;
      } = JSON.parse(event.dataTransfer.getData('application/reactflow'));

      // check if the dropped element is valid
      if (typeof jsonType === 'undefined' || !jsonType) {
        return;
      }

      const type = jsonType.name;

      const newSystem: systemType = {
        ...jsonType,
        type,
        typeClass: jsonType.className,
        name: getUniqueSysName(jsonType.className, systemList),
        position: getMousePosInGraph(
          event,
          reactFlowWrapper.current,
          flowInstance
        )
      };

      setSystemList(systemList.concat(newSystem));
    },
    [flowInstance, systemList]
  );

  return (
    <ReactFlow
      nodes={nodes}
      onNodesChange={handleNodesChange}
      onNodeDragStop={handleNodeDragStop}
      onNodesDelete={deleteNodes}
      onNodeContextMenu={showKwargsPopUp}
      edges={edges}
      onEdgesChange={handleEdgesChange}
      onEdgesDelete={deleteEdges}
      onEdgeMouseEnter={showEdgeLabel}
      onEdgeMouseMove={moveEdgeLabel}
      onEdgeMouseLeave={hideEdgeLabel}
      onEdgeDoubleClick={handleEdgeDoubleClick}
      onConnectStart={unselectAll}
      onConnect={handleConnect}
      onConnectEnd={handleConnectEnd}
      nodeTypes={nodeTypes}
      edgeTypes={edgeTypes}
      onInit={(reactFlowInstance: ReactFlowInstance) =>
        props.setFlowInstance(reactFlowInstance)
      }
      onDrop={onDrop}
      onDragOver={onDragOver}
      onContextMenu={unselectAll}
      fitView
      style={{ zIndex: 1 }}
      selectionKeyCode={null}
      deleteKeyCode="Delete"
    >
      <MiniMap nodeColor={nodeColor} zoomable pannable />
      <Background />
      <CustomControls setShowResetPopUp={props.setShowResetPopUp} />
    </ReactFlow>
  );
}

export default SystemFlow;

import React, { useState, useCallback, useEffect, useRef } from 'react';
import ReactFlow, {
  Node,
  Edge,
  addEdge,
  getConnectedEdges,
  PanOnScrollMode,
  applyEdgeChanges,
  Connection,
  EdgeChange,
  ReactFlowProvider,
  ReactFlowInstance
} from 'reactflow';
import ReactMarkdown from 'react-markdown';

import VariableNode, { VarNodeData } from './VariableNode';
import { FlowCenteredPopUp } from '../../PopUp';
import { OkCrossForm } from '../../OkCrossButtons';

import {
  connectionType,
  packDataType,
  getConnErrorsParams,
  portVariableType,
  ClientPosition,
  sysPullType
} from '../../../tools/customTypes';
import {
  getMousePosInGraph,
  getPortVar
} from '../../../tools/genericFunctions';

const nodeTypes = { VariableNode };
type VariableNodeType = Node<VarNodeData>;

type propsPortSysType = {
  from: { name: string; type: string; pack: string };
  to: { name: string; type: string; pack: string };
};

type edgeProps = { system: string; varName: string };

const getEdgeId = (source: string, target: string) => `${source}.${target}`;

const createEdge = (sourceProp: edgeProps, targetProp: edgeProps) => {
  const source = getEdgeId(sourceProp.system, sourceProp.varName);
  const target = getEdgeId(targetProp.system, targetProp.varName);
  return {
    id: getEdgeId(source, target),
    source,
    target
  };
};

export type ConnVar = { system: string; port: string; var: string };
type ConnVarDict = Record<string, ConnVar[]>;

const addListOrKey = (
  key: string,
  value: ConnVar,
  dictToChange: ConnVarDict
) => {
  const connList = dictToChange[key];
  if (connList) {
    connList.push(value);
  } else {
    // eslint-disable-next-line no-param-reassign
    dictToChange[key] = [value];
  }
};

interface IProps {
  connectionList: connectionType[];
  sysPullsDict: sysPullType;
  getConnErrors: (params: getConnErrorsParams) => Promise<void>;

  packages: packDataType[];
  ports: propsPortSysType;
  systems: propsPortSysType;
  index: number;
  setIndex: (val: number, options?: any) => void;
  setShow: (val: boolean, options?: any) => void;
}

/** Pop up for partial port connection */
function ConnectionPopUp(props: IProps) {
  const { connectionList, sysPullsDict, index } = props;
  const { from: portFrom, to: portTo } = props.ports;
  const { from: sysFrom, to: sysTo } = props.systems;

  const [isMounted, setIsMounted] = useState(false);
  const [nodes, setNodes] = useState<VariableNodeType[]>([]);
  const [edges, setEdges] = useState<Edge[]>([]);

  const reactFlowWrapper = useRef<HTMLDivElement>(null);
  const [flowInstance, setFlowInstance] = useState<ReactFlowInstance>();
  const [mousePos, setMousePos] = useState<ClientPosition>({
    clientX: 0,
    clientY: 0
  });
  const [hoverTxt, setHoverTxt] = useState('');
  const [hoverPos, setHoverPos] = useState({ left: 0, top: 0 });
  const [offset] = useState({ x: 200, y: 36 }); // for mouse

  useEffect(() => {
    if (hoverTxt !== '') {
      const graphPos = getMousePosInGraph(
        mousePos,
        reactFlowWrapper.current,
        flowInstance
      );
      const newHovPos = {
        left: graphPos.x + offset.x,
        top: graphPos.y + offset.y
      };
      setHoverPos(newHovPos);
    }
  }, [mousePos]);

  const sysFromName = sysFrom.name;
  const sysToName = sysTo.name;

  // get port variables
  const varsFrom = getPortVar(portFrom, sysFrom, props.packages);
  const varsTo = getPortVar(portTo, sysTo, props.packages);

  useEffect(() => {
    if (!isMounted) {
      setIsMounted(true);

      // get which variables are connected to another port
      const connVarsFrom: ConnVarDict = {};
      const connVarsTo: ConnVarDict = {};
      connectionList.forEach(({ systems, ports, variables }, i) => {
        if (i !== index) {
          // not the connection that is being changed
          const definedVars = variables || [];
          if (systems.from === sysFromName && ports.from === portFrom.name) {
            definedVars.forEach(varDuo =>
              addListOrKey(
                varDuo.from,
                { system: systems.to, port: ports.to, var: varDuo.to },
                connVarsFrom
              )
            );
          } else if (systems.to === sysToName && ports.to === portTo.name) {
            definedVars.forEach(varDuo =>
              addListOrKey(
                varDuo.to,
                { system: systems.from, port: ports.from, var: varDuo.from },
                connVarsTo
              )
            );
          }
        }
      });

      /** Get connections to parent */
      const getPullConn = (
        systemName: string,
        portName: string,
        connVars: ConnVarDict
      ) => {
        const pullings = sysPullsDict[systemName];
        if (pullings) {
          const portPulling = pullings.find(({ port }) => port === portName);
          const varsPulling = portPulling?.variables;
          if (portPulling && varsPulling) {
            varsPulling.forEach(({ name, mapping }) =>
              addListOrKey(
                name,
                {
                  system: 'ParentSystem',
                  port: portPulling.port,
                  var: mapping || name
                },
                connVars
              )
            );
          }
        }
      };

      getPullConn(sysFromName, portFrom.name, connVarsFrom);
      getPullConn(sysToName, portTo.name, connVarsTo);

      /** Create a list of nodes from a list of variables */
      const createNodesFromList = (
        varList: portVariableType[],
        sysName: string,
        connVars: ConnVarDict,
        isSource: boolean
      ): VariableNodeType[] =>
        varList.map(({ name, desc }, varIndex) => ({
          id: getEdgeId(sysName, name),
          position: {
            x: isSource ? 0 : 275,
            y: varIndex * 50 + 10
          },
          data: {
            label: name,
            isSource,
            desc,
            connections: connVars[name],
            setHoverTxt,
            setMousePos
          },
          type: 'VariableNode'
        }));

      const nodesFrom = createNodesFromList(
        varsFrom,
        sysFromName,
        connVarsFrom,
        true
      );
      const nodesTo = createNodesFromList(varsTo, sysToName, connVarsTo, false);
      setNodes([...nodesFrom, ...nodesTo]);

      let initialEdges: Edge[]; // initialize edges
      if (index !== -1) {
        const { variables } = connectionList[index];
        if (variables) {
          // connect variables already connected
          initialEdges = variables.map(({ from, to }) =>
            createEdge(
              { system: sysFromName, varName: from },
              { system: sysToName, varName: to }
            )
          );
        } else if (portFrom.type === portTo.type) {
          initialEdges = varsFrom.map(({ name: varName }) =>
            createEdge(
              { system: sysFromName, varName },
              { system: sysToName, varName }
            )
          );
        } else initialEdges = [];
      } else {
        // by default, edge betweeen variables with same name created
        initialEdges = varsFrom
          .filter(({ name: varName }) => {
            const isOutVarCo = connVarsTo[varName];
            const isVarInVarTo = varsTo.some(varTo => varTo.name === varName);
            return !isOutVarCo && isVarInVarTo;
          })
          .map(({ name: varName }) =>
            createEdge(
              { system: sysFromName, varName },
              { system: sysToName, varName }
            )
          );
      }
      setEdges(initialEdges);
    }
  });

  const onConnect = useCallback(
    (params: Connection) =>
      setEdges(eds => {
        const nodesTest = nodes.filter(({ id }) => id === params.target);
        if (getConnectedEdges(nodesTest, eds).length < 1)
          return addEdge(params, eds);
        return eds;
      }),
    [nodes]
  );

  const onEdgesChange = useCallback(
    (changes: EdgeChange[]) => setEdges(eds => applyEdgeChanges(changes, eds)),
    []
  );

  /** Set a new `connectionList` containing the new connection */
  const handleClick = () => {
    const newConnectionList = [...connectionList];
    if (index > -1) newConnectionList.splice(index, 1); // delete previous conn if it exists
    if (edges.length > 0) {
      const variables = edges.flatMap(({ source, target }) => {
        const srcData = nodes.find(({ id }) => id === source)?.data;
        const tgtData = nodes.find(({ id }) => id === target)?.data;
        return srcData && tgtData
          ? { from: srcData.label, to: tgtData.label }
          : [];
      });

      newConnectionList.push({
        systems: { from: sysFromName, to: sysToName },
        ports: { from: portFrom.name, to: portTo.name },
        variables
      });
    }
    props.getConnErrors({ newConnectionList });
  };

  const closePopUp = () => {
    props.setIndex(-1);
    props.setShow(false);
  };

  // for closing pop up
  useEffect(() => {
    if (isMounted) {
      closePopUp();
    }
  }, [props.connectionList]);

  let maxLength = 0;
  if (varsFrom && varsTo) {
    maxLength =
      varsFrom.length > varsTo.length ? varsFrom.length : varsTo.length;
  }

  return (
    <>
      <FlowCenteredPopUp className="connPopUp" closePopUp={closePopUp}>
        <div className="title">
          <div>{`${sysFromName}: ${portFrom.name}`}</div>
          <div>{`${sysToName}: ${portTo.name}`}</div>
        </div>
        <ReactFlowProvider>
          <div
            className="connFlowContainer"
            ref={reactFlowWrapper}
            style={{
              height: `min(${maxLength * 50}px, calc(var(--flowMinHeight) - 5px))`
            }}
          >
            <ReactFlow
              nodes={nodes}
              edges={edges}
              onConnect={onConnect}
              onEdgesChange={onEdgesChange}
              nodeTypes={nodeTypes}
              fitView
              onInit={(reactFlowInstance: ReactFlowInstance) =>
                setFlowInstance(reactFlowInstance)
              }
              panOnDrag={false}
              panOnScroll
              panOnScrollMode={PanOnScrollMode.Vertical}
              autoPanOnConnect={false}
              zoomOnScroll={false}
              zoomOnPinch={false}
              zoomOnDoubleClick={false}
              selectionKeyCode={null}
              deleteKeyCode="Delete"
            />
          </div>
        </ReactFlowProvider>
        {hoverTxt !== '' ? (
          <div className="hover" style={hoverPos}>
            <ReactMarkdown>{hoverTxt}</ReactMarkdown>
          </div>
        ) : (
          ''
        )}
        <OkCrossForm handleOk={handleClick} closePopUp={closePopUp} />
      </FlowCenteredPopUp>
    </>
  );
}

export default ConnectionPopUp;

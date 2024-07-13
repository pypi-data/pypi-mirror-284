import { ReactFlowInstance, XYPosition } from 'reactflow';

import {
  systemClassType,
  portClassType,
  pullingType,
  sysPortType,
  packDataType,
  systemType,
  sysPullType,
  getConnErrorsParams,
  ClientPosition,
  HTMLPosition,
  portVariableType
} from './customTypes';
import { widgetId } from './widgetParams';

/**
 * Check if the port type is ExtensiblePort or ModeVarPort, or a Port.
 * @param portTypeName name of the type of the port to check
 * @returns `true` if the port type is ExtensiblePort or ModeVarPort
 */
export function isNotPort(portTypeName: string) {
  return portTypeName === 'ExtensiblePort' || portTypeName === 'ModeVarPort';
}

/** Find the object whose name is `srcName` in `srcList` and return it.
 *
 * If it isn't found, throws an error.
 * @param srcName name of the object
 * @param srcList list to search from
 * @param desc Description for the error message: `${desc} ${srcName} not found.`
 */
function srcByName(srcName: string, srcList: any[], desc: string) {
  const obj = srcList.find(({ name }) => name === srcName);
  if (!obj) {
    throw new Error(`${desc} ${srcName} not found.`);
  }
  return obj;
}

export const getSystem = (
  sysName: string,
  systemList: systemType[]
): systemType => srcByName(sysName, systemList, 'System');
const getPort = (portName: string, portList: sysPortType[]): sysPortType =>
  srcByName(portName, portList, 'Port');
const getPackage = (packName: string, packages: packDataType[]): packDataType =>
  srcByName(packName, packages, 'System');

/**
 * Return the type of a system given its type name and package name.
 *
 * The type must be in `packages`.
 * @param typeName name of the type of the system
 * @param packName name of the package the type is in (used for quicker search)
 * @param packages list of all imported packages
 * @returns type of the system, throw an error if the system was not found
 */
export function getSysType(
  typeName: string,
  packName: string,
  packages: packDataType[]
): systemClassType {
  const { systems } = getPackage(packName, packages);
  return srcByName(typeName, systems, 'System class');
}

/**
 * Return the type of a port given its type name and package name.
 *
 * The type must be in `packages`.
 * @param typeName name of the type of the port
 * @param packName name of the package the type is in (used for quicker search)
 * @param packages list of all imported packages
 * @returns object representing the type of the port or throw an error if the port was not found
 */
export function getPortType(
  typeName: string,
  packName: string,
  packages: packDataType[]
): portClassType {
  const { ports } = getPackage(packName, packages);
  return srcByName(typeName, ports, 'Port class');
}

/**
 * Return the name and package of the type of port,
 * given the name of the port and the ports of the system it belongs to.
 * @param portName name of the port
 * @param ports inputs and outputs if the system
 * @returns name and package or `undefined` if the port was not found
 */
export function getPortTypePack(
  portName: string,
  { inputs, outputs }: systemClassType
) {
  const getInList = (portList: sysPortType[]) => {
    const port = portList.find(({ name }) => name === portName);
    return port ? { name: port.type, pack: port.pack } : port;
  };

  const input = getInList(inputs || []);
  const output = getInList(outputs || []);
  if (input && output) {
    throw new Error(`Port ${portName} in both inputs and outputs.`);
  }
  const port = input || output;
  if (!port) {
    throw new Error(`Port ${portName} not found.`);
  }
  return port;
}

/**
 * Return wether a port if an input or an output port in a system,
 * given the name of the port, and the inputs and outputs of the system.
 * @param portName name of the port
 * @param ports inputs and outputs of the system
 * @returns `true` if the port is an input, `false` if it is an output,
 * and `undefined` if the port was not found or in both lists
 */
export function isPortInOut(
  portName: string,
  { inputs, outputs }: systemClassType
) {
  const isInput = (inputs || []).some(({ name }) => name === portName);
  const isOutput = (outputs || []).some(({ name }) => name === portName);
  if (isInput === isOutput) {
    throw new Error(`Port ${portName} in both inputs and outputs.`);
  }
  return isInput;
}

/**
 * Generates an object containing all information necessary for the creation of a pulling edge.
 * @param systemName name of the system used in the pulling
 * @param pulling pulling that will be represented by the edge
 * @param systemList list of all the systems (system named `systemName` must be in it)
 * @param packages list of all the packages (must contain the type of `systemName`)
 * @returns informations needed to create the edge,
 * or `undefined` if the system, its type or the port type (input/output) were not found
 */
export function getPullingEdgeInfos(
  systemName: string,
  pulling: pullingType,
  systemList: systemType[],
  packages: packDataType[]
) {
  const { port } = pulling;
  const { type: typeName, pack } = getSystem(systemName, systemList);
  const sysType = getSysType(typeName, pack, packages);
  const boolInOut = isPortInOut(port, sysType);
  const source = boolInOut ? 'pullingsIn' : systemName;
  const target = boolInOut ? systemName : 'pullingsOut';
  const portHandle = pulling.portMapping || port;

  return {
    id: `${systemName}.${port}.${boolInOut ? source : target}.${portHandle}`,
    type: 'PullingEdge',
    source,
    sourceHandle: boolInOut ? portHandle : port,
    target,
    targetHandle: boolInOut ? port : portHandle
  };
}

/**
 * Returns all variables in a port.
 * @param port port to extract variables from
 * @param system system the port belongs to
 * @param packages list of all the packages
 * @returns variables of the port or `undefined` if the port or its variables were not found
 */
export function getPortVar(
  port: { name: string; type: string; pack: string },
  system: { type: string; pack: string },
  packages: packDataType[]
) {
  let variables: portVariableType[];
  if (isNotPort(port.type)) {
    // ExtensiblePort or ModeVarPort
    const { inputs, outputs } = getSysType(system.type, system.pack, packages);
    const ports = [...(inputs || []), ...(outputs || [])];
    variables = getPort(port.name, ports).variables || [];
  } else {
    ({ variables } = getPortType(port.type, port.pack, packages));
  }

  return variables;
}

/**
 * Convert a window position to its position in the widget
 * @param position dict containing the position names and their values.
 * @returns dict that has the same structure as `position`
 */
export function getPosInWidget(position: HTMLPosition) {
  const finalPos = position;
  Object.entries(position).forEach(([key, value]) => {
    const widget = document.getElementById(widgetId);
    if (!widget) {
      throw new Error('Widget not found.');
    }
    if (key === 'top' || key === 'left') {
      finalPos[key] = value - widget.getBoundingClientRect()[key];
    } else if (key === 'right' || key === 'bottom') {
      finalPos[key] = widget.getBoundingClientRect()[key] - value;
    }
  });
  return finalPos;
}

/**
 * Calculate the position of the mouse in the widget.
 * @param mousePosition position of the mouse in the current window
 * @returns left and top style argument for the placement of an HTML element
 */
export function getMousePosInWidget({ clientX, clientY }: ClientPosition) {
  const { top, left } = getPosInWidget({ left: clientX, top: clientY });
  if (!top || !left) {
    throw new Error("Can't find position.");
  }
  return { top, left };
}

/**
 * Calculate the position of the mouse in a ReactFlow `flowInstance`.
 * @param mousePosition position of the mouse in the current window
 * @param currentFlowWrapper wrapper in which `flowInstance` is contained
 * @param flowInstance instance of the Reactflow
 * @returns x and y position of the mouse in the flow
 */
export function getMousePosInGraph(
  { clientX, clientY }: ClientPosition,
  currentFlowWrapper: HTMLDivElement | null,
  flowInstance: ReactFlowInstance<any, any> | undefined
) {
  let result: XYPosition = { x: 0, y: 0 };
  if (currentFlowWrapper !== null) {
    const reactFlowBounds = currentFlowWrapper.getBoundingClientRect();
    if (flowInstance) {
      result = flowInstance.project({
        x: clientX - reactFlowBounds.left,
        y: clientY - reactFlowBounds.top
      });
    }
  }
  return result;
}

/**
 * Add a pulling in pulling in sysPullsDict.
 * @param newPulling pulling to be added sysPullsDict
 * @param systemName name of the system the pulling is related to
 * @param sysPullsDict list of all the pullings
 * @param getConnErrors function that will call the API and set the new sysPullsDict
 */
export function addPortPulling(
  newPulling: pullingType,
  systemName: string,
  sysPullsDict: sysPullType,
  getConnErrors: (params: getConnErrorsParams) => Promise<void>
) {
  let finalSysPulls: pullingType[];
  const existingPullings = sysPullsDict[systemName];
  if (existingPullings) {
    const pullings = [...existingPullings];
    const portIndex = pullings.findIndex(
      ({ port }) => port === newPulling.port
    );
    if (portIndex > -1) {
      pullings[portIndex] = newPulling;
    } else {
      pullings.push(newPulling);
    }
    finalSysPulls = pullings;
  } else {
    finalSysPulls = [newPulling];
  }

  const newSysPullsDict = { ...sysPullsDict };
  newSysPullsDict[systemName] = finalSysPulls;
  getConnErrors({ newSysPullsDict });
}

/**
 * Create a unique name from a proposition.
 *
 * If the name is already taken, add a number to its end.
 * @param sysName proposition of a name
 * @param systemList list of all systems in the assembly
 * @returns unique name for the system
 */
export function getUniqueSysName(sysName: string, systemList: systemType[]) {
  const checkName = (srcName: string) =>
    systemList.some(({ name }) => name === srcName);
  const upCaseName = sysName.charAt(0).toLowerCase() + sysName.slice(1);

  let doesNameExist = checkName(upCaseName);
  let c = -1;
  while (doesNameExist) {
    c += 1;
    doesNameExist = checkName(upCaseName + c);
  }

  return c === -1 ? upCaseName : upCaseName + c;
}

/**
 * Merge `systemList` and `sysPullsDict` for API calls.
 * @param systemList
 * @param sysPullsDict
 * @returns merged list
 */
export function mergeSysPulls(
  systemList: systemType[],
  sysPullsDict: sysPullType
) {
  return systemList.map(system => ({
    ...system,
    pullings: sysPullsDict[system.name]
  }));
}

type PortNameType = { name: string; type: string } & Record<string, any>;
/**
 * Order ports by alphabetical order, on their types and then names.
 *
 * Always place `ExtensiblePort` first, then `ModeVarPort`, then other types.
 */
export function sortPorts(
  { type: type1, name: name1 }: PortNameType,
  { type: type2, name: name2 }: PortNameType
) {
  if (type1 === 'ExtensiblePort') {
    return -1;
  } else if (type2 === 'ExtensiblePort') {
    return 1;
  } else if (type1 === 'ModeVarPort') {
    return -1;
  } else if (type2 === 'ModeVarPort') {
    return 1;
  } else if (type1 === type2) {
    return name1 > name2 ? 1 : -1;
  } else {
    return type1 > type2 ? 1 : -1;
  }
}

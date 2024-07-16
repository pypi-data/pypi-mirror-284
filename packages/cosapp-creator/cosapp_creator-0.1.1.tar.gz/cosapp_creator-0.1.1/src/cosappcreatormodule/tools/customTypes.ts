// pack = package
// mod =  module
// `package` and `module` are already defined in typescript

import { XYPosition } from 'reactflow';

/** Widget data type for a variable in a pulling */
export type pullingVariableType = { name: string; mapping?: string };

/** Widget data type for a pulling in a system */
export type pullingType = {
  port: string;
  variables?: pullingVariableType[];
  portMapping?: string;
};

/** Widget data for kwargs */
export type Kwargs = Record<string, any>;

export type ContextContent = { context: string; content: string };
/** Widget data a mathematical problem */
export type MathProblem = {
  nUnknowns?: number;
  nEquations?: number;
  unknowns?: ContextContent[];
  equations?: ContextContent[];
};

/** Widget data type for all pullings in one system */
export type sysPullType = Record<string, pullingType[]>;

/**  Widget data type */
export type systemType = {
  name: string;
  type: string;
  typeClass: string;
  pack: string;
  kwargs?: Kwargs;
  position: XYPosition;
};

export type FromTo = { from: string; to: string };

/** Widget data type */
export type connectionType = {
  systems: FromTo;
  ports: FromTo;
  variables?: FromTo[];
};

/** Widget data type */
export type scopeType = 'PRIVATE' | 'PROTECTED' | 'PUBLIC';
/** Widget data type */
export type rangeType = [any, any];
/** Widget data type */
export type pythonType = 'int' | 'float';

/** Widget data type */
export type extPortVariableType = {
  // inward/outward
  name: string;
  value?: any;
  unit?: string;
  dtype?: pythonType;
  valid_range?: rangeType;
  invalid_comment?: string;
  limits?: rangeType;
  out_of_limits_comment?: string;
  desc?: string;
  scope?: scopeType;
};

/** Widget data type */
export type unknownType = {
  unknown: string;
  max_rel_step?: number;
  max_abs_step?: number;
  lower_bound?: number;
  upper_bound?: number;
};

/**  Widget data type */
export type equationType = {
  equation: string;
  name?: string;
  reference?: any;
};

/** Widget data type */
export type designMethodType = {
  name: string;
  unknowns?: unknownType[];
  equations?: equationType[];
};

/** Widget data type */
export type eventType = {
  name: string;
  desc?: string;
  trigger?: string;
  final?: boolean;
};

/** Package data type */
export type portVariableType = {
  name: string;
  desc?: string;
  unit?: string;
};

/** Package data type */
export type sysPortType = {
  name: string;
  type: string;
  pack: string;
  desc?: string;
  variables?: portVariableType[];
};

/** Package data type */
export type portClassType = {
  name: string;
  pack: string;
  desc?: string;
  variables: portVariableType[];
  kwargs?: Kwargs;
};

/** Package data type */
export type systemClassType = {
  name: string;
  className: string;
  pack: string;
  mod: string;
  desc?: string;
  inputs?: sysPortType[];
  outputs?: sysPortType[];
  kwargs?: Kwargs;
  mathProblem?: MathProblem;
};

/** Package data type */
export type packDataType = {
  name: string;
  version?: string;
  systems: systemClassType[];
  ports: portClassType[];
};

// other
export interface IPropsPackages {
  packages: packDataType[];
}

export type pullingPortInfos = {
  systemName: string;
  portName: string;
  mapping?: string;
};

export interface getConnErrorsParams {
  newSystemList?: systemType[];
  newConnectionList?: connectionType[];
  newSysPullsDict?: sysPullType;
  check?: boolean;
}

/** Position of the mouse in the window */
export type ClientPosition = { clientX: number; clientY: number };

export type HTMLPosition = {
  top?: number;
  left?: number;
  bottom?: number;
  right?: number;
};

/** `index` is the index of the package to replace
 *
 * `pack` is the new package that will replace `packages[index]`
 */
export type ReplacePack = { index?: number; pack?: packDataType };

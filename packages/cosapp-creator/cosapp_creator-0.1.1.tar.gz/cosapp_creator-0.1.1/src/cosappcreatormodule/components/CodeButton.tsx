import React, { useState } from 'react';
import {
  connectionType,
  designMethodType,
  equationType,
  eventType,
  extPortVariableType,
  packDataType,
  pullingType,
  sysPullType,
  systemType,
  unknownType
} from '../tools/customTypes';
import { getSysType } from '../tools/genericFunctions';

const tab = '    ';
const tab2 = tab + tab;
const lineBreak = '\n';
/** Add two linebreaks if `str` is not empty */
const formatStr = (str: string) =>
  str !== '' ? str + lineBreak + lineBreak : str;

/**
 * Convert an object to a string representing it in Python code
 * @param obj object to convert
 * @returns string containing the representation of `obj`
 */
const anyToPython = (obj: any): string => {
  if (typeof obj === 'string') {
    return `'${obj}'`;
  }
  if (typeof obj === 'boolean') {
    return obj ? 'True' : 'False';
  }
  if (Array.isArray(obj)) {
    const tabString = obj.map(val => anyToPython(val)).join(', ');
    return obj.length === 1 ? tabString : `[${tabString}]`;
  }
  return String(obj);
};

/** Return `name : mapping` if mapping exist else return `name` */
const getPullingStr = (name: string, mapping?: string) =>
  `${anyToPython(name)}${mapping ? `: ${anyToPython(mapping)}` : ''}`;

/**
 * Create a string containing Python code for the mapping dictionary for `pulling`
 * @param pulling
 * @returns created string
 */
const pullingPort = ({ variables, port, portMapping }: pullingType) =>
  (variables || [{ name: port, mapping: portMapping }])
    .map(({ name, mapping }) => getPullingStr(name, mapping))
    .join(', ');

const getAllPullingsStr = (pullings: pullingType[]) =>
  pullings.map(pulling => pullingPort(pulling)).join(', ');

/**
 * Create a string for all pullings in a system,
 * return an empty string if the system doesn't have any
 * @param pullings
 * @returns created string
 */
const pullingsToPython = (pullings: pullingType[]) => {
  let pullingsStr: string;
  // if name mapping (by construction, either all pullings have one or none does)
  if (
    pullings[0].portMapping || // if name mapping
    (pullings[0].variables && pullings[0].variables[0].mapping)
  ) {
    pullingsStr = `{${getAllPullingsStr(pullings)}}`;
  } else if (pullings.length === 1 && !pullings[0].variables) {
    // one pulling, no variables
    pullingsStr = anyToPython(pullings[0].port);
  } else if (
    pullings.length === 1 && // one pulling, one variable
    pullings[0].variables &&
    pullings[0].variables.length === 1
  ) {
    pullingsStr = anyToPython(pullings[0].variables[0].name);
  } else {
    pullingsStr = `[${getAllPullingsStr(pullings)}]`;
  }

  return pullingsStr ? `, pulling=${pullingsStr}` : '';
};

/**
 * Create a string of Pyhton code to create unknowns for a mathematical problem
 * @param unknownList
 * @returns created string
 */
const unknownsToPython = (unknownList: unknownType[]) =>
  unknownList
    .map(
      ({
        unknown,
        max_abs_step: maStep,
        max_rel_step: mrStep,
        lower_bound: lbound,
        upper_bound: ubound
      }) => {
        const argsTab: string[] = [anyToPython(unknown)];
        if (maStep) argsTab.push(`max_abs_step=${maStep}`);
        if (mrStep) argsTab.push(`max_rel_step=${mrStep}`);
        if (lbound) argsTab.push(`lower_bound=${lbound}`);
        if (ubound) argsTab.push(`upper_bound=${ubound}`);
        return `.add_unknown(${argsTab.join(', ')})`;
      }
    )
    .join('');

/**
 * Create a string of Pyhton code to create equations for a mathematical problem
 * @param equationList
 * @returns  created string
 */
const equationsToPython = (equationList: equationType[]) =>
  equationList
    .map(({ equation, name, reference }) => {
      const argsTab: string[] = [anyToPython(equation)];
      if (name) argsTab.push(`name=${anyToPython(name)}`);
      if (reference) argsTab.push(`reference=${anyToPython(reference)}`);
      return `.add_equation(${argsTab.join(', ')})`;
    })
    .join('');

const computePython = () => `${tab}def compute(self):${lineBreak}${tab2}pass`;

interface IProps {
  assemblyName: string;
  systemList: systemType[];
  connectionList: connectionType[];
  sysPullsDict: sysPullType;
  inwardList: extPortVariableType[];
  outwardList: extPortVariableType[];
  designMethodList: designMethodType[];
  offDesignUnknownList: unknownType[];
  offDesignEquationList: equationType[];
  eventList: eventType[];
  packages: packDataType[];
}

/** Show generated code */
function CodeButton(props: IProps) {
  const {
    systemList,
    connectionList,
    sysPullsDict,
    inwardList,
    outwardList,
    designMethodList,
    offDesignUnknownList,
    offDesignEquationList,
    eventList,
    packages
  } = props;

  /**
   * Check all imports neeeded by the assembly and create a string of Python code containing them
   * @returns string generated
   */
  const importsToPython = () => {
    const cosappImport = `from cosapp.base import System${lineBreak}`;

    // check if scope is used
    const boolScope = [...inwardList, ...outwardList].some(
      variable => variable.scope
    );
    const scopeImport = boolScope
      ? `from cosapp.ports.enum import Scope${lineBreak}`
      : '';

    // for the systems used
    const modList = systemList.map(
      ({ pack, type }) => getSysType(type, pack, packages).mod
    );
    const modImport = [...new Set(modList)]
      .map(mod => `import ${mod}`)
      .join(lineBreak);

    return formatStr(cosappImport + scopeImport + modImport);
  };

  /** Write a string of Python code for a class named
   * `props.assemblyName` inheriting from `cosapp.base.System` */
  const defPython = () =>
    `class ${props.assemblyName}(System):${lineBreak}${tab}def setup(self):${lineBreak}`;

  /**
   * Create a string containing Python code for all children of the assembly
   * @returns created string
   */
  const childrenToPython = () => {
    const childrenTab = systemList.map(system => {
      const sysType = getSysType(system.type, system.pack, packages);
      const mod = sysType ? sysType.mod : '';

      const { kwargs = {} } = system;
      const sysArgsTab = [anyToPython(system.name)].concat(
        Object.entries(kwargs).map(([varName, value]) => `${varName}=${value}`)
      );
      const sysStr = `${mod}.${system.typeClass}(${sysArgsTab.join(', ')})`;

      const pullings = sysPullsDict[system.name];
      const pullingStr = pullings ? pullingsToPython(pullings) : '';

      return `${tab2}self.add_child(${sysStr}${pullingStr})`;
    });
    return formatStr(childrenTab.join(lineBreak));
  };

  /**
   * Creates a string containing Python code for inwards and outwards of the assembly
   * @param listType ('inward' or 'outward'), indicates which port to write
   * @returns created string
   */
  const extensiblePortsToPython = (listType: 'inward' | 'outward') => {
    const list = listType === 'inward' ? inwardList : outwardList;
    const extPortsTab = list.map(
      ({
        name,
        value,
        unit,
        dtype,
        limits,
        desc,
        scope,
        valid_range: vRange,
        invalid_comment: invComment,
        out_of_limits_comment: oolComment
      }) => {
        const argTab: string[] = [name];
        if (value !== undefined) argTab.push(anyToPython(value));
        if (unit) argTab.push(`unit=${anyToPython(unit)}`);
        if (dtype) argTab.push(`dtype=${dtype}`);
        if (vRange) argTab.push(`valid_range=${anyToPython(vRange)}`);
        if (invComment)
          argTab.push(`invalid_comment=${anyToPython(invComment)}`);
        if (limits) argTab.push(`limits=${anyToPython(limits)}`);
        if (oolComment)
          argTab.push(`out_of_limits_comment=${anyToPython(oolComment)}`);
        if (desc) argTab.push(`desc=${anyToPython(desc)}`);
        if (scope) argTab.push(`scope=Scope.${anyToPython(invComment)}`);
        return `${tab2}self.add_${listType}(${argTab.join(', ')})`;
      }
    );
    return formatStr(extPortsTab.join(lineBreak));
  };

  /**
   * Create a string of Python code connecting ports and variables
   * @returns created string
   */
  const connectionsToPython = () => {
    const connTab = connectionList.map(({ systems, ports, variables }) => {
      const argsTab = [
        `self.${systems.from}.${ports.from}, self.${systems.to}.${ports.to}`
      ];
      if (variables && variables.length > 0) {
        argsTab.push(
          `{${variables.map(varDuo => `${anyToPython(varDuo.from)}: ${anyToPython(varDuo.to)}`)}}`
        );
      }
      return `${tab2}self.connect(${argsTab.join(', ')})`;
    });
    return formatStr(connTab.join(lineBreak));
  };

  /**
   * Create of string of Python code to create all design methods for an assembly
   * @returns created string
   */
  const designMethodsToPython = () => {
    const designMethodsTab = designMethodList.map(
      ({ name, unknowns, equations }) => {
        const unknownsEquas: string[] = [];
        if (unknowns) unknownsEquas.push(unknownsToPython(unknowns));
        if (equations) unknownsEquas.push(equationsToPython(equations));
        return `${tab2}self.add_design_method(${anyToPython(name)})${unknownsEquas.join('')}`;
      }
    );
    return formatStr(designMethodsTab.join(lineBreak));
  };

  const offDesignUnknownsToPython = () =>
    offDesignUnknownList.length > 0
      ? formatStr(`${tab2}self${unknownsToPython(offDesignUnknownList)}`)
      : '';

  const offDesignEquationsToPython = () =>
    offDesignEquationList.length > 0
      ? formatStr(`${tab2}self${equationsToPython(offDesignEquationList)}`)
      : '';

  /**
   * Create of string of Python code to create all events for an assembly
   * @returns created string
   */
  const eventsToPython = () => {
    let eventsToPythonStr = '';

    if (eventList.length > 0) {
      const transTab = [`${tab}def transition(self):`];
      const eventsStr = eventList
        .map(({ name, desc, trigger, final }) => {
          transTab.push(
            `${tab2}if self.${name}.present:${lineBreak + tab2 + tab}pass${lineBreak}`
          );

          const argsTab = [anyToPython(name)];
          if (desc) argsTab.push(`desc=${anyToPython(desc)}`);
          if (trigger) argsTab.push(`trigger=${anyToPython(trigger)}`);
          if (final) argsTab.push(`final=${anyToPython(final)}`);
          return `${tab2}self.add_event(${argsTab.join(', ')})`;
        })
        .join(lineBreak);

      eventsToPythonStr = formatStr(
        eventsStr + lineBreak + transTab.join(lineBreak)
      );
    }

    return eventsToPythonStr;
  };

  /**
   * Create a Python code string for the assembly
   * @returns created code
   */
  const toPython = () => {
    const provSetupStr =
      childrenToPython() +
      extensiblePortsToPython('inward') +
      extensiblePortsToPython('outward') +
      connectionsToPython() +
      designMethodsToPython() +
      offDesignUnknownsToPython() +
      offDesignEquationsToPython() +
      eventsToPython();

    const setupStr =
      provSetupStr === '' ? formatStr(`${tab2}pass`) : provSetupStr;
    return importsToPython() + defPython() + setupStr + computePython();
  };

  const [show, setShow] = useState(false);

  /** Copy code to clipboard */
  const codeToClipBorad = () => {
    navigator.clipboard.writeText(toPython());
  };

  return (
    <>
      <div>
        <button
          type="button"
          className="codeButton"
          onClick={() => setShow(true)}
        >
          Generate Code
        </button>
        {show ? (
          <>
            <button
              type="button"
              className="codeButton"
              onClick={() => setShow(false)}
            >
              Hide Code
            </button>
            <button
              type="button"
              className="codeButton"
              onClick={codeToClipBorad}
            >
              Copy Code
            </button>
          </>
        ) : (
          ''
        )}
      </div>
      {show ? (
        <>
          <div id="codeFrame" className="container codeFrame">
            <div className="codeOutput">{toPython()}</div>
          </div>
        </>
      ) : (
        ''
      )}
    </>
  );
}

export default CodeButton;

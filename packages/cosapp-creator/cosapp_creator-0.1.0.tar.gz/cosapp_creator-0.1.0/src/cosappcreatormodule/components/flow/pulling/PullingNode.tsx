import React, { useEffect, useState } from 'react';
import { NodeProps, useUpdateNodeInternals } from 'reactflow';
import {
  packDataType,
  sysPullType,
  systemType
} from '../../../tools/customTypes';
import {
  getSysType,
  getPortTypePack,
  getSystem,
  isPortInOut,
  isNotPort,
  sortPorts
} from '../../../tools/genericFunctions';
import { HandleProps } from '../handles/CustomHandle';
import PullingHandle, {
  portPullingHandleProps
} from '../handles/PullingHandle';

export type PullingNodeData = {
  boolInOut: boolean;
  sysPullsDict: sysPullType;
  systemList: systemType[];
  packages: packDataType[];
};

type HandleInfosValues = { port: portPullingHandleProps } & HandleProps;
type HandleInfos = Record<string, HandleInfosValues>;

/** Parent inputs and parent outputs nodes */
function PullingNode(props: NodeProps<PullingNodeData>) {
  const { boolInOut, sysPullsDict, systemList, packages } = props.data;
  const typeStr = boolInOut ? 'Inputs' : 'Outputs';
  const [handleComponent, setHandleComponent] = useState<JSX.Element[]>([]);

  useEffect(() => {
    const handleInfos: HandleInfos = {};
    let pullingNumber = 0;

    Object.entries(sysPullsDict).forEach(([systemName, pullings]) => {
      try {
        const system = getSystem(systemName, systemList);
        const { type: typeName, pack: packName } = system;
        const sysType = getSysType(typeName, packName, packages);

        pullings.forEach(({ port, portMapping, variables }) => {
          const portTypeName = getPortTypePack(port, sysType).name;
          const pullName = portMapping || port;

          const extistingInfos = handleInfos[pullName];
          if (!extistingInfos || isNotPort(portTypeName)) {
            if (isPortInOut(port, sysType) === boolInOut) {
              let vars: Set<string> | undefined;
              if (isNotPort(portTypeName)) {
                // get all variables if extensible or modevar port
                const varTab = (variables || []).map(
                  variable => variable.mapping || variable.name
                );
                vars = new Set(varTab);
                if (extistingInfos) {
                  // get variables from other pullings on this port
                  const existingVars = extistingInfos.port.vars || new Set();
                  extistingInfos.port.vars = new Set([
                    ...vars,
                    ...existingVars
                  ]);
                }
              }

              if (!extistingInfos) {
                pullingNumber += 1;
                handleInfos[pullName] = {
                  port: { name: pullName, type: portTypeName, vars },
                  counter: 0, // doesn't matter here
                  nbTotal: 0,
                  direction: boolInOut
                };
              }
            }
          }
        });
      } catch (error) {
        /* Ignore errors due to system deletion and system renaming. */
      }
    });

    pullingNumber += 1;

    const newHandles = Object.values(handleInfos)
      .sort(({ port: port1 }, { port: port2 }) => sortPorts(port1, port2))
      .map((infos, index) => (
        <PullingHandle
          {...infos}
          counter={index + 1}
          key={infos.port.name}
          nbTotal={pullingNumber}
        />
      ));

    newHandles.push(
      <PullingHandle
        key="newPulling"
        direction={boolInOut}
        counter={pullingNumber}
        nbTotal={pullingNumber}
      />
    );

    setHandleComponent(newHandles);
  }, [sysPullsDict]);

  // let ReactFlow know handles have changed
  const updateNodeInternals = useUpdateNodeInternals();
  updateNodeInternals(props.id);

  return (
    <div className="pullingNode">
      {typeStr}
      {handleComponent}
    </div>
  );
}

export default PullingNode;

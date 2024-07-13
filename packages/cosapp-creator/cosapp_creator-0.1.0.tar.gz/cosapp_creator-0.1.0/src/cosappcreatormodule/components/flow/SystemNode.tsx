import React, { useEffect, useState } from 'react';
import { NodeProps } from 'reactflow';

import NameInput from '../HiddenInput';
import SystemHandle from './handles/SystemHandle';
import MathPbDisplay from '../MathProblem';

import { getSysType, sortPorts } from '../../tools/genericFunctions';
import {
  Kwargs,
  MathProblem,
  packDataType,
  sysPortType
} from '../../tools/customTypes';

export type SystemNodeData = {
  type: string;
  pack: string;
  packages: packDataType[];
  setRenameSys: (
    val: { oldName: string; newName: string },
    options?: any
  ) => void;
  kwargs?: Kwargs;
};

/** Node for a system */
function SystemNode(props: NodeProps<SystemNodeData>) {
  const { type, pack, packages, setRenameSys } = props.data;

  const [systemModType] = useState(getSysType(type, pack, packages));
  const [mathPb] = useState(systemModType.mathProblem);
  const [showRename, setShowRename] = useState(false);
  const [sysName, setSysName] = useState(props.id);

  const createHandles = (portList: sysPortType[], direction = true) =>
    portList
      .sort(sortPorts)
      .map((port, index) => (
        <SystemHandle
          key={port.name}
          packages={packages}
          pack={pack}
          direction={direction}
          port={port}
          counter={index + 1}
          nbTotal={portList.length}
        />
      ));

  const handleDoubleClick = () => setShowRename(true);

  useEffect(() => {
    if (sysName !== props.id && sysName !== '') {
      setRenameSys({ oldName: props.id, newName: sysName });
    }
  }, [sysName]);

  const { inputs = [], outputs = [] } = systemModType;

  return (
    <div
      className="flowNode"
      onDoubleClick={handleDoubleClick}
      style={props.selected ? { borderColor: 'darkgreen' } : {}}
    >
      {createHandles(inputs)}
      {showRename ? (
        <div className="nodeInput">
          <NameInput
            placeholder="SystemName"
            parentState={sysName}
            setParentState={setSysName}
            setShow={setShowRename}
          />
        </div>
      ) : (
        <div className="hiddenOverflow">{props.id}</div>
      )}
      <div className="hiddenOverflow">{type}</div>
      {mathPb ? <MathPbHover mathPb={mathPb} /> : ''}
      {createHandles(outputs, false)}
    </div>
  );
}

type MathPbProps = { mathPb: MathProblem };
function MathPbHover({ mathPb }: MathPbProps) {
  const [showHover, setShowHover] = useState(false);

  return (
    <>
      <div
        onMouseEnter={() => setShowHover(true)}
        onMouseLeave={() => setShowHover(false)}
        className="nodeMathPb"
      >
        &Sigma;
      </div>
      {showHover ? (
        <div className="hover graphHover mathPbHover">
          <MathPbDisplay mathPb={mathPb} />
        </div>
      ) : (
        ''
      )}
    </>
  );
}

export default SystemNode;

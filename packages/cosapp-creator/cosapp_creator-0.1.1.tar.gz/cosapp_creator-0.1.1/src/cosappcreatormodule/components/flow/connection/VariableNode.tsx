import React from 'react';
import { NodeProps, Handle, Position } from 'reactflow';

import { ConnVar } from './ConnectionPopUp';

const connStr = (conn: ConnVar) => `${conn.system}.${conn.port}.${conn.var}`;
const connInListStr = (conn: ConnVar) => `\n- ${connStr(conn)}`;

export type VarNodeData = {
  label: string;
  isSource: boolean;
  desc?: string;
  connections?: ConnVar[];
  setHoverTxt: (val: string, options?: any) => void;
  setMousePos: (
    val: { clientX: number; clientY: number },
    options?: any
  ) => void;
};

function VariableNode(props: NodeProps<VarNodeData>) {
  const { label, desc, isSource, connections, setMousePos, setHoverTxt } =
    props.data;

  const changePosHover = (e: React.MouseEvent) => {
    if (connections || desc) setMousePos(e);
  };

  const showHover = (e: React.MouseEvent) => {
    changePosHover(e);
    const descStr = desc ? `${desc}\n\n` : '';
    if (connections) {
      const hovBeg = '-------\nAlready connected to ';
      const hoverText =
        connections.length > 1
          ? `: \n${connections.map(connInListStr).join('')}`
          : connections.map(connStr);
      setHoverTxt(descStr + hovBeg + hoverText);
    } else if (desc) setHoverTxt(descStr);
  };

  const hideHover = () => {
    setHoverTxt('');
  };

  const cssClass = () => {
    const isConnected = connections !== undefined;
    const isConnectable = isConnected && !isSource;
    return `flowNode ${isConnected ? 'connNode' : ''} ${isConnectable ? 'forbiddenNode' : ''}`;
  };

  return (
    <>
      <div
        className={cssClass()}
        onMouseEnter={showHover}
        onMouseMove={changePosHover}
        onMouseLeave={hideHover}
      >
        {label}
        {!(connections && !isSource) ? (
          <Handle
            type={isSource ? 'source' : 'target'}
            position={isSource ? Position.Right : Position.Left}
          />
        ) : (
          ''
        )}
      </div>
    </>
  );
}

export default VariableNode;

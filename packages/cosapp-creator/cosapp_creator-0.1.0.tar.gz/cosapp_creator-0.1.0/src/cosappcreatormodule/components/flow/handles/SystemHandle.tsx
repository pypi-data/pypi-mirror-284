import React from 'react';
import { HandleType, Position } from 'reactflow';

import { sysPortType, packDataType } from '../../../tools/customTypes';
import { getPortType, isNotPort } from '../../../tools/genericFunctions';

import HoverHandle, { HandleProps } from './CustomHandle';

interface SysHandleProps {
  port: sysPortType;
  pack: string;
  packages: packDataType[];
}

/** Port handle in a system */
function SystemHandle(props: HandleProps & SysHandleProps) {
  const { name, type, variables } = props.port;

  let handleType: HandleType;
  let position: Position;
  let yPosHover: { bottom: number } | { top: number };
  const gap = 44; // space for the hover not to be on the node
  if (props.direction) {
    handleType = 'target';
    position = Position.Top;
    yPosHover = { bottom: gap };
  } else {
    handleType = 'source';
    position = Position.Bottom;
    yPosHover = { top: gap };
  }

  let hoverText: string;
  let desc: string | undefined;
  if (isNotPort(type)) {
    const portVariables = variables || [];
    const varListStr = portVariables
      .map(({ name: varName }) => varName)
      .join('`\n- `');
    ({ desc } = props.port);
    hoverText = `- \`${varListStr}\``;
  } else {
    ({ desc } = getPortType(type, props.pack, props.packages));
    hoverText = `\`${type}\``;
  }

  return (
    <HoverHandle
      port={{ name, type, desc }}
      handleType={handleType}
      position={position}
      yPosHover={yPosHover}
      hoverText={hoverText}
      direction={props.direction}
      counter={props.counter}
      nbTotal={props.nbTotal}
    />
  );
}

export default SystemHandle;

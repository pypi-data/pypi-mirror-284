import React from 'react';
import { HandleType, Position } from 'reactflow';

import HoverHandle, { HandleProps } from './CustomHandle';

export type portPullingHandleProps = {
  name: string;
  type: string;
  vars?: Set<string>;
};

export type PullingHandleProps = {
  port?: portPullingHandleProps;
} & HandleProps;

/** Returns the type of handle and its position (top or bottom) */
function getHandleTypePos(direction: boolean) {
  const handleType: HandleType = direction ? 'source' : 'target';
  const position = direction ? Position.Bottom : Position.Top;
  return { handleType, position };
}

/** Handle for pullingNode */
export function PullingHandle(props: PullingHandleProps) {
  const { port } = props;

  const { handleType, position } = getHandleTypePos(props.direction);
  const gap = 26; // space for the hover to be under the node
  const yPosHover = props.direction ? { top: gap } : { bottom: gap };

  let hoverText: string;
  if (port) {
    const { vars, type } = port;
    hoverText = vars ? `- \`${[...vars].join('`\n- `')}\`` : type;
  } else hoverText = 'Drag a port here to add a new pulling';

  return (
    <HoverHandle
      handleType={handleType}
      position={position}
      yPosHover={yPosHover}
      hoverText={hoverText}
      {...props}
    />
  );
}

export default PullingHandle;

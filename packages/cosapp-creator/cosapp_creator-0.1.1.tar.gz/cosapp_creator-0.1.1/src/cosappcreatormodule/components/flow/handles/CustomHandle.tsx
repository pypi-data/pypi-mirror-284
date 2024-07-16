import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Handle, Position, HandleType } from 'reactflow';

import { isNotPort } from '../../../tools/genericFunctions';

export interface HandleProps {
  direction: boolean; // true = input
  counter: number;
  nbTotal: number;
}

interface CustomHandleProps {
  port?: { name: string; type: string; desc?: string };
  handleType: HandleType;
  position: Position;
  yPosHover: { bottom: number } | { top: number };
  hoverText: string;
}

/** Base handle with a hover */
function HoverHandle(props: CustomHandleProps & HandleProps) {
  const { port } = props;
  const { name, type, desc } = port || {};
  const [showHover, setShowHover] = useState(false);
  const [showDesc, setShowDesc] = useState(false);
  const left = `calc((var(--nodeWidth) + 6px) * ${props.counter} / ${props.nbTotal + 1})`;
  const hoverLeft = `calc((var(--nodeWidth) + 6px) * ${props.counter} / ${props.nbTotal + 1} + 5px)`;
  let color: string;
  let borderColor: string;
  if (type) {
    borderColor = 'white';
    if (isNotPort(type)) color = type === 'ExtensiblePort' ? 'gold' : 'red';
    else color = 'navy';
  } else {
    borderColor = 'black';
    color = 'white';
  }

  const hideAll = () => {
    setShowHover(false);
    setShowDesc(false);
  };

  const getDecodedString = (str: string) => {
    const txt = document.createElement('textarea');
    txt.innerHTML = str;
    return txt.value;
  };

  return (
    <>
      <div
        onMouseEnter={() => {
          setShowHover(true);
        }}
        onMouseLeave={hideAll}
      >
        <Handle
          id={name || 'newPulling'}
          type={props.handleType}
          position={props.position}
          style={{
            left,
            backgroundColor: color,
            borderRadius: props.direction ? '50px' : '0px', // direction =/= type pour les pullingHandle
            borderColor
          }}
          onClick={() => setShowDesc(true)}
        />
      </div>
      {showHover || (showDesc && desc) ? (
        <div
          className="hover graphHover"
          style={{ ...props.yPosHover, left: hoverLeft }}
        >
          {port ? (
            <ReactMarkdown
              className="reactMarkdown"
              remarkPlugins={[remarkGfm]}
            >
              {`\`${name}\`\n\n`}
            </ReactMarkdown>
          ) : (
            ''
          )}
          <ReactMarkdown
            className="reactMarkdownVariables"
            remarkPlugins={[remarkGfm]}
          >
            {showDesc && desc ? getDecodedString(desc) : props.hoverText}
          </ReactMarkdown>
        </div>
      ) : (
        ''
      )}
    </>
  );
}

export default HoverHandle;

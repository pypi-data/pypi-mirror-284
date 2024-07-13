import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';

import { systemClassType } from '../../../tools/customTypes';
import { getPosInWidget } from '../../../tools/genericFunctions';

/** System component for packages sidebar. */
function SystemComponent({ sysType }: { sysType: systemClassType }) {
  const [showDescription, setShowDescription] = useState(false);
  const [top, setTop] = useState(0);
  const [right, setRight] = useState(0);

  /** Start drag and hide description. */
  const handleDragStart = (event: React.DragEvent<HTMLDivElement>) => {
    event.dataTransfer.setData(
      'application/reactflow',
      JSON.stringify(sysType)
    );
    // eslint-disable-next-line no-param-reassign
    event.dataTransfer.effectAllowed = 'move';
    setShowDescription(false);
  };

  /** Set position of the description hover and display it. */
  const handleMouseEnter = () => {
    const sysEl = document.getElementById(sysType.name);
    if (!sysEl) throw new Error(`${sysType.name} not found.`);
    const rect = sysEl.getBoundingClientRect();
    setRight(getPosInWidget({ right: rect.right }).right || 0);
    setShowDescription(true);
  };

  /** Move the hover with the mouse. */
  const handleMouseMove = (event: React.MouseEvent) => {
    if (!showDescription) {
      setShowDescription(true);
    }
    // 15 for the hover not to be right under the mouse
    setTop((getPosInWidget({ top: event.clientY }).top || 0) + 50);
  };

  const { kwargs = {} } = sysType;
  const kwargsStr = Object.entries(kwargs)
    .map(([varName, value]) => `\`${varName}\` \`=\` \`${value}\``)
    .join('\n\n');

  return (
    <>
      <div
        className="hiddenOverflow dragNode"
        id={sysType.name}
        onDragStart={handleDragStart}
        draggable
        onMouseEnter={handleMouseEnter}
        onMouseMove={handleMouseMove}
        onMouseLeave={() => setShowDescription(false)}
      >
        <div className="flowNode" />
        {sysType.name}
      </div>
      {showDescription ? (
        <div
          className="hover nodeHover"
          style={{ top, right, minWidth: '150px' }}
        >
          <ReactMarkdown className="center">
            {`${sysType.name}${sysType.name !== sysType.className ? ` (\`${sysType.className}\`)` : ''}`}
          </ReactMarkdown>
          {sysType.desc ? (
            <ReactMarkdown>{`\n\n${sysType.desc}\n\n${kwargsStr}`}</ReactMarkdown>
          ) : (
            ''
          )}
        </div>
      ) : (
        ''
      )}
    </>
  );
}

export default SystemComponent;

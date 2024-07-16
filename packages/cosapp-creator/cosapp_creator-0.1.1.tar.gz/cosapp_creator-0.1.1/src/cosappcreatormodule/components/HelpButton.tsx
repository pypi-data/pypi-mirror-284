import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { vs2015 } from 'react-syntax-highlighter/dist/esm/styles/hljs';

import readMe from '../readMe/ReadMe_Parser.md?raw';

function HelpButton() {
  const [showHelp, setShowHelp] = useState(false);

  return (
    <>
      <button type="button" onClick={() => setShowHelp(!showHelp)}>
        {showHelp ? 'Hide help' : 'Help'}
      </button>
      {showHelp ? (
        <ReactMarkdown
          className="readMe"
          remarkPlugins={[remarkGfm]}
          components={{
            code({ children, ...props }) {
              return children.some(child =>
                child?.toString().includes('\n')
              ) ? (
                <SyntaxHighlighter
                  language="python"
                  style={vs2015 as any}
                  children={String(children).replace(/\n$/, '')}
                  {...props}
                />
              ) : (
                <code className="singleCodeLine">{children}</code>
              );
            }
          }}
        >
          {readMe}
        </ReactMarkdown>
      ) : (
        ''
      )}
    </>
  );
}

export default HelpButton;

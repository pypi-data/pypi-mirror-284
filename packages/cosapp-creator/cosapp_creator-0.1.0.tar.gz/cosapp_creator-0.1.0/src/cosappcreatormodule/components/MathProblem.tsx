import React from 'react';

import { ContextContent, MathProblem } from '../tools/customTypes';

type FormatFunc = (param: ContextContent) => string;

function MathPbDisplay({ mathPb }: { mathPb: MathProblem }) {
  const formatUnknown: FormatFunc = ({ content, context }: ContextContent) =>
    `\t${context !== '' ? `${context}.` : ''}${content}\n`;
  const formatEquation: FormatFunc = ({ content, context }: ContextContent) =>
    `\t${context !== '' ? `${context}: ` : ''}${content}\n`;

  const formatObjList = (formatObj: FormatFunc, ogList?: ContextContent[]) =>
    ogList && ogList.length > 0 ? (
      ogList.map(formatObj).join('')
    ) : (
      <>{'\tNone\n'}</>
    );

  const nUnknowns = mathPb.nUnknowns === undefined ? 0 : mathPb.nUnknowns;
  const nEquations = mathPb.nEquations === undefined ? 0 : mathPb.nEquations;

  return (
    <>
      <div>{`${nUnknowns}x${nEquations} problem`}</div>
      <br />
      <div className="mathPb">
        <div>Unknowns :</div>
        {formatObjList(formatUnknown, mathPb.unknowns)}
        <br />
        <div>Equations :</div>
        {formatObjList(formatEquation, mathPb.equations)}
      </div>
    </>
  );
}

export default MathPbDisplay;

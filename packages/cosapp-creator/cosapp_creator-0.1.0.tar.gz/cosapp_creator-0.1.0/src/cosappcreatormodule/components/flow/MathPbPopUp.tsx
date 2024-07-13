import React, { useEffect, useState } from 'react';

import { FlowCenteredPopUp } from '../PopUp';
import MathPbDisplay from '../MathProblem';

import { ContextContent, MathProblem } from '../../tools/customTypes';

export type MathProblemProp = MathProblem[] | undefined;

interface MathPbProps {
  mathProblems: MathProblemProp;
  setMathProblems: (val: MathProblemProp, options?: any) => void;
}

function MathPbPopUp(props: MathPbProps) {
  const [finalMathPb, setFinalMathPb] = useState<MathProblem>({
    nUnknowns: 0,
    nEquations: 0,
    unknowns: [],
    equations: []
  });

  const { mathProblems } = props;
  useEffect(() => {
    if (mathProblems) {
      let newNbUnk = 0;
      let newNbEqua = 0;
      let newUnknowns: ContextContent[] = [];
      let newEquations: ContextContent[] = [];

      mathProblems.forEach(({ nUnknowns, nEquations, unknowns, equations }) => {
        newNbUnk += nUnknowns || 0;
        newNbEqua += nEquations || 0;
        if (unknowns) newUnknowns = newUnknowns.concat(unknowns);
        if (equations) newEquations = newEquations.concat(equations);
      });

      setFinalMathPb({
        nUnknowns: newNbUnk,
        nEquations: newNbEqua,
        unknowns: newUnknowns,
        equations: newEquations
      });
    }
  }, [mathProblems]);

  const closePopUp = () => props.setMathProblems(undefined);

  return (
    <FlowCenteredPopUp className="mathPbPopUp" closePopUp={closePopUp}>
      <MathPbDisplay mathPb={finalMathPb} />
      <br />
      <button type="button" onClick={closePopUp}>
        ok
      </button>
    </FlowCenteredPopUp>
  );
}

export default MathPbPopUp;

import React from 'react';

import { FlowCenteredPopUp } from '../PopUp';

interface ErrorProps {
  errorMessage: string[];
  setErrorMessage: (val: string[], options?: any) => void;
}

function ErrorPopUp(props: ErrorProps) {
  const closePopUp = () => props.setErrorMessage([]);

  return (
    <FlowCenteredPopUp className="errorPopUp" closePopUp={closePopUp}>
      <ul>
        {props.errorMessage.map(str => (
          <li key={str}>{str}</li>
        ))}
      </ul>
      <button type="button" onClick={closePopUp}>
        ok
      </button>
    </FlowCenteredPopUp>
  );
}

export default ErrorPopUp;

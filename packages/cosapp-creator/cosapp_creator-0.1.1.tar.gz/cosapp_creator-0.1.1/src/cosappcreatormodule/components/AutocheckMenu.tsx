import React from 'react';
import { getConnErrorsParams } from '../tools/customTypes';

interface IProps {
  autocheck: boolean;
  setAutocheck: (val: boolean, options?: any) => void;
  getConnErrors: (params: getConnErrorsParams) => Promise<void>;
}

/**
 * Menu for connection autocheck
 */
function autocheckMenu(props: IProps) {
  const { autocheck } = props;
  const checkboxId = 'testCheckBox';

  return (
    <div className="connCheckMenu">
      <label htmlFor={checkboxId}>
        Autocheck connections
        <input
          type="checkbox"
          id={checkboxId}
          checked={autocheck}
          onChange={() => props.setAutocheck(!autocheck)}
        />
      </label>
      <button
        type="button"
        onClick={() => props.getConnErrors({ check: true })}
        disabled={autocheck}
      >
        Check
      </button>
    </div>
  );
}

export default autocheckMenu;

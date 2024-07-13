import React from 'react';

import { FlowCenteredPopUp } from '../PopUp';
import { OkCrossForm } from '../OkCrossButtons';

import { getConnErrorsParams } from '../../tools/customTypes';

interface ResetProps {
  setShowResetPopUp: (val: boolean, options?: any) => void;
  getConnErrors: (params: getConnErrorsParams) => Promise<void>;
}

/** Pop up to confirm assembly reset */
function ResetPopUp(props: ResetProps) {
  const closePopUp = () => props.setShowResetPopUp(false);

  const resetFlow = () => {
    props.getConnErrors({
      newSystemList: [],
      newConnectionList: [],
      newSysPullsDict: {}
    });
    closePopUp();
  };

  return (
    <FlowCenteredPopUp closePopUp={closePopUp}>
      Do you really want to reset the systems and connections of your assembly?
      <OkCrossForm handleOk={resetFlow} closePopUp={closePopUp} />
    </FlowCenteredPopUp>
  );
}

export default ResetPopUp;

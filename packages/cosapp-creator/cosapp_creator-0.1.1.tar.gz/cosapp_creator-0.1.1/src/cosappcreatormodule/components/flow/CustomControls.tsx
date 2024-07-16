import React from 'react';
import { Controls, ControlButton, ControlProps } from 'reactflow';

interface testProps {
  setShowResetPopUp: (val: boolean, options?: any) => void;
}

function CustomControls(props: ControlProps & testProps) {
  return (
    <Controls>
      <ControlButton onClick={() => props.setShowResetPopUp(true)}>
        &#8635;
      </ControlButton>
    </Controls>
  );
}

export default CustomControls;

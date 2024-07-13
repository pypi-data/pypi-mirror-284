import React, { useState, useEffect, useRef } from 'react';

import { MousePopUp } from '../../PopUp';

import {
  ClientPosition,
  getConnErrorsParams,
  pullingPortInfos,
  sysPullType
} from '../../../tools/customTypes';
import { addPortPulling } from '../../../tools/genericFunctions';
import { sysNameCrit } from '../../../tools/widgetParams';

interface IProps {
  sysPullsDict: sysPullType;
  getConnErrors: (params: getConnErrorsParams) => Promise<void>;
  setShow: (val: boolean, options?: any) => void;
  infos: pullingPortInfos;
  mousePos: ClientPosition;
}

/** Pop up for port pulling */
function PopUp(props: IProps) {
  const { infos, setShow } = props;
  const { portName } = infos;
  const [mapping, setMapping] = useState(infos.mapping || portName);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => inputRef.current?.select(), []);

  /** Close pop up if the name mapping follows CoSApp pattern */
  const handleKeyUp = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      const input = inputRef.current;
      if (input && input.reportValidity()) {
        addPortPulling(
          {
            port: portName,
            portMapping: mapping !== '' ? mapping : portName
          },
          infos.systemName,
          props.sysPullsDict,
          props.getConnErrors
        );
        setShow(false);
      }
    }
    e.preventDefault();
  };

  return (
    <MousePopUp
      className="fullPullPopUp"
      mousePos={props.mousePos}
      closePopUp={() => setShow(false)}
    >
      <input
        ref={inputRef}
        type="text"
        className="defaultTextInput portName"
        value={mapping}
        placeholder="Name mapping"
        {...sysNameCrit}
        required
        onChange={e => setMapping(e.target.value)}
        onKeyUp={handleKeyUp}
      />
    </MousePopUp>
  );
}

export default PopUp;

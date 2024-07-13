import React, { useState } from 'react';

import { MousePopUp } from '../PopUp';
import { OkCrossButtons } from '../OkCrossButtons';

import { ClientPosition, Kwargs, systemType } from '../../tools/customTypes';

export type kwargsPropsType = {
  name: string;
  kwargs: Kwargs;
  mousePos: ClientPosition;
};

interface DynamicInputsProps {
  formState: Kwargs;
  handleInputChange: (
    event: React.ChangeEvent<HTMLInputElement>,
    change: string
  ) => void;
}

function DynamicInputs(props: DynamicInputsProps) {
  const { formState } = props;
  return (
    <>
      {Object.entries(formState).map(([varName, value]) => (
        <div className="field" key={varName}>
          <div className="label">
            <label htmlFor={varName}>{`${varName}: `}</label>
          </div>
          <input
            id={varName}
            value={value}
            onChange={e => props.handleInputChange(e, varName)}
            placeholder="Value"
            className="defaultTextInput"
          />
        </div>
      ))}
    </>
  );
}

interface SystemKwargsProps {
  kwargsProps: kwargsPropsType;
  setShow: (val: boolean, options?: any) => void;
  systemList: systemType[];
  setSystemList: (val: systemType[], options?: any) => void;
}

/** Pop up for changing kwargs value */
function KwargsPopUp(props: SystemKwargsProps) {
  const { name, kwargs, mousePos: position } = props.kwargsProps;
  const closePopUp = () => props.setShow(false);

  const [formState, setFormState] = useState(kwargs);

  const handleInputChange = (
    event: React.ChangeEvent<HTMLInputElement>,
    varName: string
  ) => {
    const kwargsInputs = { ...formState };
    kwargsInputs[varName] = event.target.value;
    setFormState(kwargsInputs);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const newSystemList = props.systemList.map(system => ({
      ...system,
      kwargs: system.name === name ? { ...formState } : system.kwargs
    }));
    props.setSystemList(newSystemList);
    closePopUp();
  };

  return (
    <MousePopUp closePopUp={closePopUp} mousePos={position}>
      <div className="center">
        <div>Kwargs:</div>
        <div style={{ color: 'orange' }}>
          &#9888; Structure kwarg modification not supported
        </div>
      </div>
      <form onSubmit={handleSubmit} action="demo" className="formPopUp">
        <DynamicInputs
          formState={formState}
          handleInputChange={handleInputChange}
        />
        <OkCrossButtons closePopUp={closePopUp} />
      </form>
    </MousePopUp>
  );
}

export default KwargsPopUp;

import React, { useEffect, useState } from 'react';

import { OkCrossButtons } from '../../OkCrossButtons';
import { MousePopUp } from '../../PopUp';

import {
  ClientPosition,
  getConnErrorsParams,
  portVariableType,
  sysPullType
} from '../../../tools/customTypes';
import { addPortPulling } from '../../../tools/genericFunctions';
import { sysNameCrit, systemFlowId } from '../../../tools/widgetParams';

type formStateType = { id: string; mapping: string; isChecked: boolean };

interface IPropsCh {
  formState: formStateType[];
  onCheckboxChange: (
    event: React.ChangeEvent<HTMLInputElement>,
    change: formStateType
  ) => void;
  onInputChange: (
    event: React.ChangeEvent<HTMLInputElement>,
    change: formStateType
  ) => void;
}

function DynamicCheckbox(props: IPropsCh) {
  return (
    <>
      {props.formState.map(variable => {
        const { id, isChecked, mapping } = variable;
        return (
          <div key={id} className="field">
            <div className="hiddenOverflow label">
              <label htmlFor={id}>{`${id}: `}</label>
            </div>
            <div className="inputs">
              <input
                type="checkbox"
                id={id}
                value={id}
                checked={isChecked}
                onChange={e => props.onCheckboxChange(e, variable)}
              />
              <input
                type="text"
                className="defaultTextInput"
                id={id}
                value={mapping}
                onChange={e => props.onInputChange(e, variable)}
                placeholder="Name mapping"
                {...sysNameCrit}
              />
            </div>
          </div>
        );
      })}
    </>
  );
}

interface IProps {
  sysPullsDict: sysPullType;
  getConnErrors: (params: getConnErrorsParams) => Promise<void>;
  setShow: (val: boolean, options?: any) => void;
  portName: string;
  systemName: string;
  portVar: portVariableType[];
  mousePos: ClientPosition;
}

/** Pop up for partial pulling */
function VarPopUp(props: IProps) {
  const { portName, sysPullsDict, getConnErrors } = props;
  const [isMounted, setIsMounted] = useState(false);
  const closePopUp = () => props.setShow(false);

  // get pulling data if the port is partially connected
  const sysPulls = sysPullsDict[props.systemName] || [];
  const pulledPort = sysPulls.find(
    ({ port, variables }) => variables && port === portName
  );
  const pulledVarList = pulledPort?.variables || [];

  const initChecked = pulledVarList.length === 0;
  const initialFormState: formStateType[] = props.portVar.map(({ name }) => {
    const existingPull = pulledVarList.find(
      pulledVar => pulledVar.name === name
    );
    const isChecked = existingPull ? true : initChecked;
    const existingMap = existingPull ? existingPull.mapping : undefined;

    return {
      id: name,
      mapping: existingMap || isChecked ? name : '',
      isChecked
    };
  });

  const [formState, setFormState] = useState(initialFormState);

  /** Handle checkbox change and empty input if it is not checked */
  const handleCheckboxChange = (
    event: React.ChangeEvent<HTMLInputElement>,
    change: formStateType
  ) => {
    const variables = formState.map(variable =>
      variable.id === change.id
        ? {
            ...variable,
            isChecked: event.target.checked,
            mapping: event.target.checked ? variable.mapping : ''
          }
        : variable
    );
    setFormState(variables);
  };

  /** Handle input change and uncheck if the input is empty */
  const handleInputChange = (
    event: React.ChangeEvent<HTMLInputElement>,
    change: formStateType
  ) => {
    const variables = formState.map(variable =>
      variable.id === change.id
        ? {
            ...variable,
            mapping: event.target.value,
            isChecked: event.target.value !== ''
          }
        : variable
    );
    setFormState(variables);
  };

  /** Add pulling to sysPullsDict */
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    const pullingVar = formState
      .filter(({ isChecked, mapping }) => isChecked || mapping !== '')
      .map(({ id, mapping }) => ({ name: id, mapping: mapping || id }));

    if (pullingVar.length > 0) {
      addPortPulling(
        {
          port: portName,
          variables: pullingVar
        },
        props.systemName,
        sysPullsDict,
        getConnErrors
      );
    } else {
      const newSysPullsDict: sysPullType = {};
      Object.entries(sysPullsDict).forEach(([sysName, sysPullings]) => {
        if (sysName !== props.systemName)
          newSysPullsDict[sysName] = sysPullings;
      });
      getConnErrors({ newSysPullsDict });
    }
    e.preventDefault();
  };

  // for closing pop up
  useEffect(() => {
    setIsMounted(true);
  }, []);
  useEffect(() => {
    if (isMounted) props.setShow(false);
  }, [sysPullsDict]);

  return (
    <MousePopUp
      closePopUp={closePopUp}
      mousePos={props.mousePos}
      elementId={systemFlowId}
    >
      <form onSubmit={handleSubmit} action="demo" className="formPopUp">
        <DynamicCheckbox
          formState={formState}
          onCheckboxChange={handleCheckboxChange}
          onInputChange={handleInputChange}
        />
        <OkCrossButtons closePopUp={closePopUp} />
      </form>
    </MousePopUp>
  );
}

export default VarPopUp;

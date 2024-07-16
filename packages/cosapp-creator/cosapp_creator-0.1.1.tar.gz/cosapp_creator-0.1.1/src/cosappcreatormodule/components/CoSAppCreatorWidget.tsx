import React, { useEffect, useState } from 'react';

import ImportSaveForm from './ImportSaveForm';
import AutocheckMenu from './AutocheckMenu';
import SystemFlowProvider from './flow/SystemFlowProvider';
import CodeButton from './CodeButton';
import FileNameInput from './HiddenInput';
import HelpButton from './HelpButton';

import { widgetId } from '../tools/widgetParams';
import { MathProblemProp } from './flow/MathPbPopUp';
import { getSysType, mergeSysPulls } from '../tools/genericFunctions';
import {
  connectionType,
  designMethodType,
  equationType,
  eventType,
  extPortVariableType,
  packDataType,
  sysPullType,
  systemType,
  unknownType,
  getConnErrorsParams,
  ReplacePack,
  MathProblem,
  ContextContent
} from '../tools/customTypes';

import demoPackage from '../ccube (demoPackage).json';

import 'reactflow/dist/style.css';

import '../css/widget.css';
import '../css/flow.css';
import '../css/popup.css';
import '../css/code.css';
import '../css/sidebar.css';
import { ApiClient } from '../tools/apiTool';

interface WidgetProps {
  apiClient: ApiClient;
}

type MessageErrorDict = { message: string };

type DataError = { kind: 'data' } & MessageErrorDict;
type PullError = { kind: 'pull'; mapping: string } & MessageErrorDict;
type ConnError = {
  kind: 'conn';
  connection: connectionType;
} & MessageErrorDict;
type CoSAppError = DataError | PullError | ConnError;

const delay = (ms: number) => new Promise(res => setTimeout(res, ms));

export function CoSAppCreatorWidget(props: WidgetProps) {
  // states
  const [fileName, setFileName] = useState('AssemblyName');
  const [errorMessage, setErrorMessage] = useState<string[]>([]);
  const [mathProblems, setMathProblems] = useState<MathProblemProp>(undefined);
  const [autocheck, setAutocheck] = useState(true);

  const [systemList, setSystemList] = useState<systemType[]>([]);
  const [connectionList, setConnectionList] = useState<connectionType[]>([]);
  const [sysPullsDict, setSysPullsDict] = useState<sysPullType>({});
  const [inwardList, setInwardList] = useState<extPortVariableType[]>([]);
  const [outwardList, setOutwardList] = useState<extPortVariableType[]>([]);
  const [designMethodList, setDesignMethodList] = useState<designMethodType[]>(
    []
  );
  const [offDesignUnknownList, setOffDesignUnknownList] = useState<
    unknownType[]
  >([]);
  const [offDesignEquationList, setOffDesignEquationList] = useState<
    equationType[]
  >([]);
  const [eventList, setEventList] = useState<eventType[]>([]);
  const [packages, setPackages] = useState<packDataType[]>([]);

  // import pop up
  const [replace, setReplace] = useState<ReplacePack>({});

  // for changing assembly name
  const [showInput, setShowInput] = useState(false);

  const formatContext = (sysName: string, mathList?: ContextContent[]) =>
    (mathList || []).map(({ content, context }) => ({
      context: context === '' ? sysName : `${sysName}.${context}`,
      content
    }));

  const getMathPb = (): MathProblem[] =>
    systemList.flatMap(({ name: sysName, type, pack }) => {
      const { mathProblem: classPb } = getSysType(type, pack, packages);
      if (classPb) {
        const { unknowns, equations } = classPb;

        return {
          ...classPb,
          unknowns: formatContext(sysName, unknowns),
          equations: formatContext(sysName, equations)
        };
      }
      return [];
    });

  // API
  const { apiClient } = props;
  const [wrongConns, setWrongConns] = useState<connectionType[]>([]);
  const [wrongPulls, setWrongPulls] = useState<string[]>([]);

  /**
   * Set `errorMessage`, `wrongConns` and `wrongPulls` based on `errors`.
   * @param errors list of errors
   */
  const handleCoSAppErrors = (errors: Array<CoSAppError>) => {
    const newMessages: string[] = [];
    const newWrongConns: connectionType[] = [];
    const newWrongPulls: string[] = [];
    errors.forEach(err => {
      newMessages.push(err.message);
      switch (err.kind) {
        case 'pull':
          newWrongPulls.push(err.mapping);
          break;
        case 'conn':
          newWrongConns.push(err.connection);
          break;
        default:
          break;
      }
    });
    setErrorMessage(newMessages);
    setWrongConns(newWrongConns);
    setWrongPulls(newWrongPulls);
  };

  /**
   * Make an APi call if `test` or `override` are `true`.
   *
   * Set `systemList` to `newSystemList` if `newSystemList` is not equal to `systemList`.
   *
   * Set `connectionList` to `newConnectionList`
   * and `sysPullsDict` to `newSysPullsDict`
   * if the API manages to build the assembly without errors.
   *
   * If `test` is `false`,
   * set `connectionList` and `sysPullsDict` without calling the API.
   * @param newSystemList new list of systems (optional)
   * @param newConnectionList new list of connections to test (optional)
   * @param newSysPullsDict new list of pullings to test (optional)
   * @param test state for autocheck (optional)
   */
  const getConnErrors = async ({
    newSystemList = systemList,
    newConnectionList = connectionList,
    newSysPullsDict = sysPullsDict,
    check = autocheck
  }: getConnErrorsParams) => {
    let errors: CoSAppError[] | undefined;
    if (
      check &&
      (newConnectionList.length > 0 || Object.keys(newSysPullsDict).length > 0)
    ) {
      try {
        const response = await apiClient.update({
          url: 'detectConnectionError',
          headers: { Accept: 'application/json' },
          data: {
            systemList: mergeSysPulls(newSystemList, newSysPullsDict),
            connectionList: newConnectionList,
            packages
          }
        });
        errors = response.data;
      } catch (e) {
        console.error(e);
      }
    } else {
      // bug when renaming a system with pullings without autocheck without it
      await delay(1);
    }
    if (!errors || errors.length === 0) {
      // no errors
      if (newSystemList !== systemList) {
        setSystemList(newSystemList);
      }
      setConnectionList(newConnectionList);
      setSysPullsDict(newSysPullsDict);
    } else {
      handleCoSAppErrors(errors);
    }
  };

  type LoopsResult = { loops: MathProblem; errors: CoSAppError[] };
  /** Make an APi call that returns loops in the assembly. */
  const checkLoops = async (allPb?: boolean) => {
    try {
      const response = await apiClient.update({
        url: 'getLoops',
        headers: { Accept: 'application/json' },
        data: {
          systemList: mergeSysPulls(systemList, sysPullsDict),
          connectionList,
          packages
        }
      });
      const { loops, errors }: LoopsResult = response.data;
      if (errors.length === 0) {
        const newMathPbList = allPb ? [loops, ...getMathPb()] : [loops];
        setMathProblems(newMathPbList);
      } else {
        handleCoSAppErrors(errors);
      }
    } catch (e) {
      console.error(e);
    }
  };

  useEffect(() => setErrorMessage([]), [packages]);

  return (
    <div id={widgetId} className="cosapp_creator">
      <ImportSaveForm
        fileName={fileName}
        setFileName={setFileName}
        packages={packages}
        setPackages={setPackages}
        setReplace={setReplace}
        setErrorMessage={setErrorMessage}
        systemList={systemList}
        connectionList={connectionList}
        sysPullsDict={sysPullsDict}
        getConnErrors={getConnErrors}
        inwardList={inwardList}
        setInwardList={setInwardList}
        outwardList={outwardList}
        setOutwardList={setOutwardList}
        designMethodList={designMethodList}
        setDesignMethodList={setDesignMethodList}
        offDesignUnknownList={offDesignUnknownList}
        setOffDesignUnknownList={setOffDesignUnknownList}
        offDesignEquationList={offDesignEquationList}
        setOffDesignEquationList={setOffDesignEquationList}
        eventList={eventList}
        setEventList={setEventList}
      />
      {packages.length > 0 ? (
        <>
          <AutocheckMenu
            autocheck={autocheck}
            setAutocheck={setAutocheck}
            getConnErrors={getConnErrors}
          />
          <div className="assemblyNameContainer">
            {showInput ? (
              <FileNameInput
                placeholder="AssemblyName"
                parentState={fileName}
                setParentState={setFileName}
                setShow={setShowInput}
              />
            ) : (
              <div onDoubleClick={() => setShowInput(true)}>{fileName}</div>
            )}
          </div>
          <SystemFlowProvider
            packages={packages}
            setPackages={setPackages}
            replace={replace}
            setReplace={setReplace}
            systemList={systemList}
            setSystemList={setSystemList}
            connectionList={connectionList}
            sysPullsDict={sysPullsDict}
            getConnErrors={getConnErrors}
            checkLoops={checkLoops}
            mathProblems={mathProblems}
            setMathProblems={setMathProblems}
            errorMessage={errorMessage}
            setErrorMessage={setErrorMessage}
            wrongConns={wrongConns}
            wrongPulls={wrongPulls}
          />
          <CodeButton
            assemblyName={fileName}
            systemList={systemList}
            connectionList={connectionList}
            sysPullsDict={sysPullsDict}
            inwardList={inwardList}
            outwardList={outwardList}
            designMethodList={designMethodList}
            offDesignUnknownList={offDesignUnknownList}
            offDesignEquationList={offDesignEquationList}
            eventList={eventList}
            packages={packages}
          />
        </>
      ) : (
        <>
          <div className="defaultText">
            {errorMessage.length === 0
              ? 'Please import a package'
              : errorMessage.join('\n')}
          </div>
          <div className="demoDiv">
            <button
              type="button"
              className="demoButton"
              onClick={() => setPackages([demoPackage])}
            >
              Use demo package
            </button>
            <HelpButton />
          </div>
        </>
      )}
    </div>
  );
}

import React, { useRef, useState } from 'react';
import { ReactFlowInstance, ReactFlowProvider } from 'reactflow';

import DragDropSidebar from '../sidebars/dragDrop/DragDropSidebar';
import ExecOrder from '../sidebars/ExecOrder';
import ConnectionPopUp from './connection/ConnectionPopUp';
import VarPopUp from './pulling/PullingVariablePopUp';
import PortPopUp from './pulling/PullingPortPopUp';
import SystemFlow from './SystemFlow';
import ErrorPopUp from './ErrorPopUp';
import KwargsPopUp, { kwargsPropsType } from './KwargsPopUp';
import ResetPopUp from './ResetPopUp';
import ImportPopUp from './ImportPopUp';

import {
  packDataType,
  systemType,
  connectionType,
  portVariableType,
  pullingPortInfos,
  sysPullType,
  getConnErrorsParams,
  ClientPosition,
  ReplacePack
} from '../../tools/customTypes';
import { systemFlowId } from '../../tools/widgetParams';
import MathPbPopUp, { MathProblemProp } from './MathPbPopUp';

export interface BaseFlowProps {
  packages: packDataType[];

  systemList: systemType[];
  setSystemList: (val: systemType[], options?: any) => void;

  connectionList: connectionType[];
  sysPullsDict: sysPullType;
  getConnErrors: (params: getConnErrorsParams) => Promise<void>;

  wrongConns: connectionType[];
  wrongPulls: string[];
}

export type connSysPortInfos = {
  from: {
    name: string;
    type: string;
    pack: string;
  };
  to: {
    name: string;
    type: string;
    pack: string;
  };
};

export type pullPortInfos = {
  name: string;
  type: string;
};

const handleContextMenu = (event: React.MouseEvent) => {
  event.stopPropagation();
  event.preventDefault();
};

// inits for the states to have the right type
const initconnSysPortInfos: connSysPortInfos = {
  from: { name: '', type: '', pack: '' },
  to: { name: '', type: '', pack: '' }
};

const initPullInfos: pullingPortInfos = {
  systemName: '',
  portName: '',
  mapping: undefined
};
const initPosition: ClientPosition = { clientX: 0, clientY: 0 };

const initKwargs: kwargsPropsType = {
  name: '',
  kwargs: {},
  mousePos: initPosition
};

interface FlowProviderProps {
  setPackages: (val: packDataType[], options?: any) => void;
  replace: ReplacePack;
  setReplace: (val: ReplacePack, options?: any) => void;

  errorMessage: string[];
  setErrorMessage: (val: string[], options?: any) => void;

  mathProblems: MathProblemProp;
  setMathProblems: (val: MathProblemProp, options?: any) => void;

  checkLoops: (allPb?: boolean) => Promise<void>;
}

/** Provider for system flow */
function SystemFlowWithProvider(props: BaseFlowProps & FlowProviderProps) {
  const {
    packages,
    systemList,
    setSystemList,
    connectionList,
    sysPullsDict,
    getConnErrors,
    errorMessage,
    setErrorMessage,
    mathProblems
  } = props;

  // connection pop up
  const [showConnPopUp, setShowConnPopUp] = useState(false);
  const [portsConn, setPortsConn] = useState(initconnSysPortInfos);
  const [sysConn, setSysConn] = useState(initconnSysPortInfos);
  const [indexConn, setIndexConn] = useState(-1);
  // -1 = connection doesn't already exist, >0 = connection index

  // pulling variables pop up
  const [showPullingVariablePopUp, setShowPullingVariablePopUp] =
    useState(false);
  const [portPullName, setPortPullName] = useState('');
  const [sysNamePull, setSysNamePull] = useState('');
  const [portVarPull, setPortVarPull] = useState<portVariableType[]>([]);

  // pulling port pop up
  const [showPullingPortPopUp, setShowPullingPortPopUp] = useState(false);
  const [portPullInfos, setPortPullnfos] = useState(initPullInfos);
  const [position, setPosition] = useState(initPosition);

  // kwargs pop up
  const [showKwargs, setShowKwargs] = useState(false);
  const [kwargsProps, setKwargsProps] = useState(initKwargs);

  // reset pop up
  const [showResetPopUp, setShowResetPopUp] = useState(false);

  // flow instance
  const reactFlowWrapper = useRef<HTMLDivElement>(null);
  const [flowInstance, setFlowInstance] = useState<ReactFlowInstance>();

  return (
    <div
      className="container flowProvider"
      id={systemFlowId}
      onContextMenu={handleContextMenu}
    >
      {showConnPopUp ? (
        <ConnectionPopUp
          setShow={setShowConnPopUp}
          ports={portsConn}
          systems={sysConn}
          index={indexConn}
          setIndex={setIndexConn}
          packages={packages}
          connectionList={connectionList}
          sysPullsDict={sysPullsDict}
          getConnErrors={getConnErrors}
        />
      ) : (
        ''
      )}
      {showPullingVariablePopUp ? (
        <VarPopUp
          setShow={setShowPullingVariablePopUp}
          portName={portPullName}
          systemName={sysNamePull}
          portVar={portVarPull}
          mousePos={position}
          sysPullsDict={sysPullsDict}
          getConnErrors={getConnErrors}
        />
      ) : (
        ''
      )}
      {showPullingPortPopUp ? (
        <PortPopUp
          setShow={setShowPullingPortPopUp}
          infos={portPullInfos}
          mousePos={position}
          sysPullsDict={sysPullsDict}
          getConnErrors={getConnErrors}
        />
      ) : (
        ''
      )}
      {showKwargs && kwargsProps.kwargs ? (
        <KwargsPopUp
          kwargsProps={kwargsProps}
          setShow={setShowKwargs}
          systemList={systemList}
          setSystemList={setSystemList}
        />
      ) : (
        ''
      )}
      {errorMessage.length > 0 ? (
        <ErrorPopUp
          errorMessage={errorMessage}
          setErrorMessage={setErrorMessage}
        />
      ) : (
        ''
      )}
      {mathProblems ? (
        <MathPbPopUp
          mathProblems={mathProblems}
          setMathProblems={props.setMathProblems}
        />
      ) : (
        ''
      )}
      {showResetPopUp ? (
        <ResetPopUp
          setShowResetPopUp={setShowResetPopUp}
          getConnErrors={getConnErrors}
        />
      ) : (
        ''
      )}
      {props.replace.index && props.replace.index > -1 && props.replace.pack ? (
        <ImportPopUp
          packages={packages}
          setPackages={props.setPackages}
          replace={props.replace}
          setReplace={props.setReplace}
        />
      ) : (
        ''
      )}

      <ExecOrder
        systemList={systemList}
        setSystemList={setSystemList}
        checkLoops={props.checkLoops}
      />
      <ReactFlowProvider>
        <div
          className="flowContainer"
          ref={reactFlowWrapper}
          id="flowContainer"
        >
          <SystemFlow
            {...props}
            setShowConnPopUp={setShowConnPopUp}
            setSysConn={setSysConn}
            setPortsConn={setPortsConn}
            setIndexConn={setIndexConn}
            setShowPullingVariablePopUp={setShowPullingVariablePopUp}
            setPortPullName={setPortPullName}
            setSysNamePull={setSysNamePull}
            setPortVarPull={setPortVarPull}
            setShowPullingPortPopUp={setShowPullingPortPopUp}
            setPortPullnfos={setPortPullnfos}
            setPosition={setPosition}
            setShowKwargs={setShowKwargs}
            setKwargsProps={setKwargsProps}
            reactFlowWrapper={reactFlowWrapper}
            flowInstance={flowInstance}
            setFlowInstance={setFlowInstance}
            setShowResetPopUp={setShowResetPopUp}
          />
        </div>
        <DragDropSidebar packages={packages} />
      </ReactFlowProvider>
    </div>
  );
}

export default SystemFlowWithProvider;

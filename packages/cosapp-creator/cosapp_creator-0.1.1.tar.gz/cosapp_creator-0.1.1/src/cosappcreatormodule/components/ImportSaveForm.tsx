import React, { useRef } from 'react';

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
  ReplacePack
} from '../tools/customTypes';

interface IProps {
  fileName: string;
  setFileName: (val: string, options?: any) => void;
  setErrorMessage: (val: string[], options?: any) => void;

  packages: packDataType[];
  setPackages: (val: packDataType[], options?: any) => void;
  setReplace: (val: ReplacePack, options?: any) => void;

  systemList: systemType[];
  connectionList: connectionType[];
  sysPullsDict: sysPullType;
  getConnErrors: (params: getConnErrorsParams) => Promise<void>;

  inwardList: extPortVariableType[];
  setInwardList: (val: extPortVariableType[], options?: any) => void;
  outwardList: extPortVariableType[];
  setOutwardList: (val: extPortVariableType[], options?: any) => void;
  designMethodList: designMethodType[];
  setDesignMethodList: (val: designMethodType[], options?: any) => void;
  offDesignUnknownList: unknownType[];
  setOffDesignUnknownList: (val: unknownType[], options?: any) => void;
  offDesignEquationList: equationType[];
  setOffDesignEquationList: (val: equationType[], options?: any) => void;
  eventList: eventType[];
  setEventList: (val: eventType[], options?: any) => void;
}

/**
 * Set an object if the parameter is not `undefined`
 * @param obj object to set
 * @param setObj setter of the object
 */
const setList = (
  obj: any[],
  setObj: (val: typeof obj, options?: any) => void
) => {
  if (typeof obj !== 'undefined') {
    setObj(obj);
  } else {
    setObj([]);
  }
};

/** Menu for import and save functionalities */
function ImportSaveButton(props: IProps) {
  const { fileName, packages, setPackages } = props;
  const fileInput = useRef<HTMLInputElement>(null);

  /** Create and save a file containing all assembly data */
  const handleSaveClick = (e: React.FormEvent) => {
    if (fileName !== '') {
      const assembly = {
        systemList: props.systemList,
        connectionList: props.connectionList,
        sysPullsDict: props.sysPullsDict,
        inwardList: props.inwardList,
        outwardList: props.outwardList,
        designMethodList: props.designMethodList,
        offDesignUnknownList: props.offDesignUnknownList,
        offDesignEquationList: props.offDesignEquationList,
        eventList: props.eventList
      };
      const dataStr = `data:text/json;charset=utf-8,${encodeURIComponent(JSON.stringify(assembly))}`;
      const dlNode = document.createElement('a');
      dlNode.setAttribute('href', dataStr);
      dlNode.setAttribute('download', `${fileName}.json`);
      document.body.appendChild(dlNode);
      dlNode.click();
      dlNode.remove();
    }

    e.preventDefault();
  };

  /**
   * Return names of all packages neeeded for `sysList` that aren't imported
   * @param sysList list of systems
   * @returns list of packages not imported
   */
  const getNotImportedPackages = (sysList: systemType[]) => {
    const notInPacks = sysList.filter(
      ({ pack }) => !packages.some(({ name }) => name === pack)
    );
    const notImportedPacks = new Set(notInPacks.map(({ pack }) => pack));
    return [...notImportedPacks];
  };

  /**
   * Add a package to the list of packages.
   *
   * If a package with the same name is already in `packages`,
   * open a pop up.
   * @param pack package to add to `packages`
   */
  const addPackage = (pack: packDataType) => {
    const index = packages.findIndex(
      ({ name: tryName }) => tryName === pack.name
    );
    if (index > 0)
      props.setReplace({ index, pack }); // replace pop up if package with same name
    else setPackages([...packages].concat(pack));
  };

  /** Import package or assembly from a file */
  const handleFileImport = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { files } = event.target;
    if (files) {
      const file = files[0];
      new Response(file).json().then(
        json => {
          if (typeof json.name === 'undefined') {
            // check if file is a package or an assembly
            const newSystemList = json.systemList;
            if (newSystemList) {
              // if no systems, invalid import
              const notImportedPackages = getNotImportedPackages(newSystemList);
              if (notImportedPackages.length === 0) {
                props.setFileName(file.name.split('.', 1)[0]);
                props.getConnErrors({
                  newSystemList,
                  newConnectionList: json.connectionList,
                  newSysPullsDict: json.sysPullsDict
                });
                setList(json.inwardList, props.setInwardList);
                setList(json.outwardList, props.setOutwardList);
                setList(json.designMethodList, props.setDesignMethodList);
                setList(
                  json.offDesignUnknownList,
                  props.setOffDesignUnknownList
                );
                setList(
                  json.offDesignEquationList,
                  props.setOffDesignEquationList
                );
                setList(json.eventList, props.setEventList);
              } else {
                props.setErrorMessage([
                  `Please import ${notImportedPackages.join(', ')} and retry`
                ]);
              }
            }
          } else {
            addPackage(json);
          }
        },
        () => {}
      );
    }
    // eslint-disable-next-line no-param-reassign
    event.target.value = '';
  };

  return (
    <div className="SaveImportMenu">
      <button
        type="button"
        aria-label="Import"
        onClick={() => fileInput.current?.click()}
      >
        Import Package/Assembly
      </button>
      <input
        type="file"
        ref={fileInput}
        accept=".json"
        style={{ display: 'none' }}
        onChange={handleFileImport}
      />
      {packages.length > 0 ? (
        <button type="button" onClick={handleSaveClick}>
          Save Assembly
        </button>
      ) : (
        ''
      )}
    </div>
  );
}

export default ImportSaveButton;

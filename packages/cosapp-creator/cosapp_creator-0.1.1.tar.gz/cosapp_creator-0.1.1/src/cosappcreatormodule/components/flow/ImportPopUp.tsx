import React from 'react';

import { FlowCenteredPopUp } from '../PopUp';
import { OkCrossForm } from '../OkCrossButtons';

import { packDataType, ReplacePack } from '../../tools/customTypes';

interface IProps {
  packages: packDataType[];
  setPackages: (val: packDataType[], options?: any) => void;
  replace: ReplacePack;
  setReplace: (val: ReplacePack, options?: any) => void;
}

/** Import pop up to confirm wether to replace a package or not */
function ImportPopUp(props: IProps) {
  const { pack, index } = props.replace;

  const closePopUp = () => {
    props.setReplace({});
  };

  /** Replace `packages[props.replace.index]` with `props.replace.pack` */
  const replacePackage = () => {
    if (pack && index) {
      const newPackages = [...props.packages];
      newPackages[index] = pack;
      props.setPackages(newPackages);
    }
    closePopUp();
  };

  return (
    <FlowCenteredPopUp closePopUp={closePopUp}>
      {`Do you want to replace ${pack?.name}?`}
      <OkCrossForm handleOk={replacePackage} closePopUp={closePopUp} />
    </FlowCenteredPopUp>
  );
}

export default ImportPopUp;

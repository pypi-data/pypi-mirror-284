import React, { useState } from 'react';

import { TreeData, PackageTree } from './DragDropSidebar';

import DragSystem from './SystemComponent';

interface FolderProps {
  name: string;
  treeData: TreeData;
}

/** Folder compenent containing folders and a system list. */
function FolderComponent(props: FolderProps) {
  const { folders, systemList } = props.treeData;
  const [isOpen, setIsOpen] = useState(true);

  const borderBottom = isOpen ? 'var(--sidebarFolderBorder)' : '';
  const folderArrow = isOpen ? <>&#9661;</> : <>&#9655;</>;
  const display = isOpen ? 'block' : 'none';

  const systemListComponent = systemList
    .sort((sys1, sys2) => (sys1.name > sys2.name ? 1 : -1))
    .map(system => <DragSystem key={system.name} sysType={system} />);

  return (
    <div className="folderContainer">
      <button
        type="button"
        className="hiddenOverflow"
        onClick={() => setIsOpen(!isOpen)}
        style={{ borderBottom }}
      >
        <div className="symbol">{folderArrow}</div>
        {props.name}
      </button>
      <div className="folder" style={{ display }}>
        <TreeComponent tree={folders} />
        {systemListComponent}
      </div>
    </div>
  );
}

/** Turn a tree into a `JSX.Element` containing a list of `FolderComponent`. */
function TreeComponent({ tree }: { tree: PackageTree }) {
  return (
    <>
      {Object.entries(tree)
        .sort(([folderName1], [folderName2]) =>
          folderName1 > folderName2 ? 1 : -1
        )
        .map(([folderName, data]) => (
          <FolderComponent key={folderName} name={folderName} treeData={data} />
        ))}
    </>
  );
}

export default TreeComponent;

import React from 'react';

import TreeComponent from './FoldersComponent';

import {
  IPropsPackages,
  packDataType,
  systemClassType
} from '../../../tools/customTypes';

// eslint-disable-next-line no-use-before-define
export type TreeData = { folders: PackageTree; systemList: systemClassType[] };
export type PackageTree = Record<string, TreeData>;

/** Returns `path.folders[key]`.
 * Create it if needed.
 * @param key
 * @param path
 */
const returnPath = (key: string, path: TreeData) => {
  const newPath = path.folders;
  let keyPath = newPath[key];
  if (!keyPath) {
    // create a new folder if it doesn't already exists
    newPath[key] = { folders: {}, systemList: [] };
    keyPath = newPath[key]; // path to the new folder
  }
  return keyPath;
};

/**
 * Remove levels containing only one folder and no system from a dictionary.
 * @param packageTree The tree to reduce
 * @returns Reduced tree
 */
function reducePackageDict(packageTree: PackageTree): PackageTree {
  let dictToReturn: PackageTree | undefined;
  const treeDicts = Object.values(packageTree);
  if (treeDicts.length === 1) {
    const { folders, systemList } = treeDicts[0];
    dictToReturn =
      systemList.length === 0 ? reducePackageDict(folders) : packageTree;
  }
  return dictToReturn || packageTree;
}

/**
 * Create a tree from all systems in package `pack` and reduce it.
 * @param pack
 * @returns dictionary ( `pack.name` = reduced tree )
 */
function getPackageDict(pack: packDataType): PackageTree {
  const packageDict: TreeData = { folders: {}, systemList: [] };

  pack.systems.forEach(system => {
    // create package dictionary
    let path = packageDict;
    system.mod.split('.').forEach(pathPart => {
      path = returnPath(pathPart, path);
    });
    path.systemList.push(system);
  });

  const folders = reducePackageDict({ mock: packageDict });

  // if there are systems in directly in the package
  const keys = Object.keys(folders);
  if (keys.length === 1 && keys[0] === pack.name) return folders;

  return {
    [pack.name]: {
      folders,
      systemList: []
    }
  };
}

/** Sidebar with a tree view of all packages. */
function DragDropSidebar(props: IPropsPackages) {
  return (
    <aside className="hiddenOverflow sidebar dragDropSidebar">
      <div className="ltr">
        <div className="title">Packages</div>
        <div className="tree">
          {props.packages.map(pack => (
            <TreeComponent key={pack.name} tree={getPackageDict(pack)} />
          ))}
        </div>
      </div>
    </aside>
  );
}

export default DragDropSidebar;

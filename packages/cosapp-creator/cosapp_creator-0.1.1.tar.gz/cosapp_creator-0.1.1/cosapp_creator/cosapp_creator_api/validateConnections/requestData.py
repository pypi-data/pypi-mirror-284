from typing import List, Dict, Tuple, Any

def appendOrCreateKey(dct: Dict[str, List[str]], key: str, value: Any):
    """Append `value` to `dict[key]` if `dict[key]` exists and create a list containing `value` if it doesn't
    """
    values = dct.setdefault(key, [])
    if value not in values:
        values.append(value)


def getClassesToCreate(packages: List[Dict[str, Any]], systemList: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Get all system and port class descriptions needed by `data`
    
    Returns:
    --------
    systemClassList: Dict[str, Any]
    portClassList: Dict[str, Any]
    """
    
    def getClassList(classNameDict: Dict[str, List[str]], getPort = False):
        """Get system classes and port class name if `getPort = True`, else get port classes
        
        Returns:
        --------
        objTypeList: [Dict[str, Dict]]
        portClassName: Dict[str, List[str]]
        """
        
        if (getPort):
            listName = 'systems'
            portClassNames: Dict[str, List[str]]  = dict()
        else:
            listName = 'ports'

        objTypeList = []
        for pack in packages:
            packageName = pack['name']
            if packageName in classNameDict:
                for objType in pack[listName]:
                    if objType['name'] in classNameDict[packageName]:
                        objTypeList.append(objType)
                        
                        if (getPort):
                            portList = (objType['inputs'] or []) + (objType['outputs'] or [])
                            for port in portList:
                                appendOrCreateKey(portClassNames, port['pack'], port['type'])  # get port class names
        if (getPort):
            return objTypeList, portClassNames
        else:
            return objTypeList
    
    systemClassNames: Dict[str, List[str]] = dict()
    for system in systemList:
        appendOrCreateKey(systemClassNames, system['pack'], system['type'])  # get system class names
    
    systemClassList, portClassNames = getClassList(systemClassNames, getPort = True)
    portClassList = getClassList(portClassNames)
    
    return systemClassList, portClassList
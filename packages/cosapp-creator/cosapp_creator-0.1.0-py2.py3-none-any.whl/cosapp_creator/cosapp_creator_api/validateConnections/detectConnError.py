from cosapp.base import System

from typing import List, Dict, Any, Union
from .createAssembly import createAssembly


def getConnVarDict(varDesc: Dict[str, str]) -> Dict[str, str]:
    """Return the dict argument for variables 
    """
    return { varDesc['from']: varDesc['to'] }


def getConnErrorMessage(error: Exception, connDesc: Dict[str, Any], vars = None):
    connFrom = f"{connDesc['systems']['from']}.{connDesc['ports']['from']}"
    connTo = f"{connDesc['systems']['to']}.{connDesc['ports']['to']}"
    if vars:
        connFrom += f".{vars['from']}"
        connTo += f".{vars['to']}"
    return f'{connFrom} \u2192 {connTo}: {str(error)}'


def getAllConnError(assembly: System, connDescList: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return a list of all errors generated when trying to connect ports and/or variables in an assembly
    """
    def getConnError(connDesc: Dict[str, Any]):
        errors = []
        systems = connDesc['systems']
        ports = connDesc['ports']
        varDescList = connDesc.get('variables', None)
        portFrom = assembly[systems['from']][ports['from']]
        portTo = assembly[systems['to']][ports['to']]
        if varDescList:
            for varDesc in varDescList:
                var = getConnVarDict(varDesc)
                try:
                    assembly.connect(
                        object1 = portFrom,
                        object2 = portTo,
                        mapping = var
                    )
                except Exception as error:
                    errors.append({
                        'kind': 'conn',
                        'connection': connDesc,
                        'message': getConnErrorMessage(error, connDesc, varDesc),
                    })
                    continue
        else:
            try:
                assembly.connect(
                    object1 = portFrom,
                    object2 = portTo,
                )
            except Exception as error:
                errors.append({
                    'kind': 'conn',
                    'connection': connDesc,
                    'message': getConnErrorMessage(error, connDesc),
                })
        return errors

    errors = []
    for connDesc in connDescList:
        errors.extend(getConnError(connDesc))
    return errors


def detectConnError(systemDescList: List[Dict[str, Any]], packagesDescList: List[Dict[str, Any]], connDescList: List[Dict[str, Any]]):
    """Returns all connection errors given a JSON description of a system state
    """
    errors: Union[List[Dict[str, Any]]]
    assembly = None
    if packagesDescList:
        if systemDescList:
            assembly, errors = createAssembly(packagesDescList, systemDescList)
            if connDescList:
                errors.extend(getAllConnError(assembly, connDescList))
        else:
            errors = [{ 'kind':'data', 'message': 'No systems'}]
    else:
        errors = [{ 'kind': 'data', 'message': 'No packages'}]
    return {'errors': errors, 'assembly': assembly}
from cosapp.base import System, Port
from typing import Type, List, Dict, Any, Union, Tuple

from .requestData import getClassesToCreate


def getUnit(var: Dict[str, Any]) -> str:
    return var.get('unit', '') or ''


def getClassName(name: str, pack: str) -> str:
    return f'{pack}_{name}'


def getClass(className: str, classList: List[Any]):
    """Returns Class in `classList` whose name is `className`
    """
    for classTest in classList:
        if classTest.__name__ == className:
            return classTest
    raise NameError(f'Class {className} not found')


def getPortPulling(pullingDesc: Dict[str, Any]) -> Dict[str, str]:
    """Returns dict for one pull from its json description
    """
    variables = pullingDesc.get('variables', None)
    port = pullingDesc['port']

    pullDict = dict()
    if variables:
        if port == 'inwards' or port == 'outwards' or port == 'modeVarIn' or port == 'modeVarOut' :
            port = ''
        else:
            port += '.'
        for var in variables:
            name = var['name']
            mapping = var.get('mapping', name) or name
            pullDict[name] = mapping
    else:
        pullDict[port] = pullingDesc.get('portMapping', port) or port
    return pullDict

 
def getAllSystemPulling(pullingsDesc: List[Dict[str, Any]]) -> Union[Dict[str, str], None]:
    """Returns dict for all pullings for one system from their json description
    """
    if pullingsDesc:
        argDict: Dict[str, str] = dict()
        for pull in pullingsDesc:
            argDict = {**argDict, **getPortPulling(pull)}
        return argDict
    return None


def createPortClass(portTypeDesc: Dict[str, Any]) -> Type[Port]:
    """Factory creating a port class from the JSON description of the port type
    """
    classname = getClassName(portTypeDesc['name'], portTypeDesc['pack'])
    variableList = portTypeDesc['variables']

    class PortMockup(Port):
        def setup(self):
            for var in variableList:
                self.add_variable(
                    name=var['name'],
                    unit=getUnit(var),
                    value=var.get('value', 0.0),  # value and dtype should be irrelevant, here
                )

    return type(classname, (PortMockup,), {})


def createSystemClass(sysTypeDesc: Dict[str, Any], portClassList: List[Any]) -> Type[System]:
    """Factory creating a system class from the JSON description of the system type
    """
    classname = getClassName(sysTypeDesc['name'], sysTypeDesc['pack'])
    inputs = sysTypeDesc['inputs'] or []
    outputs = sysTypeDesc['outputs'] or []

    class SystemMockup(System):
        def setup(self):
            for input_to_add in inputs:
                if input_to_add['type'] == 'ExtensiblePort':
                    for var in input_to_add['variables']:
                        self.add_inward(
                            definition=var['name'],
                            unit=getUnit(var),
                            value=var.get('value', 0.0),
                        )
                elif input_to_add['type'] == 'ModeVarPort':
                    for var in input_to_add['variables']:
                        self.add_inward_modevar(
                            name=var['name'],
                            unit=getUnit(var),
                            value=var.get('value', 0.0),
                        )
                else:
                    className = getClassName(input_to_add['type'], input_to_add['pack'])
                    inputClass = getClass(className, portClassList)
                    self.add_input(inputClass, input_to_add['name'])

            for output_to_add in outputs:
                if output_to_add['type'] == 'ExtensiblePort':
                    for var in output_to_add['variables']:
                        self.add_outward(
                            definition=var['name'],
                            unit=getUnit(var),
                            value=var.get('value', 0.0),
                        )
                elif output_to_add['type'] == 'ModeVarPort':
                    for var in output_to_add['variables']:
                        self.add_outward_modevar(
                            name=var['name'],
                            unit=getUnit(var),
                            value=var.get('value', 0.0),
                        )
                else:
                    className = getClassName(output_to_add['type'], output_to_add['pack'])
                    outputClass = getClass(className, portClassList)
                    self.add_output(outputClass, output_to_add['name'])

    return type(classname, (SystemMockup,), {})


def instantiateHeadSystem(systemListDesc: List[Dict[str, Any]], systemClassList: List[Any]) -> Tuple[System, List[Dict[str, Any]]]:
    """Create a class for the head system
    Return an instance of the class and a list containing error messages if any error happened during pullings
    """
    errors = []
    class HeadSystem(System):
        def pop_child(self, name):
            """Ignore errors when popping children"""
            try:
                super().pop_child(name)
            except Exception:
                pass

        def setup(self):
            for system in systemListDesc:
                classname=getClassName(system['type'], system['pack'])
                sysClass = getClass(classname, systemClassList)
                systemName = system['name']
                try:
                    self.add_child(
                        sysClass(systemName),
                        pulling=getAllSystemPulling(system.get('pullings', []))
                    )
                except Exception:
                    self.pop_child(systemName)

                    pullsDict = getAllSystemPulling(system.get('pullings', []))
                    for varChild, varParent in zip(pullsDict.keys(), pullsDict.values()): # try each pulling individually
                        try:
                            self.add_child(sysClass(systemName), pulling={ varChild: varParent })
                        except Exception as error:
                            errors.append({
                                'kind': 'pull',
                                'mapping': varParent,
                                'message': str(error)
                            })
                        self.pop_child(systemName)

                    try:
                        self.add_child(sysClass(systemName))
                    except ValueError:
                        pass
                    continue

    return HeadSystem('assembly'), errors


def createAssembly(packagesDesc: List[Dict[str, Any]], systemListDesc: List[Dict[str, Any]]) -> Tuple[System, List[Dict[str, Any]]]:
    """Create and return whole assembly from packages and system list description
    """
    systemClassDescList, portClassDescList = getClassesToCreate(packagesDesc, systemListDesc)
    
    portClassList = list(map(createPortClass, portClassDescList))
    systemClassList = [
        createSystemClass(systemDesc, portClassList)
        for systemDesc in systemClassDescList
    ]

    return instantiateHeadSystem(systemListDesc, systemClassList)
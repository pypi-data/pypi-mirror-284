from cosapp.base import System, Port
from cosapp.ports import PortType

from typing import OrderedDict

def assert_port(actualPort: Port, expectedPort: Port):
    assert len(actualPort) == len(expectedPort), f"different number of variables in {actualPort.owner.name}.{actualPort.name}"
    for actual, expected in zip(actualPort.variables(), expectedPort.variables()):
        assert actual.name == expected.name
        assert actual.to_dict() == expected.to_dict(), f"variable {actual.name}"


def assert_port_list(actPorts: OrderedDict[str, Port], expPorts: OrderedDict[str, Port]):
    assert len(actPorts) == len(expPorts), f"different number of ports in {actPorts}"
    for actualPort, expectedPort in zip(actPorts.values(), expPorts.values()):
        assert(actualPort.name == expectedPort.name)
        assert_port(actualPort, expectedPort)
        

def assert_system(actualSystem: System, expectedSystem: System):
    assert_port_list(actualSystem.inputs, expectedSystem.inputs)
    assert_port_list(actualSystem.outputs, expectedSystem.outputs)
    
    actualChildren = actualSystem.children.values()
    expectedChildren = expectedSystem.children.values()
    assert len(actualChildren) == len(expectedSystem.children), f"different number of children in {actualSystem.name}"
    for actualChild, expectedChild in zip(actualChildren, expectedChildren):
        assert actualChild.name == expectedChild.name
        assert_system(actualChild, expectedChild)


def assert_class(ActualClass, ExpectedClass, classname: str):
    assert ActualClass.__name__ == classname
 
    if issubclass(ExpectedClass, System):
        assert issubclass(ActualClass, System), f"{ActualClass.__name__} is not a system"
        assert_system(ActualClass("test"), ExpectedClass("test"))
        
        
    elif issubclass(ExpectedClass, Port):
        assert issubclass(ActualClass, Port), f"{ActualClass.__name__} is not a port"
        assert_port(ActualClass("test", PortType.IN), ExpectedClass("test", PortType.IN))
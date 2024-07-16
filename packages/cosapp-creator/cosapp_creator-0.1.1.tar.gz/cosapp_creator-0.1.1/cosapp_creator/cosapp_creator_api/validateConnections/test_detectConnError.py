import pytest

from cosapp.base import System, Port
# from cosapp.core import Connector

from .detectConnError import getConnVarDict, getAllConnError, detectConnError


def test_getConnVarDict():
    assert getConnVarDict({ "from": "A", "to": "B" }) == {'A': 'B'}

 
def test_createConns_getAllConnError(connDescList):

    class portType(Port):
        def setup(self):
            self.add_variable('A', unit='', value=0.0)

    class Sys1(System):
        def setup(self):
            self.add_output(portType, 'port_out')
            self.add_inward('var3')
            self.add_inward('var4')

    class Sys2(System):
        def setup(self):
            self.add_input(portType, 'port_in')
            self.add_outward('var1')
            self.add_outward('var2')

    class HeadSystem(System):
        def setup(self):
            self.add_child(Sys1('sys1'))
            self.add_child(Sys2('sys2'))

    assembly = HeadSystem('head')
    
    connError = getAllConnError(assembly, connDescList)
    expectedConnInfo = [
        ('sys2.port_in', 'sys1.port_out'),
        ('sys1.inwards', 'sys2.outwards', {'var3': 'var1', 'var4': 'var2'}),
    ]
    
    for conn, expConn in zip(assembly.connectors().values(), expectedConnInfo):
        assert conn.info() == expConn

    assert connError == []


def test_errors_getAllConnError(connDescList):
    
    connDescList.append({
            "systems": { "from": "sys1", "to": "sys2", },
            "ports": { "from": "port_out2", "to": "port_in", },
            "variables": None,
        })

    class portType(Port):
        def setup(self):
            self.add_variable('A', unit='', value=0.0)
            
    class Sys1(System):
        def setup(self):
            self.add_output(portType, 'port_out')
            self.add_output(portType, 'port_out2')
            self.add_inward('var3', unit='K')
            self.add_inward('var4', unit='C')
            
    class Sys2(System):
        def setup(self):
            self.add_input(portType, 'port_in')
            self.add_outward('var1', unit='m')
            self.add_outward('var2', unit='C')
            
    class HeadSystem(System):
        def setup(self):
            self.add_child(Sys1('sys1'))
            self.add_child(Sys2('sys2'))
    
    assembly = HeadSystem('head')
    
    connError = getAllConnError(assembly, connDescList)
    expectedConnInfo = [
        ('sys2.port_in', 'sys1.port_out'),
        ('sys1.inwards', 'sys2.outwards', {'var4': 'var2'}),
    ]
    
    assert len(assembly.connectors().values()) == len(expectedConnInfo)
    for conn, expConn in zip(assembly.connectors().values(), expectedConnInfo):
        assert conn.info() == expConn

    assert len(connError) == 2


def test_detectConnError(systemDescList, packageDescList, connDescList):
    errors = detectConnError(systemDescList, packageDescList, connDescList)
    assert len(errors) == 2


@pytest.fixture
def connDescList():
    return [
        {
            "systems": { "from": "sys1", "to": "sys2", },
            "ports": { "from": "port_out", "to": "port_in", },
            "variables": None,
        },
        {
            "systems": { "from": "sys2", "to": "sys1", },
            "ports": { "from": "outwards", "to": "inwards", },
            "variables": [
                { "from": "var1", "to": "var3", },
                { "from": "var2", "to": "var4", },
            ],
        },
    ]


@pytest.fixture
def systemDescList():
    return [
        {
            "name": "sys1",
            "type": "Sys1",
            "pack": "pck",
            "pullings": None,
        },
        {
            "name": "sys2",
            "type": "Sys2",
            "pack": "pck",
            "pullings": None,
        },
    ]


@pytest.fixture
def packageDescList():
    return [
        {
            "name": "pck",
            "systems": [
                {
                    "name": "Sys1",
                    "pack": "pck",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": [
                        {
                            "type": "ExtensiblePort",
                            "name": "inwards",
                            "pack": "pck",
                            "variables": [
                                {
                                    "name": "var3",
                                    "unit": "K",
                                },
                            ],
                        },
                    ],
                    "outputs": [
                        {
                            "type": "PortType1",
                            "name": "port_out",
                            "pack": "pck",
                        },
                    ],
                },
                {
                    "name": "Sys2",
                    "pack": "pck",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": [
                        {
                            "name": "port_in",
                            "pack": "pck",
                            "type": "PortType2",
                            "variables": [ { "name": "D", }, ],
                        },
                    ],
                    "outputs": [
                        {
                            "type": "ExtensiblePort",
                            "name": "outwards",
                            "pack": "pck",
                            "variables": [
                                {
                                    "name": "var1",
                                    "unit": "m",
                                },
                            ],
                        },
                    ],
                },
            ],
            "ports": [
                {
                    "name": "PortType1",
                    "pack": "pck",
                    "variables": [
                        {
                            "name": "A",
                            "desc": None,
                        },
                    ],
                },
                {
                    "name": "PortType2",
                    "pack": "pck",
                    "variables": [
                        {
                            "name": "B",
                            "desc": None,
                        },
                    ],
                },
            ],
        },
    ]
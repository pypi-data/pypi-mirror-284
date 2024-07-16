import pytest
from cosapp.base import System, Port


from .createAssembly import getPortPulling, getAllSystemPulling, createPortClass, createSystemClass, instantiateHeadSystem, createAssembly
from .customAssert import assert_system, assert_class


def test_variables_getPortPulling():
    pullDesc = {
        "port": "inwards",
        "variables": [
            {
                "name": "D",
                "mapping": "D",
            },
            {
                "name": "L",
                "mapping": "L",
            },
        ],
        "portMapping": None,
    }
    
    assert getPortPulling(pullDesc) == {'D': 'D', 'L': 'L'}


def test_port_without_mapping_getPortPulling():
    pullDesc = {
        "port": "portName",
        "portMapping": None,
    }
    
    assert getPortPulling(pullDesc) == {'portName': 'portName'}

 
def test_port_with_mapping_getPortPulling():
    pullDesc = {
        "port": "portName",
        "portMapping": "mapping",
    }
    
    assert getPortPulling(pullDesc) == {'portName': 'mapping'}

    
def test_getAllSystemPulling():
    pullings = [
        {
            "port": "inwards",
            "variables": [
                {
                    "name": "D",
                    "mapping": "D",
                },
            ],
            "portMapping": None,
        },
        {
            "port": "port1",
            "variables": None,
            "portMapping": "port1",
        }
    ]
    
    assert getAllSystemPulling(pullings) == {'D': 'D', 'port1': 'port1'}


def test_None_getAllSystemPulling():
    assert getAllSystemPulling([]) is None


def test_createPortClass():
    portDict = {
        "name": "PortType1",
        "pack": "package1",
        "variables": [
            {
                "name": "A",
                "desc": None,
                "unit": "K"
            },
            {
                "name": "B",
                "desc": "other variable",
            }
        ]
    }
    
    PortClass = createPortClass(portDict)
    
    class ExpectedClass(Port):
        def setup(self):
            self.add_variable("A", unit='K', value=0.0)
            self.add_variable("B", unit='', value=0.0)

            
    assert_class(PortClass, ExpectedClass, 'package1_PortType1')


def test_createSystemClass(systemDesc):
    
    class package4_PortType1(Port):
        def setup(self):
            self.add_variable("M", value=0.0)
            
    class package2_PortType1(Port):
        def setup(self):
            self.add_variable("J", value=0.0)
    
    portClassList = [package4_PortType1, package2_PortType1]
    
    systemClass = createSystemClass(systemDesc, portClassList)
    
    class ExpectedSystemClass(System):
        def setup(self):
            self.add_input(package4_PortType1, "port2")
            self.add_inward_modevar("X", unit= "K", value=0.0)
            self.add_inward("C", value=0.0)
            
            self.add_output(package4_PortType1, "port3")
            self.add_output(package2_PortType1, "port1")
            self.add_outward("A", value=0.0)
            self.add_outward("B", value=0.0)
            self.add_outward_modevar("Z", value=0.0)
            self.add_outward_modevar("Y", value=0.0)
            
    assert_class(systemClass, ExpectedSystemClass, "package2_SysType1")


def test_instantiateHeadSystem(systemListDesc):

    class package1_SysType1(System):
        def setup(self):
            self.add_inward('W')
    
    class package2_SysType2(System):
        def setup(self):
            self.add_inward('D')
            
    systemClassList = [package1_SysType1, package2_SysType2]
    headSystem, errors = instantiateHeadSystem(systemListDesc, systemClassList)
    
    class ExpectedClass(System):
        def setup(self):
            self.add_child(package1_SysType1('sys1'))
            self.add_child(package2_SysType2('sys2'), pulling={'D': 'D'})
    expectedSystem = ExpectedClass('head')

    assert_system(headSystem, expectedSystem)
    assert errors == []


def test_unitError_instantiateHeadSystem(systemListDesc):
    systemListDesc[0]['pullings'] = [
        {
            "port": "inwards",
            "variables": [
                {
                    "name": "W",
                    "mapping": "W",
                },
            ],
            "portMapping": None,
        },
    ]
    
    systemListDesc[1]['pullings'] = [
        {
            "port": "inwards",
            "variables": [
                {
                    "name": "D",
                    "mapping": "W",
                },
            ],
            "portMapping": None,
        },
    ]

    class package1_SysType1(System):
        def setup(self):
            self.add_inward('W', unit='m')
    
    class package2_SysType2(System):
        def setup(self):
            self.add_inward('D', unit='K')
            
    systemClassList = [package1_SysType1, package2_SysType2]
    headSystem, errors = instantiateHeadSystem(systemListDesc, systemClassList)
    
    class ExpectedClass(System):
        def setup(self):
            self.add_child(package1_SysType1('sys1'), pulling={'W': 'W'})
            self.add_child(package2_SysType2('sys2'))
    expectedSystem = ExpectedClass('head')

    assert_system(headSystem, expectedSystem)
    assert len(errors) == 1
    

def test_ConnectorError_instantiateHeadSystem(systemListDesc):
    systemListDesc[0]['pullings'] = [
        {
            "port": "port_in",
            "variables": None,
            "portMapping": "port_in",
        },
    ]
    
    systemListDesc[1]['pullings'] = [
        {
            "port": "port_out",
            "variables": None,
            "portMapping": "port_in",
        },
    ]
    
    class Port1(Port):
        def setup(self):
            self.add_variable("M", value=0.0)
    
    class package1_SysType1(System):
        def setup(self):
            self.add_input(Port1, 'port_in')
    
    class package2_SysType2(System):
        def setup(self):
            self.add_output(Port1, 'port_out')
            
    systemClassList = [package1_SysType1, package2_SysType2]
    headSystem, errors = instantiateHeadSystem(systemListDesc, systemClassList)
    
    class ExpectedClass(System):
        def setup(self):
            self.add_child(package1_SysType1('sys1'), pulling={'port_in': 'port_in'})
            self.add_child(package2_SysType2('sys2'))
    expectedSystem = ExpectedClass('head')

    assert_system(headSystem, expectedSystem)
    assert len(errors) == 1


def test_createAssembly(systemListDesc, packagesDesc):
    assembly, errors = createAssembly(packagesDesc, systemListDesc)

    class package1_PortType1(Port):
        def setup(self):
            self.add_variable('A', unit='', value=0.0)
            
    class package2_PortType1(Port):
        def setup(self):
            self.add_variable('B', unit='', value=0.0)
            
    class package1_SysType1(System):
        def setup(self):
            self.add_input(package1_PortType1, 'port1')
            self.add_input(package2_PortType1, 'port2')
            self.add_output(package1_PortType1, 'port3')
            self.add_output(package2_PortType1, 'port4')
            
    class package2_SysType2(System):
        def setup(self):
            self.add_outward('D', unit='', value=0.0)
            
    class HeadSystem(System):
        def setup(self):
            self.add_child(package1_SysType1('sys1'))
            self.add_child(package2_SysType2('sys2'), pulling={'D': 'D'})
    
    expectedAssembly = HeadSystem('head')
    
    assert errors == []
    assert_system(assembly, expectedAssembly)


@pytest.fixture
def systemDesc():
    return {
        "name": "SysType1",
        "pack": "package2",
        "mod": "bogus",
        "desc": None,
        "inputs": [
            {
                "type": "PortType1",
                "name": "port2",
                "pack": "package4",
            },
            {
                "pack": "package2",
                "name": "modeVarIn",
                "type": "ModeVarPort",
                "variables": [
                    {
                        "name": "X",
                        "unit": "K",
                    }
                ]
            },
            {
                "pack": "package2",
                "name": "inwards",
                "type": "ExtensiblePort",
                "variables": [
                    {
                        "name": "C"
                    },
                ],
            },
        ],
        "outputs": [
            {
                "type": "PortType1",
                "name": "port3",
                "pack": "package4",
            },
            {
                "type": "PortType1",
                "name": "port1",
                "pack": "package2",
            },
            {
                "pack": "package2",
                "name": "outwards",
                "type": "ExtensiblePort",
                "variables": [
                    {
                        "name": "A"
                    },
                    {
                        "name": "B"
                    }
                ],
            },
            {
                "pack": "package2",
                "name": "modeVarOut",
                "type": "ModeVarPort",
                "variables": [
                    {
                        "name": "Z",
                        
                    },
                    {
                        "name": "Y",
                    }
                ],
            },
        ]
    }


@pytest.fixture
def systemListDesc():
    return [
        {
            "name": "sys1",
            "type": "SysType1",
            "pack": "package1",
            "pullings": None,
        },
        {
            "name": "sys2",
            "type": "SysType2",
            "pack": "package2",
            "pullings": [
                {
                    "port": "inwards",
                    "variables": [
                        {
                            "name": "D",
                            "mapping": "D"
                        },
                    ],
                    "portMapping": None,
                },
            ],
        },
    ]

@pytest.fixture
def packagesDesc():
    return [
        {
            "name": "package1",
            "systems": [
                {
                    "name": "SysType1",
                    "pack": "package1",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": [
                        {
                            "type": "PortType1",
                            "name": "port1",
                            "pack": "package1",
                        },
                        {
                            "type": "PortType1",
                            "name": "port2",
                            "pack": "package2",
                        },
                    ],
                    "outputs": [
                        {
                            "type": "PortType1",
                            "name": "port3",
                            "pack": "package1",
                        },
                        {
                            "type": "PortType1",
                            "name": "port4",
                            "pack": "package2",
                        },
                    ],
                },
                {
                    "name": "SysType2",
                    "pack": "package1",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": [
                        {
                            "type": "PortType2",
                            "name": "port1",
                            "pack": "package1",
                        },
                        {
                            "type": "PortType3",
                            "name": "port2",
                            "pack": "package3",
                        },
                    ],
                    "outputs": None,
                }
            ],
            "ports": [
                {
                    "name": "PortType1",
                    "pack": "package1",
                    "variables": [
                        {
                            "name": "A",
                            "desc": None
                        }
                    ]
                },
                {
                    "name": "PortType2",
                    "pack": "package1",
                    "variables": [
                        {
                            "name": "A",
                            "desc": None
                        }
                    ]
                },
            ],
        },
        {
            "name": "package2",
            "systems": [
                {
                    "name": "SysType1",
                    "pack": "package2",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": None,
                    "outputs": [
                        {
                            "type": "PortType1",
                            "name": "port3",
                            "pack": "package4",
                        },
                        {
                            "type": "PortType1",
                            "name": "port1",
                            "pack": "package2",
                        },
                    ],
                },
                {
                    "name": "SysType2",
                    "pack": "package2",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": None,
                    "outputs": [
                        {
                            "name": "outwards",
                            "pack": "package2",
                            "type": "ExtensiblePort",
                            "variables": [ { "name": "D" } ]
                        },
                    ],
                }
            ],
            "ports": [
                {
                    "name": "PortType1",
                    "pack": "package2",
                    "variables": [
                        {
                            "name": "B",
                            "desc": None
                        }
                    ]
                },
                {
                    "name": "PortType2",
                    "pack": "package2",
                    "variables": [
                        {
                            "name": "A",
                            "desc": None,
                        }
                    ]
                },
            ],
        },
        {
            "name": "package3",
            "systems": [
                {
                    "name": "SysType2",
                    "pack": "package3",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": None,
                    "outputs": None,
                },
                {
                    "name": "SysType3",
                    "pack": "package3",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": None,
                    "outputs": None,
                }
            ],
            "ports": [
                {
                    "name": "PortType3",
                    "pack": "package3",
                    "variables": [
                        {
                            "name": "A",
                            "desc": None
                        }
                    ]
                },
            ],
        }
    ]
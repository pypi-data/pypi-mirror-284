import pytest

from .requestData import appendOrCreateKey, getClassesToCreate

def test_append_appendOrCreateKey():
    dictToTest = dict(key1= ['str1', 'str2'])
    appendOrCreateKey(dictToTest, 'key1', 'str3')
    
    assert dictToTest == {
        "key1": [
            "str1",
            "str2",
            "str3",
        ]
    }
    
def test_create_appendOrCreateKey():
    dictToTest = dict(key1= ['str1', 'str2'])
    appendOrCreateKey(dictToTest, 'key2', 'str3')
    
    assert dictToTest == {
        "key1": [
            "str1",
            "str2",
        ],
        "key2": [
            "str3",
        ]
    }
    
def test_no_double_appendOrCreateKey():
    dictToTest = dict(key1= ['str1', 'str2'])
    appendOrCreateKey(dictToTest, 'key1', 'str1')
    
    assert dictToTest == dict(key1= ['str1', 'str2'])
    

def test_getClassesToCreate(packages, expectedSystemClassList, expectedPortClassList):
    systemList = [
        {"name":"sys1","type":"sysType1","pack":"package1"},
        {"name":"sys2","type":"sysType2","pack":"package1"},
        {"name":"sys3","type":"sysType1","pack":"package2"},
        {"name":"sys4","type":"sysType3","pack":"package3"},
    ]
    systemClassList, portClassList = getClassesToCreate(packages, systemList)
    
    assert systemClassList == expectedSystemClassList
    assert portClassList == expectedPortClassList


@pytest.fixture
def packages():
    return [
        {
            "name": "package1",
            "systems": [
                {
                    "name": "sysType1",
                    "pack": "package1",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": [
                        {
                            "type": "portType1",
                            "name": "port1",
                            "pack": "package1",
                        },
                        {
                            "type": "portType1",
                            "name": "port2",
                            "pack": "package2",
                        },
                    ],
                    "outputs": [
                        {
                            "type": "portType1",
                            "name": "port3",
                            "pack": "package1",
                        },
                        {
                            "type": "portType1",
                            "name": "port4",
                            "pack": "package2",
                        },
                    ],
                },
                {
                    "name": "sysType2",
                    "pack": "package1",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": [
                        {
                            "type": "portType2",
                            "name": "port1",
                            "pack": "package1",
                        },
                        {
                            "type": "portType3",
                            "name": "port2",
                            "pack": "package3",
                        },
                    ],
                    "outputs": None,
                }
            ],
            "ports": [
                {
                    "name": "portType1",
                    "pack": "package1",
                    "variables": [
                        {
                            "name": "A",
                            "desc": None
                        }
                    ]
                },
                {
                    "name": "portType2",
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
                    "name": "sysType1",
                    "pack": "package2",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": None,
                    "outputs": [
                        {
                            "type": "portType1",
                            "name": "port3",
                            "pack": "package4",
                        },
                        {
                            "type": "portType1",
                            "name": "port1",
                            "pack": "package2",
                        },
                    ],
                },
                {
                    "name": "sysType3",
                    "pack": "package2",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": None,
                    "outputs": None,
                }
            ],
            "ports": [
                {
                    "name": "portType1",
                    "pack": "package2",
                    "variables": [
                        {
                            "name": "A",
                            "desc": None
                        }
                    ]
                },
                {
                    "name": "portType2",
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
                    "name": "sysType2",
                    "pack": "package3",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": None,
                    "outputs": None,
                },
                {
                    "name": "sysType3",
                    "pack": "package3",
                    "mod": "bogus",
                    "desc": None,
                    "inputs": None,
                    "outputs": None,
                }
            ],
            "ports": [
                {
                    "name": "portType3",
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


@pytest.fixture
def expectedSystemClassList():
    return [
        {
            "name": "sysType1",
            "pack": "package1",
            "mod": "bogus",
            "desc": None,
            "inputs": [
                {
                    "type": "portType1",
                    "name": "port1",
                    "pack": "package1"
                },
                {
                    "type": "portType1",
                    "name": "port2",
                    "pack": "package2"
                },
            ],
            "outputs": [
                {
                    "type": "portType1",
                    "name": "port3",
                    "pack": "package1"
                },
                {
                    "type": "portType1",
                    "name": "port4",
                    "pack": "package2"
                },
            ],
        },
        {
            "name": "sysType2",
            "pack": "package1",
            "mod": "bogus",
            "desc": None,
            "inputs": [
                {
                    "type": "portType2",
                    "name": "port1",
                    "pack": "package1"
                },
                {
                    "type": "portType3",
                    "name": "port2",
                    "pack": "package3"
                },
            ],
            "outputs": None,
        },
        {
            "name": "sysType1",
            "pack": "package2",
            "mod": "bogus",
            "desc": None,
            "inputs": None,
            "outputs": [
                {
                    "type": "portType1",
                    "name": "port3",
                    "pack": "package4"
                },
                {
                    "type": "portType1",
                    "name": "port1",
                    "pack": "package2"
                },
            ],
        },
        {
            "name": "sysType3",
            "pack": "package3",
            "mod": "bogus",
            "desc": None,
            "inputs": None,
            "outputs": None,
        },
    ]


@pytest.fixture
def expectedPortClassList():
    return [
        {
            "name": "portType1",
            "pack": "package1",
            "variables": [
                {
                    "name": "A",
                    "desc": None
                }
            ]
        },
        {
            "name": "portType2",
            "pack": "package1",
            "variables": [
                {
                    "name": "A",
                    "desc": None
                }
            ]
        },
        {
            "name": "portType1",
            "pack": "package2",
            "variables": [
                {
                    "name": "A",
                    "desc": None
                }
            ]
        },
        {
            "name": "portType3",
            "pack": "package3",
            "variables": [
                {
                    "name": "A",
                    "desc": None
                }
            ]
        }
    ]
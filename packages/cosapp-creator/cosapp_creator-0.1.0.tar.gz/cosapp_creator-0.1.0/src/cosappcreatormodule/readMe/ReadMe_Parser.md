# Parse Python module

A CoSApp module can be parsed using CoSApp, creating a JSON file.
To parse a module named `exampleModule` :

```Python
import exampleModule
from cosapp.tools import parse_module

parse_module(exampleModule)
```

This JSON file can then be imported in CoSApp Creator.

## Classes with kwargs

In case `exampleModule` contains systems that need kwargs to instanciate,
these systems will not be parsed.
In order to parse them, `parse_module` has a `ctor_config` optional argument.
This argument is a dictionary, with the keys being the name of the class.
The values can either be a dictonary, or a list of dictionaries, which have to contain the kwargs and their value.

If the value is a dictionary, the class will only be parsed once.
If it is a list of dictionary, the class will be parsed once for each dictionary.

```Python
import exampleModule
from cosapp.tools import parse_module

ctor_config =  = dict(
    SystemClass = dict(x = 0.5), # parse SystemClass with x = 0.5
    OtherClass = [
        dict(y = 0.5), # parse OtherClass with y=0.5. It will be named "OtherClass (y = 0.5)" in CoSApp Creator
        dict(y = 1, __alias__ = "OtherClassAlias") # parse OtherClass with y = 1. It will be named "OtherClassAlias" in CoSApp Creator
    ],
)

parse_module(exampleModule, ctor_config= ctor_config)
```

## Exclusion and inclusion

By default, all system classes are parsed, unless their kwargs are missing.
It is possible to filter which class to parse using exclusion and inclusion patterns.

```Python
import exampleModule
from cosapp.tools import parse_module

includes = 'T*' # Only include classes whose name starts with 'T'
excluses = [
    'Ta?',  # Exclude all classes whose name starts with 'Ta' and has 3 letters
    'To?*' # Exclude all classes whose name starts with 'To' and have at least 3 letters
]

parse_module(exampleModule, includes= includes, excludes= excludes)
```

## Other options

```Python
import exampleModule
from cosapp.tools import parse_module

path= '/folder' # path to save JSON file to
customName = 'customExampleModule' # custom name for the module

parse_module(exampleModule, path= path, package_name= customName)
```

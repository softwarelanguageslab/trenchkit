# Installation

Trenchkit uses [Poetry](https://python-poetry.org/) to package and manage it's dependencies.

```
poetry install
```
You can run trenchkit using poetry. The tool name is the directory name of the tool in the `tools` directory.
```
poetry run trenchkit <tool_name> <tool_args>
```
Poetry adds the ability to build packages so that they can be installed using pip
```
poetry build
```
This will generate packages in the `dist` folder. It is recommended to install these and so that you don't have to be in the trenchkit directory to run the application.

# Extending trenchkit 
- New tools should be added in the tools directory.
- Each tool should represent a python package.
- Each tool should have a main.py file with a run(args) function
```
├── trenchkit/
│   ├── __init__.py
│   ├── trenchkit.py       
│   └── tools/             
│       ├── __init__.py
│       ├── tool_1.py
|           └── __init__.py 
|           └── main.py 
│       ├── tool_2.py
|           └── __init__.py 
|           └── main.py 
│       └── ...            
├── pyproject.toml
```


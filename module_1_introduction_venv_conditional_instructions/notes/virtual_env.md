#### The `venv` module supports creating lightweight `virtual environments`, each with their own independent set of Python packages installed in their site directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s `base` Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

##### Create virtual environment
```shell
python -m venv env
```

##### How to use?

##### Linux:
```shell
source env/Scripts/activate
```

##### Windows:
```shell
source env/Scripts/activate.bat
```

###### Poetry
## Installation

The backend is written in python and therefore requires python, pyenv and pyenv virtualenv to be installed. 
Unless you run it through a docker container :).

1. Create a virtualenv
```bash
pyenv virtualenv 3.8.12 petli
```

2.
```
pyenv activate petli
```

3. TODO: Move test requirements to dev_requirements.txt
```
pip install -r requirements.txt
```

## Running Tests

Assuming the environment is setup you can run test by doing
```
pytest
```
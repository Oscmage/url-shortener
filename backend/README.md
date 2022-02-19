## Installation

The backend is written in python and requires pyenv and pyenv virtualenv installed


1. Create a virtualenv
```bash
pyenv virtualenv 3.8.12 petli
```

2.
```
pyenv activate petli
```

3. 
```
pip install -r requirements.txt
```

## Running Tests

Assuming the environment is setup you can run test by doing
```
python -m unittest
```
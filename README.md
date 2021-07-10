# Test legacy api

## Check the Flask blueprints

### Flask introduced the blueprints that encapsulate the modules. I like it and wanted to test

## Installation

Make sure you have python installed

Create a virtual environment

```
python -m venv venv
```

Activate the virtual environment

```
source venv/bin/activate
```

Install libyaml

```
brew install libyaml         # Mac with Homebrew
apt-get install libyaml-dev  # Ubuntu
dnf install libyaml-devel      # Fedora
```

Install the dependencies

```
pip install -r requirements.txt
```

## Run the app
```
export FLASK_APP=items_api
export FLASK_ENV=development
flask run
```

Go to http://127.0.0.1:5000/items

Example use: http://127.0.0.1:5000/items?page=32&perPage=10

## Tests

To run tests:

```
pytest
```

To test a specific file

```
pytest path/to/file.py
```

Checking coverage

```
coverage run -m pytest
coverage report
```

In case you want to generate an HTML report, add the next one

```
coverage html
```

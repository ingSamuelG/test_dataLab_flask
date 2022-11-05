# Image-clasiffier

## Database requirements

you should already have a working database running on a server

## Installation

This is a flask web application so if the installation is in a brand new instance you need to install python and a SQL database
check [Python](https://www.python.org/downloads/)

The next step is to install the lib to create virtual environments in python

```bash
sudo apt-get install python3-venv
```

once you get a correct install, clone this repository

when you have successfully cloned the repository create a virtual environment with this command

```bash
python3 -m venv virtual-environment-name
```

you can activate your virtual environment

Linux

```bash
source venv/bin/activate
```

you will see this prompt in your console

```bash
(virtual-environment-name) $
```

now install all the dependecies of the app with

```bash
pip install -r requirements.txt
```

with the dependecies installed now we have 2 options we can run a dev server or run the app on the production server

### Dev server

You have to set to enviroment variables that flask needs to run the server:

```bash
export FLASK_APP=datalab.py
```

```bash
export FLASK_DEBUG=1
```

then run the server:

```bash
flask run
```

it will serve the app in localhost:5000

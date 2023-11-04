# Speech Jokey
This project is an application which synthesises speech from user-provided text. The application is written in Python and uses the [Kivy](https://kivy.org/#home) framework for the user interface.

We envision the application to be used as a means to become DJ of your preferred voice, hence the name speech jokey. With the application you'll be creating synthesized speech from your own provided text.

## Speech synthesis
Speech synthesis is done using various speech synthesis engines. The application currently supports the following speech synthesis engines:
* ... (TODO)

# Project setup
The project is written in Python 3.11.0. To install Python, follow the instructions on the [Python website](https://www.python.org/downloads/).

## Install dependencies
We use poetry for dependency management. To install poetry, run:
```
pip install poetry
```
Installing the virtual environment is done by running:
```
poetry install
```

### How-to use poetry
Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.
For a short introduction to poetry, see [this tutorial](https://python-poetry.org/docs/basic-usage/).

Otherwise, here is a video tutorial on how to use poetry: [https://www.youtube.com/watch?v=0f3moPe_bhk](https://www.youtube.com/watch?v=0f3moPe_bhk)

## Managing Dependencies
The dependencies are listed in the [pyproject.toml](pyproject.toml) file. To add a new dependency, run:
```
poetry add <dependency>
```

# Running the application
To run the application, execute the following command in the root of the project:
```
poetry run python src/app.py
```
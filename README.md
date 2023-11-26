# Speech Jokey
This project is an application which synthesises speech from user-provided text. The application is written in Python and uses the [Kivy](https://kivy.org/#home) framework for the user interface.

We envision the application to be used as a means to become DJ of your preferred voice, hence the name speech jokey. With the application you'll be creating synthesized speech from your own provided text.

## Speech synthesis
Speech synthesis is done using various speech synthesis engines. The application currently supports the following speech synthesis engines:
* ... (TODO)

# Project setup
The project is based on Python `3.11`, but it also supports version above `3.9`. To install Python, follow the instructions on the [Python website](https://www.python.org/downloads/).

## Install dependencies
We use poetry for dependency management. To install poetry, run:
```
pip install poetry
```

Make sure to configure poetry to install the virtual environment in the project root. This can be done by running:
```
poetry config virtualenvs.in-project true
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
poetry run python src/main.py
```

# Tutorials for beginner contributors
## How to use Git
Git is a version control system. It allows you to keep track of changes made to your code and to collaborate with others. To learn more about Git, see [this fundamental beginner tutorial](https://www.youtube.com/watch?v=HVsySz-h9r4).

Alternatively, you can play the [Git game](https://ohmygit.org/) to learn git interactively.

## How to use GitHub
GitHub is a platform for hosting Git repositories. It allows you to collaborate with others on your code. To learn more about GitHub, see [this crash course](https://www.youtube.com/watch?v=iv8rSLsi1xo).

## How to use VS Code
VS Code is a code editor. It allows you to write code and to collaborate with others. To learn more about VS Code, see [this crash course](https://www.youtube.com/watch?v=WPqXP_kLzpo).

## How to use Kivy
Kivy is a framework for building user interfaces. It allows you to build user interfaces for your application. To learn more about Kivy, watch [this playlist](https://www.youtube.com/playlist?list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg) for a beginner friendly introduction to the framework.
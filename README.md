# Speech Jokey

This project is about building an application which synthesises speech from user-provided text. The application is written in Python and uses the [Kivy](https://kivy.org/#home) framework for the user interface.

Encoding intonation and emotions remains a significant challenge in the Assistive Technology Text-To-Speach field, which if overcome could definitely enhance the communication experience for people with speech impairment. The aim of Speech Jokey is therefore to allow people with communication difficulties to interact with more intonation, emotions and emphasis pauses. 
In addition, the application is specifically designed to be used with eye tracking systems, facilitating the positioning of the cursor between lines and words of a text.  

We envision the application to be used as a means to become DJ of your preferred voice, hence the name speech jokey. With the application you'll be creating synthesized speech from your own provided text.

The designed logo for the application is currently: 

<details><summary>Application screenshot</summary><img a="https://github.com/HackXIt/assist-heidi-speech-jokey/assets/1595680/74a5821a-faea-4734-90e4-1d00d71938d4"/></details>

## Speech synthesis
Speech synthesis is done using various speech synthesis engines. The application currently supports the following speech synthesis engines:
* ElevenLabs API

# Project setup
The project is based on Python `3.11`, but it also supports lower version down to `3.9`. To install Python, follow the instructions on the [Python website](https://www.python.org/downloads/).

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

## Managing Dependencies
The dependencies are listed in the [pyproject.toml](pyproject.toml) file. To add a new dependency, run:
```
poetry add <dependency>
```

# Project build
The following procedures assume that you have installed the dependencies and that you are working inside the virtual environment.

## Running the application (Any OS / Development)
To run the application, execute the following command in the root of the project:
```
poetry run python src/main.py
```

## Building the application executable (Windows / Local Development)
To build the application, execute the following command in the root of the project:

_(You might wanna grab a coffee while running this)_
```
poetry run pyinstaller src/main.py --onefile --name SpeechJokey
```

The created build application specification `SpeechJokey.spec` can now be found in the root of the project.
This file needs to be modified according to the following steps:
1. Import kivy dependencies at the top of the file: `from kivy_deps import sdl2, glew`
2. Add source tree after `COLLECT(exe,`: `Tree('src\\'),`
3. Add source dependencies after `a.datas,`: `*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],`

After these modifications, the application can be finalized by running:

_(Should be very quick after the initial build)_
```
poetry run pyinstaller SpeechJokey.spec
```

Inside the `dist` output folder a folder with the name `SpeechJokey` can be found. This folder contains the final `.exe` build of the application.

For a detailed step-by-step guide on how to build a Kivy application, see [this written tutorial](https://github.com/CovidCoder/Kivy-App-Package-Windows-Tutorial/blob/master/KivyPackageTut.md). 
_(Keep in mind that the tutorial doesn't use poetry, so any command should be preceeded by `poetry run`)_

## Building the application executable (Windows / CI)
To build the application similar to how it would be built by the CI, copy the `SpeechJokey.spec` from `.github\static` to the project root and then execute the following command in the root of the project:
```
poetry run pyinstaller SpeechJokey.spec
```

# Intended features  
<details><summary>Click here to visualize the current app interface</summary><img a="https://github.com/martinatumsich/git-exercise/assets/146335643/c96a5033-ebfb-47ac-b21d-06b50eb91605"/></details>

## Loading the text
The idea of Speech Jokey is to give the user the possibility to edit the text that he previously wrote, loading it in text input of the application. 
<details><summary>Load</summary><img a="https://github.com/ChiaraCalvo/git-exercise/assets/146334030/f61731c8-2529-4369-a9df-3a00e0e86f1c"/></details>

## Editing the text
The editing part is facilitated thanks to the fact that the line where the cursor is, will be "zoomed". This means that the user will visualize that line with a bigger linespace before and
after and with a bigger space inbetween words. 
<details><summary>Editing</summary><img a="https://github.com/ChiaraCalvo/git-exercise/assets/146334030/9fe969ae-a399-4d36-9f8d-ca0d118edc63"/></details>

The editing feature is adressed especially to people who need eye tracking devices to move the cursor. 

## SSML features for encoding intonation
The buttons (_Add Break, Change Pitch, Emphasize_) enable to insert SSML tags between the text for the speech syntesis. 
<details><summary>Add Break</summary><img a="https://github.com/ChiaraCalvo/git-exercise/assets/146334030/39508a72-aee9-49f7-aa97-c2bd5eb76607"/></details>
<details><summary>Change Pitch</summary><img a="https://github.com/ChiaraCalvo/git-exercise/assets/146334030/31dca5c9-76db-4a04-8b6d-3eef8a2f97f8"/></details>
<details><summary>Emphasize</summary><img a="https://github.com/ChiaraCalvo/git-exercise/assets/146334030/31dca5c9-76db-4a04-8b6d-3eef8a2f97f8"/></details>

## Generation of an audio file 
An audio file is generated thanks to a selected Text-To-Speech API voice. 

The user can listen to it, pause it and play it. 

## Saving the final audio file 
The final version of the edited text can be saved as a file in audio format.



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

## How-to use poetry
Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.
For a short introduction to poetry, see [this tutorial](https://python-poetry.org/docs/basic-usage/).
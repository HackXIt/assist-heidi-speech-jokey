# Supported APIs

This directory contains the client wrappers for the supported APIs.

A client wrapper is a class that implements the API calls and provides a settings widget for the application to use for configuration.
Any settings that are required for the API shall be stored in the settings class.

New APIs can be added by following the instructions below and **must** follow the described structure.

For a reference implementation, see the [example API](exampleapi/).

## Structure

An API module **must** be stored in a directory under `src/api/`, using `<api_name>` as the directory name.

API modules **must** consist of three classes, stored in the `<api_name>.py` file:
- `<ApiName>Widget`: The widget for the API to view and edit settings in the application settings popup. This class should use CamelCase naming.
- `<ApiName>Settings`: The settings class for the API, which **must** inherit from `BaseApiSettings`. This class should use CamelCase naming.
- `<ApiName>`: The API implementation class. This class should use CamelCase naming.

Example for the naming scheme:
`<api_name>`: `exampleapi`
`<ApiName>`: `ExampleApi` (should be a CamelCase version of `<api_name>`)
`<ApiName>Widget`: `ExampleApiWidget`
`<ApiName>Settings`: `ExampleApiSettings`

The `BaseApiSettings` class implements the required Singleton pattern for the settings class. It ensures proper dynamic loading of the API during application startup by declaring methods that **must** be implemented by the settings class.

Additionally, the API module may contain a `<api_name>.kv` file, which contains the kivy rules for the settings view of the specific API.

The widget for the settings holds the reference to the singleton instance of the settings class for the API.
Whenever settings are changed in the settings widget, the settings class should be updated accordingly.
Whenever settings are used, they shall be retrieved via the settings widget or via the settings class.

The settings class **must** implement the following methods:
- `isSupported()`: Returns a boolean indicating whether the API is functionally supported by the current environment. Setting this to false will ignore the API during the application startup.
- `get_settings_widget()`: Returns an instance of the settings widget for the API.
- `load_settings()`: Loads the settings from the global settings instance into the internal state of the API settings. Internally this shall call `global_settings.get_setting(api_name, setting_name)` for each setting that is required by your API.
- `save_settings()`: Saves the internal state of the API settings into the global settings instance. Internally this shall call `global_settings.update_setting(api_name, setting_name, value)` for each setting that is required to be stored for your API.

## How to add a new API

1. Create a new directory for the API under `src/api/`.
2. Add these files into the created directory `__init__.py`, `<api_name>.py`, `<api_name>.kv`.
3. Update `<api_name>.py` with the following content:

```python
from kivy.app import App
from ..base_settings import BaseApiSettings

class <ApiName>Widget(<LayoutForSettings>):
    # Add the properties for the settings widget here
    # Example: example_setting = StringProperty('')
    settings = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(<ApiName>Widget, self).__init__(**kwargs)
        self.add_widget(Label(text="Hello World!"))
        self.settings = <ApiName>Settings()
        self.settings.load_settings()

class <ApiName>Settings(BaseApiSettings):
    api_name = '<ApiName>'
    # Add relevant settings for the API here
    # Example: example_setting = 'Foo'

    def __init__(self, **kwargs):
        super(ExampleAPISettings, self).__init__(**kwargs)
        self.load_settings()

    @classmethod
    def isSupported(cls):
        return False # Set to true once the API is functionally supported
    
    @classmethod
    def get_settings_widget(cls):
        return <ApiName>Widget()

    def load_settings(self):
        app_instance = App.get_running_app()
        # Update the internal settings state for the API here
        # Example: token = app_instance.global_settings.get_setting(self.api_name, "example_setting")

    def save_settings(self):
        app_instance = App.get_running_app()
        # Save the internal settings state from the API here
        # Example: app_instance.global_settings.update_setting(self.api_name, "example_setting", self.example_setting)

class <ApiName>():
    # The API implementation goes here
```

4. Update `<api_name>.kv` with the following content:

```kivy
<ApiName>Widget:
    # Add the settings view for your specific API here
    # Example: TextInput:
    #              text: root.example_setting
    #              on_text_validate: root.save_settings()
```
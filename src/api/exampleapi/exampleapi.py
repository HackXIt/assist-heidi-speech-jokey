from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from ..base import BaseApiSettings, BaseApi

# NOTE This class holds the widget properties and logic for the specific API settings view. It also holds the instance of the specific API settings class.
class ExampleAPIWidget(BoxLayout):
    settings = ObjectProperty(None)
    example_setting_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ExampleAPIWidget, self).__init__(**kwargs)
        self.add_widget(Label(text="Hello World!")) # Example initialization for the widget
        self.settings = ExampleAPISettings(self) # The settings instance must be created here
        self.example_setting_input.bind(text=self.settings.setter('example_setting')) # Bind text input to update example_setting
        self.settings.bind(example_setting=self.example_setting_input.setter('text')) # Bind example_setting to update text input
        self.settings.load_settings() # An initial loading of the settings is recommended
    
    def update(self, instance, value):
        self.example_setting_input.text = value

# NOTE This class holds the state of the specific API settings and must be derived from BaseApiSettings, which implements the required Singleton pattern for you.
class ExampleAPISettings(BaseApiSettings):
    example_setting = StringProperty('')

    def __init__(self, widget, **kwargs):
        super(ExampleAPISettings, self).__init__(**kwargs)
        self.load_settings()
        self.widget = widget

    @classmethod
    def isSupported(cls):
        return True
    
    @classmethod
    def get_settings_widget(cls):
        return ExampleAPIWidget()

    def load_settings(self): # Settings are loaded using the global settings instance
        app_instance = App.get_running_app()
        self.example_setting = app_instance.global_settings.get_setting(self.api_name, "example_setting")

    def save_settings(self): # Settings are stored using the global settings instance
        app_instance = App.get_running_app()
        app_instance.global_settings.update_setting(self.api_name, "example_setting", self.example_setting)
    
    def __str__(self) -> str:
        return f"ExampleAPISettings{{example_setting: {self.example_setting}}}"

# NOTE This class holds the API logic and performs the API calls. When instantiated, the settings class of the API shall be passed.
class ExampleAPI(BaseApi):
    def __init__(self, settings: ExampleAPISettings):
        super().__init__(settings)
    
    # Implement abstract methods of BaseApi
    def play(self, input: str):
        # Placeholder implementation
        pass

    def synthesize(self, input: str, file: str):
        # Placeholder implementation
        pass
    
    def do_api_specific_stuff(self):
        print(f"Doing stuff with Example setting: {self.settings.example_setting}")
    
    def __str__(self) -> str:
        return f"ExampleAPI"
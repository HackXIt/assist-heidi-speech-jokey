from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from ..base_settings import BaseApiSettings

# NOTE This class holds the widget properties and logic for the specific API settings view. It also holds the instance of the specific API settings class.
class ExampleAPIWidget(BoxLayout):
    example_setting = StringProperty('')
    settings = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ExampleAPIWidget, self).__init__(**kwargs)
        self.add_widget(Label(text="Hello World!")) # Example initialization for the widget
        self.settings = ExampleAPISettings() # The settings instance must be created here
        self.settings.load_settings() # An initial loading of the settings is recommended

# NOTE This class holds the state of the specific API settings and must be derived from BaseApiSettings, which implements the required Singleton pattern for you.
class ExampleAPISettings(BaseApiSettings):
    api_name = 'ExampleAPI'
    example_setting = 'Foo'

    def __init__(self, **kwargs):
        super(ExampleAPISettings, self).__init__(**kwargs)
        self.load_settings()

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

# NOTE This class holds the API logic and performs the API calls. When instantiated, the settings class of the API shall be passed.
class ExampleAPI():
    def __init__(self, api_settings: ExampleAPISettings):
        self.api_settings = api_settings
    
    def do_stuff(self):
        print(f"Doing stuff with Example setting: {self.api_settings.example_setting}")
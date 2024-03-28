# Kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.logger import Logger as log
# KivyMD
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from kivymd.uix.slider import MDSlider
from kivymd.uix.selectioncontrol import MDSwitch
# stdlib
# Custom
from ..base import BaseApiSettings, BaseApi

# NOTE This class holds the widget properties and logic for the specific API settings view. It also holds the instance of the specific API settings class.
class ExampleAPIWidget(MDExpansionPanel):
    def __init__(self, **kwargs):
        super(ExampleAPIWidget, self).__init__(**kwargs)
        self.settings = ExampleAPISettings(self) # The settings instance is created here
        self.settings.load_settings() # An initial loading of the settings is recommended
        # TODO loaded setting values shall be applied to the settings widget elements
    
    def on_change(self, id: str):
        if id not in self.ids:
            log.error("%s: Invalid setting ID: %s", self.__class__.__name__, id)
        # NOTE I'd recommend a more sophisticated way of determining which widget corresponds to which setting
        # for the sake of simplicity, I'll use the ID and the type of the widget
        if self.ids[id] is MDCheckbox:
            self.settings.setting_1 = self.ids[id].active
        elif self.ids[id] is MDTextField:
            self.settings.setting_2 = self.ids[id].text
        elif self.ids[id] is MDSlider:
            self.settings.setting_3 = self.ids[id].value
        elif self.ids[id] is MDSwitch:
            self.settings.setting_4 = self.ids[id].active

# NOTE This class holds the state of the specific API settings and must be derived from BaseApiSettings, which implements the required Singleton pattern for you.
class ExampleAPISettings(BaseApiSettings):
    def __init__(self, widget, **kwargs):
        super(ExampleAPISettings, self).__init__(**kwargs)
        self.load_settings()
        self.widget = widget
        self.setting_1 = False
        self.setting_2 = "default_value"
        self.setting_3 = 75
        self.setting_4 = True

    @classmethod
    def isSupported(cls):
        return True
    
    @classmethod
    def get_settings_widget(cls):
        return ExampleAPIWidget()

    def load_settings(self): # Settings are loaded using the global settings instance
        app_instance = App.get_running_app()
        self.example_setting = app_instance.global_settings.get_setting(self.__class__.__name__, "setting_1")

    def save_settings(self): # Settings are stored using the global settings instance
        app_instance = App.get_running_app()
        app_instance.global_settings.update_setting(self.__class__.__name__, "example_setting", self.example_setting)
    
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

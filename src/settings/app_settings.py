# Kivy
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, ListProperty
from kivy.event import EventDispatcher
from kivy.logger import Logger as log
# KivyMD
from kivymd.uix.screen import MDScreen
# stdlib
import os
import importlib
import inspect
import json
from pathlib import Path
# Custom
from api.base import BaseApiSettings
from modules.util.widget_loader import load_widget

def none_settings():
    pass

class GlobalSettings(EventDispatcher):
    _instance = None
    _settings_file = "app_settings.json"
    _default_settings = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalSettings, cls).__new__(cls)
            cls._instance.load_or_initialize_settings()
        return cls._instance

    def load_or_initialize_settings(self):
        if not os.path.exists(self._settings_file):
            self.reset()
        else:
            with open(self._settings_file, 'r') as file:
                self._settings = json.load(file)


    def save_settings(self):
        with open(self._settings_file, 'w') as file:
            json.dump(self._settings, file, indent=4)
            log.info(f"{self.__class__.__name__}: Settings saved: {self._settings_file}")
    
    def load_settings(self):
        if os.path.exists(self._settings_file):
            with open(self._settings_file, 'r') as file:
                self._settings = json.load(file)
        else:
            log.error(f"{self.__class__.__name__}: Settings file does not exist. Reset or save is required.")

    def update_setting(self, api_name, key, value):
        log.debug(f"{self.__class__.__name__}: Update {api_name}: {key} to '{value}'.")
        if api_name in self._settings.keys():
            self._settings[api_name][key] = value
            self.save_settings()
        else:
            self._settings[api_name] = {key: value}
            self.save_settings()

    def get_setting(self, api_name, key, default=None):
        value = self._settings.get(api_name, {}).get(key, default)
        log.debug(f"{self.__class__.__name__}: Load {key}: {value}")
        return value
    
    def reset(self):
        self._settings = self._default_settings.copy()
        self.save_settings()

""" OLD
class AppSettingsPopup(Popup):
    settings_container = ObjectProperty(None)
    api_settings_container = ObjectProperty(None)
    supported_apis = {'None': none_settings}
    api_options = ListProperty(supported_apis.keys())

    def __init__(self, **kwargs):
        super(AppSettingsPopup, self).__init__(**kwargs)
        self.discover_supported_apis()

    def discover_supported_apis(self):
        api_dir = Path(__file__).parent.parent / "api"
        skipped = ['__pycache__']
        for api_path in api_dir.iterdir():
            if api_path.is_dir() and api_path.name not in skipped:
                api_name = api_path.name.capitalize()
                log.debug(f"{self.__class__.__name__}: Potential API {api_name}")
                settings_module_name = f"api.{api_name.lower()}.{api_name.lower()}"
                try:
                    settings_module = importlib.import_module(settings_module_name)
                    # Iterate over all members of the module and find the subclass of BaseApiSettings
                    for name, obj in inspect.getmembers(settings_module, predicate=inspect.isclass):
                        if issubclass(obj, BaseApiSettings) and obj is not BaseApiSettings:
                            if obj.isSupported():
                                self.supported_apis[api_name] = lambda api_name=api_name, obj=obj: self.load_api_settings_widget(api_name, obj)
                                log.info(f"{self.__class__.__name__}: Discovered API {api_name}: {obj.__name__}")
                                self.api_options = self.supported_apis.keys()
                            else:
                                log.debug(f"{self.__class__.__name__}: API {api_name} is not supported yet")
                            break
                        else:
                            log.debug(f"{self.__class__.__name__}: Skipping {name} in {settings_module_name}")
                except ImportError as e:
                    log.error(f"{self.__class__.__name__}: Could not import {settings_module_name}: {e}")
            else:
                log.debug(f"{self.__class__.__name__}: Skipping {api_path.name}")

    def on_api_selected(self, api_name):
        if api_name in self.supported_apis:
            self.supported_apis[api_name]()
        else:
            log.info(f"{self.__class__.__name__}: API {api_name} is not supported yet")

    def load_api_settings_widget(self, api_name: str, settings_class: BaseApiSettings):
        try:
            # FIXME Doesn't work in packaged build due to paths - using direct load in the beginning instead
            # Get the module in which the class is defined
            # module = inspect.getmodule(settings_class)
            # if module is None:
            #     raise ImportError(f"Module for class {settings_class.__name__} not found")

            # Load the KV file
            # kv_file_path = os.path.join(os.path.dirname(module.__file__), f"{module.__file__.replace('.py', '.kv')}")
            # load_widget(kv_file_path)

            # Load the settings widget
            self.load_settings_widget(settings_class.get_settings_widget())
        except (ImportError, AttributeError, ValueError) as e:
            log.error(f"{self.__class__.__name__}: Error loading settings for {api_name}: {e}")
    
    def load_settings_widget(self, settings_widget):
        if self.api_settings_container is not None:
            self.settings_container.remove_widget(self.api_settings_container)
        self.api_settings_container = settings_widget
        self.settings_container.add_widget(self.api_settings_container)
        self.api_settings_container.settings.load_settings()

    def save_settings(self):
        # Logic to save settings
        self.api_settings_container.settings.save_settings()
        self.dismiss()
    
    def load_settings(self):
        App.get_running_app().global_settings.load_settings()
        if self.api_settings_container is not None:
            self.api_settings_container.settings.load_settings()
        self.settings_container.do_layout()

    def reset_settings(self):
        App.get_running_app().global_settings.reset()
        if self.api_settings_container is not None:
            self.settings_container.remove_widget(self.api_settings_container)
            self.api_settings_container = ObjectProperty(None)
"""
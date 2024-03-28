# Kivy
from kivy.logger import Logger as log
# KivyMD
# stdlib
import os
import importlib
import traceback
# Custom
from modules.util.widget_loader import load_widget

class ApiFactory:
    @staticmethod
    def get_api(api_name: str):
        try:
            api_module = importlib.import_module(f"api.{api_name}.{api_name.lower()}")
            log.debug(f"{__class__.__name__}: Imported API module: {api_module}")
            api_class = getattr(api_module, api_name) # TODO Unused api_class
            settings_class = getattr(api_module, f"{api_name}Settings") # TODO Unused settings_class
            widget_class = getattr(api_module, f"{api_name}Widget")
            load_widget(os.path.join(os.path.dirname(api_module.__file__), f"{api_name.lower()}.kv"))
            return widget_class()
        except (ModuleNotFoundError, AttributeError) as e:
            log.error(f"{__class__.__name__}: Error loading API {api_name}: {e}")
            log.debug(f"{__class__.__name__}: {traceback.format_exc()}")
            return None

# Dynamic loading of APIs based on directory structure
def load_apis():
    # TODO Implement dynamic loading based on directory structure instead of a static name list
    # api_names = [name for name in os.listdir("api") if os.path.isdir(os.path.join("api", name))]
    api_names = ["ExampleAPI"]
    apis = {}
    for name in api_names:
        apis[name] = ApiFactory.get_api(name)
    return apis

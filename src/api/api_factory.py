# api_factory.py
import os
import importlib

class ApiFactory:
    @staticmethod
    def get_api(api_name):
        try:
            api_module = importlib.import_module(f"api.{api_name}")
            api_class = getattr(api_module, api_name)
            settings_class = getattr(api_module, f"{api_name}Settings")
            settings = settings_class()
            return api_class(settings)
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Error loading API {api_name}: {e}")
            return None

# Dynamic loading of APIs based on directory structure
def load_apis():
    api_names = [f.name for f in os.scandir("api") if f.is_dir()]
    apis = {}
    for name in api_names:
        apis[name] = ApiFactory.get_api(name)
    return apis

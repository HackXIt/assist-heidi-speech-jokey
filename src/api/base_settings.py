from abc import ABC, abstractmethod
from kivy.event import EventDispatcher
from kivy.clock import Clock

class BaseApiSettings(ABC, EventDispatcher):
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BaseApiSettings, cls).__new__(cls)
        return cls._instance

    def __init__(self, **kwargs):
        super(BaseApiSettings, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.load_settings, 1.5) # Do an initial load of settings

    @classmethod
    @abstractmethod
    def isSupported(cls):
        """
        This property must be overridden in derived classes.
        It should return a boolean indicating if the API is functionally supported yet.
        """
        pass

    @classmethod
    @abstractmethod
    def get_settings_widget(cls):
        """
        This method must be overridden in derived classes.
        It should return the widget that will be displayed in the settings popup.
        """
        pass

    @abstractmethod
    def load_settings(self):
        """
        This method must be overridden in derived classes.
        It should load the API specific settings into the application.
        """
        pass

    @abstractmethod
    def save_settings(self):
        """
        This method must be overridden in derived classes.
        It should return the settings from the API in JSON format.
        """
        pass

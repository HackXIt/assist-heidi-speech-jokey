# Kivy
from kivy.properties import StringProperty
from kivy.logger import Logger as log
# KivyMD
from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget
# stdlib
# Custom

class Settings(MDScreen):
    title = StringProperty()
    def __init__(self, title: str, api: MDWidget, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)
        self.title = title
        log.debug(f"{self.__class__.__name__}: API: {api}")
        if api is not None:
            self.ids.settings_container.add_widget(api)
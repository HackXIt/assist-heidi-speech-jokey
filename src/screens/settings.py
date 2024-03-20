# Kivy
from kivy.properties import StringProperty
from kivy.logger import Logger as log
# KivyMD
from kivymd.uix.screen import MDScreen
# stdlib
# Custom

class Settings(MDScreen):
    title = StringProperty()
    def __init__(self, title: str, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)
        self.title = title
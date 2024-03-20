# Kivy
from kivy.properties import StringProperty
# KivyMD
from kivymd.uix.screen import MDScreen
# stdlib
# Custom

class About(MDScreen):
    title = StringProperty()
    about_text = StringProperty()
    def __init__(self, title: str, **kwargs):
        super(About, self).__init__(**kwargs)
        self.title = title
        self.about_text = "Made by HackXIt"
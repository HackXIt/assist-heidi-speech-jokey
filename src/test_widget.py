from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from api.ExampleAPI.exampleapi import ExampleAPIWidget
from modules.util.widget_loader import load_widget
import os
import sys

if __name__ == "__main__":
    MDApp().run()
    load_widget(os.path.join(os.path.dirname(sys.modules[ExampleAPIWidget.__module__].__file__), 'exampleapi.kv'))
    screen = MDScreen()
    screen.add_widget(MDBoxLayout(orientation="vertical", id="container"))
    screen.ids.container.add_widget(ExampleAPIWidget())
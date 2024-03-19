from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.logger import Logger as log, LOG_LEVELS
from kivy.config import Config
import os
import sys
from kivy.resources import resource_add_path, resource_find

from modules.dialog import loaddialog, savedialog
from modules.util.widget_loader import load_widget
from settings import app_settings
from api.api_factory import load_apis

class MainScreen(BoxLayout):
    text_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.file_load_popup = loaddialog.LoadDialog(callback=self.load_textfile, title="Load file", size_hint=(0.9, 0.9))
        # self.file_load_popup.size = (400, 400)
        self.file_save_popup = savedialog.SaveDialog(callback=self.save_textfile, title="Save file", size_hint=(0.9, 0.9))
        # self.file_save_popup.size = (400, 400)
        self.settings_popup = app_settings.AppSettingsPopup()

    def load_file(self):
        # Open dialog
        self.file_load_popup.open()

    def save_file(self):
        self.file_save_popup.open()

    def load_textfile(self, file: str):
        with open(os.path.abspath(file), 'r') as file:
            text = file.read()
            log.info(f"Text: {text[0:40]}...")
            self.text_input.text = text

    def save_textfile(self, file: str):
        if file is not None:
            with open(file, 'w') as file:
                file.write(self.text_input.text)

    def on_play(self):
        # Logic to play audio
        pass

    def on_synthesize(self):
        api = App.get_running_app().api
        if api:
            try:
                api.synthesize(self.text_input.text, "output_file.wav")
            except NotImplementedError:
                print("Synthesize not implemented for this API.")
            except Exception as e:
                print(f"Error during synthesis: {e}")

    def open_settings(self):
        self.settings_popup.open()

class SpeechJokey(App):
    def build(self):
        load_widget(os.path.join(os.path.dirname(loaddialog.__file__), 'loaddialog.kv'))
        load_widget(os.path.join(os.path.dirname(savedialog.__file__), 'savedialog.kv'))
        load_widget(os.path.join(os.path.dirname(app_settings.__file__), 'AppSettingsPopup.kv'))
        self.global_settings = app_settings.GlobalSettings()
        self.icon = os.path.join(os.curdir, 'speech-jokey.ico')
        Config.set('kivy','window_icon', self.icon)
        log.setLevel(LOG_LEVELS["debug"])
        self.title = 'Speech Jokey'
        self.apis = load_apis()
        self.api = self.apis.get("exampleapi", None)
        return MainScreen()

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    SpeechJokey().run()
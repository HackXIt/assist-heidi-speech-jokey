from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.logger import Logger as log, LOG_LEVELS
from kivy.config import Config
import os

from modules.dialog import loaddialog
from modules.util.widget_loader import load_widget
from settings import app_settings

class MainScreen(BoxLayout):
    text_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.file_popup = loaddialog.LoadDialog(callback=self.load_textfile, title="Load file", size_hint=(0.9, 0.9))
        self.file_popup.size = (400, 400)
        self.settings_popup = app_settings.AppSettingsPopup()

    def load_file(self):
        # FIXME The popup menu doesn't contain the file browser, but instead the file browser is opened as a separate popup
        # Open dialog
        self.file_popup.open()

    def load_textfile(self, selection):
        with open(selection[0], 'r') as file:
            text = file.read()
            log.info(f"Text: {text[0:40]}...")
            self.text_input.text = text

    def play_audio(self):
        # Logic to play audio
        pass

    def generate_audio(self):
        # Logic to save generated voice audio to file
        pass

    def open_settings(self):
        self.settings_popup.open()

    def save_file(self):
        # Logic to save audio file
        pass

    def insert_ssml_tag(self, tag_name):
        # Logic to insert SSML tags into text
        pass

    def playback_control(self, action):
        # Logic to control audio playback
        pass

class SpeechJokey(App):
    def build(self):
        load_widget(os.path.join(os.path.dirname(loaddialog.__file__), 'loaddialog.kv'))
        load_widget(os.path.join(os.path.dirname(app_settings.__file__), 'AppSettingsPopup.kv'))
        self.global_settings = app_settings.GlobalSettings()
        self.icon = 'assets/speech-jokey.png'
        Config.set('kivy','window_icon', os.path.join(os.path.dirname(__file__), self.icon))
        log.setLevel(LOG_LEVELS["debug"])
        return MainScreen()

if __name__ == '__main__':
    SpeechJokey().run()
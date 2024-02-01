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
from api.elevenlabsapi.elevenlabsapi import ElevenLabsTTS
from settings import app_settings

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

    def play_audio(self):
        # Logic to play audio
        pass

    def generate_audio(self):
        # Logic to save generated voice audio to file
        api = App.get_running_app().api
        if isinstance(api, ElevenLabsTTS):
            log.debug(f"Synthesizing: {self.text_input.text[0:10]}...")
            try:
                api.synthesize(self.text_input.text, os.path.join("tmp/", "tmp.wav"))
            except Exception as e:
                log.error(f"Audio generation failed: {e}")

    def open_settings(self):
        self.settings_popup.open()

    def insert_ssml_tag(self, tag_name):
        # Logic to insert SSML tags into text
        pass

    def playback_control(self, action):
        # Logic to control audio playback
        pass

class SpeechJokey(App):
    def build(self):
        load_widget(os.path.join(os.path.dirname(loaddialog.__file__), 'loaddialog.kv'))
        load_widget(os.path.join(os.path.dirname(savedialog.__file__), 'savedialog.kv'))
        load_widget(os.path.join(os.path.dirname(app_settings.__file__), 'AppSettingsPopup.kv'))
        self.global_settings = app_settings.GlobalSettings()
        self.icon = 'assets/speech-jokey.png'
        Config.set('kivy','window_icon', os.path.join(os.path.dirname(__file__), self.icon))
        log.setLevel(LOG_LEVELS["debug"])
        self.title = 'Speech Jokey'
        self.api = None
        return MainScreen()

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    SpeechJokey(kv_file="SpeechJokey.kv").run()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.logger import Logger, LOG_LEVELS

# Import other necessary Kivy modules
import os

from modules.dialog import loaddialog
from settings import app_settings

class MainScreen(BoxLayout):
    def load_file(self):
        # loaddialog.LoadDialog.load_widget()
        self.file_popup = loaddialog.LoadDialog(title="Load file", size_hint=(0.9, 0.9))
        self.file_popup.load.on_release = self.load
        self.file_popup.cancel.on_release = self.dismiss_popup
        # Open dialog
        self.file_popup.open()

    def load_text_file(self, selection):
        if selection:
            with open(selection[0], 'r') as file:
                self.ids.text_input.text = file.read()

    def play_audio(self):
        # Logic to play audio
        pass

    def generate_audio(self):
        # Logic to save generated voice audio to file
        pass

    def open_settings(self):
        app_settings_popup_file = os.path.join(os.path.dirname(app_settings.__file__), 'AppSettingsPopup.kv')
        Builder.unload_file(app_settings_popup_file)
        Builder.load_file(app_settings_popup_file)
        settings_popup = app_settings.AppSettingsPopup()
        settings_popup.open()

    def save_file(self):
        # Logic to save audio file
        pass

    def insert_ssml_tag(self, tag_name):
        # Logic to insert SSML tags into text
        pass

    def playback_control(self, action):
        # Logic to control audio playback
        pass        

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as file:
            self.ids.text_input.text = file.read()
        self.dismiss_popup()

    def dismiss_popup(self):
        self.file_popup.dismiss()

class SpeechJokey(App):
    def build(self):
        self.global_settings = app_settings.GlobalSettings()
        Logger.setLevel(LOG_LEVELS["debug"])
        return MainScreen()

if __name__ == '__main__':
    SpeechJokey().run()
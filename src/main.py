# from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.filemanager import MDFileManager
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

class MainScreen(MDScreen):
    text_input = ObjectProperty(None)
    menu_options = ["Settings", "About", "Exit"]
    supported_text_files = ["txt", "md", "rst"]

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        # self.file_load_popup = loaddialog.LoadDialog(callback=self.load_textfile, title="Load file", size_hint=(0.9, 0.9))
        # # self.file_load_popup.size = (400, 400)
        # self.file_save_popup = savedialog.SaveDialog(callback=self.save_textfile, title="Save file", size_hint=(0.9, 0.9))
        # # self.file_save_popup.size = (400, 400)
        # self.settings_popup = app_settings.AppSettingsPopup()
        self.last_path = None
        self.opened_file = None
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            icon_selection_button="folder-marker"
        )
 
    def on_menu_open(self):
        menu_items = [
            {
                "text": option,
                "on_release": lambda x=option: self.menu_callback(x),
            } for option in self.menu_options
        ]
        MDDropdownMenu(
            caller=self.ids.btn_menu, items=menu_items
        ).open()
    
    def menu_callback(self, text_item):
        print(text_item)

    def on_load_file(self):
        # Open dialog
        # self.file_load_popup.open()
        if self.last_path is not None:
            path = self.last_path
        else:
            path = os.path.expanduser("~")
        self.file_manager.show(path)
        self.manager_open = True

    def select_path(self, path):
        log.info(f"{self.__class__.__name__}: Selected path: {path}")
        if os.path.isfile(path):
            self.last_path = os.path.dirname(path)
        elif os.path.isdir(path):
            self.last_path = path
        else:
            log.error(f"{self.__class__.__name__}: Invalid path selected: {path}")
        self.exit_manager()
    
    def exit_manager(self, *args):
        if self.last_path is not None and os.path.isfile(self.last_path):
            self.opened_file = self.last_path
            self.load_textfile(self.last_path)
        else:
            log.error(f"{self.__class__.__name__}: No file selected. Last path: {self.last_path}")
        self.manager_open = False
        self.file_manager.close()

    def on_save_file(self):
        if self.opened_file is not None:
            self.save_textfile(self.opened_file)
        else:
            log.error(f"{self.__class__.__name__}: No file opened to save.")

    def load_textfile(self, file: str):
        file_ext = file.split('.')[-1]
        if file_ext not in self.supported_text_files:
            log.error(f"{self.__class__.__name__}: Unsupported file type: {file_ext}")
            return
        with open(os.path.abspath(file), 'r') as file:
            text = file.read()
            log.info(f"{self.__class__.__name__}: Text: {text[0:40]}...")
            self.ids.text_main.text = text

    def save_textfile(self, file: str):
        if file is not None:
            with open(file, 'w') as file:
                file.write(self.ids.text_main.text)

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

class SpeechJokey(MDApp):
    def build(self):
        # load_widget(os.path.join(os.path.dirname(loaddialog.__file__), 'loaddialog.kv'))
        # load_widget(os.path.join(os.path.dirname(savedialog.__file__), 'savedialog.kv'))
        # load_widget(os.path.join(os.path.dirname(app_settings.__file__), 'AppSettingsPopup.kv'))
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
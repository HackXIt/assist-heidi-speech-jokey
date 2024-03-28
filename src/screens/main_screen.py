# Kivy
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.logger import Logger as log
# KivyMD
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.filemanager import MDFileManager
# stdlib
import os
import sys
# Custom
from modules.dialog.exitdialog import ExitDialog

class MainScreen(MDScreen):
    title = StringProperty()
    text_input = ObjectProperty(None)
    # FIXME The values of this dictionary needs to be kept in sync with the screen names in main.py (Unfortunately)
    menu_options = {
        "Settings": "settings",
        "About": "about",
        "Exit": None # NOTE Exit just closes the app and doesn't have an associated screen
    }
    supported_text_files = ["txt", "md", "rst"]

    def __init__(self, title: str, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        # self.file_load_popup = loaddialog.LoadDialog(callback=self.load_textfile, title="Load file", size_hint=(0.9, 0.9))
        # # self.file_load_popup.size = (400, 400)
        # self.file_save_popup = savedialog.SaveDialog(callback=self.save_textfile, title="Save file", size_hint=(0.9, 0.9))
        # # self.file_save_popup.size = (400, 400)
        # self.settings_popup = app_settings.AppSettingsPopup()
        self.title = title
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
            } for option in self.menu_options.keys()
        ]
        MDDropdownMenu(
            caller=self.ids.btn_menu, items=menu_items
        ).open()
    
    def menu_callback(self, text_item):
        self.manager.transition.direction = 'left'
        if text_item not in self.menu_options.keys():
            log.error(f"{self.__class__.__name__}: Invalid menu option: {text_item}")
            return
        if text_item == "Exit":
            ExitDialog().open()
        self.manager.current = self.menu_options[text_item]

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
            self.opened_file = os.path.basename(path)
            self.last_path = os.path.dirname(path)
            log.debug(f"{self.__class__.__name__}: File: {self.opened_file} - Path: {self.last_path}")
        elif os.path.isdir(path):
            self.last_path = path
        else:
            log.error(f"{self.__class__.__name__}: Invalid path selected: {path}")
        self.exit_manager()
    
    def exit_manager(self, *args):
        if self.last_path is not None and os.path.isfile(os.path.join(self.last_path, self.opened_file)):
            self.opened_file = self.last_path
            self.load_textfile(os.path.join(self.last_path, self.opened_file))
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
        # TODO Implement audio playback (this is mostly a placeholder without a backend implementation yet)
        api = App.get_running_app().api
        if api:
            try:
                api.play(self.text_input.text)
            except NotImplementedError:
                log.error(f"{self.__class__.__name__}: Audio playback not implemented for this API.")
            except Exception as e:
                log.error(f"{self.__class__.__name__}: Error during playback: {e}")

    def on_synthesize(self):
        # TODO Implement text to speech synthesis (this is mostly a placeholder without a backend implementation yet)
        api = App.get_running_app().api
        if api:
            try:
                api.synthesize(self.text_input.text, "output_file.wav")
            except NotImplementedError:
                msg = "Text to speech synthesis not implemented for this API."
                log.error(f"{self.__class__.__name__}: {msg}")
                self.label_status.text = msg
            except Exception as e:
                msg = f"Error during synthesis"
                log.error(f"{self.__class__.__name__}: {msg}: {e}")
                self.ids.label_status.text = msg

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
        self.manager_open = False # FIXME This is used to keep track of the file manager state (open or closed) but is not currently used
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            icon_selection_button="folder-marker"
        )
        # TODO Adjust the scrollbar within MDFileManager to be more visible (not just a thin line)
 
    def on_menu_open(self):
        menu_items = [
            {
                "text": option,
                "on_release": lambda x=option: self.menu_callback(x),
            } for option in self.menu_options.keys()
        ]
        self.drop_menu = MDDropdownMenu(
            caller=self.ids.btn_menu, items=menu_items
        )
        self.drop_menu.open()
    
    def menu_callback(self, text_item):
        self.manager.transition.direction = 'left'
        if text_item not in self.menu_options.keys():
            log.error("%s: Invalid menu option: %s", self.__class__.__name__, text_item)
            return
        if text_item == "Exit":
            ExitDialog().open()
        self.manager.current = self.menu_options[text_item]
        self.drop_menu.dismiss()

    def select_path(self, path):
        log.info("%s: Selected path: %s", self.__class__.__name__, path)
        if os.path.isfile(path):
            self.opened_file = os.path.basename(path)
            self.last_path = os.path.dirname(path)
            log.debug("%s: File: %s - Path: %s", self.__class__.__name__, self.opened_file, self.last_path)
        elif os.path.isdir(path):
            self.last_path = path
        else:
            log.error("%s: Invalid path selected: %s", self.__class__.__name__, path)
        self.exit_manager()
    
    def exit_manager(self, *args):
        if self.last_path is not None and self.opened_file is not None and os.path.isfile(os.path.join(self.last_path, self.opened_file)):
            file = os.path.join(self.last_path, self.opened_file)
            self.load_textfile(file)
        else:
            log.error("%s: No file selected. Last path: %s", self.__class__.__name__, self.last_path)
        self.manager_open = False
        self.file_manager.close()

    def on_load_file(self):
        if self.last_path is not None:
            path = self.last_path
        else:
            path = os.path.expanduser("~")
        self.file_manager.show(path)
        self.manager_open = True

    def on_save_file(self):
        if self.last_path is None or self.opened_file is None:
            log.error("%s: No file opened to save.", self.__class__.__name__)
            return
        file = os.path.join(self.last_path, self.opened_file)
        self.save_textfile(file)

    def load_textfile(self, file: str):
        if file is None:
            log.error("%s: No file selected to load.", self.__class__.__name__)
            return
        file_base, file_ext = os.path.splitext(file)
        log.debug("%s: File: %s - Extension: %s", self.__class__.__name__, file_base, file_ext)
        if file_ext[1:] not in self.supported_text_files: # NOTE [1:] Skip the leading period
            log.error("%s: Unsupported file type: %s. Supported types: %s", self.__class__.__name__, file_ext, self.supported_text_files)
            self.opened_file = None
            self.ids.text_main.text = ""
            return
        # FIXME This is not handling file encoding properly and will cause issues with non-ASCII characters (e.g. mutated vowels such as á, é, í, ó, ú, etc.)
        with open(os.path.abspath(file), 'r') as file:
            text = file.read()
            log.info("%s: Loaded file: %s", self.__class__.__name__, file)
            log.debug("%s: Text: %s...", self.__class__.__name__, text[0:40])
            self.ids.text_main.text = text

    def save_textfile(self, file: str):
        if file is None:
            log.error("%s: No file selected to save.", self.__class__.__name__)
            return
        with open(os.path.abspath(file), 'w') as file:
            file.write(self.ids.text_main.text)
            log.info("%s: Saved file: %s", self.__class__.__name__, file)

    def on_play(self):
        # TODO Implement audio playback (this is mostly a placeholder without a backend implementation yet)
        api = App.get_running_app().api
        if api:
            try:
                api.play(self.text_input.text)
            except NotImplementedError:
                log.error("%s: Audio playback not implemented for this API.", self.__class__.__name__)
            except Exception as e:
                log.error("%s: Error during playback: %s", self.__class__.__name__, e)

    def on_synthesize(self):
        # TODO Implement text to speech synthesis (this is mostly a placeholder without a backend implementation yet)
        api = App.get_running_app().api
        if api:
            try:
                api.synthesize(self.text_input.text, "output_file.wav")
            except NotImplementedError:
                msg = "Text to speech synthesis not implemented for this API."
                log.error("%s: %s", self.__class__.__name__, msg)
                self.label_status.text = msg
            except Exception as e:
                msg = "Error during synthesis"
                log.error("%s: %s: %s", self.__class__.__name__, msg, e)
                self.ids.label_status.text = msg

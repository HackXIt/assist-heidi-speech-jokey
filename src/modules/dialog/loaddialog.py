from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.logger import Logger as log
import os

class LoadDialog(Popup):
    # filebrowser_list = ObjectProperty(None)
    filebrowser_icon = ObjectProperty(None)
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def __init__(self, callback, **kwargs):
        super(LoadDialog, self).__init__(**kwargs)
        self.filebrowser_icon.rootpath = os.path.expanduser("~")
        self.callback = callback

    def on_browser_select(self, selection):
        log.debug(f"Selection: {selection}")
    
    def on_fileload(self):
        selection = self.filebrowser_icon.selection
        log.debug(f"Selection: {selection}")
        self.dismiss()
        if selection:
            log.info(f"Selected file: {selection}")
        else:
            log.info("No file selected")
        self.callback(selection)

    def on_filecancel(self):
        self.dismiss()
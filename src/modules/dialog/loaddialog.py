from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.logger import Logger as log
import os

class LoadDialog(Popup):
    # filebrowser_list = ObjectProperty(None)
    label = ObjectProperty(None)
    filechooser = ObjectProperty(None)
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def __init__(self, callback, **kwargs):
        super(LoadDialog, self).__init__(**kwargs)
        self.filechooser.rootpath = os.path.expanduser("~")
        self.callback = callback

    def on_browser_select(self, selection):
        if len(self.filechooser.selection) == 0:
            return
        selection = selection[0]
        log.debug("Selection: %s", selection)
        self.label.text = selection
    
    def on_fileload(self):
        if len(self.filechooser.selection) == 0:
            log.info("No file selected")
            return
        selection = self.filechooser.selection[0]
        log.info("Selected file: %s", selection)
        self.dismiss()
        self.callback(selection)
        self.label.text = ""
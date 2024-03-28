from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.logger import Logger as log
import os

class SaveDialog(Popup):
    # filebrowser_list = ObjectProperty(None)
    filechooser = ObjectProperty(None)
    filename_input = ObjectProperty(None)
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def __init__(self, callback, **kwargs):
        super(SaveDialog, self).__init__(**kwargs)
        self.filechooser.rootpath = os.path.expanduser("~")
        self.callback = callback

    def on_browser_select(self, selection):
        if len(selection) == 0:
            return
        log.debug("File selected: %s", selection[0])
        self.filename_input.text = os.path.basename(selection[0])

    def on_filesave(self, path, filename):
        if len(path) == 0:
            return
        elif os.path.isfile(path[0]):
            path = os.path.dirname(path[0])
        else:
            path = path[0]
        full_path = os.path.join(path, filename)
        # Implement the actual file saving logic here
        print("Saving to:", full_path)
        # Close the popup after saving
        self.dismiss()
        self.callback(full_path)
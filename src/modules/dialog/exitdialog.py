# Kivy
from kivy.app import App
# KivyMD
from kivymd.uix.dialog import MDDialog
# stdlib
# Custom

class ExitDialog(MDDialog):
    def __init__(self, **kwargs):
        super(ExitDialog, self).__init__(**kwargs)
    
    def on_cancel(self, *args):
        self.dismiss()
    
    def on_exit(self, *args):
        App.get_running_app().stop()
        exit(0)
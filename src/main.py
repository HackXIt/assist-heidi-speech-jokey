# Kivy
from kivymd.app import MDApp
from kivy.logger import Logger as log, LOG_LEVELS
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from kivy.resources import resource_add_path
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.metrics import dp
# KivyMD
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.list import MDListItemTrailingIcon
# stdlib
import os
import sys
# Custom
from screens.about import About
from screens.settings import Settings
from screens.main_screen import MainScreen
from modules.dialog.exitdialog import ExitDialog
from modules.util.widget_loader import load_widget
from settings.app_settings import GlobalSettings 
from api.api_factory import load_apis

TMP_FOLDER = 'tmp'

class TrailingPressedIconButton(
    ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
):
    # NOTE necessary class to allow for the chevron to rotate when the expansion panel is opened or closed
    ...

class SpeechJokey(MDApp):
    def build(self):
        # load_widget(os.path.join(os.path.dirname(loaddialog.__file__), 'loaddialog.kv'))
        # load_widget(os.path.join(os.path.dirname(savedialog.__file__), 'savedialog.kv'))
        # load_widget(os.path.join(os.path.dirname(app_settings.__file__), 'AppSettingsPopup.kv'))
        load_widget(os.path.join(os.path.dirname(sys.modules[MainScreen.__module__].__file__), 'main_screen.kv'))
        load_widget(os.path.join(os.path.dirname(sys.modules[Settings.__module__].__file__), 'settings.kv'))
        load_widget(os.path.join(os.path.dirname(sys.modules[About.__module__].__file__), 'about.kv'))
        load_widget(os.path.join(os.path.dirname(sys.modules[ExitDialog.__module__].__file__), 'exitdialog.kv'))
        self.sm = ScreenManager()
        # self.screens = [Screen(name='Title {}'.format(i)) for i in range(4)]
        # self.screens = {
        #     "main": MainScreen(title="Speech Jokey", name="main"),
        #     "settings": Settings(title="Settings", name="settings"),
        #     "about": About(title="About", name="about")
        # }
        self.global_settings = GlobalSettings()
        self.icon = os.path.join(os.curdir, 'speech-jokey.ico')
        Config.set('kivy','window_icon', self.icon)
        log.setLevel(LOG_LEVELS["debug"])
        self.apis = load_apis()
        self.api = self.apis.get("ExampleAPI", None)
        self.sm.add_widget(MainScreen(title="Speech Jokey", name="main"))
        self.sm.add_widget(Settings(title="Settings", api=self.api, name="settings"))
        self.sm.add_widget(About(title="About", name="about"))
        return self.sm

    # NOTE Global method for all expansion panels to call
    def tap_expansion_chevron(
        self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
    ):
        Animation(
            padding=[0, dp(12), 0, dp(12)]
            if not panel.is_open
            else [0, 0, 0, 0],
            d=0.2,
        ).start(panel)
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(
            chevron
        ) if not panel.is_open else panel.set_chevron_up(chevron)
        # if panel.panel_is_open and len(self.panel.content.children) > 1:
        #     self.panel.height += item.height
        # elif self.panel_is_open and len(self.panel.content.children) == 1:
        #     self.panel.height -= (self.panel.height - item.height) - self.panel.panel_cls.height
        for child in panel.ids.content.children:
            panel.parent.height += child.height + 200
            # panel.ids.content.height += child.height if not panel.is_open else -child.height
            # panel.parent.height += child.height if not panel.is_open else -child.height
            # panel.parent.parent.height += child.height if not panel.is_open else -child.height
         os.makedirs(TMP_FOLDER, exist_ok=True)

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    SpeechJokey(kv_file="SpeechJokey.kv").run()
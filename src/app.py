'''
File: app.py
Created on: Thursday, 2023-10-05 @ 16:22:13
Author: HackXIt (<hackxit@gmail.com>)
-----
Last Modified: Thursday, 2023-10-05 @ 16:30:10
Modified By:  HackXIt (<hackxit@gmail.com>) @ dev-machine
-----
'''

from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
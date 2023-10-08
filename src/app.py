'''
File: app.py
Created on: Thursday, 2023-10-05 @ 16:22:13
Author: HackXIt (<hackxit@gmail.com>)
-----
Last Modified: Sunday, 2023-10-08 @ 11:41:30
Modified By:  HackXIt (<hackxit@gmail.com>) @ HACKXIT
-----
'''
from kivy.app import App
from kivy.uix.splitter import Splitter
from kivy.uix.label import Label


class SplitViewApp(App):
    def build(self):
        # Create a splitter and add two labels
        splitter = Splitter(sizable_from = 'left')
        splitter.add_widget(Label(text = 'Panel 1', size_hint = (0.6, 1)))

        splitter2 = Splitter(sizable_from = 'right')
        splitter2.add_widget(Label(text = 'Panel 2', size_hint = (0.4, 1)))

        splitter.add_widget(splitter2)

        return splitter


if __name__ == "__main__":
    SplitViewApp().run()
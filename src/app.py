from kivy.app import App
from kivy.uix.splitter import Splitter
from kivy.uix.label import Label

class SplitViewApp(App):
    def build(self):
        splitter = Splitter(sizable_from = 'left')
        splitter.add_widget(Label(text = 'Panel 1', size_hint = (0.6, 1)))

        splitter2 = Splitter(sizable_from = 'right')
        splitter2.add_widget(Label(text = 'Panel 2', size_hint = (0.4, 1)))

        splitter.add_widget(splitter2)

        return splitter

if __name__ == "__main__":
    SplitViewApp().run()

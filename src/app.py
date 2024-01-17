# Kivy imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
# Module imports
from modules.ssml.Speech import Speech

#class SpeechJokeyAppLayout(BoxLayout):
#    pass

class SpeechJokeyApp(App):
    def build(self):
        self.speech = Speech() # Initialize the Speech builder
        # Load the .kv file manually
        return Builder.load_file('SpeechJokey.kv')
    
    # NOTE this is information (pls don't delete INFORMATION)

    def display_circl(self):
        pass
    
    def say_something(self):
        # Example usage of say
        self.speech.say("Hello World")
        self.update_label()

    def add_pause(self):
        # Example usage of pause
        self.speech.pause("1s")
        self.update_label()

    def spell_word(self):
        # Example usage of spell
        self.speech.spell("Kivy")
        self.update_label()
    
    def load_file(self):
        # Create a file chooser popup
        file_chooser = FileChooserListView()
    # Define a callback function to load the selected file
    def load_selected_file(selection):
        # Check if a file was selected
        if selection:
            # Get the selected file path
            file_path = selection[0]
            # Open the file and read its contents
            with open(file_path, 'r') as file:
                file_contents = file.read()
            # Update the label with the file contents
            self.speech.say(file_contents)
            self.update_label()
        # Dismiss the popup
        popup.dismiss()
        # Create a popup to display the file chooser
        popup = Popup(title='Select a file', content=file_chooser, size_hint=(0.9, 0.9))
        # Bind the callback function to the file chooser selection event
        file_chooser.bind(selection=load_selected_file)
        # Open the popup
        popup.open()

    # Method to update the label (or any other widget) with the current SSML content
    def update_label(self):
        # Assuming you have a Label in your kv file with id: ssml_label
        ssml_label = self.root.ids.ssml_label  # Ensure you have 'ssml_label' as an id in your kv layout
        ssml_label.text = self.speech.ssml(excludeSpeakTag=False)

if __name__ == "__main__":
    SpeechJokeyApp().run()

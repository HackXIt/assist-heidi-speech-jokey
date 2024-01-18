from kivy.lang import Builder
import os

def load_widget(kv_file_path: str = None):
    # Load kivy file if provided
    if kv_file_path is not None and os.path.exists(kv_file_path):
        Builder.unload_file(kv_file_path)
        Builder.load_file(kv_file_path)
    else:
        raise ValueError("Invalid kv file path provided: {kv_file_path}")
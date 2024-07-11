from io import TextIOWrapper
import os
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Conversation:
    def __init__(self, identifier: str, file_path: str = None):
        self.identifier = identifier
        if file_path == None or not os.path.exists(file_path):
            file_path = f"{identifier}-history.txt"
        with open(file_path, "w") as file:
            file.write(f"Started conversation at {get_current_time()}\n")
        self.file_path = file_path

    def get_read_file(self) -> TextIOWrapper:
        return open(self.file_path, "r")
    def get_write_file(self) -> TextIOWrapper:
        return open(self.file_path, "a")
    def add_log(self, source: str, message: str):
        self.get_write_file().write(f"{get_current_time()} [{source}]: {message}\n")
    def delete_conversation(self):
        os.remove(self.file_path)
    
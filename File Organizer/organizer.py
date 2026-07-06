from pathlib import Path
from shutil import move
import shutil

class File_Organizer:

    FILE_TYPES = {
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",

        ".pdf": "Documents",
        ".docx": "Documents",
        ".txt": "Documents",

        ".mp4": "Videos",
        ".avi": "Videos",

        ".mp3": "Music",

        ".zip": "Archives",
        ".rar": "Archives",
    }

    def __init__(self):
        self.folder = None

    def select_folder(self):
        path = input("Enter Folder path: ")
        if not path:
            return False, "path cannot be empty"
        folder = Path(path)
        if not folder.exists():
            return False, "Folder does not exist."

        if not folder.is_dir():
            return False, "The specified path is not a directory"

        self.folder = folder
        return True, "Folder selected successfully"

    def show_files(self):
        if self.folder is None:
            return False, "No Folder Selected" 
        for file in self.folder.iterdir():
            print(file.name)
        return True, "File Listed successfully."

    def get_category(self,file):
        return self.FILE_TYPES.get(file.suffix.lower(), 'others')

    def organize_files(self):
        if self.folder is None:
            return False, "No folder selected."

        for file in self.folder.iterdir():
            if file.is_file():
                category = self.get_category(file)

                folder = self.folder / category
                folder.mkdir(parents=True, exist_ok=True)

                destination = folder/file.name
                if file.parent.name == category:
                    continue
                shutil.move(file, destination)
        
        return True, "Files organized successfully."

    def get_statistics(self):
        if self.folder is None:
            return False, "No Folder selected"

        count = {
            "Images" : 0,
            "Documents" : 0,
            "Videos" : 0,
            "Archives" : 0,
            "Music" : 0,
            "others" : 0
        }

        for file in self.folder.iterdir():
            if file.is_file():
                category = self.get_category(file)

                count[category] += 1

        return True, count
            
            

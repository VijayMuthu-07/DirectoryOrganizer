import os
from pathlib import Path

subdirectory = {
    "Documents": [".pdf", ".txt", ".rtf"],
    "LibreOffice": [".ppt", ".odt", ".pptx", ".doc", ".docx", ".odf"],
    "Videos": [".mp4", ".mov", ".wmv", ".avi", ".mkv"],
    "Images": [".jpg", ".jpeg", ".png", ".ico", ".gif", ".webp"],
    "LabFiles": [".fig", ".m", ".py", ".slddrw"],
    "Audios": [".mp3", ".wav", ".wma"]   
}
#subdir = {
   # "PDF": ".pdf", "Text": ".txt", "Word": [".docx", ".doc", ".odt"],
    #"Powerpoint": [".pptx", ".ppt", ".odf"], "Excel": [".xlsx"],
    #"Videos": [".mp4", ".mov", ".wmv", ".avi", ".mkv"],
    #"Images": [".jpg", ".jpeg", ".png", ".ico", ".gif", ".webp"],
    #"Audios": [".mp3", ".wav", ".wma"]
#}

def pickDirectory(extension):
    for category, suffixes in subdirectory.items():
        if extension in suffixes:
            return category
    return "Misc"

def organizeDirectory(path):
    items = os.scandir(path)
    for item in items:
        if item.is_dir():
            continue
        filePath = Path(item)
        fileName = os.path.basename(filePath)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(path).joinpath(Path(directory))
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(fileName))

if __name__ == '__main__':
    try:
        print("Welcome TO Directory Organizer")
        path = input("Enter the directory path: ")
        organizeDirectory(path)
        print("Directory organized successfully")
        
    except Exception:
        print("Something Went Wrong")
    finally:
        input("Press Enter to exit program.")
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:18:53 2024

@author: DamilolaAyodele
"""

import os
import shutil
from pathlib import Path

# Formats for different file types/categories
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".mts", ".m2ts", ".ts", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf", '.mkv', ".srt", ".MP4")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif", ".PNG")

document = ('.doc', '.docx', '.html', '.htm', '.odt',
            '.pdf', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt', '.csv', '.txt', ".bib")

compressed = ('.zip', '.zipx', '.rar', '.7z','.gz', '.iso', '.img', '.tar', '.gz', '.taz', 
          '.tgz', '.gzip', '.xz', '.bz2', '.vhd', '.tz', '.cab', '.mime', '.vmdk', 
          '.tar', '.bz', '.Lha', '.lzh', '.hqx', '.xx', '.tbz', 'vsix')

scripts = (".py", ".ipynb", ".pyc", ".pyd", ".pyo", ".pyw", ".whl", ".pyx", ".pxd",
           ".pxi", ".pyp", ".pyz", ".egg", ".js", ".php"".rb", ".java", ".cpp" ".h", ".cs"".go",
           ".swift", ".sh", ".pl", ".lua", ".ps1",".bat", ".css")

program = (".exe", ".deskthemepack", '.diagcab')

folder = ('')

# Create the function to format the directory_path
def convert_to_cross_platform_path(path):
    """Convert Windows-style path to cross-platform path."""
    return str(Path(path).as_posix())

# Function to create destination folders if they don't exist
def create_destination_folders(destination_path):
    folders = ['Pictures', 'Audio', 'Videos', 'Documents', 'Compressed', 'Programs', 'Scripts', 'Others']
    for folder_name in folders:
        folder_path = os.path.join(destination_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

# Functions for sorting different files
def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_img(file):
    return os.path.splitext(file)[1] in img

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_document(file):
    return os.path.splitext(file)[1] in document

def is_compressed(file):
    return os.path.splitext(file)[1] in compressed

def is_script(file):
    return os.path.splitext(file)[1] in scripts

def is_folder(file):
    return os.path.splitext(file)[1] in folder

def is_app(file):
    return os.path.splitext(file)[1] in program

# Get input from the user for the destination path
destination_path = Path(input("Enter the destination path: "))

# Convert Windows-style path to cross-platform path
destination_path = convert_to_cross_platform_path(destination_path)

# Ensure the destination folders exist
create_destination_folders(destination_path)

# Loop for sorting the files into different folders
for file in os.listdir(destination_path):
    if os.path.isfile(os.path.join(destination_path, file)):
        try:
            if is_img(file):
                shutil.move(os.path.join(destination_path, file), os.path.join(destination_path, 'Pictures', file))
            elif is_audio(file):
                shutil.move(os.path.join(destination_path, file), os.path.join(destination_path, 'Audio', file))
            elif is_video(file):
                shutil.move(os.path.join(destination_path, file), os.path.join(destination_path, 'Videos', file))
            elif is_document(file):
                shutil.move(os.path.join(destination_path, file), os.path.join(destination_path, 'Documents', file))
            elif is_compressed(file):
                shutil.move(os.path.join(destination_path, file), os.path.join(destination_path, 'Compressed', file))
            elif is_app(file):
                shutil.move(os.path.join(destination_path, file), os.path.join(destination_path, 'Programs', file))
            elif is_script(file):
                shutil.move(os.path.join(destination_path, file), os.path.join(destination_path, 'Scripts', file))
            elif is_folder(file):
                print('This is a folder')
            else:
                shutil.move(os.path.join(destination_path, file), os.path.join(destination_path, 'Others', file))
        except FileNotFoundError:
            print(f"FileNotFoundError: [Errno 2] No such file or directory: {file}")

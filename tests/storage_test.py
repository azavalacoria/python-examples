'''
From how-to import modules from parent:
    - https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
'''
import os, sys
from pathlib import Path
sys.path.insert(1, str(Path(__file__).resolve().parents[1]))
from classes.file_helper import file_helper

fh = file_helper('files-example')
fh.add_file()
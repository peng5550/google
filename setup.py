import sys
from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = r'C:\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36-32\tcl\tk8.6'


include_files=[
    r'C:\Python36-32\DLLs\tcl86t.dll',
    r'C:\Python36-32\DLLs\tk86t.dll'
]




# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"],"include_files":include_files}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="video1",#打完包后取的名字
      version="2.1",#版本
      description="aaaaa",#描述
      options={"build_exe": build_exe_options},
      executables=[Executable("video.py", base=base)])
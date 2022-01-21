import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files (x86)\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\bruno\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_calculator():
    sp.Popen(paths['calculator'])


def open_cmd():
    os.system('start cmd')

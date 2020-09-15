#!/usr/bin/python3

import os
import threading

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper

from Folder import Folder
from Key import Key

from Hue import Hue_Folder

from OBS import *


root = Folder("root", 32)

folder_latex = Folder("LaTeX", 32)
folder_xournal = Folder("Xournal", 32)
folder_obs = Folder("OBS", 32)
folder_epson = Folder("Epson", 32)
folder_hue = Hue_Folder(32)

root.set_key(0, "LaTeX", "icon platzhalter", folder_latex)
root.set_key(1, "Xournal", "icon platzhalter", folder_xournal)
root.set_key(2, "OBS", "icon platzhalter", folder_obs)
root.set_key(3, "Epson", "icon platzhalter", folder_epson)
root.set_key(4, "Hue", "icon platzhalter", folder_hue)


folder_obs.set_key(0, "Recording", "icon platzhalter", toggle_recording)
folder_obs.set_key(1, "Streaming", "icon platzhalter", toggle_streaming)





root.current_dir()
root.key_pressed_callback(5)
root.key_pressed_callback(6)
root.key_pressed_callback(2)
root.current_dir()
root.key_pressed_callback(2)
root.current_dir()
root.key_pressed_callback(0)
root.key_pressed_callback(1)
root.key_pressed_callback(31)
root.current_dir()
root.key_pressed_callback(4)
root.current_dir()
root.key_pressed_callback(0)
root.current_dir()
root.key_pressed_callback(31)
root.key_pressed_callback(1)
root.current_dir()
root.key_pressed_callback(31)
root.current_dir()



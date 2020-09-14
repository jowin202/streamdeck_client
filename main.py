#!/usr/bin/python3

import os
import threading

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper

from Folder import Folder
from Key import Key



root = Folder("root", 32)

folder_latex = Folder("LaTeX", 32)
folder_xournal = Folder("Xournal", 32)
folder_obs = Folder("OBS", 32)
folder_epson = Folder("Epson", 32)
folder_hue = Folder("Hue", 32)

root.set_key(0, "icon platzhalter", folder_latex)
root.set_key(1, "icon platzhalter", folder_xournal)
root.set_key(2, "icon platzhalter", folder_obs)
root.set_key(3, "icon platzhalter", folder_epson)
root.set_key(4, "icon platzhalter", folder_hue)



root.key_pressed_callback(5)
root.key_pressed_callback(6)
root.key_pressed_callback(2)
root.key_pressed_callback(2)
root.current_dir()

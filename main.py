#!/usr/bin/python3

import os
import threading
import time

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
import PIL

from streamdeck import render_key_image

from Folder import Folder
from Key import Key

from LaTeX import LaTeX_Folder
from Hue import Hue_Folder
from Xournal import Xournal_Folder

from OBS import OBS_Folder

ICON_PATH = os.path.join(os.path.dirname(__file__), "icons")



root = Folder("root", 32)

folder_latex = LaTeX_Folder(32)
folder_xournal = Xournal_Folder(32)
folder_obs = OBS_Folder(32)
folder_epson = Folder("Epson", 32)
#folder_hue = Hue_Folder(32)

root.set_key(0, "LaTeX", "latex.png", folder_latex)
root.set_key(1, "Xournal", "xournal/xournal.png", folder_xournal)
root.set_key(2, "OBS", "obs.png", folder_obs)
root.set_key(3, "Epson", "epson.jpg", folder_epson)
#root.set_key(4, "Hue", "hue.png", folder_hue)







'''root.current_dir()
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
root.key_pressed_callback(0)
root.current_dir()
root.key_pressed_callback(31)
root.key_pressed_callback(1)
root.current_dir()
root.key_pressed_callback(31)
root.current_dir()'''



#print(root.get_keys())
#root.key_pressed_callback(4)
#print(root.get_keys())


#exit()



    

def update_buttons(deck):
    keys = root.get_keys()
    for i in keys:
        key = keys[i]
        icon = key[0]
        if type(icon) == str:
            icon_filename = os.path.join(ICON_PATH, icon)
            try:
                image = Image.open(icon_filename)
            except:
                image = Image.open(os.path.join(ICON_PATH, "notfound.png"))
        elif type(icon) == PIL.Image.Image:
            image = icon
        img = render_key_image(deck, image, os.path.join(ICON_PATH, "font.ttf"), key[1])
        deck.set_key_image(i, img)



def key_change_callback(deck, key, state):
    print("Deck {} Key {} = {}".format(deck.id(), key, state), flush=True)
    if state == True:
        root.key_pressed_callback(key)
    else:
        deck.reset()
        update_buttons(deck)





while True:
    streamdecks = DeviceManager().enumerate()
    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))
    for index, deck in enumerate(streamdecks):
        deck.open()
        deck.reset()

        print("Opened '{}' device (serial number: '{}')".format(deck.deck_type(), deck.get_serial_number()))

        # Set initial screen brightness to 30%.
        deck.set_brightness(100)

        # Set initial key images.
        update_buttons(deck)

        # Register callback function for when a key state changes.
        deck.set_key_callback(key_change_callback)

        # Wait until all application threads have terminated (for this example,
        # this is when all deck handles are closed).
        for t in threading.enumerate():
            if t is threading.currentThread():
                continue

            if t.is_alive():
                t.join()
    time.sleep(10)
    

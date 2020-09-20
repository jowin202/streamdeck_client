from Folder import Folder
from Key import Key

import math

from PIL import Image, ImageDraw, ImageFont

import os


ICON_PATH = os.path.join(os.path.dirname(__file__), "icons")

def to_hex(num):
    num = round(num)
    if num <= 9:
        return str(int(num))
    elif num == 10: return 'A'
    elif num == 11: return 'B'
    elif num == 12: return 'C'
    elif num == 13: return 'D'
    elif num == 14: return 'E'
    elif num == 15: return 'F'


class Color_Folder(Folder):
    state = 1
    r = 80
    g = 80
    b = 80
    color_changed_callback = None # change color somewhere else
    color_source = None # get initial color from somewhere else when opened
    
    def __init__(self, maxkey):
        super().__init__("Color", maxkey)
        self.update_buttons()
        
    def update_buttons(self):
        self.set_key(1, "", self.create_icon("+1"), lambda: self.change_value('r', 16))
        self.set_key(2, "", self.create_icon("+1"), lambda: self.change_value('r', 1))
        self.set_key(3, "", self.create_icon("+1"), lambda: self.change_value('g', 16))
        self.set_key(4, "", self.create_icon("+1"), lambda: self.change_value('g', 1))
        self.set_key(5, "", self.create_icon("+1"), lambda: self.change_value('b', 16))
        self.set_key(6, "", self.create_icon("+1"), lambda: self.change_value('b', 1))
        
        self.set_key (9, "", self.create_icon_color(self.r,self.g,self.b, to_hex(self.r//16)), None)
        self.set_key(10, "", self.create_icon_color(self.r,self.g,self.b, to_hex(self.r % 16)), None)
        self.set_key(11, "", self.create_icon_color(self.r,self.g,self.b, to_hex(self.g//16)), None)
        self.set_key(12, "", self.create_icon_color(self.r,self.g,self.b, to_hex(self.g % 16)), None)
        self.set_key(13, "", self.create_icon_color(self.r,self.g,self.b, to_hex(self.b//16)), None)
        self.set_key(14, "", self.create_icon_color(self.r,self.g,self.b, to_hex(self.b % 16)), None)
        
        
        self.set_key(17, "", self.create_icon("-1"), lambda: self.change_value('r', -16))
        self.set_key(18, "", self.create_icon("-1"), lambda: self.change_value('r', -1))
        self.set_key(19, "", self.create_icon("-1"), lambda: self.change_value('g', -16))
        self.set_key(20, "", self.create_icon("-1"), lambda: self.change_value('g', -1))
        self.set_key(21, "", self.create_icon("-1"), lambda: self.change_value('b', -16))
        self.set_key(22, "", self.create_icon("-1"), lambda: self.change_value('b', -1))
        
        
        self.set_key(16, "", self.create_icon_color(255,120,0, ''), lambda: self.set_color(255,120,0))
        
        self.set_key(24, "", self.create_icon_color(255,0,0, ''), lambda: self.set_color(255,0,0))
        self.set_key(25, "", self.create_icon_color(0,255,0, ''), lambda: self.set_color(0,255,0))
        self.set_key(26, "", self.create_icon_color(0,0,255, ''), lambda: self.set_color(0,0,255))
        self.set_key(27, "", self.create_icon_color(255,255,0, ''), lambda: self.set_color(255,255,0))
        self.set_key(28, "", self.create_icon_color(255,0,255, ''), lambda: self.set_color(255,0,255))
        self.set_key(29, "", self.create_icon_color(0,255,255, ''), lambda: self.set_color(0,255,255))
        self.set_key(30, "", self.create_icon_color(255,255,255, ''), lambda: self.set_color(255,255,255))
        if self.color_changed_callback != None:
            self.color_changed_callback(self.r,self.g,self.b)

        
    def create_icon(self,text):
        W, H = (100, 100)
        img = Image.new('RGB', (W, H), color = (80, 80, 80))
                
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(os.path.join(ICON_PATH, "font.ttf"), 60)
        w, h = d.textsize(text)
        d.text(((W-w)/2-20,(H-h)/2-30), text, fill=(175,175,175), font=font, align="center")
        
        return img
        
    def create_icon_color(self,r,g,b,text):
        W, H = (100, 100)
        img = Image.new('RGB', (W, H), color = ((int(r), int(g), int(b))))
                
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(os.path.join(ICON_PATH, "font.ttf"), 60)
        w, h = d.textsize(text)
        d.text(((W-w)/2-20,(H-h)/2-30), text, fill=(255-int(r),255-int(g),255-int(b)), font=font, align="center")
        
        return img

    def set_color(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        self.update_buttons()

    def change_value(self, col, val):
        if col == 'r':
            self.r += val
        elif col == 'g':
            self.g += val
        else:
            self.b += val
        
        self.r = min(max(self.r,0),255)
        self.g = min(max(self.g,0),255)
        self.b = min(max(self.b,0),255)
        
        self.update_buttons()
    
    def on_open(self):
        self.r, self.g, self.b = self.color_source()
        self.update_buttons()

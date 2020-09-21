from PIL import Image, ImageDraw, ImageFont
from Folder import Folder
from Color import Color_Folder
import socket


class Xournal_Folder(Folder):
    def __init__(self, maxkey):
        super().__init__("Xournal", maxkey)
        
        color = Color_Folder(32)
        color.color_changed_callback = self.send_color
        
        self.set_key(16, "Black", self.create_icon_color(0,0,0), lambda: self.send_color(0,0,0))
        self.set_key(17, "Blue", self.create_icon_color(0,0,255), lambda: self.send_color(0,0,255))
        self.set_key(18, "Red", self.create_icon_color(255,0,0), lambda: self.send_color(255,0,0))
        self.set_key(19, "Green", self.create_icon_color(0,128,0), lambda: self.send_color(0,128,0))
        self.set_key(20, "Gray", self.create_icon_color(128,128,128), lambda: self.send_color(128,128,128))
        self.set_key(21, "LightBlue", self.create_icon_color(0,192,255), lambda: self.send_color(0,192,255))

        self.set_key(24, "LightGreen", self.create_icon_color(0,255,0), lambda: self.send_color(0,255,0))
        self.set_key(25, "Magenta", self.create_icon_color(255,0,255), lambda: self.send_color(255,0,255))
        self.set_key(26, "Orange", self.create_icon_color(255,128,0), lambda: self.send_color(255,128,0))
        self.set_key(27, "Yellow", self.create_icon_color(255,255,0), lambda: self.send_color(255,255,0))
        self.set_key(28, "White", self.create_icon_color(255,255,255), lambda: self.send_color(255,255,255))
        self.set_key(29, "Choose Color", "color.png", color)
        
        
    def create_icon_color(self,r,g,b):
        W, H = (100, 100)
        img = Image.new('RGB', (W, H), color = ((int(r), int(g), int(b))))
        return img
    
    
    def send_color(self,r,g,b):
        msg = 'hexcol_' + str("%0.2X" % r) + str("%0.2X" % g) + str("%0.2X" % b)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(msg.encode())


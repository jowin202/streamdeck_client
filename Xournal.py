from PIL import Image, ImageDraw, ImageFont
from Folder import Folder
from Color import Color_Folder
import socket


class Xournal_Folder(Folder):
    def __init__(self, maxkey):
        super().__init__("Xournal", maxkey)
        
        color = Color_Folder(32)
        color.color_changed_callback = self.send_color
        
        
        self.set_key(0, "Pen", "xournal_pencil.png", self.set_pen)
        self.set_key(1, "Eraser", "xournal_eraser.png", self.set_eraser)
        self.set_key(2, "Highlighter", "xournal_highlighter.png", self.set_highlighter)
        self.set_key(3, "Rectangle", "xournal_rect.png", self.set_rect)
        self.set_key(4, "Vspace", "xournal_vspace.png", self.set_vspace)
        self.set_key(5, "Move", "xournal_move.png", self.set_move)
        
        self.set_key(6, "Graph", "xournal_graph.png", self.set_graph)
        self.set_key(14, "Blank", self.create_icon_color(255,255,255), self.set_blank)
        
        
        self.set_key(7, "New Page before", "xournal_newpage.png", self.newpage_before)
        self.set_key(15, "New Page after", "xournal_newpage.png", self.newpage_after)
        self.set_key(23, "New Page end", "xournal_newpage.png", self.newpage_end)
        
        self.set_key(8, "Very Thin", "thickness_very_fine.png", lambda: self.set_thickness(0))
        self.set_key(9, "Thin", "thickness_fine.png", lambda: self.set_thickness(1))
        self.set_key(10, "Medium", "thickness_medium.png", lambda: self.set_thickness(2))
        self.set_key(11, "Thick", "thickness_thick.png", lambda: self.set_thickness(3))
        self.set_key(12, "Very Thick", "thickness_very_thick.png", lambda: self.set_thickness(4))
        self.set_key(13, "Sensitivity", "xournal_sensitivity.png", self.toggle_sensitivity)


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


    def set_pen(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"select_pen")
        
    def set_eraser(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"select_eraser")
        
        
    def set_highlighter(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"select_highlighter")
        
    def set_rect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"select_rect")
        
    def set_vspace(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"select_vspace")
        
    def set_move(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"select_move")
        
    def toggle_sensitivity(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"toggle_sensitivity")
        
    def newpage_before(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"newpage_before")
    
    def newpage_after(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"newpage_after")

    def newpage_end(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"newpage_end")
    

    def set_graph(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"paper_graph")
    
    def set_blank(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        s.sendall(b"paper_blank")
    
    def set_thickness(self, val):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 2345))
        if val == 0:
            s.sendall(b"pen_veryfine")
        elif val == 1:
            s.sendall(b"pen_fine")
        elif val == 2:
            s.sendall(b"pen_medium")
        elif val == 3:
            s.sendall(b"pen_thick")
        elif val == 4:
            s.sendall(b"pen_verythick")

from Folder import Folder
from Key import Key

from Color import Color_Folder

import ssl

import urllib, urllib.request, json
from phue import Bridge

import math
import colorsys






class Hue_Folder(Folder):
    bridge = None
    
    def __init__(self, maxkey):
        super().__init__("Hue", maxkey)
        
        folder_lights = Folder("Lights", maxkey)
        folder_rooms = Folder("Rooms", maxkey)
        
        self.set_key(0, "Lights", "light.png", folder_lights)
        self.set_key(1, "Rooms", "room.png", folder_rooms)
        
        
        #parse json resonse to get ip
        #try:
        if True:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen("https://discovery.meethue.com/", context=ctx) as url:
                data = json.loads(url.read())
                ip = "192.168.0.160" #data[0]['internalipaddress'] #TODO
                self.bridge = Bridge(ip)
                self.bridge.connect()
                
                i = 0
                for light in self.bridge.lights:
                    f = Hue_Light_Folder(light.name, maxkey, self.bridge, light)
                    folder_lights.set_key(i, light.name, "light.png", f)
                    i += 1
                    
                i = 0
                for group in self.bridge.groups:
                    f = Hue_Light_Folder(group.name, maxkey, self.bridge, group)
                    folder_rooms.set_key(i, group.name, "room.png", f)
                    i += 1
        #except:
        #    print("hue error")
        #    pass # do nothing in case of error, empty folder


class Hue_Light_Folder(Folder):
    bridge = None
    light = None
    
    def __init__(self, name, maxkey, bridge, light):
        super().__init__(name, maxkey)
        self.light = light
        self.bridge = bridge
        
        color = Color_Folder(32)
        color.r, color.g, color.b = self.get_color()
        
        color.color_changed_callback = self.set_color # return color when color_changed
        color.color_source = self.get_color
        
        self.set_key(0, "On", "platzhalter", self.on_off)
        self.set_key(1, "Brightness 25%", "platzhalter", lambda: self.set_bri(64))
        self.set_key(2, "Brightness 50%", "platzhalter", lambda: self.set_bri(128))
        self.set_key(3, "Brightness 75%", "platzhalter", lambda: self.set_bri(192))
        self.set_key(4, "Brightness 100%", "platzhalter", lambda: self.set_bri(255))
        self.set_key(5, "Color", "color.png", color)
        
        
    def on_off(self):
        self.light.on ^= True
        self.keys[0].text = "Off" if self.light.on else "On"
            

    def set_bri(self, bri):
        self.light.brightness = bri

    def set_color(self,r,g,b):
        h,s,v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        self.light.hue = math.ceil(65535.0*h)
        self.light.saturation = math.ceil(255*s)
        self.light.brightness = math.ceil(255*v)
        
    def get_color(self):
        r,g,b = colorsys.hsv_to_rgb(self.light.hue/65535.0, self.light.saturation/255.0, self.light.brightness/255.0)
        return 255*r,255*g,255*b

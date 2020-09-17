from Folder import Folder
from Key import Key

import ssl

import urllib, urllib.request, json
from phue import Bridge








class Hue_Folder(Folder):
    bridge = None
    
    def __init__(self, maxkey):
        super().__init__("Hue", maxkey)
        
        folder_lights = Folder("Lights", maxkey)
        folder_rooms = Folder("Rooms", maxkey)
        
        self.set_key(0, "Lights", "light.png", folder_lights)
        self.set_key(1, "Rooms", "room.png", folder_rooms)
        
        
        #parse json resonse to get ip
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen("https://discovery.meethue.com/", context=ctx) as url:
                data = json.loads(url.read())
                ip = data[0]['internalipaddress']
                self.bridge = Bridge(ip)
                self.bridge.connect()
                
                i = 0
                for light in self.bridge.lights:
                    f = Hue_Light_Folder(light.name, maxkey, self.bridge, light)
                    folder_lights.set_key(i, light.name, "light.png", f)
                    i += 1
                    
                i = 0
                for group in self.bridge.groups:
                    f = Folder(group.name, maxkey)
                    folder_rooms.set_key(i, group.name, "room.png", None)
                    i += 1
        except:
            pass # do nothing in case of error, empty folder


class Hue_Light_Folder(Folder):
    bridge = None
    light = None
    
    def __init__(self, name, maxkey, bridge, light):
        super().__init__(name, maxkey)
        self.light = light
        self.bridge = bridge
        
        self.set_key(0, "On", "platzhalter", self.on_off)
        self.set_key(1, "Brightness 25%", "platzhalter", lambda: self.set_bri(64))
        self.set_key(2, "Brightness 50%", "platzhalter", lambda: self.set_bri(128))
        self.set_key(3, "Brightness 75%", "platzhalter", lambda: self.set_bri(192))
        self.set_key(4, "Brightness 100%", "platzhalter", lambda: self.set_bri(255))
        
        
    def on_off(self):
        self.light.on ^= True
        self.keys[0].text = "Off" if self.light.on else "On"
            

    def set_bri(self, bri):
        print("test")
        print(bri)
        self.light.brightness = bri

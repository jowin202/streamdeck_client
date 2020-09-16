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
        
        self.set_key(0, "Lights", "icon platzhalter", folder_lights)
        self.set_key(1, "Rooms", "icon platzhalter", folder_rooms)
        
        
        #parse json resonse to get ip
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
                f = Folder(light.name, maxkey)
                folder_lights.set_key(i, light.name, "platzhalter", None)
                i += 1
                
            i = 0
            for group in self.bridge.groups:
                f = Folder(group.name, maxkey)
                folder_rooms.set_key(i, group.name, "platzhalter", None)
                i += 1
        
    

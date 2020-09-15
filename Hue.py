from Folder import Folder
from Key import Key

import urllib, urllib.request, json
from phue import Bridge

class Hue_Folder(Folder):
    def __init__(self, maxkey):
        super().__init__("Hue", maxkey)
        
        folder_lights = Folder("Lights", maxkey)
        folder_rooms = Folder("Rooms", maxkey)
        
        self.set_key(0, "Lights", "icon platzhalter", folder_lights)
        self.set_key(1, "Rooms", "icon platzhalter", folder_rooms)
        
        
        #parse json resonse to get ip
        #with urllib.request.urlopen("https://discovery.meethue.com/") as url:
        #    data = json.loads(response.read())
        
        ip = "192.168.0.160"

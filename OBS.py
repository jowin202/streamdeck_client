from Folder import Folder

import asyncio
import simpleobsws



class OBS_Folder(Folder):
    def __init__(self, maxkey):
        super().__init__("OBS", maxkey)
        
        self.set_key(0, "Recording", "icon platzhalter", toggle_recording)
        self.set_key(1, "Streaming", "icon platzhalter", toggle_streaming)
        self.set_key(2, "Mute Mic", "mute.png", toggle_mute_mic)
        
        self.set_key(24, "Black Screen", "icon platzhalter", set_black_screen)
        self.set_key(25, "Titelpage", "icon platzhalter", set_titlepage)
        self.set_key(26, "Xournal", "xournal/xournal.png", set_xournal)
        self.set_key(27, "Xournal+Cam", "cam.png", set_xournal_webcam)

    


def set_scene(scene_name):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password='', loop=loop) # Every possible argument has been passed, but none are required. See lib code for defaults.

    async def make_request():
        await ws.connect() # Make the connection to OBS-Websocket
        data = {'scene-name':scene_name}
        result = await ws.call('SetCurrentScene', data) # Make a request with the given data
        print(result)
        await ws.disconnect() # Clean things up by disconnecting. Only really required in a few specific situations, but good practice if you are done making requests or listening to events.

    loop.run_until_complete(make_request())
    
    
    
def set_black_screen():
    set_scene("Scene_Black")
    
def set_titlepage():
    set_scene("Scene_Titelpage")
    
def set_xournal():
    set_scene("Scene_Xournal")
    
def set_xournal_webcam():
    set_scene("Scene_Xournal_Webcam")
    

def toggle_recording():
    print("toggle recording")
    
def toggle_streaming():
    print("toggle streaming")
    
def toggle_mute_mic():
    print("toggle mute mic")

    
def show_xournal():
    print("show xournal")
    
def show_webcam():
    print("show webcam")

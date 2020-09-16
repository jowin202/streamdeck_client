from Folder import Folder


class OBS_Folder(Folder):
    def __init__(self, maxkey):
        super().__init__("OBS", maxkey)
        
        self.set_key(0, "Recording", "icon platzhalter", toggle_recording)
        self.set_key(1, "Streaming", "icon platzhalter", toggle_streaming)
        self.set_key(2, "Mute Mic", "icon platzhalter", toggle_mute_mic)
        self.set_key(3, "Xournal", "icon platzhalter", show_xournal)
        self.set_key(4, "Webcam", "icon platzhalter", show_webcam)

    
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

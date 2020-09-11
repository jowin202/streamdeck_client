

class Folder:
    num = -1
    name = ""
    icons = []
    callb = []
    next_dir = None
    prev_dir = None
    selected_key = -1
    
    def __init__(self, name, num):
        self.num = num
        self.name = name
        self.icons = [None] * num
        self.callb = [None] * num
        #todo back button
        
    def set_key(self, key, icon, callb):
        self.icons[key] = icon
        self.callb[key] = callb
        if type(callb) == Folder:
            callb.prev_dir = self
        
    def key_pressed_callback(self, key):
        if self.callb[key] == None:
            print("button " + str(key) + " in folder " + str(self.name) + " does not work")
        if type(self.callb[key]) == Folder: # check if back button
            self.next_dir = self.callb[key]
        else:
            pass # run programm
        
    
    def current_dir(self):
        print(self.name)
        if self.next_dir:
            self.next_dir.current_dir()

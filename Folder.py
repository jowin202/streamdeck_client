from Key import Key

class Folder:
    num = -1
    name = ""
    keys = []
    next_dir = None
    prev_dir = None
    selected_key = -1
    
    def __init__(self, name, num):
        self.num = num
        self.name = name
        self.keys = [None] * num
        #todo back button
        
    def set_key(self, keynr, icon, callback):
        if type(callback) == Folder:
            callback.prev_dir = self
        self.keys[keynr] = Key(keynr, icon, callback)
        
        
    #export this from class
    def key_pressed_callback(self, keynr):
        if self.keys[keynr] == None or self.keys[keynr].callback == None:
            print("button " + str(keynr) + " in folder " + str(self.name) + " does not work")
        elif type(self.keys[keynr].callback) == Folder: # check if back button
            self.next_dir = self.keys[keynr].callback
        else:
            pass # run programm
        
    
    def current_dir(self):
        if self.next_dir:
            self.next_dir.current_dir()
        elif self.next_dir == None:
            print(self.name)

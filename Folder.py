from Key import Key

class Folder:
    maxkey = -1
    name = ""
    keys = []
    next_dir = None
    prev_dir = None
    selected_key = -1
    
    def __init__(self, name, maxkey):
        self.maxkey = maxkey
        self.name = name
        self.keys = [None] * maxkey
        self.keys[maxkey-1] = Key(None, None, None, None)
        self.keys[maxkey-1].is_back_button = True
        #todo back button
        
    def set_key(self, keynr, text, icon, callback):
        if issubclass(type(callback), Folder):
            callback.prev_dir = self
        self.keys[keynr] = Key(keynr, text, icon, callback)
        
        
    #export this from class
    def key_pressed_callback(self, keynr):
        current_dir = self
        while current_dir.next_dir != None:
            current_dir = current_dir.next_dir
        
        if current_dir.keys[keynr] != None and current_dir.keys[keynr].is_back_button:
            current_dir.prev_dir.next_dir = None
        elif current_dir.keys[keynr] == None or current_dir.keys[keynr].callback == None:
            print("button " + str(keynr) + " in folder " + str(self.name) + " does not work")
        elif issubclass(type(current_dir.keys[keynr].callback), Folder): 
            current_dir.next_dir = current_dir.keys[keynr].callback
        else:
            current_dir.keys[keynr].callback()
        
    
    def current_dir(self):
        if self.next_dir:
            self.next_dir.current_dir()
        elif self.next_dir == None:
            print(self.name)

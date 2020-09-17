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
        self.keys[maxkey-1] = Key(None, "Back", "back.jpg", None)
        self.keys[maxkey-1].is_back_button = True
        #todo back button
        
    def set_key(self, keynr, text, icon, callback):
        if issubclass(type(callback), Folder):
            callback.prev_dir = self
        self.keys[keynr] = Key(keynr, text, icon, callback)
        
        
    def key_pressed_callback(self, keynr):
        if self.next_dir != None:
            self.next_dir.key_pressed_callback(keynr)
            return
        
        if self.keys[keynr] != None and self.keys[keynr].is_back_button:
            self.prev_dir.next_dir = None
        elif self.keys[keynr] == None or self.keys[keynr].callback == None:
            print("button " + str(keynr) + " in folder " + str(self.name) + " does not work")
        elif issubclass(type(self.keys[keynr].callback), Folder): 
            self.next_dir = self.keys[keynr].callback
        else:
            self.keys[keynr].callback()
        
    
    def current_dir(self):
        if self.next_dir:
            self.next_dir.current_dir()
        elif self.next_dir == None:
            print(self.name)

    def show_dir(self, depth = 0):
        indent = '\t' * depth
        for i in range(self.maxkey):
            if self.keys[i] != None:
                print(indent + str(i) + ": " + self.keys[i].text)
                if issubclass(type(self.keys[i].callback), Folder):
                    self.keys[i].callback.show_dir(depth+1)
                    
    def get_keys(self):
        if self.next_dir != None:
            return self.next_dir.get_keys() #recursion
            
        res = {}
        for i in range(self.maxkey):
            if self.keys[i] != None:
                res[i] = [self.keys[i].icon, self.keys[i].text]
        return res
                    

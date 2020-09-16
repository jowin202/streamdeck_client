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
        
        
    #export this from class
    def key_pressed_callback(self, keynr):
        current_dir = self
        while current_dir.next_dir != None:
            current_dir = current_dir.next_dir
        
        if current_dir.keys[keynr] != None and current_dir.keys[keynr].is_back_button:
            current_dir.prev_dir.next_dir = None
        elif current_dir.keys[keynr] == None or current_dir.keys[keynr].callback == None:
            print("button " + str(keynr) + " in folder " + str(current_dir.name) + " does not work")
        elif issubclass(type(current_dir.keys[keynr].callback), Folder): 
            current_dir.next_dir = current_dir.keys[keynr].callback
        else:
            current_dir.keys[keynr].callback()
        
    
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
        current_dir = self
        while current_dir.next_dir != None:
            current_dir = current_dir.next_dir
            
        res = {}
        for i in range(self.maxkey):
            if current_dir.keys[i] != None:
                res[i] = [current_dir.keys[i].icon, current_dir.keys[i].text]
        return res
                    

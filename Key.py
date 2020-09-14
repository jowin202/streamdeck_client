

class Key:
    keynr = -1
    icon = None
    callback = None
    is_back_button = False 
    
    def __init__(self, keynr, icon, callback):
        self.keynr= keynr
        self.icon = icon
        self.callback = callback
        

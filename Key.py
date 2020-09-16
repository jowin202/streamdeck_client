

class Key:
    keynr = -1
    icon = None
    text = ""
    callback = None
    is_back_button = False 
    
    def __init__(self, keynr, text, icon, callback):
        self.keynr= keynr
        self.icon = icon
        self.callback = callback
        self.text = text

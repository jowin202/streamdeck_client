from Folder import Folder
from pynput.keyboard import Key, Controller
import pyperclip


class LaTeX_Folder(Folder):
    def __init__(self, maxkey):
        super().__init__("LaTeX", maxkey)
        self.keyboard = Controller()
        self.set_key(0, "Bold", "bold.png", self.bold)
        self.set_key(1, "Italic", "italic.png", self.italic)
        self.set_key(2, "Underline", "underline.png", self.underline)
        self.set_key(3, "Strikethrough", "strikethrough.png", self.strikethrough)

    def bold(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('x')
        text = pyperclip.paste()
        text = "\\textbf{" + text + "}"
        pyperclip.copy(text)
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('v')
        
    def italic(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('x')
        text = pyperclip.paste()
        text = "\\textit{" + text + "}"
        pyperclip.copy(text)
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('v')
        
    def underline(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('x')
        text = pyperclip.paste()
        text = "\\underline{" + text + "}"
        pyperclip.copy(text)
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('v')
        
    def strikethrough(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('x')
        text = pyperclip.paste()
        text = "\\sout{" + text + "}"
        pyperclip.copy(text)
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('v')
        
    def insert_image(self):
        print("insert image")
    

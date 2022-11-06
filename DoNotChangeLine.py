from tkinter import Tk
import pyperclip
full_str = Tk().clipboard_get().replace('\r','').replace('\n',' ')
print(full_str)
pyperclip.copy(full_str)
pyperclip.paste()
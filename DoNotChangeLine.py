from tkinter import Tk
import pyperclip
print(Tk().clipboard_get().replace('\r','').replace('\n',''))
pyperclip.copy(Tk().clipboard_get().replace('\r','').replace('\n',''))
pyperclip.paste()
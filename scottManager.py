import tkinter as tk
from tkinter import ttk
from unittest import TestCase

class Application(ttk.Frame):
    
    def __init__(self, parent):
        super.__init__(parent)
        self.title_label = ttk.Label(parent, text="Scott Manager")
        self.title_label.place(x=60, y=80)
    

ventana = tk.Tk()
ventana.title("Scott Manager")
ventana.config(height=600, width=900)
app = Application(ventana)
ventana.mainloop()
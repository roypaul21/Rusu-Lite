from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import webbrowser









def callback(url):
    webbrowser.open_new(url)

root = Tk()
link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))


def movie():
    movie_p = Tk()
    w = 860
    h = 630
    movie_p.geometry(f'{w}x{h}+{250}+{40}')
    movie_p.configure(background="black")
    movie_p.resizable(False, False)


    movie_p.mainloop()

import tkinter as tk
import os
from tkinter import filedialog
from pygame import mixer

root = tk.Tk()
root.title("Music Player")
root.geometry("300x300")


def browse_file():
    global filename
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("Music Files", "*.mp3*"), ("all files", "*.*")))
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()


browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

root.mainloop()

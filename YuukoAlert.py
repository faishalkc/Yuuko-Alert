import ctypes
import pygame
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image,ImageTk

def get_default_system_font_and_size():
    root = tk.Tk()
    default_font = tkFont.nametofont("TkDefaultFont")
    system_font = default_font.actual()['family']
    system_font_size = default_font.actual()['size']
    root.destroy()
    return system_font, system_font_size

ctypes.windll.user32.SetProcessDPIAware()

default_system_font, default_font_size = get_default_system_font_and_size()

pygame.init()
root = tk.Tk()
root.resizable(False,False)
root.geometry("350x160")
root.eval('tk::PlaceWindow . center')
root.iconbitmap("files/icon.ico")
root.title("Yuuko Alert")

canvas= tk.Canvas(root, width= 250, height= 80)
canvas.pack(padx=5, pady=5)

img= (Image.open("files/face.png"))
resized_image= img.resize((80,72), Image.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(10,10, anchor="nw", image=new_image)
canvas.create_text(170, 50, text="Selamat Pagi !", fill="black", font=(default_system_font, default_font_size))

close = tk.Button(root, text="        OK        ", font=(default_system_font, default_font_size), command=root.destroy)
close.pack(padx=5, pady=5)

my_sound = pygame.mixer.Sound('files/sound.mp3')
my_sound.play()
my_sound.set_volume(0.8)

root.attributes('-toolwindow', True)
root.attributes('-topmost', True)
root.mainloop()
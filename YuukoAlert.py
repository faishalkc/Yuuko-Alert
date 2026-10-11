import ctypes
import ctypes.wintypes
import pygame
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


class SoundPlayer:
    def __init__(self, path, volume):
        self.sound = pygame.mixer.Sound(path)
        self.sound.set_volume(volume)

    def play(self):
        self.sound.play()


class AlertWindow:
    SCALE = 1.0

    BASE_IMAGE = 80
    BASE_GAP = 16
    BASE_PAD = 32
    BASE_PAD_INNER = 16
    BASE_MIN_WIDTH = 350
    BASE_BUTTON_IPADY = 2

    TITLE = "Yuuko Alert"
    MESSAGE = "Selamat Pagi !"
    BUTTON_TEXT = "OK"
    BUTTON_WIDTH = 10

    ICON_PATH = "files/icon.ico"
    IMAGE_PATH = "files/face.png"
    SOUND_PATH = "files/sound.mp3"
    VOLUME = 0.8

    SPI_GETWORKAREA = 48

    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

        self._setup_window()
        self._setup_font()
        self._build_content()
        self._build_button()
        self._setup_attributes()
        self._center()

        self.root.deiconify()
        self.sound = SoundPlayer(self.SOUND_PATH, self.VOLUME)

    def run(self):
        self.sound.play()
        self.root.mainloop()

    def _s(self, value):
        return int(round(value * self.SCALE))

    def _setup_window(self):
        self.root.resizable(False, False)
        self.root.iconbitmap(self.ICON_PATH)
        self.root.title(self.TITLE)

    def _setup_font(self):
        system_font = tkFont.nametofont("TkDefaultFont").actual()
        self.font = tkFont.Font(family=system_font["family"],
                                size=self._s(system_font["size"]))

    def _build_content(self):
        self.canvas = tk.Canvas(self.root, highlightthickness=0, borderwidth=0)
        self.canvas.pack(padx=self._s(self.BASE_PAD),
                         pady=(self._s(self.BASE_PAD),
                               self._s(self.BASE_PAD_INNER)))

        image_size = self._s(self.BASE_IMAGE)
        image = Image.open(self.IMAGE_PATH).resize((image_size, image_size),
                                                   Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.create_text(image_size + self._s(self.BASE_GAP),
                                image_size // 2, anchor="w",
                                text=self.MESSAGE, fill="black",
                                font=self.font)

        x1, y1, x2, y2 = self.canvas.bbox("all")
        self.canvas.configure(width=x2 - x1, height=y2 - y1)

    def _build_button(self):
        self.button = tk.Button(self.root, text=self.BUTTON_TEXT,
                                width=self.BUTTON_WIDTH, font=self.font,
                                command=self.root.destroy)
        self.button.pack(padx=self._s(self.BASE_PAD),
                         pady=(0, self._s(self.BASE_PAD)),
                         ipady=self._s(self.BASE_BUTTON_IPADY))

    def _setup_attributes(self):
        self.root.attributes("-toolwindow", False)
        self.root.attributes("-topmost", True)

    def _get_work_area(self):
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.SystemParametersInfoW(
            self.SPI_GETWORKAREA, 0, ctypes.byref(rect), 0)
        return rect

    def _center(self):
        self.root.update_idletasks()
        w = max(self.root.winfo_reqwidth(), self._s(self.BASE_MIN_WIDTH))
        h = self.root.winfo_reqheight()

        area = self._get_work_area()
        x = area.left + (area.right - area.left - w) // 2
        y = area.top + (area.bottom - area.top - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")


def main():
    ctypes.windll.user32.SetProcessDPIAware()
    pygame.init()
    AlertWindow().run()


if __name__ == "__main__":
    main()
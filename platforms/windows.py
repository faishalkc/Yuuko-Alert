import ctypes
import ctypes.wintypes
import os

SPI_GETWORKAREA = 48


def enable_dpi_awareness():
    ctypes.windll.user32.SetProcessDPIAware()


def get_work_area(root):
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_GETWORKAREA, 0, ctypes.byref(rect), 0)
    return rect.left, rect.top, rect.right, rect.bottom


def set_icon(root, files_dir):
    root.iconbitmap(os.path.join(files_dir, "icon.ico"))

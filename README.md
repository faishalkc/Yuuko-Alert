<div align="center">

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieeRWIRrEnIFTEf3PQQj-7FLBOb2XvgQryDKUI_o_jtddHzogqpFCRXDzqgShHBwscSxrt_y60OxipEt5wBhGpfTNyx3hXuaCqpnPoIJOEeX1Jgdi6QtMCzgbJ2Ae7lzfE60KyZ5R8zVLI2KHwWZnfTCxxhRehC3PGP06ncK5ZOUQMleZkMIKlBX_EfK4/s512/130423.png" alt="Yuuko Alert Icon" width="120" height="120" />

# Yuuko Alert

### A Cheerful Morning Greeting for Your Desktop

[![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=flat-square&logo=opentofu&logoColor=white)](https://www.microsoft.com/windows)
[![Language](https://img.shields.io/badge/Language-Python-B08D35?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/faishalkc/Yuuko-Alert)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-7952B3?style=flat-square&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![Pygame](https://img.shields.io/badge/Pygame-Audio-46A832?style=flat-square&logo=python&logoColor=white)](https://www.pygame.org/)
[![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-367C80?style=flat-square&logo=python&logoColor=white)](https://python-pillow.org/)

**Start your day with Yuuko's cheerful “Selamat Pagi!” greeting.**

A small Windows desktop application featuring a pop-up greeting inspired by Yuuko Aioi from *Nichijou*, accompanied by her voice.

</div>

---

## 📖 About

Yuuko Alert is a lightweight desktop application created to bring a little fun and positivity to your day.

Inspired by **Yuuko Aioi**, the cheerful and energetic character from the anime *Nichijou*, the application displays a pop-up window featuring the Indonesian morning greeting **“Selamat Pagi!”**, accompanied by an audio clip of Yuuko's voice.

The application features a compact graphical interface with Yuuko's image, a greeting message, and an OK button to close the window. It brings a small, anime-inspired touch to your desktop without unnecessary complexity.

## ✨ Features

- 🌞 **Cheerful Morning Greeting** — displays a “Selamat Pagi!” message in a pop-up window.
- 🔊 **Voice Playback** — plays an audio clip when the application starts.
- 🖼️ **Character Image** — displays Yuuko's face alongside the greeting.
- 🪟 **Always-on-Top Window** — keeps the greeting window above other windows.
- 📐 **Compact Interface** — uses a fixed-size, centered window.
- 🖥️ **Display Scaling Support** — includes Windows DPI awareness in the current version.
- 💖 **Simple Interaction** — close the application using the OK button.

## 🖥️ Application Preview

<img src="https://github.com/user-attachments/assets/21f4e4a0-d075-418c-9d0a-0287734ba884" alt="Yuuko Alert desktop application screenshot" width="420" />

## 🎮 How to Use

### Using the Windows Executable

1. Download the ZIP package from the [GitHub Releases](https://github.com/faishalkc/Yuuko-Alert/releases) page.
2. Extract the archive to a folder of your choice.
3. Keep the executable and its required assets in their original directory structure.
4. Launch the executable to display the greeting.
5. Click **OK** to close the application.

### Running from Source

1. Clone the repository:

   ```bash
   git clone https://github.com/faishalkc/Yuuko-Alert.git
   ```

2. Open the project directory:

   ```bash
   cd Yuuko-Alert
   ```

3. Install the dependencies listed in `requirements.txt`:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

**Note:** Run the script from the project root directory so that the relative paths to the files in `files/` resolve correctly.

## 📋 Requirements

### For Windows Executable

- Microsoft Windows.
- The application assets included in the release package.
- A working audio output device for voice playback.

### For Source Code

- Microsoft Windows.
- Python 3 with Tkinter available.
- Pygame.
- Pillow.

## 📂 Project Structure

```text
Yuuko-Alert/
├── files/
│   ├── face.png
│   ├── icon.ico
│   └── sound.mp3
├── platforms/
│   └── windows.py
├── main.py
├── requirements.txt
└── README.md
```

| File | Description |
|---|---|
| `main.py` | Main Python script containing the application window (`AlertWindow`), greeting, image, and audio playback (`SoundPlayer`). |
| `platforms/windows.py` | Windows-specific functions: DPI awareness, desktop work area (above the taskbar), and window icon. |
| `files/face.png` | Character image displayed in the greeting window. |
| `files/icon.ico` | Application window icon (used on Windows). |
| `files/sound.MP3` | Audio clip played when the application starts. |
| `requirements.txt` | List of third-party Python dependencies. |
| `README.md` | Project documentation. |

## 🐧 Running on Linux / macOS

The Windows-specific code is isolated in `platforms/windows.py`. To run the app on other systems:

1. Open `main.py`.
2. Delete this single line near the top:

```python
   from platforms import windows as winapi
```

3. Run `python main.py`.

Without that line, the app falls back to default Tk behavior: the window is centered on the full screen and the default Tk icon is used. The `platforms/` folder can be safely removed.

> On some Linux distributions, Tkinter must be installed separately, for example `sudo apt install python3-tk`.

## 🛠️ Technologies

- **Python** — application logic.
- **Tkinter** — graphical user interface.
- **Pygame** — audio playback.
- **Pillow** — image loading, resizing, and display.
- **Windows API (`ctypes`)** — Windows-specific DPI awareness.

## 🎨 Inspiration

Yuuko Alert takes inspiration from **Yuuko Aioi**, one of the main characters in the comedy anime *Nichijou*.

Known for her energetic personality and expressive reactions, Yuuko is the inspiration behind this playful desktop greeting. The application brings a small piece of that cheerful anime atmosphere to your daily computer use.

## ⚠️ Notes and Limitations

- **Windows only:** The application uses Windows-specific functionality through `ctypes` and Tkinter's `iconbitmap()`.
- **Required assets:** Keep `face.png`, `icon.ico`, and `sound.MP3` in the `files` directory.
- **Relative asset paths:** Run the application from the project root directory unless the executable package has been prepared to handle its assets accordingly.
- **Audio playback:** Voice playback depends on successful audio initialization and a working audio output device.
- **No automatic scheduling:** The application plays the audio when launched; it does not schedule a greeting for a specific time.
- **Executable availability:** Download a compiled executable from the Releases page if you prefer not to install Python and the required libraries.

## 📄 License

Yuuko Alert is open-source software licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software in accordance with the terms of the license.

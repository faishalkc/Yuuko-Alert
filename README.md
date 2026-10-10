<div align="center">

<img src="https://github.com/user-attachments/assets/9e8e5c80-5c41-47df-bf4f-af620f0f2b47" alt="Yuuko Alert Icon" width="120" height="120" />

# Yuuko Alert

### A Cheerful Morning Greeting for Your Desktop

[![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Language](https://img.shields.io/badge/Language-Python-B08D35?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/faishalkc/Yuuko-Alert)

[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-B08D35?style=flat-square&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![Pygame](https://img.shields.io/badge/Pygame-Audio-46A832?style=flat-square&logo=python&logoColor=white)](https://www.pygame.org/)
[![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-367C80?style=flat-square&logo=python&logoColor=white)](https://python-pillow.org/)

**Start your day with Yuuko's cheerful “Selamat Pagi!” greeting.**

A small Windows desktop application featuring a pop-up greeting inspired by Yuuko Aioi from *Nichijou*, accompanied by her voice.

</div>

---

## 📖 About

Yuuko Alert is a lightweight desktop application created to bring a little fun and positivity to your day.

Inspired by **Yuuko Aioi**, the cheerful and energetic character from the anime *Nichijou*, the application displays a pop-up window featuring the Indonesian morning greeting **“Selamat Pagi!”**, accompanied by an audio clip of Yuuko's voice.

The application uses a simple graphical interface with Yuuko's image, a greeting message, and an OK button to close the window. It provides a small, anime-inspired touch to your desktop without unnecessary complexity.

## ✨ Features

- 🌞 **Cheerful Morning Greeting** — displays a “Selamat Pagi!” message in a pop-up window.
- 🔊 **Voice Playback** — plays an audio clip when the application starts.
- 🖼️ **Character Image** — displays Yuuko's face alongside the greeting.
- 🪟 **Always-on-Top Window** — keeps the greeting window above other windows.
- 📐 **Compact Interface** — uses a fixed-size, centered window.
- 🖥️ **Windows DPI Awareness** — enables process DPI awareness for display scaling.
- 💖 **Simple Interaction** — close the application using the OK button.

## 🖥️ Application Preview

<img src="https://github.com/user-attachments/assets/21f4e4a0-d075-418c-9d0a-0287734ba884" alt="Yuuko Alert desktop application screenshot" width="420" />

## 🎮 How to Use

1. Launch `YuukoAlert.py`.
2. Wait for the Yuuko Alert window to appear.
3. Listen to the accompanying voice clip and enjoy the greeting.
4. Click **OK** to close the application.

The audio playback and greeting window are initialized when the application starts.

## 📋 Requirements

- **Operating System:** Microsoft Windows.
- **Python:** Python 3.
- **Python Libraries:** Pygame and Pillow.
- **Audio Output:** A working audio device to play the voice clip.
- **Project Assets:** The image, icon, and audio files included in the `files` directory.

Tkinter is included with most standard Python installations for Windows.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/faishalkc/Yuuko-Alert.git
```

### 2. Open the Project Directory

```bash
cd Yuuko-Alert
```

### 3. Install Dependencies

```bash
python -m pip install pygame Pillow
```

### 4. Run the Application

```bash
python YuukoAlert.py
```

**Note:** Run the application from the project root directory so that the relative paths to the files in `files/` resolve correctly.

## 📂 Project Structure

```text
Yuuko-Alert/
├── files/
│   ├── face.png
│   ├── icon.ico
│   └── sound.MP3
├── YuukoAlert.py
└── README.md
```

| File | Description |
|---|---|
| `YuukoAlert.py` | Main Python script responsible for the application window, greeting, image, and audio playback. |
| `files/face.png` | Character image displayed in the greeting window. |
| `files/icon.ico` | Application window icon. |
| `files/sound.MP3` | Audio clip played when the application starts. |
| `README.md` | Project documentation. |

## 🛠️ Technologies

- **Python** — application logic.
- **Tkinter** — graphical user interface.
- **Pygame** — audio playback.
- **Pillow** — image loading, resizing, and display.
- **Windows API (`ctypes`)** — process DPI awareness.

## 🎨 Inspiration

Yuuko Alert takes inspiration from **Yuuko Aioi**, one of the main characters in the comedy anime *Nichijou*.

Known for her energetic personality and expressive reactions, Yuuko is the inspiration behind this playful desktop greeting. The application brings a small piece of that cheerful anime atmosphere to your daily computer use.

## ⚠️ Notes and Limitations

- **Windows only:** The application uses Windows-specific functionality through `ctypes.windll.user32` and `iconbitmap()`.
- **Required assets:** Keep `face.png`, `icon.ico`, and `sound.MP3` in the `files` directory.
- **Run from the project directory:** The application uses relative asset paths.
- **Audio playback:** The greeting's voice depends on successful audio initialization and a working audio output device.
- **No automatic scheduling:** The current implementation plays the audio when the application launches; it does not schedule a greeting for a specific time.
- **No installer included:** The repository provides the Python source and required assets. Python and its dependencies must be installed to run the source directly.

## 📄 License

No license has been specified for this project. Unless a license is added to the repository, the default copyright rules apply.

# YouTube Music Downloader 🎶

This script allows you to search and download songs from YouTube in MP3 format based on a list of song titles. It uses `yt-dlp` to download the videos and `youtubesearchpython` to search for YouTube videos.

---

### Prerequisites

- **Python** 3.7+
- **yt-dlp**: To download videos from YouTube.
- **youtubesearchpython**: To search for videos on YouTube by title.
- **FFmpeg**: Required to extract audio in MP3 format.

---

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```

#### 2. Install the Python Dependencies

```bash
pip install yt-dlp youtubesearchpython
```

#### 3. Install FFmpeg

- **Windows**: Download FFmpeg and add it to your system PATH.
- **macOS**: Install with Homebrew:
  
  ```bash
  brew install ffmpeg
  ```

- **Linux**: Use your package manager:

  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```

---

### Usage

1. Open the script file and edit the `musicas` list with the titles of the songs you want to download:

    ```python
    musicas = [
        "Eduardo Costa - Vê se volta comigo",
        "Zezé de Camargo e Luciano - Será que foi saudade",
        # Add more songs here
    ]
    ```

2. Run the script in the terminal:

    ```bash
    python script_name.py
    ```

The script will search for each song on YouTube, download the audio, and save it as an MP3 file.

---

### How It Works

1. The script searches for each title in the `musicas` list on YouTube.
2. It downloads the audio in high-quality MP3 format (192 kbps) and saves it with a formatted name based on the list.

---

### Notes

- The script saves the MP3 files in the same folder where it is executed.
- Ensure that FFmpeg is installed and configured correctly on your system.

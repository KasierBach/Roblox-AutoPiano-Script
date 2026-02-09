# Roblox Auto Player Piano Script  

This is a Roblox auto player script designed specifically for playing the piano in Roblox. It allows for the automated playback of songs, simulating precise key presses based on predefined sequences.  

## Features  
- 🎹 Automatically plays piano in Roblox with accurate timing and note execution.  
- 🎵 Customizable to include new songs or adjust tempo for specific performances.  
- ⚡ Lightweight and easy to use, with seamless integration into Roblox games.  

## Usage  
1. Add your desired song's note sequence to the script.  
2. Adjust tempo or playback speed if needed.  
3. Load the script into your Roblox game and enjoy automated piano performances!  

## Contributions  
Feel free to edit, improve, or expand upon this code to fit your specific needs. Contributions and feedback are welcome—help make this project even better!  

## Disclaimer  
This script is intended for educational and personal use. Use responsibly and ensure compliance with Roblox’s Terms of Service.  

---  

Happy playing! 🎼  

# 🚀 Enhanced Features & Instructions

## 🛠️ Setup

1.  **Install Python:** Make sure you have Python 3.8+ installed.
2.  **Install Dependencies:**
    Open your terminal/command prompt in this folder and run:
    ```bash
    pip install -r requirements.txt
    ```

## 🎮 Hotkeys & Controls

| Key | Function | Description |
| :--- | :--- | :--- |
| **DELETE** | **Play / Pause** | Starts or stops the script. |
| **F8** | **Reload Song** | Reloads `song.txt` without restarting the script. |
| **F7** | **Set Speed 0.75x** | Quickly sets playback speed to 0.75. |
| **PAGE UP** | **Speed Up** | Increases playback speed by 10%. |
| **PAGE DOWN** | **Slow Down** | Decreases playback speed by 10%. |
| **HOME** | **Rewind** | Jumps back 10 notes. |
| **END** | **Skip** | Jumps forward 10 notes. |
| **INSERT** | **Legit Mode** | Adds random slight delays to mimic human playing. |
| **ESC** | **Exit** | Closes the script. |

## 🎵 Adding New Songs

### Option A: Text Sheet (Letters)
1.  Open `sheetConversion.txt` and paste your sheet music (letters) into it.
2.  Run the converter:
    ```bash
    python convert_song_v2.py
    ```
3.  Enter the **Tempo** (e.g., 90) and **Playback Speed** (e.g., 0.75) when prompted.
4.  In the player, press **F8** to reload the new song instantly.

### Option B: MIDI Files
1.  Download a `.mid` file and place it in the `midi/` folder.
2.  Run `python pyMIDI.py`.
3.  Follow the instructions to convert it.

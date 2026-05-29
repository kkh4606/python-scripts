import subprocess
import time
import os
import sys
from tkinter import messagebox

# Get the folder where the EXE is actually located
if getattr(sys, 'frozen', False):
    # Running as a PyInstaller EXE
    GAME_DIR = os.path.dirname(sys.executable)
else:
    # Running as a .py script
    GAME_DIR = os.path.dirname(os.path.abspath(__file__))

SIDER_EXE = os.path.join(GAME_DIR, "sider.exe")
PES_EXE   = os.path.join(GAME_DIR, "pes2017.exe")

def main():
    # Check both files exist
    missing = []
    if not os.path.exists(SIDER_EXE):
        missing.append("sider.exe")
    if not os.path.exists(PES_EXE):
        missing.append("pes2017.exe")

    if missing:
        messagebox.showerror(
            "PES 17 Launcher",
            f"Could not find: {', '.join(missing)}\n\nMake sure this launcher is in the same folder as your game files."
        )
        sys.exit(1)

    # Launch Sider first
    subprocess.Popen([SIDER_EXE], cwd=GAME_DIR)

    # Wait for Sider to initialize
    time.sleep(3)

    # Launch PES 2017
    subprocess.Popen([PES_EXE], cwd=GAME_DIR)

if __name__ == "__main__":
    main()

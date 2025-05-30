import time
import pygetwindow as gw
import pyautogui
import platform
import os
import sys
from playsound3 import playsound

SYSTEM = platform.system()
WINDOW_TITLE = "Sober" if SYSTEM == "Linux" else "Roblox"
SOUND_DIR = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "notif.mp3")

def bring_window_to_front():
    try:
        pos_x, pos_y = pyautogui.position()
        sleep_time = 0.1
        offset = 60
        windows = gw.getWindowsWithTitle(WINDOW_TITLE)
        
        win = None
        for window in windows:
            if window.title == WINDOW_TITLE:
                win = window

        if win:
            if win.isMinimized:
                win.restore()
            win.activate()
            print(f"Brought '{WINDOW_TITLE}' to front.")
            
            pyautogui.moveTo(win.left + offset, win.top + offset)    
            pyautogui.mouseDown(button='right')
            time.sleep(sleep_time)
            pyautogui.mouseUp(button='right')
            time.sleep(sleep_time)
            pyautogui.click()
            time.sleep(sleep_time)
            pyautogui.moveTo(pos_x, pos_y)
            pyautogui.click()
            time.sleep(sleep_time)
        else:
            print(f"Window '{WINDOW_TITLE}' not found.")
    except Exception as e:
        print(f"Error: {e}")
        sound = playsound(SOUND_DIR)
        sound.stop()

if __name__ == "__main__":
    while True:
        bring_window_to_front()
        time.sleep(60 * 15)

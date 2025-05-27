import time
from datetime import datetime
import pygetwindow as gw
from playsound3 import playsound
import os
import sys

WINDOW_TITLE = r'C:\WINDOWS\system32\cmd.exe'

def wait_until_target():
    c = 0
    
    while True:
        now = datetime.now()
        
        if now.minute == 0:
            c += 1
            notify(c)
        else:
            c = 0

        print(f"{now.hour}h {now.minute}m")
        time.sleep(20)

def notify(c):
    if c < 2:
        try:
            windows = gw.getWindowsWithTitle(WINDOW_TITLE)
            
            if windows:
                win = windows[0]
                if win.isMinimized:
                    win.restore()
                win.activate()
            else:
                print("Window does not exist.")
        except:
            pass
        
        print("Open Grow A Garden in Roblox for hourly event.")
        sound_dir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "sound.mp3")
        sound = playsound(sound_dir)
        sound.stop()

wait_until_target()
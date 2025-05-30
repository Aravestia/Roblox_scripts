import time
from datetime import datetime
import pygetwindow as gw
from playsound3 import playsound
import os
import sys

prev = datetime.now()
wait_time = 60 * 10

WINDOW_TITLE = r'C:\WINDOWS\system32\cmd.exe'

def wait_until_target():
    while True:
        global prev

        now = datetime.now()
        et = (now - prev).seconds
        
        if et >= wait_time:
            notify(now)

        print(et)
        time.sleep(5)

def notify(now):
    global prev
    prev = now

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
    
    print("Open BGSI in Roblox to collect your chests.")
    sound_dir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "chest_collect_notification_sound_2.mp3")
    sound = playsound(sound_dir)
    sound.stop()

wait_until_target()
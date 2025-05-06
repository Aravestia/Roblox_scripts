import time
import pygetwindow as gw
import pyautogui
import platform

SYSTEM = platform.system()
WINDOW_TITLE = "Sober" if SYSTEM == "Linux" else "Roblox"

def bring_window_to_front():
    try:
        pos_x, pos_y = pyautogui.position()
        sleep_time = 0.1
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
            time.sleep(sleep_time)
            
            offset = 65
            pyautogui.moveTo(win.left + offset, win.top + offset)    
            pyautogui.mouseDown(button='right')
            time.sleep(sleep_time)
            pyautogui.mouseUp(button='right')
            time.sleep(sleep_time)
            pyautogui.click()
            time.sleep(sleep_time)
            pyautogui.mouseDown(button='right')
            time.sleep(sleep_time)
            pyautogui.mouseUp(button='right')
            time.sleep(sleep_time)
            pyautogui.click()
            print(f"Clicked '{WINDOW_TITLE}'.")
            time.sleep(sleep_time * 2)
            
            win.minimize()
            print(f"Minimised '{WINDOW_TITLE}'.")
            
            pyautogui.moveTo(pos_x, pos_y)
        else:
            print(f"Window '{WINDOW_TITLE}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        bring_window_to_front()
        time.sleep(600)

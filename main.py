import time
import mss
import pyautogui

boundries = ()


with mss.mss() as sct:
    monitor = sct.monitors[1]

    shot = sct.grab(monitor)

    time.sleep(2)
    pyautogui.click(1730, 55)

    while True:
        print(pyautogui.position())








import time
import mss
import pyautogui
from pynput.keyboard import Key, Listener
import pynput
import threading


run = False


boundries = (670, 159, 1200, 1000)
x_axis = (743, 880, 1030, 1174)

tab = [0] * 4


def on_press(key):
    global run

    try: k = key.char # single-char keys
    except: k = key.name # other keys
    print(k)
    if key == Key.esc:
        run = False
    if k == 's':
        tab[1] = 10
        run = True

def on_click(x, y, button, pressed):
    with mss.mss() as sct:
        monitor = sct.monitors[1]

        shot = sct.grab(monitor)
        print(x,y)
        print(shot.pixel(x, y))




if __name__ == '__main__':

    key_thread = Listener(on_press = on_press)
    key_thread.start()

    mouse_thread = pynput.mouse.Listener(on_click=on_click)
    mouse_thread.start()






    # pyautogui.click(1730, 55)
    # 55 while True:
    #      listener = Listener(on_press=on_press)
    #      # listener.start()
    # with Listener(on_press=on_press, on_release=on_release) as listener:
    #     listener.start()


    while True:
        pass
        # with mss.mss() as sct:
        #     monitor = sct.monitors[1]
        #
        #     shot = sct.grab(monitor)
        #
        #
        #     time.sleep(1)
        #     print(pyautogui.position())
        #     print(shot.pixel(pyautogui.position().x, pyautogui.position().y))

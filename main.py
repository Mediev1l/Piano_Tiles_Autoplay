import time
import mss
import pyautogui
from pynput.keyboard import Key, Listener
import threading

boundries = ()


def key_thread():
    with Listener(on_press=on_press) as lis:
        lis.join()


def on_press(key):
    return key



def exit_(ASCII_key):
    hit = msvcrt.kbhit()

    if hit:
        return msvcrt.getch()
    else:
        return None


if __name__ == '__main__':

    key_thread = threading.Thread(target=key_thread)
    key_thread.start()


    with mss.mss() as sct:
        monitor = sct.monitors[1]

        shot = sct.grab(monitor)

        time.sleep(2)



    # pyautogui.click(1730, 55)
    # 55 while True:
    #      listener = Listener(on_press=on_press)
    #      # listener.start()
    # with Listener(on_press=on_press, on_release=on_release) as listener:
    #     listener.start()


    while key_thread.:
        print(threading.active_count())
        key_thread= threading.Thread(target=key_thread)

        print(pyautogui.position())

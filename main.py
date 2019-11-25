import time
import mss
import pyautogui
from pynput.keyboard import Key, Listener
import threading

run = False

start = (876, 688)
boundries = (670, 159, 1200, 1000)
x_axis = (75, 220, 360, 490)

results = [0] * 4
threads = []


def on_press(key):
    global run

    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if key == Key.esc:
        run = False
    if k == 's':
        run = True


def on_click(x, y, button, pressed):
    with mss.mss() as sct:
        monitor = sct.monitors[1]

        shot = sct.grab(monitor)

        search(shot, 880, 0)
        print(x, y)
        print(shot.pixel(x, y))


def search(sc, x, index):
    for i in range(boundries[3] - boundries[1] - 1, 0, -1):
        pixel = sc.pixel(x, i)[0]
        if pixel < 40:
            results[index] = i
            return

    results[index] = 0


if __name__ == '__main__':

    key_thread = Listener(on_press=on_press)
    key_thread.start()

    # mouse_thread = pynput.mouse.Listener(on_click=on_click)
    # mouse_thread.start()

    time.sleep(2)

    with mss.mss() as sct:
        shot = sct.grab(boundries)
        # img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")
        # img.save("test.png")
        # img.show()

    for index, x in enumerate(x_axis):
        threads.append(threading.Thread(target=search, args=(shot, x, index)))

    for thr in threads:
        thr.start()

    for thr in threads:
        thr.join()

    pyautogui.click(*start)

    # img = cv2.imread(shot, 0)
    #
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # pyautogui.click(1730, 55)
    # 55 while True:
    #      listener = Listener(on_press=on_press)
    #      # listener.start()
    # with Listener(on_press=on_press, on_release=on_release) as listener:
    #     listener.start()

    while True:
        with mss.mss() as sct:
            monitor = sct.monitors[1]
    
            shot = sct.grab(monitor)

        time.sleep(1)
        print(pyautogui.position())
        print(shot.pixel(pyautogui.position().x, pyautogui.position().y))

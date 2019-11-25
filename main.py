import mss
import pyautogui
from pynput.keyboard import Key, Listener
import threading

run = False

offset = 50
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
        if pixel < 59:
            results[index] = i
            return

    results[index] = 0


if __name__ == '__main__':

    key_thread = Listener(on_press=on_press)
    key_thread.start()

    # mouse_thread = pynput.mouse.Listener(on_click=on_click)
    # mouse_thread.start()

    while True:

        while run:

            with mss.mss() as sct:
                shot = sct.grab(boundries)

            threads.clear()

            for index, x in enumerate(x_axis):
                threads.append(threading.Thread(target=search, args=(shot, x, index)))

            for thr in threads:
                thr.start()

            for thr in threads:
                thr.join()

            x = boundries[0] + x_axis[results.index(max(results))]
            y = boundries[1] + max(results) + offset

            if(y > boundries[1] + offset):
                offset += 0.3
                pyautogui.click(x, y)

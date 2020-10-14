# pip install pyautogui
# Edit the path to set destination of screen captures
# Edit the time.sleep(seconds) to set interval between captures

import pyautogui
import time

def screenshot():
    x = 0
    y = 100
    im1 = pyautogui.screenshot(region=(x, y, 1920, 900))
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    im1.save("C:/Users/liang/Downloads/oanda/screenshots/"+timestr+".png")

while True:
    screenshot()
    time.sleep(300) # 300 sec = 5 minutes
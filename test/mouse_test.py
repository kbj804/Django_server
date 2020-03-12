import pyautogui
from time import sleep

pyautogui.PAUSE =1
pyautogui.FAILSAFE = True

while True:
    try:
        pyautogui.moveRel(-1,0)
        sleep(6)
        pyautogui.moveRel(0,-1)
        sleep(6)
        pyautogui.moveRel(1,0)
        sleep(6)
        pyautogui.moveRel(0,1)
        sleep(6)
    except:
        exit()
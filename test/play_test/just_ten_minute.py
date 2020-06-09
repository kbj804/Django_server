#-*- coding:utf-8 -*-
import os
import pyautogui
from time import sleep
import time
import datetime
import shutil
import glob


if __name__ == "__main__":
    pyautogui.PAUSE =1
    pyautogui.FAILSAFE = True

    pre_mpX = 0
    pre_mpY = 0
    
    startTime = time.time()

    while True:
        now = datetime.datetime.now()
        hour = now.hour
        m = now.minute
        print("### 현재 시간 {}시 {}분 ###".format(hour, m))
        try:
            # 몇초에 한번 체크할건가?
            sleep(270)

            if (hour == 12 and m > 0) or (hour == 13 and m < 0):
                print("### 지금은 점심시간 입니다 ###")

            elif (hour >= 20 and hour < 8):
                print("### 지금은 업무시간이 아닙니다 ###")
                exit()

            else:
                eTime = time.time() - startTime

                endTime_M = int(eTime) / 60
                endTime_S = int(eTime) % 60

                mousePositionX, mousePositionY = pyautogui.position()
                
                if mousePositionX == pre_mpX and mousePositionY == pre_mpY:
                    print("# 현재 자리 비움 시간 {}분 {}초 #".format(int(endTime_M), endTime_S))
                    pre_mpX = mousePositionX
                    pre_mpY = mousePositionY

                    if int(endTime_M) < 10:
                        # 시계로 이동 후 클릭
                        pyautogui.moveTo(1863, 1061, duration=2, tween=pyautogui.easeInOutQuad)
                        pyautogui.click()
                        #pyautogui.moveRel(-10, 0, duration=1, tween=pyautogui.easeInOutQuad)
                    
                    else:
                        pass

                else:
                    print("일하는중")
                    # 움직임이 감지되면 시작시간 초기화
                    startTime = time.time()

                pre_mpX = mousePositionX
                pre_mpY = mousePositionY

        except Exception as e:
            print(e)
            exit()

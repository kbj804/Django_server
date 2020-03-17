import pyautogui
from time import sleep
import time
import datetime


pyautogui.PAUSE =1
pyautogui.FAILSAFE = True


pre_mpX = 0
pre_mpY = 0

print("4분 30초에 한번씩 동작함")

startTime = time.time()

while True:
    try:
        # 몇 초 동안 가만히 있으면 시작할건지?
        sleep(2)
        eTime = time.time() - startTime

        endTime_M = int(eTime) / 60
        endTime_S = int(eTime) % 60

        print("현재 경과 시간 {}분 {}초".format(int(endTime_M), endTime_S))
        mousePositionX, mousePositionY = pyautogui.position()
        
        if mousePositionX == pre_mpX and mousePositionY == pre_mpY:
            pre_mpX = mousePositionX
            pre_mpY = mousePositionY


            ''' 이것 저것
            pyautogui.hotkey('win', 'r')
            sleep(1)
            pyautogui.typewrite('notepad', interval=0.01)

            sleep(1)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')

            pyautogui.typewrite('test ~ ', interval=1)
            '''

            # 시계로 이동   
            # pyautogui.moveTo(1863, 1061, duration=2, tween=pyautogui.easeInOutQuad)
            # pyautogui.click()
            pyautogui.moveRel(-10, 0, duration=1, tween=pyautogui.easeInOutQuad)
            sleep(0.5)
            pyautogui.moveRel(0, -10, duration=1, tween=pyautogui.easeInOutQuad)
            sleep(0.5)
            pyautogui.moveRel(10, 0, duration=1, tween=pyautogui.easeInOutQuad)
            sleep(0.5)
            pyautogui.moveRel(0, 10, duration=1, tween=pyautogui.easeInOutQuad)
            sleep(0.5)
            

        else:
            pre_mpX = mousePositionX
            pre_mpY = mousePositionY

        # pyautogui.moveRel(-1,0)
        # sleep(0.1)
        # pyautogui.moveRel(0,-1)
        # sleep(0.1)
        # pyautogui.moveRel(1,0)
        # sleep(0.1)
        # pyautogui.moveRel(0,1)
        # sleep(0.1)
    except Exception as e:
        print(e)
        exit()


'''
# 모니터 사이즈 세로 크기 구하고 변수에 지정
backWidth, backHeight = pyautogui.size()

# 마우스의 현재 위치 출력(While 문과 함께 쓰면 실시간으로 좌표 확인 가능)
mousePositionX, mousePositionY = pyautogui.position()

# 마우스 이동
pyautogui.moveTo(200,150)

# 마우스 클릭
pyautogui.click()

# 마우스 현재 위치에서 이동
pyautogui.moveRel(100, 100)

# 마우스 더블 클릭
pyautogui.doubleClick()

# 마우스를 해당 지점까지 서서히 이동
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)

# 타자로 텍스트를 입력
pyautogui.typewrite('Hello world! This is my world', interval=0.01)

# esc를 누른다.
pyautogui.press('esc')

# Shift를 누른다.
pyautogui.keyDown('shift')

# Shift를 손에서 뗀다
pyautogui.keyUp('shift')

# Left를 누른다.
pyautogui.press(['left', 'left'])

# ctrl, s 동시 입력
pyautogui.hotkey('ctrl', 's')
'''
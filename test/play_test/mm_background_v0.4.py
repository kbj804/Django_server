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


    """# 시작 프로그램에 등록하고 싶은 경우(Windows)
    start_path="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup/"

    # 시작 파일 목록 가져오기
    file_list = glob.glob(start_path+'*')

    # py 파일 목록 거르기
    py_list = [file for file in file_list if file.endswith(".py")]

    real_path = os.path.realpath()
    real_path = real_path.replace("\\","/")
    real_path = real_path.replace(".py",".exe")
    print(real_path)

    # py 삭제
    for py in py_list:
        # 실행 파일이 이미 시작프로그램에 등록되어있는 경우
        if py == real_path:
            pass

        else:
            os.remove(py)

    # 현재 파일을 시작프로그램에 등록  -> 파이썬 파일이 뭔가 존재하면 지우는것도 설정해야할듯 
    shutil.copy(real_path, start_path)
    """

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

            if (hour == 12 and m > 30) or (hour == 13 and m < 30):
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

                    # 시계로 이동 후 클릭
                    pyautogui.moveTo(1863, 1061, duration=2, tween=pyautogui.easeInOutQuad)
                    pyautogui.click()
                    #pyautogui.moveRel(-10, 0, duration=1, tween=pyautogui.easeInOutQuad)

                else:
                    print("일하는중")
                    # 움직임이 감지되면 시작시간 초기화
                    startTime = time.time()

                pre_mpX = mousePositionX
                pre_mpY = mousePositionY

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

# 이것 저것
pyautogui.hotkey('win', 'r')
sleep(1)
pyautogui.typewrite('notepad', interval=0.01)

sleep(1)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

pyautogui.typewrite('test ~ ', interval=1)
            



# 빙글뱅글
            sleep(0.5)
            pyautogui.moveRel(0, -10, duration=1, tween=pyautogui.easeInOutQuad)
            sleep(0.5)
            pyautogui.moveRel(10, 0, duration=1, tween=pyautogui.easeInOutQuad)
            sleep(0.5)
            pyautogui.moveRel(0, 10, duration=1, tween=pyautogui.easeInOutQuad)
            sleep(0.5)


'''
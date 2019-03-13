import pyautogui
import time
import random


def yaoqi():
    # 休眠时间随机
    secs = random.randint(0, 3)
    # 点击组队
    pyautogui.moveTo(424, 904)
    pyautogui.click()
    time.sleep(secs)
    # 点击妖气封印
    pyautogui.moveTo(433, 852)
    pyautogui.click()
    time.sleep(secs)
    start = time.clock()
    while(True):
        end = time.clock()

        # 鼠标移动时间随机
        mouseMoveSecs = random.uniform(0.1, 0.3)
        # 鼠标范围随机
        randomSize = random.uniform(0, 2)
        # 刷新、加入，准备
        print('时间打印：', secs, mouseMoveSecs, randomSize)

        time.sleep(secs)
        pyautogui.moveTo(1116+randomSize, 907+randomSize, mouseMoveSecs)
        pyautogui.typewrite('Hello world!',0.25)
        pyautogui.click()
        time.sleep(secs)
        pyautogui.moveTo(1538+randomSize, 330+randomSize, mouseMoveSecs)
        pyautogui.typewrite('Hello world!',0.25)
        pyautogui.click()
        time.sleep(secs)
        pyautogui.moveTo(1668+randomSize, 806+randomSize, mouseMoveSecs)
        pyautogui.typewrite('Hello world!',0.25)
        pyautogui.click()
        # 判断运行时长
        if int(end-start) == 600:
            break


yaoqi()

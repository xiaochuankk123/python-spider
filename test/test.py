import pyautogui
import time
import random

def moveAndClick(x,y,*timeout):
    #随机常量

    #x,y随机距离
    randomSize=random.uniform(0, 20)
    #鼠标移动时间
    mouseMoveSecs=random.uniform(0, 0.1)
    #点击次数
    clickTimes=random.randint(4,8)
    #间隔
    secs=random.uniform(0.3,0.8)

    print('时间打印：', clickTimes, mouseMoveSecs, randomSize)
    time.sleep(secs)
    pyautogui.moveTo(x+randomSize, y+randomSize, mouseMoveSecs)
    pyautogui.click(clicks=clickTimes)

def yuhun():
    while(True):
        #开始战斗按钮：
        moveAndClick(x=1759,y=428)
        time.sleep(60+random.uniform(1,2))
        #等60秒，点点点
        moveAndClick(x=1560,y=70)
        moveAndClick(x=1560,y=570)
        time.sleep(1+random.uniform(1,2))
        moveAndClick(x=1560,y=70)
        moveAndClick(x=1560,y=570)
        time.sleep(1+random.uniform(1,2))
        moveAndClick(x=1560,y=70)
        moveAndClick(x=1560,y=570)
        time.sleep(1+random.uniform(1,2))
        moveAndClick(x=1560,y=70)
        moveAndClick(x=1560,y=570)
        time.sleep(10+random.uniform(1,2))
yuhun()

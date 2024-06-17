import pyautogui
import time
import keyboard
import random
import pydirectinput
def ads():
    x, y = random.randint(1497, 1502), random.randint(189, 194)
    pydirectinput.moveTo(x, y)
    x, y = random.randint(1497, 1502), random.randint(189, 194)
    pydirectinput.moveTo(x, y)
    time.sleep(0.05)  # Small delay to ensure the cursor move is registered
    pydirectinput.click()

def warp():
    if pyautogui.pixel(164, 69) != (253, 253, 253):
        x, y = random.randint(164, 167), random.randint(17, 24)
        pydirectinput.moveTo(x, y)
        x, y = random.randint(164, 167), random.randint(17, 24)
        pydirectinput.moveTo(x, y)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
    else:
        x, y = random.randint(188, 200), random.randint(250, 258)
        pydirectinput.moveTo(x, y)
        x, y = random.randint(188, 200), random.randint(250, 258)
        pydirectinput.moveTo(x, y)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        pydirectinput.keyDown('w')
        time.sleep(2)
        pydirectinput.keyUp('w')

def walk():
    time.sleep(0.1)
    pydirectinput.keyDown('d')
    time.sleep(0.2)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(0.3)
    pydirectinput.keyDown('a')
    time.sleep(3)
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('w')
    time.sleep(3)
    pydirectinput.keyUp('w')

    pydirectinput.keyDown('a')
    time.sleep(1)
    pydirectinput.keyDown('w')
    time.sleep(2)
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('w')


    pydirectinput.keyDown('d')
    time.sleep(0.5)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(2.5)
    pydirectinput.keyUp('w')

    pydirectinput.keyDown('a')
    time.sleep(0.1)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(0.1)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(0.1)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(0.1)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(0.1)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(0.1)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(0.1)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(0.1)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(0.1)
    pydirectinput.keyUp('a')

    pydirectinput.keyDown('w')
    time.sleep(3)
    pydirectinput.keyUp('w')
def map():
    x, y = random.randint(542, 547), random.randint(368, 373)
    pydirectinput.moveTo(x, y)
    x, y = random.randint(542, 547), random.randint(368, 373)
    pydirectinput.moveTo(x, y)
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp() ## Click World

    x, y = random.randint(840, 845), random.randint(700, 705)
    pydirectinput.moveTo(x, y)
    x, y = random.randint(840, 845), random.randint(700, 705)
    pydirectinput.moveTo(x, y)
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp() # Click Infinite

def start():
    if pyautogui.pixel(1064, 538)[0] >= 255:
        x, y = random.randint(985, 990), random.randint(815, 820)
        pydirectinput.moveTo(x, y)
        x, y = random.randint(985, 990), random.randint(815, 820)
        pydirectinput.moveTo(x, y)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp() ## Confirm Map
        time.sleep(0.5)
        x, y = random.randint(1537, 1543), random.randint(645, 650)
        pydirectinput.moveTo(x, y)
        x, y = random.randint(1537, 1543), random.randint(645, 650)
        pydirectinput.moveTo(x, y)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp() ## Start

def spawn():
    x, y = random.randint(500, 510), random.randint(500, 510)
    pydirectinput.moveTo(x, y)
    x, y = random.randint(500, 510), random.randint(500, 510)
    pydirectinput.moveTo(x, y)
    topdown()

def topdown():
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.moveRel(0, 10)
    pydirectinput.mouseUp(button='right')
    pydirectinput.keyDown('o')
    time.sleep(0.1)
    pydirectinput.keyUp('o')
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.moveRel(0, 10)
    pydirectinput.mouseUp(button='right')

def end():
    x, y = random.randint(700, 700), random.randint(880, 885)
    pydirectinput.moveTo(x, y)
    x, y = random.randint(700, 700), random.randint(880, 885)
    pydirectinput.moveTo(x, y)
    time.sleep(0.1)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()

def place():
    global hero,spawn_X,spawn_Y,i,j
    pydirectinput.keyDown(str(hero))
    time.sleep(0.01)
    pydirectinput.keyUp(str(hero))
    pydirectinput.moveTo(j, i+2)
    time.sleep(0.1)
    pydirectinput.moveTo(j, i-2)
    time.sleep(0.1)
    pydirectinput.keyDown('e')
    time.sleep(0.01)
    pydirectinput.keyUp('e')
    time.sleep(0.1)

def upgrade():
    global i,j
    px = 45
    pydirectinput.keyDown('c')
    time.sleep(0.01)
    pydirectinput.keyUp('c')
    time.sleep(0.1)
    x, y = random.randint(j, j + 2), random.randint(i, i + 2)
    pydirectinput.moveTo(x, y)
    x, y = random.randint(j, j + 2), random.randint(i, i + 2)
    pydirectinput.moveTo(x, y)
    time.sleep(0.1)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()
    time.sleep(0.1)

    pydirectinput.moveTo(j, i - (px + 4))
    pydirectinput.moveTo(j, i - px)
    time.sleep(0.1)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()

def twenty_six():
    if pyautogui.pixel(531, 60) == (255, 255, 255) and pyautogui.pixel(535, 58) == (255, 255, 255) and \
            pyautogui.pixel(539,62) == (255, 255, 255) and pyautogui.pixel(531, 70) == (255, 255, 255) and \
            pyautogui.pixel(539, 71) == (255, 255, 255) and pyautogui.pixel(552, 58) == (255, 255, 255) and \
            pyautogui.pixel(545, 62) == (255, 255, 255) and pyautogui.pixel(544, 67) == (255, 255, 255) and \
            pyautogui.pixel(552, 68) == (255, 255, 255) and pyautogui.pixel(548, 71) == (255, 255, 255) and \
            pyautogui.pixel(548, 64) == (255, 255, 255):
        return True
    else:
        return False

def three_one():
    if pyautogui.pixel(531, 60) == (255, 255, 255) and pyautogui.pixel(535, 57) == (255, 255, 255) and \
            pyautogui.pixel(538,60) == (255, 255, 255) and pyautogui.pixel(548, 58) == (255, 255, 255) and \
            pyautogui.pixel(534, 63) == (255, 255, 255) and pyautogui.pixel(538, 66) == (255, 255, 255) and \
            pyautogui.pixel(534, 71) == (255, 255, 255) and pyautogui.pixel(530, 68) == (255, 255, 255) and \
            pyautogui.pixel(548, 69) == (255, 255, 255) and pyautogui.pixel(548, 64) == (255, 255, 255):
        return True
    else:
        return False


camera = 0
ingame = 0
game_round = 0
path = 0
spawn_X = [840,920,1000,1080,1160,1240]
spawn_Y = [420,500,580,660,740]

while not keyboard.is_pressed('q'):
    if pyautogui.pixel(1497, 189)[0] > 180 and pyautogui.pixel(1497, 189)[1] < 10 and pyautogui.pixel(1497, 189)[2] < 20 :
        ads()
        walk()
    if three_one():
        x, y = random.randint(120, 125), random.randint(20, 25)
        pydirectinput.moveTo(x, y)
        x, y = random.randint(120, 125), random.randint(20, 25)
        pydirectinput.moveTo(x, y)
        time.sleep(0.1)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        game_round += 1
        camera = 0
        path = 0
        ingameworld = 0
        time.sleep(5)
        print(game_round)

        x, y = random.randint(160, 165), random.randint(130, 135)
        pydirectinput.moveTo(x, y)
        x, y = random.randint(160, 165), random.randint(130, 135)
        pydirectinput.moveTo(x, y)
        time.sleep(0.1)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()

        x, y = random.randint(850, 855), random.randint(640, 645)
        pydirectinput.moveTo(x, y)
        x, y = random.randint(850, 855), random.randint(640, 645)
        pydirectinput.moveTo(x, y)
        time.sleep(0.1)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()

    elif pyautogui.pixel(530, 790)[0] <= 20 and pyautogui.pixel(530, 790)[1] <= 20 and pyautogui.pixel(530, 790)[2] <= 20:
        map()
        start()
        time.sleep(5)
    #elif pyautogui.pixel(806, 912) == (216, 206, 255):
     #   warp()
    elif pyautogui.pixel(1058, 50) == (125, 206, 70) and camera == 0:
        spawn()
        camera = 1
        ingame = 1
        time.sleep(1)
    elif ingame == 1:
        if keyboard.is_pressed('q'):
            exit()
        elif pyautogui.pixel(1000, 246) == (0, 0, 0):
            ingame = 0
        else:
            for i in spawn_Y:
                if ingame == 0:
                    break
                if three_one():
                    break
                for j in spawn_X:
                    if keyboard.is_pressed('q'):
                        exit()
                    if three_one():
                        break
                    elif pyautogui.pixel(1000, 246) == (0, 0, 0):
                        ingame = 0
                    elif ingame == 0:
                        break
                    elif pyautogui.pixel(j, i)[0] > 180:
                        continue
                    elif i == 420:
                        hero = 1
                        place()
                        upgrade()
                    elif i == 500:
                        hero = 2
                        place()
                        upgrade()
                    elif i == 580:
                        hero = 3
                        place()
                        upgrade()
                    elif i == 660:
                        hero = 4
                        place()
                        upgrade()
                    elif i == 740:
                        hero = 5
                        place()
                        upgrade()


    elif pyautogui.pixel(1000, 246) == (0, 0, 0) and pyautogui.pixel(1811, 145) != 255:
        end()
        game_round += 1
        camera = 0
        path = 0
        ingameworld = 0
        time.sleep(5)
        print(game_round)
import pyautogui
import time
import keyboard
import pydirectinput
def ads():
    pydirectinput.moveTo(1497, 189)
    time.sleep(0.03)
    pydirectinput.moveTo(1502, 194)
    time.sleep(0.05)
    pydirectinput.click()

def warp():
    if pyautogui.pixel(164, 69) != (253, 253, 253):
        pydirectinput.moveTo(164, 17)
        time.sleep(0.03)

        pydirectinput.moveTo(167, 24)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
    else:
        pydirectinput.moveTo(188, 250)
        time.sleep(0.03)
        pydirectinput.moveTo(190, 247)
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
    if keyboard.is_pressed('q'):
        exit()
    time.sleep(0.3)
    pydirectinput.keyDown('a')
    time.sleep(3)
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('w')
    time.sleep(4.4)
    pydirectinput.keyUp('w')

    pydirectinput.keyDown('a')
    time.sleep(2)
    pydirectinput.keyDown('w')
    time.sleep(2)
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('w')
    if keyboard.is_pressed('q'):
        exit()

    pydirectinput.keyDown('d')
    time.sleep(0.6)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(2.4)
    pydirectinput.keyUp('w')

    for i in range(9):
        pydirectinput.keyDown('a')
        pydirectinput.keyDown('w')
        time.sleep(0.1)
        pydirectinput.keyUp('a')
        if keyboard.is_pressed('q'):
            exit()
        pydirectinput.keyUp('w')

    pydirectinput.keyDown('a')
    time.sleep(0.4)
    pydirectinput.keyUp('a')
    if keyboard.is_pressed('q'):
        exit()
    pydirectinput.keyDown('w')
    time.sleep(2.8)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('s')
    time.sleep(0.2)
    pydirectinput.keyUp('s')
    if keyboard.is_pressed('q'):
        exit()
    pydirectinput.keyDown('d')
    time.sleep(1)
    pydirectinput.keyUp('d')

    if not (pyautogui.pixel(522, 792)[0] <= 15 and pyautogui.pixel(522, 792)[1] <= 15 and pyautogui.pixel(522, 792)[2] <= 15 and pyautogui.pixel(498, 836) == (255, 255, 255)):
        pydirectinput.keyDown('s')
        time.sleep(0.3)
        pydirectinput.keyUp('s')
        pydirectinput.keyDown('d')
        time.sleep(1.5)
        pydirectinput.keyUp('d')
        if keyboard.is_pressed('q'):
            exit()
        pydirectinput.keyDown('w')
        time.sleep(0.5)
        pydirectinput.keyUp('w')

    while not (pyautogui.pixel(522, 792)[0] <= 15 and pyautogui.pixel(522, 792)[1] <= 15 and pyautogui.pixel(522, 792)[2] <= 15 and pyautogui.pixel(498, 836) == (255, 255, 255)):
        pydirectinput.keyDown('a')
        time.sleep(0.5)
        pydirectinput.keyUp('a')
        pydirectinput.keyDown('d')
        time.sleep(1)
        pydirectinput.keyUp('d')
        if keyboard.is_pressed('q'):
            exit()
        pydirectinput.keyDown('w')
        time.sleep(1.5)
        pydirectinput.keyUp('w')

def map():
    pydirectinput.moveTo(542, 368)
    time.sleep(0.03)
    pydirectinput.moveTo(547, 373)
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp() ## Click World

    pydirectinput.moveTo(840, 700)
    time.sleep(0.03)
    pydirectinput.moveTo(845, 705)
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp() # Click Infinite

def start():
    if pyautogui.pixel(1064, 538)[0] >= 255:
        pydirectinput.moveTo(985, 815)
        time.sleep(0.03)
        pydirectinput.moveTo(990, 820)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp() ## Confirm Map
        time.sleep(0.5)

        pydirectinput.moveTo(1537, 645)
        time.sleep(0.03)
        pydirectinput.moveTo(1543,650)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp() ## Start

def spawn():
    pydirectinput.moveTo(500, 500)
    time.sleep(0.03)
    pydirectinput.moveTo(510, 510)
    topdown()

def topdown():
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.moveRel(0, 10)
    pydirectinput.mouseUp(button='right')
    pydirectinput.keyDown('o')
    time.sleep(1)
    pydirectinput.keyUp('o')
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.moveRel(0, 10)
    pydirectinput.mouseUp(button='right')

def end():
    pydirectinput.moveTo(700, 880)
    time.sleep(0.03)
    pydirectinput.moveTo(700, 885)
    time.sleep(0.1)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()

def place():
    global hero,spawn_X,spawn_Y,i,j,upp
    pydirectinput.moveTo(j, i)
    time.sleep(0.03)
    pydirectinput.click()
    pydirectinput.keyDown(str(hero))
    time.sleep(0.01)
    pydirectinput.keyUp(str(hero))
    if not pyautogui.pixel(j, i-30)[0] >= 180:
        pydirectinput.moveTo(j, i+5)
        time.sleep(0.03)
        pydirectinput.moveTo(j, i-5)
        time.sleep(0.03)
        pydirectinput.keyDown('e')
        time.sleep(0.01)
        pydirectinput.keyUp('e')
        time.sleep(0.03)
        upp = 1

    pydirectinput.keyDown('c')
    time.sleep(0.01)
    pydirectinput.keyUp('c')
    time.sleep(0.03)

def upgrade():
    global i,j
    px = 45
    pydirectinput.moveTo(j, i+3)
    time.sleep(0.03)
    pydirectinput.click()
    time.sleep(0.05)
    pydirectinput.moveTo(j, i)
    time.sleep(0.03)
    pydirectinput.click()

    pydirectinput.moveTo(j+4, i - px)
    time.sleep(0.03)
    pydirectinput.moveTo(j, i - px)
    time.sleep(0.03)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()

def two_six():
    return False
    # if pyautogui.pixel(1015, 26) == (255, 255, 255) and pyautogui.pixel(1031, 27) == (255, 255, 255) \
    #         and pyautogui.pixel(1025, 37) == (255, 255, 255) and pyautogui.pixel(1019, 31) == (255, 255, 255) \
    #         and pyautogui.pixel(1010, 39) == (255, 255, 255) and pyautogui.pixel(1010, 40) == (255, 255, 255) \
    #         and pyautogui.pixel(1032, 36) == (255, 255, 255) and pyautogui.pixel(1025, 30) == (255, 255, 255) \
    #         and pyautogui.pixel(1024, 36) == (255, 255, 255) and pyautogui.pixel(1032, 36) == (255, 255, 255)\
    #         and pyautogui.pixel(1028, 33) == (255, 255, 255) and pyautogui.pixel(1033, 31) != (255, 255, 255):
    #     return True
    # else:
    #     return False

def three_one():
    if pyautogui.pixel(1011, 28) == (255, 255, 255) and pyautogui.pixel(1014, 26) == (255, 255, 255) \
            and pyautogui.pixel(1018, 28) == (255, 255, 255) and pyautogui.pixel(1014, 32) == (255, 255, 255) \
            and pyautogui.pixel(1019, 37) == (255, 255, 255) and pyautogui.pixel(1014, 40) == (255, 255, 255) \
            and pyautogui.pixel(1010, 37) == (255, 255, 255) and pyautogui.pixel(1028, 27) == (255, 255, 255) \
            and pyautogui.pixel(1029, 33) == (255, 255, 255) and pyautogui.pixel(1028, 39) == (255, 255, 255):
        return True
    else:
        return False

def disconnect():
    if pyautogui.pixel(861, 445)[0] > 55 and pyautogui.pixel(861, 445)[0] < 65 and pyautogui.pixel(861, 445)[1] > 55 and pyautogui.pixel(861, 445)[1] < 65 \
            and pyautogui.pixel(861, 445)[2] > 55 and pyautogui.pixel(861, 445)[2] < 65 and pyautogui.pixel(1000, 620) == (255,255,255):
        pydirectinput.moveTo(1000, 620)
        time.sleep(0.03)
        pydirectinput.moveTo(1005, 620)
        time.sleep(0.1)

camera = 0
ingame = 0
game_round = 0
path = 0
spawn_X = [840,920,1000,1080,1160,1240]
spawn_Y = [420,500,580,660,740]
upp = 0

while not keyboard.is_pressed('q'):
    disconnect()
    if pyautogui.pixel(1497, 190)[0] > 180 and pyautogui.pixel(1497, 190)[1] < 10 and pyautogui.pixel(1497, 190)[2] < 20 or \
            pyautogui.pixel(1534, 188)[0] > 180 and pyautogui.pixel(1534, 188)[1] < 10 and pyautogui.pixel(1534, 188)[2] < 20:
        ads()
        walk()
    if three_one():
        pydirectinput.moveTo(120, 20)
        time.sleep(0.03)
        pydirectinput.moveTo(125, 25)
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

        pydirectinput.moveTo(160, 130)
        time.sleep(0.03)
        pydirectinput.moveTo(165, 135)
        time.sleep(0.1)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()

        pydirectinput.moveTo(850, 640)
        time.sleep(0.03)
        pydirectinput.moveTo(855, 645)
        time.sleep(0.1)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()

    elif pyautogui.pixel(530, 790)[0] <= 20 and pyautogui.pixel(530, 790)[1] <= 20 and pyautogui.pixel(530, 790)[2] <= 20:
        map()
        start()
        time.sleep(3)
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
                    elif i == spawn_Y[0]:
                        hero = 1
                        place()
                        if upp == 1:
                            upgrade()
                            upp = 0
                    elif i == spawn_Y[1]:
                        hero = 2
                        place()
                        if upp == 1:
                            upgrade()
                            upp = 0
                    elif i == spawn_Y[2]:
                        hero = 3
                        place()
                        if upp == 1:
                            upgrade()
                            upp = 0
                    elif i == spawn_Y[3]:
                        hero = 4
                        place()
                        if upp == 1:
                            upgrade()
                            upp = 0
                    elif i == spawn_Y[4]:
                        hero = 5
                        place()
                        if upp == 1:
                            upgrade()
                            upp = 0


    elif pyautogui.pixel(1000, 246) == (0, 0, 0) and pyautogui.pixel(1811, 145) != 255:
        end()
        game_round += 1
        camera = 0
        path = 0
        ingameworld = 0
        time.sleep(5)
        print(game_round)
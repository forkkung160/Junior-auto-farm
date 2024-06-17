import pyautogui
import time
import keyboard
import pydirectinput
def ads1():
    pydirectinput.moveTo(808, 308)
    pydirectinput.click()
    time.sleep(0.05)
    pydirectinput.moveTo(813, 313)
    pydirectinput.click()
    time.sleep(0.05)  # Small delay to ensure the cursor move is registered
    pydirectinput.click()

def ads2():
    pydirectinput.moveTo(1770, 308)
    pydirectinput.click()
    pydirectinput.click()

    pydirectinput.moveTo(1775, 313)
    time.sleep(0.05)  # Small delay to ensure the cursor move is registered
    pydirectinput.click()

def warp():
    if pyautogui.pixel(164, 69) != (253, 253, 253):
        pydirectinput.moveTo(164, 17)
        time.sleep(0.05)
        pydirectinput.moveTo(167, 24)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
    else:
        pydirectinput.moveTo(188, 250)
        time.sleep(0.05)
        pydirectinput.moveTo(200, 258)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        pydirectinput.keyDown('w')
        time.sleep(2)
        pydirectinput.keyUp('w')

def walk():
    global player
    time.sleep(0.1)
    pydirectinput.keyDown('d')
    time.sleep(0.2)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(0.3)
    if keyboard.is_pressed('q'):
        exit()
    pydirectinput.keyDown('a')
    time.sleep(3)
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('w')
    time.sleep(4.4)
    pydirectinput.keyUp('w')
    if keyboard.is_pressed('q'):
        exit()
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
    if keyboard.is_pressed('q'):
        exit()
    for i in range(9):
        pydirectinput.keyDown('a')
        pydirectinput.keyDown('w')
        time.sleep(0.1)
        pydirectinput.keyUp('a')
        pydirectinput.keyUp('w')
        if keyboard.is_pressed('q'):
            exit()

    pydirectinput.keyDown('a')
    time.sleep(0.4)
    pydirectinput.keyUp('a')
    if keyboard.is_pressed('q'):
        exit()
    pydirectinput.keyDown('w')
    time.sleep(3)
    pydirectinput.keyUp('w')
    if player == 1:
        if not (pyautogui.pixel(260, 671)[0] <= 15 and pyautogui.pixel(260, 671)[1] <= 15 and pyautogui.pixel(260, 671)[2] <= 15 and pyautogui.pixel(244,694) == (255,255,255)):
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

        while not (pyautogui.pixel(260, 671)[0] <= 15 and pyautogui.pixel(260, 671)[1] <= 15 and pyautogui.pixel(260, 671)[2] <= 15 and pyautogui.pixel(244,694) == (255,255,255)):
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

    elif player == 2:
        if not (pyautogui.pixel(1836, 481)[0] <= 15 and pyautogui.pixel(1836, 481)[1] <= 15 and pyautogui.pixel(1836, 481)[2] <= 15):
            pydirectinput.keyDown('s')
            time.sleep(0.3)
            pydirectinput.keyUp('s')
            if keyboard.is_pressed('q'):
                exit()
            pydirectinput.keyDown('d')
            time.sleep(1.5)
            pydirectinput.keyUp('d')

        while not (pyautogui.pixel(1836, 481)[0] <= 15 and pyautogui.pixel(1836, 481)[1] <= 15 and pyautogui.pixel(1836, 481)[2] <= 15):
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
    pydirectinput.moveTo(276, 452)
    time.sleep(0.05)
    pydirectinput.moveTo(280, 457)
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp() ## Click World

    pydirectinput.moveTo(417, 629)
    time.sleep(0.05)
    pydirectinput.moveTo(422, 634)
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()
    time.sleep(0.05)

    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp() # Click Infinite

    if pyautogui.pixel(530, 544)[0] >= 255:
        pydirectinput.moveTo(494, 682)
        time.sleep(0.05)
        pydirectinput.moveTo(499, 687)
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        time.sleep(0.05)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp() ## Confirm Map
        time.sleep(0.5)

def start():
    pydirectinput.moveTo(770, 558)
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.02)
    pydirectinput.mouseUp()
    time.sleep(0.05)
    pydirectinput.moveTo(780, 563)
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.02)
    pydirectinput.mouseUp()
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.02)
    pydirectinput.mouseUp()
    time.sleep(0.05)
    pydirectinput.mouseDown()
    time.sleep(0.02)
    pydirectinput.mouseUp() ## Start

def spawn1():
    pydirectinput.moveTo(480, 500)
    time.sleep(0.05)
    pydirectinput.click()
    pydirectinput.moveTo(490,510)
    pydirectinput.click()
    time.sleep(0.3)
    topdown()
    time.sleep(0.3)

def spawn2():
    pydirectinput.moveTo(1440, 500)
    time.sleep(0.05)
    pydirectinput.click()
    pydirectinput.moveTo(1450,510)
    pydirectinput.click()
    time.sleep(0.3)
    topdown()
    time.sleep(0.3)

def topdown():
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.moveRel(0, 20)
    pydirectinput.mouseUp(button='right')
    pydirectinput.keyDown('o')
    time.sleep(0.3)
    pydirectinput.keyUp('o')
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.moveRel(0, 20)
    pydirectinput.mouseUp(button='right')

def end1():
    pydirectinput.moveTo(340, 740)
    time.sleep(0.03)
    pydirectinput.click()
    pydirectinput.moveTo(345, 745)
    time.sleep(0.03)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()
    time.sleep(2)

    pydirectinput.moveTo(1300, 740)
    pydirectinput.click()
    pydirectinput.moveTo(1305, 745)
    time.sleep(0.03)
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



def place2():
    global hero,spawn_X,spawn_Y,i,j
    pydirectinput.moveTo(j+960, i)
    time.sleep(0.03)
    pydirectinput.click()
    time.sleep(0.03)
    pydirectinput.keyDown(str(hero))
    time.sleep(0.01)
    pydirectinput.keyUp(str(hero))
    if not pyautogui.pixel(j+960, i-30)[0] >= 180:
        pydirectinput.moveTo(j+960, i+5)
        time.sleep(0.03)
        pydirectinput.moveTo(j+960, i-5)
        time.sleep(0.03)
        pydirectinput.keyDown('e')
        time.sleep(0.01)
        pydirectinput.keyUp('e')
        time.sleep(0.03)
    pydirectinput.keyDown('c')
    time.sleep(0.01)
    pydirectinput.keyUp('c')
    time.sleep(0.03)
def upgrade():
    global i,j
    px = 35
    pydirectinput.moveTo(j+5, i)
    time.sleep(0.03)
    pydirectinput.click()
    time.sleep(0.05)
    pydirectinput.moveTo(j, i)
    time.sleep(0.03)
    pydirectinput.click()

    pydirectinput.moveTo(j+4, i - px)
    pydirectinput.moveTo(j, i - px)
    time.sleep(0.03)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()

def upgrade2():
    global i,j
    px = 35
    pydirectinput.moveTo(j+960+5, i)
    time.sleep(0.03)
    pydirectinput.click()
    time.sleep(0.05)
    pydirectinput.moveTo(j+960, i)
    time.sleep(0.03)
    pydirectinput.click()

    pydirectinput.moveTo(j+960+4, i - px)
    pydirectinput.moveTo(j+960, i - px)
    time.sleep(0.03)
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
spawn_X = [240, 300, 360, 420, 480, 540, 600, 660]
spawn_Y = [380, 460, 540, 620, 700]
player = 1
ready = 0
upp = 0
upp2 = 0

while not keyboard.is_pressed('q'):
    if pyautogui.pixel(189, 747) == (0, 0, 0) and pyautogui.pixel(1303, 321) != 255:
        pydirectinput.moveTo(830, 200)
        time.sleep(0.002)
        pydirectinput.moveTo(835, 205)
        time.sleep(0.03)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        time.sleep(0.002)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        time.sleep(0.03)

        end1()
        player = 1
        game_round += 1
        camera = 0
        path = 0
        ingame = 0
        ready = 0

        time.sleep(3)
        print(game_round)
    if three_one():
        radius = 0
        while radius <= 960:
            pydirectinput.moveTo(232+radius, 50)
            pydirectinput.mouseDown()
            time.sleep(0.002)
            pydirectinput.mouseUp()
            pydirectinput.moveTo(120+radius, 50)
            pydirectinput.moveTo(125+radius, 55)
            time.sleep(0.03)
            pydirectinput.mouseDown()
            time.sleep(0.002)
            pydirectinput.mouseUp()

            pydirectinput.moveTo(155+radius, 160)
            pydirectinput.moveTo(160+radius, 165)
            time.sleep(0.03)
            pydirectinput.mouseDown()
            time.sleep(0.002)
            pydirectinput.mouseUp()

            pydirectinput.moveTo(435+radius, 585)
            pydirectinput.moveTo(440+radius, 590)
            time.sleep(0.03)
            pydirectinput.mouseDown()
            time.sleep(0.002)
            pydirectinput.mouseUp()
            radius += 960
            time.sleep(1)

        game_round += 1
        camera = 0
        path = 0
        ingame = 0
        player = 1
        ready = 0
        time.sleep(3)
        print(game_round)
    elif player == 1 :
        if (pyautogui.pixel(806, 318)[0] > 180 and pyautogui.pixel(806, 318)[1] < 10 and pyautogui.pixel(806, 318)[2] < 20) \
                or (pyautogui.pixel(784, 337)[0] > 180 and pyautogui.pixel(784, 337)[1] < 10 and pyautogui.pixel(748, 337)[2] < 20):
            pydirectinput.moveTo(790, 210)
            time.sleep(0.03)
            pydirectinput.click()
            time.sleep(0.03)
            ads1()
            while not (pyautogui.pixel(260, 671)[0] <= 15 and pyautogui.pixel(260, 671)[1] <= 15 and pyautogui.pixel(260, 671)[2] <= 15 and pyautogui.pixel(244,694) == (255,255,255)):
                walk()
        elif pyautogui.pixel(260, 671)[0] <= 20 and pyautogui.pixel(260, 671)[1] <= 20 and pyautogui.pixel(260, 671)[2] <= 20 and pyautogui.pixel(248, 693) == (255,255,255):
            map()
            time.sleep(0.1)
            player = 2
        elif ready == 1:
            pydirectinput.moveTo(790, 210)
            time.sleep(0.03)
            pydirectinput.click()
            start()
            time.sleep(3)
            ready = 0
            player = 1
    elif player == 2:
        if (pyautogui.pixel(1767, 319)[0] > 190 and pyautogui.pixel(1767, 319)[1] < 10 and pyautogui.pixel(1767, 319)[2] < 20) \
                or (pyautogui.pixel(784+960, 337)[0] > 190 and pyautogui.pixel(784+960, 337)[1] < 10 and pyautogui.pixel(748+960, 337)[2] < 20):
            pydirectinput.moveTo(1750, 210)
            time.sleep(0.1)
            pydirectinput.click()
            ads2()
            walk()
            player = 1
            ready = 1

    if pyautogui.pixel(542, 77) == (126, 210, 74) and camera == 0:
        spawn1()
        time.sleep(0.1)
        spawn2()
        camera = 1
        ingame = 1
        time.sleep(1)
    elif ingame == 1:
        if keyboard.is_pressed('q'):
            exit()
        elif pyautogui.pixel(189, 747) == (0, 0, 0):
            ingame = 0
        else:
            for i in spawn_Y:
                if ingame == 0:
                    break
                if three_one():
                    break
                if pyautogui.pixel(806, 318) == (195, 6, 14):
                    break
                for j in spawn_X:
                    if keyboard.is_pressed('q'):
                        exit()
                    if three_one():
                        break
                    if pyautogui.pixel(806, 318) == (195, 6, 14):
                        break
                    elif pyautogui.pixel(189, 747) == (0, 0, 0):
                        ingame = 0
                    elif ingame == 0:
                        break
                    elif i == spawn_Y[0]:
                        hero = 1
                        place()
                        if upp == 1:
                            upgrade()
                            upp = 0
                        place2()

                    elif i == spawn_Y[1]:
                        hero = 2
                        place()
                        if upp == 1:
                            upgrade()
                            upp = 0
                        place2()
                    elif i == spawn_Y[2]:
                        hero = 3
                        place()
                        if upp == 1:
                            upgrade()
                            upp = 0
                        place2()
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
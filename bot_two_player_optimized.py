import pyautogui
import time
import keyboard
import pydirectinput

def click_at(x, y, delay=0.05, times=1):
    pydirectinput.moveTo(x, y)
    for _ in range(times):
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
    time.sleep(delay)

def ads1():
    click_at(808, 308)
    click_at(813, 313)

def ads2():
    click_at(1770, 308, times=2)
    click_at(1775, 313)

def warp():
    if pyautogui.pixel(164, 69) != (253, 253, 253):
        click_at(164, 17)
        click_at(167, 24)
    else:
        click_at(188, 250)
        click_at(200, 258)
        pydirectinput.keyDown('w')
        time.sleep(2)
        pydirectinput.keyUp('w')

def walk():
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
    time.sleep(2)
    pydirectinput.keyDown('w')
    time.sleep(2)
    pydirectinput.keyUp('a')
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(0.6)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(2.4)
    pydirectinput.keyUp('w')

    for _ in range(9):
        pydirectinput.keyDown('a')
        pydirectinput.keyDown('w')
        time.sleep(0.1)
        pydirectinput.keyUp('a')
        pydirectinput.keyUp('w')

    pydirectinput.keyDown('a')
    time.sleep(0.4)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(2.7)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('s')
    time.sleep(0.2)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(1)
    pydirectinput.keyUp('d')

def map():
    click_at(276, 452)
    click_at(280, 457, times=2)
    click_at(417, 629)
    click_at(422, 634, times=2)

    if pyautogui.pixel(530, 544)[0] >= 255:
        click_at(494, 682)
        click_at(499, 687, times=2)
        time.sleep(0.5)

def start():
    click_at(770, 558)
    click_at(780, 563, times=3)

def spawn1():
    click_at(480, 500)
    click_at(490, 510)
    time.sleep(0.3)
    topdown()
    time.sleep(0.3)

def topdown():
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.moveRel(0, 20)
    pydirectinput.mouseUp(button='right')
    pydirectinput.keyDown('o')
    time.sleep(0.1)
    pydirectinput.keyUp('o')
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.moveRel(0, 20)
    pydirectinput.mouseUp(button='right')

def end1():
    click_at(340, 740, delay=0.03)
    click_at(345, 745, delay=0.03)
    time.sleep(2)
    click_at(1300, 740)
    click_at(1305, 745, delay=0.03)

def place():
    global hero, spawn_X, spawn_Y, i, j, upp
    click_at(j, i, delay=0.03)
    pydirectinput.keyDown(str(hero))
    time.sleep(0.01)
    pydirectinput.keyUp(str(hero))
    if not pyautogui.pixel(j, i - 30)[0] >= 180:
        pydirectinput.moveTo(j, i + 5)
        time.sleep(0.03)
        pydirectinput.moveTo(j, i - 5)
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
    global hero, spawn_X, spawn_Y, i, j
    click_at(j + 960, i + 300, delay=0.03)
    pydirectinput.keyDown('o')
    time.sleep(0.05)
    pydirectinput.keyUp('o')
    pydirectinput.keyDown(str(hero))
    time.sleep(0.01)
    pydirectinput.keyUp(str(hero))
    if not pyautogui.pixel(j + 960, i - 50 + 300)[0] >= 180:
        pydirectinput.moveTo(j + 960, i + 300 + 5)
        time.sleep(0.03)
        pydirectinput.moveTo(j + 960, i + 300 - 5)
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
    global i, j
    px = 45
    click_at(j, i + 5, delay=0.03)
    click_at(j, i, delay=0.05)
    click_at(j, i - (px + 4), delay=0.03)
    click_at(j, i - px, delay=0.03)

camera = 0
ingame = 0
game_round = 0
path = 0
spawn_X = [100, 180, 260, 340, 420, 500, 580, 660]
spawn_Y = [280, 360, 540, 620, 700]
player = 1
ready = 0
upp = 0
upp2 = 0

while not keyboard.is_pressed('q'):
    if pyautogui.pixel(189, 747) == (0, 0, 0) and pyautogui.pixel(1303, 321) != 255:
        click_at(830, 200, delay=0.03, times=2)
        end1()
        player = 1
        game_round += 1
        camera = 0
        path = 0
        ingame = 0
        ready = 0
        time.sleep(3)
        print(game_round)

    if pyautogui.pixel(531, 60) == (255, 255, 255) and all(pyautogui.pixel(531 + x, 60 + y) == (255, 255, 255) for x, y in [(4, -2), (8, 2), (0, 10), (8, 11), (21, -2), (14, 2), (13, 7), (21, 8), (17, 11), (17, 4)]):
        for radius in range(0, 1920, 960):
            click_at(232 + radius, 50)
            click_at(120 + radius, 55)
            click_at(155 + radius, 165)
            click_at(435 + radius, 590)
            time.sleep(1)
        game_round += 1
        camera = 0
        path = 0
        ingame = 0
        player = 1
        ready = 0
        time.sleep(3)
        print(game_round)

    elif player == 1:
        if pyautogui.pixel(806, 318) == (195, 6, 14):
            click_at(790)

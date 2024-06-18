from PIL import Image, ImageEnhance, ImageFilter
from scipy.ndimage import gaussian_filter
import numpy as np
import pytesseract
import pyautogui
import time
import keyboard
import pydirectinput


def solve_captcha(filename):
    try:
        # Path to tesseract executable (adjust the path based on your installation)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example
        # pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # macOS example
        # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Linux example

        # Read the image
        original = Image.open(filename)
        # Convert to grayscale
        black_and_white = original.convert("L")
        black_and_white.save("black_and_white.png")

        # Apply the first threshold
        th1 = 140
        first_threshold = black_and_white.point(lambda p: p > th1 and 255)
        first_threshold.save("first_threshold.png")

        # Apply Gaussian blur
        sig = 1.5
        blur = np.array(first_threshold)  # create an image array
        blurred = gaussian_filter(blur, sigma=sig)
        blurred = Image.fromarray(blurred)
        blurred.save("blurred.png")

        # Apply the second threshold
        th2 = 140
        final = blurred.point(lambda p: p > th2 and 255)

        # Enhance edges and sharpen the image
        final = final.filter(ImageFilter.EDGE_ENHANCE_MORE)
        final = final.filter(ImageFilter.SHARPEN)
        final.save("final.png")

        # Perform OCR using Tesseract
        number = pytesseract.image_to_string(final, lang='eng', config='--psm 10 --oem 3')

        # Remove spaces from the result
        number_no_spaces = number.replace(" ", "")

        print("RESULT OF CAPTCHA:")
        print(number_no_spaces)
        pydirectinput.moveTo(750, 740)
        time.sleep(0.03)
        pydirectinput.moveTo(755, 740)
        time.sleep(0.03)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        time.sleep(0.1)
        pyautogui.typewrite(number_no_spaces)
        pydirectinput.moveTo(1190, 740)
        time.sleep(0.03)
        pydirectinput.moveTo(1195, 740)
        time.sleep(0.03)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        time.sleep(0.1)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def screenshot():
    x1, y1 = 593, 407
    x2, y2 = 1319, 641
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    screenshot.save('ss.png')

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
    pydirectinput.click()

    pydirectinput.moveTo(j+4, i - px)
    time.sleep(0.03)
    pydirectinput.moveTo(j, i - px)
    time.sleep(0.03)
    pydirectinput.mouseDown()
    time.sleep(0.002)
    pydirectinput.mouseUp()

camera = 0
ingame = 0
game_round = 0
path = 0
spawn_X = [840,920,1000,1080,1160,1240]
spawn_Y = [420,500,580,660,740]
upp = 0

while not keyboard.is_pressed('q'):
    if pyautogui.pixel(625, 419) == (255, 255, 255) and pyautogui.pixel(1181, 789) == (120, 205, 69):
        screenshot()
        time.sleep(5)
        result = solve_captcha("ss.png")
    if pyautogui.pixel(1058, 50) == (125, 206, 70) and camera == 0:
        camera = 1
        ingame = 1
        time.sleep(1)
    if pyautogui.pixel(803, 909) == (24, 65, 255):
        pydirectinput.moveTo(803,909)
        time.sleep(0.03)
        pydirectinput.moveTo(803,904)
        time.sleep(0.03)
        pydirectinput.mouseDown()
        time.sleep(0.002)
        pydirectinput.mouseUp()
        time.sleep(2)
        ingame = 1

    elif ingame == 1:
        if keyboard.is_pressed('q'):
            exit()
        elif pyautogui.pixel(1000, 246) == (0, 0, 0):
            ingame = 0
        else:
            for i in spawn_Y:
                if ingame == 0:
                    break
                for j in spawn_X:
                    if keyboard.is_pressed('q'):
                        exit()
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

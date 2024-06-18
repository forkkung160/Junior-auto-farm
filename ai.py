import pyautogui
import time
import pydirectinput
from roboflow import Roboflow
from threading import Event

# Initialize Roboflow
rf = Roboflow(api_key="wVpGasHCyTaSeQeum2Xz")
project = rf.workspace("python-y17c3").project("roblox-ivjcr")
version = project.version(3)
model = project.version(3).model

# Define constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_CENTER_X = SCREEN_WIDTH // 2
SCREEN_CENTER_Y = SCREEN_HEIGHT // 2


# Function to take screenshot and detect objects
def take_screenshot(model):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)

    # Use the AI model to predict objects
    prediction = model.predict(screenshot_path, confidence=70, overlap=30).json()
    return prediction


# Function to find the center coordinates of the spawner
def get_spawner_center(prediction):
    for item in prediction['predictions']:
        if item['class'] == 'spawner':
            x_center = (item['x'] + item['width'] // 2)
            y_center = (item['y'] + item['height'] // 2)
            return x_center, y_center
    return None


# Function to adjust the camera
def adjust_camera(spawner_center_x):
    if spawner_center_x < SCREEN_CENTER_X:
        pydirectinput.keyDown('left')
        time.sleep(0.01)
        pydirectinput.keyUp('left')
    elif spawner_center_x > SCREEN_CENTER_X:
        pydirectinput.keyDown('right')
        time.sleep(0.01)
        pydirectinput.keyUp('right')


# Main function to continuously take screenshots and adjust camera
def main():
    stop_event = Event()
    try:
        while not stop_event.is_set():
            # Take screenshot and get prediction
            prediction = take_screenshot(model)
            spawner_center = get_spawner_center(prediction)

            # If spawner is found, adjust camera
            if spawner_center:
                adjust_camera(spawner_center[0])

    except KeyboardInterrupt:
        stop_event.set()
        print("Stopped by user")


if __name__ == "__main__":
    main()

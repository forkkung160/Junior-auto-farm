from PIL import Image
from scipy.ndimage import gaussian_filter
import numpy as np
import pytesseract
from PIL import ImageFilter


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

        print("RESULT OF CAPTCHA:")
        print(number)
        print("===================")

        # Write result to keyboard
        time.sleep(2)  # Delay to allow user to focus the input field
        pyautogui.typewrite(number)

        return number
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
result = solve_captcha("ss.png")

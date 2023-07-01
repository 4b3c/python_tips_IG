
import pyautogui

def take_screenshot(x, y, width, height):
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.crop((x, y, x + width, y + height))
    screenshot.save('screenshot.png')

# Specify the coordinates and dimensions of the area to capture
x = 312  # x-coordinate of the top-left corner
y = 100  # y-coordinate of the top-left corner
width = 590  # Width of the area
height = 500  # Height of the area

# Capture and save the screenshot
take_screenshot(x, y, width, height)


#pip install pillow pyautogui
import pyautogui
import time
from PIL import ImageChops, ImageGrab

# Function to check if the screen has changed
def has_screen_changed(img1, img2, threshold=30):
    diff = ImageChops.difference(img1, img2)
    # Get the bounding box of the non-zero regions
    bbox = diff.getbbox()
    return bbox is not None

# Main monitoring function
def monitor_screen(interval=1):
    # Initial screen capture
    last_screenshot = ImageGrab.grab()

    while True:
        time.sleep(interval)
        # Take a new screenshot
        current_screenshot = ImageGrab.grab()
        
        # Check if the screen has changed
        if has_screen_changed(last_screenshot, current_screenshot):
            print("Screen changed! Performing click action.")
            pyautogui.click()  # This clicks at the current mouse position
            # Update the last screenshot for future comparison
            last_screenshot = current_screenshot

# Run the monitoring function
if __name__ == "__main__":
    monitor_screen(interval=1)  # Adjust the interval as needed
import pyautogui
import time
import pyperclip
import argparse

# Set up argument parsin
parser = argparse.ArgumentParser(description="Type clipboard content after a delay.")
parser.add_argument('delay', type=int, help='Number of seconds to wait before typing.')
args = parser.parse_args()

# Wait for the specified number of seconds to switch to VM window
time.sleep(args.delay)

# Get clipboard content
text = pyperclip.paste()

# # Type the text in the VM
# pyautogui.typewrite(text, interval=0.0001)  # Adjust interval for typing speed

# Manually type the first character to ensure it's capitalized
pyautogui.typewrite(text[0].upper(), interval=0.0001)

# Type the rest of the text
pyautogui.typewrite(text[1:], interval=0.0001)

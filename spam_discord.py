#Made by Heribio


from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
import random

# Create a keyboard controller to press keys
keyboard_controller = Controller()

# Define a flag to control text typing
script_enabled = False

#List of phrases
phrases = [
    "Phrase 1",
    "Phrase 2",
    "Phrase 3",
    "Phrase 4",
    "Phrase 5"
]

# Define a function to be called when a key is pressed
def on_key_press(key):
    global script_enabled

    if key == Key.f5:
        script_enabled = not script_enabled  # Toggle the script state
        if script_enabled:
            print("Script is enabled")
            # You can add your script logic here
        else:
            print("Script is disabled")

# Create a keyboard listener
listener = keyboard.Listener(
    on_press=on_key_press
)

# Start listening for keypress events
listener.start()

while True:
    if script_enabled:
        text_to_type = random.choice(phrases)
        keyboard_controller.type(text_to_type)
        time.sleep(1)
        keyboard_controller.press(Key.enter)
        keyboard_controller.release(Key.enter)

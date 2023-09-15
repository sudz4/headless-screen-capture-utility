def ascii_art_signature():
    ascii_art_sudz4 = r""" # a program by,
███████ ██    ██ ██████  ███████ ██   ██ 
██      ██    ██ ██   ██    ███  ██   ██ 
███████ ██    ██ ██   ██   ███   ███████ 
     ██ ██    ██ ██   ██  ███         ██ 
███████  ██████  ██████  ███████      ██                               
    """
    print(ascii_art_sudz4)

import os
import time
import subprocess
from datetime import datetime
import pyfiglet

# Set CONSTANT vars
CLIENT_NAME = 'inovalon'  # input the clients name or topic, i.e, ACME Solutions
meeting_type = 'specs_login_page'  # input the meeting type, i.e., CAB (Change Advisory Board)
CLIENT_NAME = CLIENT_NAME.upper()

# Set screenshot (screen capture) interval here - IMPORTANT! -
INTERVAL = 5  # in seconds
COUNTDOWN_SECONDS = INTERVAL
RUNTIME_IN_MINUTES = 60

def create_screenshots_folder(client_name):
    top_folder_path = '/Users/sudz4/Desktop/SLED-DOGZ/headless-screen-capture-utility'
    if not os.path.exists(top_folder_path):
        os.makedirs(top_folder_path)

    client_folder_path = os.path.join(top_folder_path, client_name)
    if not os.path.exists(client_folder_path):
        os.makedirs(client_folder_path)

    return client_folder_path

def interval_countdown(interval):
    for i in range(interval, 0, -1):
        os.system('clear')
        countdown_text = f"Screen Capture Incoming In: {i} seconds"
        large_countdown_text = pyfiglet.figlet_format(str(i), font="big")
        if i == COUNTDOWN_SECONDS:
            print(f"{countdown_text}\n{large_countdown_text}")
        else:
            print(f"{countdown_text}\n{large_countdown_text}")
        time.sleep(1)
    return interval

def take_screenshot(folder_path, client_name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_file = os.path.join(folder_path, f"{timestamp}_{client_name}_{meeting_type}.png")
    subprocess.run(["screencapture", "-x", screenshot_file])
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{client_name} screen capture SAVED AS {screenshot_file} @ {current_time}")
    return True

def main():
    end_time = time.time() + RUNTIME_IN_MINUTES * 60
    folder_path = create_screenshots_folder(CLIENT_NAME)

    print(f"Machine screen capture in progress ({INTERVAL} second intervals) for {RUNTIME_IN_MINUTES} minutes...")
    print("Press control+c to quit or stop running program")

    while time.time() < end_time:
        remaining_time = interval_countdown(INTERVAL)
        take_screenshot(folder_path, CLIENT_NAME)
        time.sleep(remaining_time)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("\nScreen Captures SAVED!")
        print("Thanks for using sCrEeN cApTuRe!")
        ascii_art_signature()
        print()

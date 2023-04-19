#!/usr/bin/env python3
"""
Volumio music server status, start, and stop playback.
Originally (still often used) a short zsh script with the
same functionality.

To start the script (it will keep running until the user `(Q)uits`).
Example:
    $ python3 main.py

On GNU/Linux make the script executable, and run it directly.
In the repository directory:
    $ chmod u+x ./main.py

Executable example:
    $ ./main.py
"""

__author__ = "CrustyBarnacle <CrustyBarnacle@users.noreply.github.com>"
__version__ = "0.1.0"
__license__ = "GPL-3.0"

import time
import sys
import requests

VOLUMIO_HOST = "<hostname>"
api_endpoint = f"http://{VOLUMIO_HOST}/api/v1"

PREVIOUS_TRACK = ""
PLAYER_STATUS = ""


def get_user_input():
    """
    Prompt user 
    """
    user_input = input("(p)lay, (s)top, (q)uit): ")
    match user_input:
        case "play" | "p" | "start":
            start_playback()
        case "stop" | "s":
            stop_playback()
        case "quit" | "Quit" | "q" | "Q":
            exit_application()
        case _:
            return


def get_current_status():
    """
    Stuff this function does...

    Actually, what does it do?

    :param arg1: Description of argument 1.
    :type arg1: Type of argument 1.
    :param arg2: Description of argument 2.
    :type arg2: Type of argument 2.
    :return: Description of the return value.
    :rtype: Type of the return value.
    """
    try:
        response = requests.get(f"{api_endpoint}/getState", timeout=3.0)
        response_json = response.json()

        if response_json["status"] == "play":
            return {
                "title": response_json["title"],
                "artist": response_json["artist"],
                "status": response_json["status"]
            }
        return {}

    except requests.exceptions.RequestException as error:
        print(f"Unable to obtain current track info or status ({error})")
        return {}

def start_playback():
    """
    Start audio playback.
    """
    try:
        requests.get(f"{api_endpoint}/commands/?cmd=play", timeout=3.0)

    except requests.exceptions.RequestException as error:
        print(f"Unable to reach host or obtain status ({error})")

def stop_playback():
    """
    Stop audio playback.
    """
    try:
        requests.get(f"{api_endpoint}/commands/?cmd=stop", timeout=3.0)

    except requests.exceptions.RequestException as error:
        print(f"Unable to reach host or obtain status ({error})")

def exit_application():
    """
    Quit the application. Exit. Get outta here.
    """
    user_input = input("Stop playing music? (Y)/(N) ")
    match user_input:
        case "Yes" | "yes" | "Y" | "y":
            stop_playback()
    sys.exit()


while True:
    get_user_input()

    current_track = get_current_status()
    if current_track:
        current_title = current_track["title"]
        if current_title != PREVIOUS_TRACK:
            print(f"Currently playing: {current_title}\n{current_track['artist']}")
            PREVIOUS_TRACK = current_title
        current_player_status = current_track["status"]
        if current_player_status != PLAYER_STATUS:
            print(f"Player status: {current_player_status}")
            PLAYER_STATUS = current_player_status


    time.sleep(5)

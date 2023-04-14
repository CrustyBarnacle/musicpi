#!/usr/bin/env python3

import time
import requests

VOLUMIO_HOST = "<volumio_hostname>"
api_endpoint = f"http://{VOLUMIO_HOST}/api/v1"

PREVIOUS_TRACK = ""
PLAYER_STATUS = ""


def get_user_input():
    user_input = input("Enter command (start, stop, quit): ")
    if user_input == "start":
        start_playback()
    elif user_input == "stop":
        stop_playback()
    elif user_input == "quit":
        return user_input

def get_current_status():
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

def start_playback():
    try:
        requests.get(f"{api_endpoint}/commands/?cmd=play", timeout=3.0)

    except requests.exceptions.RequestException as error:
        print(f"Unable to reach host or obtain status ({error})")

def stop_playback():
    try:
        requests.get(f"{api_endpoint}/commands/?cmd=stop", timeout=3.0)

    except requests.exceptions.RequestException as error:
        print(f"Unable to reach host or obtain status ({error})")

while True:
    command = get_user_input()
    if command == "quit":
        break

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

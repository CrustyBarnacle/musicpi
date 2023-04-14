import requests
import time

volumio_host = "musicpi"
api_endpoint = f"http://{volumio_host}/api/v1"

previous_track = ""
player_status = ""


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
        response = requests.get(f"{api_endpoint}/getState")
        response_json = response.json()
        
        if response_json["status"] == "play":
            return {
                "title": response_json["title"],
                "artist": response_json["artist"],
                "status": response_json["status"]
            }
        else:
            return {}
    except Exception as error:
        print(f"Unable to obtain current track info or status ({error})")

def start_playback():
    requests.get(f"{api_endpoint}/commands/?cmd=play")

def stop_playback():
    requests.get(f"{api_endpoint}/commands/?cmd=stop")


while True:
    user_input = get_user_input()
    if user_input == "quit":
        break
    else:
        current_track = get_current_status()
        if current_track:
            current_title = current_track["title"]
            if current_title != previous_track:
                print(f"Currently playing: {current_title}\n{current_track['artist']}")
                previous_track = current_title
            current_player_status = current_track["status"]
            if current_player_status != player_status:
                print(f"Player status: {current_player_status}")
                player_status = current_player_status


    time.sleep(5)

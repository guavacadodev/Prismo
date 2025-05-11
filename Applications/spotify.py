# Imports #
import os
from colorama import Fore, Style
import pyttsx3
# ---------------------------------------------- Global Variables ---------------------------------------------- #
SPOTIFY_PROMPTS = ["open spotify", "prismo initiate spotify"]
engine = pyttsx3.init()

# ---------------------------------------------- Step 1 ---------------------------------------------- #
# This function captures the transcription to determine if the user wants to initiate Spotify.
def identify_spotify_query(transcription):
    print(Fore.LIGHTMAGENTA_EX + "User said:", transcription)

    for prompt in SPOTIFY_PROMPTS:
        if prompt in transcription:
            open_spotify()   # Command to open Spotify
            return True  # Indicate that a command was processed
    return False  # No Spotify command was found in the transcription

# ---------------------------------------------- Step 2 ---------------------------------------------- #
# This function uses the system's default method to open Spotify.
def open_spotify():
    # This is an example using a system command to open Spotify.
    # You might need to adapt this according to your OS and specific needs.
    os.system("start spotify")
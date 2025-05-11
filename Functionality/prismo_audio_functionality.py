# Imports #
import speech_recognition as sr
from colorama import Fore, Back, Style, init

# ---------------------------------------------- Global Variables ---------------------------------------------- #
r = sr.Recognizer() # Audio Recognizer
mic = sr.Microphone()   # Microphone Input

# ---------------------------------------------- Listeners ---------------------------------------------- #
# This function simply listens for all audio input from a microphone source.
# Use this function if you want microphone to capture audio and store it anywhere, for any reason.
# ---------------------------------------------------------------------------------------------------- #
def main_listener():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust pause_threshold and listen duration for quicker response
        recognizer.pause_threshold = 0.5
        try:
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=3)
        except sr.WaitTimeoutError:
            return None
    return audio

# This function listens with a timeout, especially suited for your wikipedia queries
def wiki_listener():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print(Style.BRIGHT + Fore.BLUE + "Listening For Wikipedia Query (5 seconds) . . .")
        init(autoreset=True)
        return r.listen(source, timeout=8)

def command_handlers_listener():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print(Style.BRIGHT + Fore.CYAN + "Listening for command handlers (5 seconds)...")
        init(autoreset=True)
        return r.listen(source, timeout=5)

# ---------------------------------------------- Audio Capture Function ---------------------------------------------- #
# This function uses the audio stored in a variable from Step 1 and gets transcribed into text.
# After it is transcribed, it can be used as a string value for any usage.
# Must use    audio = listener()
#             transcription = user_input(audio)    cohesively in order for audio to translate to text.
# ---------------------------------------------------------------------------------------------------- #
def user_input(audio):
    recognizer = sr.Recognizer()
    transcription = recognizer.recognize_google(audio)
    return transcription

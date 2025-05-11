# Imports #
import speech_recognition as sr
import pyttsx3
from colorama import Fore
from Functionality.prismo_wake_words import identify_wake_words, WAKE_WORDS
from Functionality.prismo_audio_functionality import main_listener, user_input, command_handlers_listener
from Functionality.prismo_commandhandlers import handle_command
import time
import threading
#testing
# ---------------------------------------------- Global Variables ---------------------------------------------- #
r = sr.Recognizer() # Audio Recognizer
mic = sr.Microphone()   # Microphone Input
engine = pyttsx3.init() # Assistant Text-To-Speech Program
stop_event = threading.Event()
current_response = None
user_agent = "PrismoBot/1.0 (jake.woodall@example.com)"
voices = engine.getProperty('voices')
WIKIPEDIA_PROMPTS = ["what is", "tell me about", "who is", "who made", "what do"]
# ---------------------------------------------- Code Start ---------------------------------------------- #
def listen_for_wake_word():
    audio = main_listener()
    if audio is None:
        print("Listening timed out while waiting for phrase to start")
        return None

    try:
        transcription = user_input(audio)
        print(Fore.LIGHTMAGENTA_EX + "User said:", transcription)
        return transcription
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Request error: {e}")
    return None


def prismo_listening_mode():
    while not stop_event.is_set():
        transcription = listen_for_wake_word()
        if transcription and any(word in transcription.lower() for word in WAKE_WORDS):
            if identify_wake_words(transcription):
                listen_for_command()

def listen_for_command():
    audio = command_handlers_listener()
    if audio is None:
        return
    try:
        transcription = user_input(audio)
        print(Fore.LIGHTYELLOW_EX + "Command:", transcription)
        handle_command(transcription)
    except sr.UnknownValueError:
        print("Command not understood.")



# Start the listening mode
prismo_listening_mode()
# def prismo_audio_capture():
#     while True:
#         try:
#             # ---------------------- Captures the Audio ---------------------- #
#             audio = main_listener()
#             transcription = user_input(audio)
#             print(Fore.LIGHTMAGENTA_EX + "User said:", transcription)
#             # ---------------------- Detects A Wake Word ---------------------- #
#             if any(word in transcription for word in WAKE_WORDS):
#                 # ---------------------- Assistant Greets User ---------------------- #
#                 wake_word_detected = identify_wake_words(transcription)
#                 # ---------------------- Assistant Listens For All Commands ---------------------- #
#                 if wake_word_detected == True:
#                     audio = command_handlers_listener()
#                     transcription = user_input(audio)
#                     handle_command(transcription)
#
#             time.sleep(1)
#         except sr.UnknownValueError:
#             print("Test error message")
# prismo_audio_capture()
#
#
#
# def prismo_stop_command():
#         engine.stop()





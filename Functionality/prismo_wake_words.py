import pyttsx3
import random
from colorama import Style, Fore
from Functionality.prismo_greetings import greetings

engine = engine = pyttsx3.init() # Assistant Text-To-Speech Program
WAKE_WORDS = ["hello prismo", "hi prismo", "hey prismo", "hi there"]  # REPLACE GOOGLE WITH PRISMO

# If any word from WAKE_WORDS list is in transcribed audio, then assistant will respond with
# PRISMO_GREETINGS list with a random greeting.
def identify_wake_words(transcription):
    for word in WAKE_WORDS:
        if word in transcription.lower():
            response = random.choice(greetings)
            print(Style.BRIGHT + Fore.RED + "Prismo: " + Fore.RESET + Style.NORMAL + response)
            engine.say(response)
            engine.runAndWait()
            return True
    return False
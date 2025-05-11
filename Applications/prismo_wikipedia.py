# Imports #
import speech_recognition as sr
import time
import random
import wikipediaapi
import requests
import threading
import queue
from colorama import Fore, Style
from Functionality.prismo_audio_functionality import wiki_listener, user_input
import pyttsx3
# ---------------------------------------------- Global Variables ---------------------------------------------- #
WIKIPEDIA_PROMPTS = ["what is", "tell me about", "who is", "who made"]
engine = pyttsx3.init()
# ---------------------------------------------------- Step 1 -------------------------------------------------- #
# This function captures audio and transcribes it to text to determine if the user is asking a Wikipedia-related question.
def identify_wikipedia_query(transcription):
    print(Fore.LIGHTMAGENTA_EX + "User said:", transcription)

    for prompt in WIKIPEDIA_PROMPTS:
        if prompt in transcription:
            topic = transcription.replace(prompt, "").strip()
            summary = get_wikipedia_summary(topic)

            speak_wikipedia_result(summary, engine)
            return True  # Indicate that a command was processed
    return False  # No Wikipedia command was found in the transcription
# ---------------------------------------------------- Step 2 -------------------------------------------------- #
# This function only acts as a search function. It takes the input from the user, and will look
# For a title of a page that best matches the query it has been given.
def search_wikipedia(query, lang='en'):
    """Search Wikipedia and return the title of the best matching article."""
    endpoint = f"https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
    }
    response = requests.get(endpoint, params=params).json()
    search_results = response.get('query', {}).get('search', [])
    if search_results:
        return search_results[0]['title']
    return None
# ---------------------------------------------------- Step 3 -------------------------------------------------- #
# This function uses the search_wikipedia function which looks for titles on a query/topic, then will return a summary from
# The Wikipedia page on that given topic. This can then be converted from the summary to text, then to engine.say.
def get_wikipedia_summary(query, lang='en'):
    wiki_lang = wikipediaapi.Wikipedia(language=lang, user_agent="PrismoBot/1.0 (jake.woodall@example.com)")

    # First, search for the best matching article
    best_matching_title = search_wikipedia(query, lang)

    # If we have a matching title, fetch its summary
    if best_matching_title:
        page = wiki_lang.page(best_matching_title)
        if page.exists():
            return page.summary

    return "I couldn't find information on that topic."
# ---------------------------------------------------- Step 4 -------------------------------------------------- #
# This function is responsible for speaking the transcribed summary from the function above.
def speak_wikipedia_result(summary, engine):
    sentences = summary.split('. ')
    for sentence in sentences:
        print(Style.BRIGHT + Fore.RED + "Prismo: " + Fore.RESET + Style.NORMAL + sentence)
        engine.say(sentence)
        engine.runAndWait()  # This is a blocking call

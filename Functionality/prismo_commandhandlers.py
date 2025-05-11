COMMAND_HANDLERS = []

from Applications.prismo_wikipedia import identify_wikipedia_query
from Applications.spotify import identify_spotify_query, SPOTIFY_PROMPTS

WIKIPEDIA_PROMPTS = ["what is", "tell me about", "who is", "who made"]

def handle_command(transcription):
    for handler in COMMAND_HANDLERS:
        if handler(transcription):
            break

def wikipedia_handler(transcription):
    if any(prompt in transcription for prompt in WIKIPEDIA_PROMPTS):
        identify_wikipedia_query(transcription)
        return True
    return False

def spotify_handler(transcription):
    return identify_spotify_query(transcription)

COMMAND_HANDLERS.append(wikipedia_handler)
COMMAND_HANDLERS.append(spotify_handler)
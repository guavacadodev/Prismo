print("You said:", transcription)  # Display the transcribed text

# Fetch API Key (better if stored securely or passed as an environment variable)
openai.api_key = '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'

# Send to OpenAI for a response
response = openai.Completion.create(engine="davinci",
                                    prompt="",
                                    max_tokens=45, temperature=0.2)
print("OpenAI responds:", response.choices[0].text.strip())
engine.say(response.choices[0].text.strip())
engine.runAndWait()
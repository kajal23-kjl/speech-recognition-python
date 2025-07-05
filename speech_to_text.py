import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile("sample_ml_audio.wav") as source:
    print("Listening...")
    audio = recognizer.record(source)

# Try to recognize speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio)
    print("Transcribed Text:")
    print(text)
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError as e:
    print(f"Request failed from Google API: {e}")

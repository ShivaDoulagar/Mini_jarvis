import speech_recognition as sr
import pyttsx3

# Initialize recognizer + TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen from microphone and return text"""
    with sr.Microphone() as source:
        print("🎤 Listening... Speak now!")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("⚠️ Sorry, I could not understand.")
        return None
    except sr.RequestError:
        print("❌ Speech recognition service error.")
        return None

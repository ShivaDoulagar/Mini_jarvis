import speech_recognition as sr
import pyttsx3
from core.llm import ask_llm   # your LLM function
import ast
from core.commands import run_command  

# Initialize recognizer (keep global)
recognizer = sr.Recognizer()

def speak(text: str):
    """Convert text to speech safely, sentence by sentence."""
    engine = pyttsx3.init()
    # Split into smaller chunks so pyttsx3 never hangs
    for chunk in text.split(". "):
        engine.say(chunk)
        engine.runAndWait()
    engine.stop()

def listen():
    """Listen from microphone and return recognized text."""
    with sr.Microphone() as source:
        print("🎤 Listening... Speak now!")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {query}")
        return query
    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand that.")
        # speak("Sorry, i couldn't understand")
        return None
    except sr.RequestError as e:
        print(f"⚠️ Error: {e}")
        return None

def clean_response(raw: str) -> str:
    """Cleans Ollama raw string so pyttsx3 can speak it safely"""
    try:
        # If Ollama wraps response in quotes
        raw = ast.literal_eval(raw)
    except Exception:
        raw = raw.strip()

    # Ensure no outer quotes
    if raw.startswith('"') and raw.endswith('"'):
        raw = raw[1:-1]

    # Replace escaped newlines with spaces
    cleaned = raw.replace("\\n", " ").replace("\n", " ")

    # Optional: shorten very long responses for speech
    if len(cleaned) > 400:
        cleaned = cleaned[:400] + " ..."

    return cleaned

if __name__ == "__main__":
    speak("Hello Shiva, I am JARVIS. How can I help you today?")
    while True:
        query = listen()
        if query:
            # First, check if it is a system command
            response = run_command(query)
            if response:
                print(f"⚡ Command executed: {response}")
                speak(response)
                continue  # Skip LLM, since we handled it

            # Otherwise, send to LLM
            print("⚡ Sending to LLM...")
            answer = ask_llm(query)
            print(f"🤖 JARVIS raw: {answer!r}")

            answer = clean_response(answer)
            print(f"🔊 Cleaned Answer: {answer!r}")

            if answer:
                speak(answer)
            else:
                speak("Sorry, I could not generate a response.")
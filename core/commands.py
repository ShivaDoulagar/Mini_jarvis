import os
import pyautogui
import webbrowser
import datetime
import subprocess

def run_command(command: str) -> str | None:
    """
    Execute system-level commands based on user voice input.
    Returns a response string if a command is executed,
    otherwise returns None (so the query can go to LLM).
    """

    command = command.lower()

    if "open notepad" in command:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad"

    elif "close notepad" in command:
        os.system("taskkill /f /im notepad.exe")
        return "Notepad closed"

    elif "open chrome" in command:
        subprocess.Popen(["chrome.exe"])
        return "Opening Google Chrome"

    elif "close chrome" in command:
        os.system("taskkill /f /im chrome.exe")
        return "Chrome closed"

    elif "screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        return "Screenshot saved as screenshot.png"

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open brave" in command:
        subprocess.Popen(["brave.exe"])
        return "Opening Brave"

    elif "close brave" in command:
        os.system("taskkill /f /im brave.exe")
        return "Brave closed"

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}"

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today}"

    return None

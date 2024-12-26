import speech_recognition as sr
import pywhatkit
import pyttsx3

def speech(text):
    """Converts text to speech."""
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_for_wake_word():
    """Listens for wake words 'jarvis' or 'Hey jarvis'."""
    recorder = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recorder.listen(source)
                wake_text = recorder.recognize_google(audio).lower()
                if "jarvis" in wake_text or "hay jarvis" in wake_text:
                    speech("\tHow may I help you?")
                    return
        except sr.UnknownValueError:
            pass  # Ignore unintelligible speech
        except sr.RequestError:
            speech("There seems to be a problem with the Google service.")
            break

def get_command():
    """Gets the user's command after the wake word is detected."""
    recorder = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            speech("Listening for your command...")
            audio = recorder.listen(source)
            command_text = recorder.recognize_google(audio).lower()
            print(f"Command received: {command_text}")
            return command_text
    except sr.UnknownValueError:
        speech("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError:
        speech("There seems to be a problem with the Google service.")
    return ""

def handle_command(command):
    """Handles the recognized command."""
    if "youtube" in command:
        speech("\tOk, I will search on YouTube.")
        pywhatkit.playonyt(command)
    elif "you are welcome" in command:
        speech("\tThanks for creating me!")
    elif command:
        speech("\tSearching on Google...")
        pywhatkit.search(command)
    else:
        speech("I didn't understand that. Please try again.")

if __name__ == "__main__":
    while True:
        listen_for_wake_word()
        command = get_command()
        handle_command(command)

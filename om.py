import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for a command and recognize it."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Could not request results; check your network connection.")
        return None

def open_browser(url):
    """Open a specified URL in a chosen web browser."""
    browser_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Change to your browser

    try:
        webbrowser.get(browser_path).open(url)
        #speak(f"Opening {url}")
    except webbrowser.Error:
        speak("Sorry, I couldn't open the browser.")

def main():
    speak("Hello! I am Meera. How can I help you, sir?")
    while True:
        command = take_command()
        if command:
            command = command.lower()

            # Exit the assistant
            if "exit" in command or "stop" in command:
                speak("Goodbye, have a nice day, sir!")
                break

            # Respond to greetings
            elif "hello Meera" in command or "hi" in command:
                speak("Hello! How can I assist you?")

            # Tell the current time
            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")

            # Open a website
            elif "open" in command:
                search_term = command.replace("open", "").strip()
                open_browser(f"https://{search_term}.com")

            # Google search
            elif "search" in command:
                search_query = command.replace("search", "").strip()
                open_browser(f"https://www.google.com/search?q={search_query}")

            # Search Wikipedia
            elif "wikipedia" in command:
                query = command.replace("wikipedia", "").strip()
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak(result)
                except wikipedia.exceptions.DisambiguationError:
                    speak("There are multiple results for that, please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak("I could not find any information on that topic.")
                except Exception:
                    speak("Sorry, I could not fetch that information.")

            # Default response for unrecognized commands
            else:
                speak("I'm sorry, I can't do that yet.")

if __name__ == "__main__":
    main()

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except sr.UnknownValueError:
            speak("Sorry, I could not understand. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Sorry, speech service is not available.")
            return ""

        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""


def voice_assistant():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! Nice to meet you.")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}.")

        elif "search" in command:
            search_query = command.replace("search", "").strip()

            if search_query:
                speak(f"Searching for {search_query}")
                url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
                webbrowser.open(url)
            else:
                speak("Please tell me what you want to search.")

        elif "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command:
            speak("Sorry, I don't know that command yet.")


if __name__ == "__main__":
    voice_assistant()
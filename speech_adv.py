import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print(e)
            speak("Sorry, I didn't quite catch that.")
            return None

def main():
    while True:
        query = listen()
        if query is None:
            continue

        if 'hello' in query.lower():
            speak("Hi! How can I help you today?")

        elif 'time' in query.lower():
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif 'date' in query.lower():
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"The current date is {current_date}")

    
        elif 'open' in query.lower():
            url = query.split(' ')[-1]
            webbrowser.open(url)
            speak(f"Opening {url}")

        elif 'launch' in query.lower():
            app = query.split(' ')[-1]
            if app == 'chrome':
                os.system('start chrome')
            elif app == 'notepad':
                os.system('start notepad')
            speak(f"Launching {app}")

        elif 'tell me about' in query.lower():
            topic = query.split(' ')[-1]
            info = wikipedia.summary(topic, sentences=2)
            speak(info)

        elif 'weather' in query.lower():
            city = query.split(' ')[-1]
            url = f"https://www.google.com/search?q=weather+{city}"
            webbrowser.open(url)
            speak(f"Showing weather for {city}")

        elif 'news' in query.lower():
            url = "https://www.google.com/news"
            webbrowser.open(url)
            speak("Showing latest news")

if __name__ == "__main__":
    main()
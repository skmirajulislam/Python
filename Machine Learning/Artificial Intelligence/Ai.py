import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from datetime import date
from sketchpy import library as lib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("good evening!")

    speak("I am your personal AI steve sir. please tell me how can i help you")


def takeCommand():
    # it takes microphone input form the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"

    return query


if __name__ == "__main__":

    wishme()
    while True:
        
        query = takeCommand().lower() # type: ignore
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("Wikipidia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia ")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("write which one")
            n = int(input("Enter "))
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strTime}")

        elif 'the date' in query:
            today = date.today()
            speak(f"today is {today}")

        elif 'open visual studio' in query:
            codePath = "C:\\Users\\Sk Miraj\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'open compiler' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Embarcadero Dev-C++"
            os.startfile(codePath)

        elif 'draw tom holland' in query:
            obj = lib.tom_holland()
            obj.draw()

        elif 'draw tony' in query:
            obj = lib.rdj()
            obj.draw()

        elif 'draw missile man' in query:
            obj = lib.apj()
            obj.draw()

        elif 'draw flag' in query:
            obj = lib.flag()
            obj.draw()

        elif 'hello' in query:
            speak("hi sir")

        elif 'who is your developer' in query:
            speak("sir i am an artificial intelligent , developed by sk miraj")

        elif 'did you hear' in query:
            speak("No worries , i'am here to help , say ")

        elif 'thank you' in query:
            speak("Welcome sir i am happy to serve it ")

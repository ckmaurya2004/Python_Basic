import pyttsx3
import  datetime
import  speech_recognition as sr
import  wikipedia
import  webbrowser
import  os
import  pyjokes
import  random

list = ['haa','yes','hu','ahan']
choice = random.choice(list)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! ")
    elif hour >=12  and hour < 18:
        speak("Good Afternoon!  ")
    else:
        speak("Good Evening!")
    speak("hello miss kiran ! I am your friend Please tell me may I help You ")

def takeComand():
    """ It take microphone input from user and return string output"""
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listing....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)

        print("Say that again Please!..")
        return  "None"
    return  query


if __name__ == '__main__':

    wishMe()
    while True:
        query = takeComand().lower()
        # logic  for executing tasks based on query
        if 'wikipedia' in query:
            speak(("Searchiing Wikipedia ..."))
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            print("According to wikipedia")
            # print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif' play song' in query:
           music_dir = "D:\Kiran\Music"
           song = os.listdir((music_dir))
           print(song)
           os.startfile(os.path.join(music_dir,song[0]))

        elif 'what the time' in query:
            time = datetime.datetime.now().strftime('%h%m%S')
            speak(time)
        elif '  joke' in query:
            joke_1 = pyjokes.get_joke(language="en",category='neutral')
            # print(joke_1)
            speak(joke_1)
        elif 'open pycharm ' in query:
           os.startfile(r'C:\\Users\\Kiran\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains')
            # os.startfile(dirs)
        elif 'what your name' in query:
            speak(" I am zera")
        elif 'listen' in query:
            speak(choice)

        elif 'exit'in query:
            speak("thank you")
            break









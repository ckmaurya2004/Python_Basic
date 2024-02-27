import pyttsx3

engine = pyttsx3.init('dummy') # used to take voice defaults in your system
voices = engine.getProperty('voices')
# print(voices[0])



engine.setProperty('voice', voices[1].id )

engine.say('I\'m a little teapot...')

engine.runAndWait()
# engine.setProperty('voices', voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# if __name__ == '__main__':
#     speak("hello i  am kiran")
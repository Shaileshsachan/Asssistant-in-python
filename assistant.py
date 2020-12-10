import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia
import pyjokes

engine = pyttsx3.init()
listener = sr.Recognizer()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'yogesh' in command:
                command = command.replace('yogesh', '')
                print(command)
    except:
        pass
    return command

def run_yogesh():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'jokes' in command:
        (pyjokes.get_joke())
    else:
        talk('Please say the command again')



while True:
    run_yogesh()
import speech_recognition as speech
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import randfacts
import quote_generator
import os


listener = speech.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)
engine.setProperty('rate', 130)


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('Hi, I am Eva. How may I help you today?')


def take_command():
    try:
        with speech.Microphone() as uservoice:
            print("Listening...")
            voice = listener.listen(uservoice)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'eva' in command:
                command = command.replace('eva', '')
    except:
        pass
    return command


# def run_eva():

while True:
    command = take_command()
    if 'hello' in command:
        talk('Hi, what can I help you with')
    elif 'how am i' in command:
        talk('You are a very nice and sweet person')
    elif 'how are you' in command:
        talk('I am fine thank you. How are you?')
    elif 'what is your name' in command:
        talk('My name is Eva')
    elif 'i am fine' in command:
        talk('Great')
    elif 'age' in command:
        talk('I was not born. I was created a few hours ago.')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        talk('The current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        talk(info)
    elif 'love you' in command:
        talk('I love you too')
    elif 'love me' in command:
        talk('Yes, you are an amazing friend')
    elif 'joke' in command:
        talk('Here is a funny joke')
        joke = pyjokes.get_joke('en', 'neutral')
        print(joke)
        talk(joke)
    elif 'search' in command:
        term = command.replace('search', '')
        talk('Searching ' + term)
        pywhatkit.search(term)
    elif 'open' in command:
        app = command.replace('open', '')
        talk('Opening' + app)
        os.system(app)
    elif 'fact' in command:
        talk('Here is an interesting fact')
        fact = randfacts.get_fact()
        print(fact)
        talk(fact)
    elif 'bye' in command:
        talk('Bye. It was nice talking to you')
        exit()
    else:
        talk("Pardon me")

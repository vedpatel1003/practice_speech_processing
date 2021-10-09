import datetime
import pyttsx3
import pywhatkit
import speech_recognition as sr
import pyjokes
import wikipedia

use_female_voice = True
if use_female_voice:
    voice = 1
else:
    voice = 0


listener = sr.Recognizer
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[voice].id)

print(sr.Microphone.list_microphone_names())
command = "where is Vadodara"


def start_alexa():
    engine.say("What can I do for you?, I'm your virtual assistant!!")
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone(device_index=1) as source:
            print('listening...')
            print(source.device_index)
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source, timeout=50)
            print("voice: ", voice)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            return command
    except:
        print("Something wrong!")
        pass


def run_alexa():
    start_alexa()

    # TODO: get command using microphone. Currently hard-coding command.
    # command = take_command()
    talk(command)

    if command is None:
        return

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(topic=song, use_api=True)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %P')
        talk('current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in command:
        item = command.replace('what is', '')
        try:
            info = wikipedia.summary(item, 1)
            print(info)
            talk(info)
        except:
            talk("Try using some other word")

    elif "where is " in command:
        item = command.replace('where is', '')
        try:
            info = wikipedia.summary(item, 2)
            print(info)
            talk(info)
        except:
            talk("Try using some other word")

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        joke_data = pyjokes.get_joke()
        print(joke_data)
        talk(joke_data)

run_alexa()

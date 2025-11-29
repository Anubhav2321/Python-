
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
from tkinter import messagebox

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Talk function
def talk(text):
    engine.say(text)
    engine.runAndWait()
    status_label.config(text=text)

# Take command from mic
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...")
            app.update()
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"Command: {command}")
    except Exception as e:
        status_label.config(text="Sorry, I didn't catch that.")
    return command

# Run assistant
def run_alexa():
    command = take_command()
    if not command:
        return

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'what time is it' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command or 'who is' in command:
        person = command.replace('who is', '').replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif 'date' in command:
        talk('Sorry, I have a headache.')

    elif 'are you single' in command:
        talk('I am in a relationship with Wi-Fi.')

    elif 'stop' in command or 'exit' in command:
        talk('Goodbye!')
        app.quit()

    else:
        talk('Please say the command again.')

# --- GUI Part ---
app = tk.Tk()
app.title("Voice Assistant")
app.geometry("400x300")
app.resizable(False, False)

title_label = tk.Label(app, text="🎙 Alexa-Like Voice Assistant", font=("Arial", 16))
title_label.pack(pady=20)

status_label = tk.Label(app, text="Click below to start listening...", font=("Arial", 12))
status_label.pack(pady=10)

listen_btn = tk.Button(app, text="Start Listening", font=("Arial", 14), command=run_alexa)
listen_btn.pack(pady=20)

exit_btn = tk.Button(app, text="Exit", font=("Arial", 12), command=app.quit)
exit_btn.pack(pady=10)

app.mainloop()



# Output ------> 
#   listening....
# command: play some music
#command: what time is it
#command: who is Albert Einstein
#command: tell me a joke
#command: date
#command: are you single
#command: stop
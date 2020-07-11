import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

nome = "Drilon"
print("Initializing Poncho")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Buongiorno "+nome)

    elif hour >= 12 and hour<18:
        speak("Buon pomeriggio "+nome)

    else:
        speak("Buonasera "+nome)

    speak("Come posso aiutarti?")



speak("Ciao "+nome+", sono Poncio")


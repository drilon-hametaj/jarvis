import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


NOME = "Drilon"
print("Initializing Poncho")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Will speak by current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Buongiorno "+NOME)

    elif hour >= 12 and hour<18:
        speak("Buon pomeriggio "+NOME)

    else:
        speak("Buonasera "+NOME)

    #speak("Come posso aiutarti?")


# Main program starts here
# this funciton will take command from the microphone
def takeCommand():
    query = None
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sto ascoltando...")
        r.adjust_for_ambient_noise(source) #remove ambient noise
        audio = r.listen(source)

    try:
        print("Riconoscendo...")
        query = r.recognize_google(audio, language='it-IT')
        print(f"l'utente ha detto: {query}\n")

    except Exception as e:
        print("Say that again please")


    return query




wishMe()
request = takeCommand()

#Logic for executing task
if 'su wikipedia' in request.lower():
    speak('Sto cercando su Wikipedia...')
    request = request.replace("su wikipedia", "")
    request = request.replace("cerca", "")
    results = wikipedia.summary(request, sentences=2)
    speak(results)

elif 'su youtube' in request.lower():
    speak('Sto cercando su YouTube...')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://youtube.com')
    time.sleep(5)
    request = request.lower()
    request = request.replace("su youtube", "")
    request = request.replace("cerca", "")
    request = request.replace("riproduci", "")
    driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input').send_keys(request)
    driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button').click()
    speak('Ecco a te... '+request + 'su Youtube...')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]').click()



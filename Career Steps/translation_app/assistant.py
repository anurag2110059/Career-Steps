import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import requests
import subprocess
import random
import pyjokes
from urllib.request import urlopen
import openai
import winshell
openai.api_key = "YOUR_API_KEY"

api_key = "60e9d31fdb19246d7ee5d3b9b7ae91d5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Your Assistant. How May I Help You?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        print(".....Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Ok, here are the results")
        query = r.recognize_google(audio, language="en-in")
        print(f"Aapne kaha: {query}\n")

        if 'chatgpt' in query:
            speak("Let me think...")
            chatgpt_response = get_chatbot_response(query)  # Call the ChatGPT function here
            print("Assistant: " + chatgpt_response)
            speak(chatgpt_response)
        else:
            return query

    except Exception as e:
        speak("Try again, please")
        return "none"

    return query


def get_chatbot_response(message):
    prompt = "User: " + message + "\nAssistant:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    reply = response.choices[0].text.strip().split("Assistant: ")[-1]
    return reply


if __name__ == "__main__":
    speak("Welcome to Career Steps")
    wishMe()
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=20)
            
            speak("Here it is ")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'akash vishwakarma' in query:
            speak("Ask from  She better known him")
        elif 'mother' in query:
            speak("anu bhadouria")
        elif 'sister' in query:
            speak("deepshi and deepika and pooja")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")
        elif "my name is" in query or "what is my name" in query or "who am i" in query:
            speak("What should I call you, sir?")
            uname = takeCommand()
            speak("Welcome, Mister " + uname)
            print(uname)
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
        elif 'search' in query or 'find' in query:
            query = query.replace("search", "")
            query = query.replace("find", "")
            webbrowser.open(query)
        elif 'news' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=YOUR_API_KEY''')
                data = json.load(jsonObj)
                i = 1
                speak('Here are some top news from The Times of India')
                print('''=============== TIMES OF INDIA ============''' + '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))
        elif 'lock window' in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak("Hold on a sec! Your system is on its way to shut down")
            subprocess.call('shutdown /p /f')
        elif 'play music' in query:
            music_dir = "C:\\Users\\mrc42\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Oh! The time is {strtime}")
        elif 'open vs code' in query:
            code_path = "C:\\Users\\mrc42\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'open photos' in query:
            code_path = "C:\\Users\\mrc42\\OneDrive\\Pictures"
            os.startfile(code_path)
        elif 'weather of' in query:
            speak("Tell your city name, please")
            city = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] == 404:
                speak("We encountered some problem, please try again later")
            else:
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("Temperature is " + str(current_temperature))
                speak("Atmospheric pressure is " + str(current_pressure))
                speak("Humidity is " + str(current_humidity))
                speak("Description: " + str(weather_description))
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin recycled")
        elif 'predict' in query:
             webbrowser.open("http://127.0.0.1:8000/predictor")
        elif 'interest' in query:
             webbrowser.open("http://127.0.0.1:8000/predict_career")
        elif 'future' in query:
             webbrowser.open("http://127.0.0.1:8000/future")  
        elif 'join' in query:
             webbrowser.open("http://127.0.0.1:8000/index2")
        elif 'experts' in query:
             webbrowser.open("http://127.0.0.1:8000/courses")


        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

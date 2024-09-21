from flask import Flask, render_template, request
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

app = Flask(__name__)

# Initialize pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # Female voice (0 for male)
def speak(text):
    with lock:
        engine.say(text)
        engine.runAndWait()
def speak(audio):
    """Speak function using pyttsx3."""
    engine.say(audio)
    engine.runAndWait()

@app.route('/')
def index():
    """Render the home page where commands are entered."""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """Process the voice command input from the web form."""
    command = request.form['command']
    query = command.lower()

    if 'wikipedia' in query:
        speak("Searching Wikipedia ...")
        query = query.replace("wikipedia", '')
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        return f"According to Wikipedia: {results}"

    elif 'are you' in query:
        response = "I am PJ, developed by Rajkamal Singh."
        speak(response)
        return response

    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return "YouTube opened."

    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return "Google opened."

    elif 'open github' in query:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")
        return "GitHub opened."

    elif 'open stackoverflow' in query:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")
        return "Stack Overflow opened."

    elif 'open spotify' in query:
        speak("Opening Spotify")
        webbrowser.open("https://spotify.com")
        return "Spotify opened."

    elif 'open whatsapp' in query:
        speak("Opening WhatsApp")
        loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(loc)
        return "WhatsApp opened."

    elif 'play music' in query:
        speak("Playing music on Spotify")
        webbrowser.open("https://spotify.com")
        return "Spotify opened."

    elif 'local disk d' in query:
        speak("Opening local disk D")
        webbrowser.open("D://")
        return "Local disk D opened."

    elif 'local disk c' in query:
        speak("Opening local disk C")
        webbrowser.open("C://")
        return "Local disk C opened."

    elif 'local disk e' in query:
        speak("Opening local disk E")
        webbrowser.open("E://")
        return "Local disk E opened."

    elif 'sleep' in query:
        speak("Goodbye!")
        exit(0)

    return "Sorry, I didn't understand that."

if __name__ == '__main__':
    speak("PJ Assistance activated. How can I help you?")
    app.run(debug=True)

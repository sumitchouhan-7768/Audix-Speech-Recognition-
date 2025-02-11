import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pw
import joblib

listening = sr.Recognizer()
engine = pt.init()

def save_objects():
    joblib.dump(listening, 'listening_model.pkl')
    

def speak(text):
    engine.say(text)
    engine.runAndWait()


def hear():
    cmd = ''  # Ensure cmd is defined to avoid potential issues
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            audio = listening.listen(mic)
            cmd = listening.recognize_google(audio)
            cmd = cmd.lower()
            if 'audix' in cmd:
                cmd = cmd.replace('audix', '')
                print(cmd)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        speak("Speech service is down. Please try again later.")
    
    return cmd

def run():
    cmd = hear()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        speak('Playing ' + song)
        pw.playonyt(song)  # Corrected playonyt function input
    else:
        speak("Sorry, I didn't understand the command.")

save_objects()

run()

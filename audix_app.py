import streamlit as st
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pw
import joblib

# Page config
st.set_page_config(page_title="Audix Speech Recognition", page_icon="🎤")

# Title and description
st.title("Audix Speech Assistant")
st.write("Click the button below and speak your command. Say 'Audix' followed by your command.")

# Initialize recognizer and text-to-speech engine
listening = sr.Recognizer()
engine = pt.init()

# Save engine configuration using joblib
def save_engine():
    joblib.dump(engine, 'engine_model.pkl')
    st.success("Engine configuration saved successfully!")

# Load engine configuration from pickle file
def load_engine():
    try:
        engine = joblib.load('engine_model.pkl')
        st.success("Engine configuration loaded successfully!")
    except FileNotFoundError:
        st.warning("Engine configuration file not found, using default settings.")
        engine = pt.init()
    return engine

def speak(text):
    engine.say(text)
    if not engine.isBusy():
        engine.runAndWait()
    return text

def hear():
    cmd = ''
    try:
        with sr.Microphone() as mic:
            st.info("Listening...")
            audio = listening.listen(mic)
            cmd = listening.recognize_google(audio)
            cmd = cmd.lower()
            if 'audix' in cmd:
                cmd = cmd.replace('audix', '')
                st.success(f"You said: {cmd}")
    except sr.UnknownValueError:
        st.error("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        st.error("Speech service is down. Please try again later.")
        speak("Speech service is down. Please try again later.")
    
    return cmd

def process_command(cmd):
    if 'play' in cmd:
        song = cmd.replace('play', '')
        message = f'Playing {song}'
        st.success(message)
        speak(message + song)
        pw.playonyt(song)
    else:
        message = "Sorry, I didn't understand the command."
        st.warning(message)
        speak(message)

# Main interface
col1, col2 = st.columns([3,1])

with col1:
    if st.button("🎤 Click to Speak", use_container_width=True):
        command = hear()
        if command:
            process_command(command)

with col2:
    if st.button("❌ Stop", use_container_width=True):
        st.stop()

# Save or load engine configuration on button click
with col1:
    if st.button("💾 Save Engine Configuration", use_container_width=True):
        save_engine()

with col2:
    if st.button("🔄 Load Engine Configuration", use_container_width=True):
        engine = load_engine()

# Instructions
st.markdown("""
### Available Commands:
- Say "Audix play [song name]" to play a song on YouTube
- More commands coming soon!
""")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Sumit")

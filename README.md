# Audix Speech Recognition 🎤

Audix is a Python-based speech recognition assistant that allows you to control your computer using voice commands. It uses the `speech_recognition` library to listen to your voice and the `pyttsx3` library to respond with text-to-speech. You can also play songs on YouTube using the `pywhatkit` library.

---

## Features ✨

- **Voice Command Recognition**: Audix listens for the keyword "Audix" followed by a command.
- **Text-to-Speech**: Audix responds to your commands using text-to-speech.
- **Play Songs on YouTube**: Say "Audix play [song name]" to play a song on YouTube.
- **Save and Load Configuration**: Save and load the speech recognition engine configuration using `joblib`.

---

## Installation 🛠️

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sumitchouhan-7768/audix-speech-recognition.git
   cd audix-speech-recognition
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.7 or higher installed. Then, install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the dependencies manually:
   ```bash
   pip install streamlit speechrecognition pyttsx3 pywhatkit joblib
   ```

3. **Run the Application**:
   - For the **Streamlit App**:
     ```bash
     streamlit run app.py
     ```
   - For the **Standalone Script**:
     ```bash
     python audix.py
     ```

---

## Usage 🚀

### Streamlit App
1. Open the app in your browser.
2. Click the **🎤 Click to Speak** button and say "Audix" followed by your command.
3. Available commands:
   - **Play a song**: Say "Audix play [song name]" to play a song on YouTube.
   - More commands coming soon!

### Standalone Script
1. Run the script using `python audix.py`.
2. Speak your command after the prompt "Listening...".
3. Audix will process your command and respond accordingly.

---

## Commands 🗣️

| Command               | Description                                  |
|-----------------------|----------------------------------------------|
| `Audix play [song]`   | Plays the song on YouTube.         |
| More commands soon!   | Stay tuned for updates.                      |

---

## File Structure 📂

```
audix-speech-recognition/
├── app.py                  # Streamlit app for Audix
├── audix.py                # Standalone script for Audix
├── requirements.txt        # List of dependencies
├── engine_model.pkl        # Saved engine configuration (optional)
├── listening_model.pkl     # Saved recognizer configuration (optional)
└── README.md               # This file
```

---

## Contributing 🤝

Contributions are welcome! If you'd like to add new features, fix bugs, or improve the code, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m "Add some feature"`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Made with ❤️ by Sumit Chouhan

---

Let me know if you'd like to add or modify anything in the README! 😊

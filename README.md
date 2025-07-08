# Meera.AI
Meera is a lightweight, voice-activated desktop assistant built using Python. It integrates speech recognition, text-to-speech, Wikipedia querying, and web search capabilities to provide a hands-free interaction experience.

✨Features
- 🔊 Text-to-Speech (TTS): Meera speaks responses using the pyttsx3 engine.
- 🎤 Speech Recognition: Understands spoken commands using Google Speech Recognition via speech_recognition.
- ⏰ Tell Time: Announces the current system time.
- 🌐 Web Access: Opens websites or performs Google searches through Chrome.
- 📚 Wikipedia Search: Summarizes queries using Wikipedia.
- 👋 Conversational Flow: Responds to greetings and exits on user command.
- 
🛠️ Technologies Used
- pyttsx3: Offline TTS engine for speaking responses
- speech_recognition: Captures and converts audio input to text
- wikipedia: Searches and retrieves information
- webbrowser: Opens URLs in the default web browser
- datetime: Fetches current time details
- os: Base module for future enhancements (currently unused)
- 
🚀 How It Works
- Launches with a voice greeting from Meera.
- Continuously listens for commands like:
- "search machine learning"
- "open github"
- "what's the time"
- "wikipedia Alan Turing"
- "stop"
- Executes voice-activated tasks accordingly.
- 
📌 Note
- Tested on Windows using Chrome (update browser_path as needed).
- Requires microphone access for voice commands.



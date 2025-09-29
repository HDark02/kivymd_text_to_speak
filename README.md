---

# Audio Conversion App

This app is built using **KivyMD** and **gTTS (Google Text-to-Speech)** to convert text into audio files. Users can enter text, choose the language and speed of speech, and save the audio file for later use. Additionally, it supports playing and removing saved audio files, and offers integration with ads through **Kivmob**. 

## Features:
- **Text to Speech Conversion:** Convert entered text into an audio file.
- **Customizable Audio:** Select language, speed, and file name for the audio.
- **Audio Management:** Play, remove, and view saved audio files.
- **Ads Integration:** Integrated banner ads using Kivmob (optional).
- **Contact Us:** Contact the developers via a link to a Telegram channel.

## Installation:
To use this app, you need to install the following dependencies:

1. **Python** (version 3.7 or higher)
2. **KivyMD** for the UI components
3. **gTTS** for Google Text-to-Speech conversion
4. **pyttsx3** for offline text-to-speech conversion
5. **Plyer** for file system interaction (if using file operations)
6. **Kivmob** for ads (optional)

You can install the required dependencies using pip:

```bash
pip install kivymd gTTS pyttsx3 kivmob plyer
```

## Usage:

1. **Running the App:**
   - After installing the dependencies, run the script by executing:
   ```bash
   python app_name.py
   ```
   
2. **Convert Text to Audio:**
   - Enter text into the provided input field.
   - Choose the desired language (e.g., English, French).
   - Select the speed of speech (slow or fast).
   - Provide a name for the audio file.
   - Press "Save" to convert the text into an audio file.

3. **View Saved Audio Files:**
   - Navigate to the audio list to view the saved audio files.
   - You can play or remove saved audio files from the list.

4. **Contact Us:**
   - Use the "Contact Us" button to open a page where you can reach the developers via Telegram.

## How It Works:

The app uses the **gTTS (Google Text-to-Speech)** library for text-to-speech conversion. If the network is unavailable, the app falls back to the **pyttsx3** library for offline text-to-speech. The audio files are saved with the user-specified name and can be played back directly from the app.

The app also integrates **Kivmob** for displaying banner ads, which can be hidden or shown based on app states (e.g., on pause, on resume).

## File Structure:

- **app_name.py:** Main Python file containing the app's logic.
- **acceuil_1.kv:** Kivy layout file for the welcome screen.
- **enter_text.kv:** Kivy layout file for the text-to-speech input screen.
- **about_us.kv:** Kivy layout file for the "About Us" screen.
- **folder_list.kv:** Kivy layout file for listing saved audio files.

## Screens:

1. **Welcome Screen:** Displays a welcoming message and options to navigate to other sections.
2. **Text-to-Speech Screen:** Allows the user to input text, choose language, speed, and name the audio file.
3. **Audio Folder List:** Displays a list of all saved audio files and allows playing or removing them.
4. **About Us Screen:** Displays information about the app and a contact option for developers.

## Contact Us:

- For any issues or feedback, please contact the developer via Telegram: [@Thekingdynamo](https://t.me/Thekingdynamo).

---

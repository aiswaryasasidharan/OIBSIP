# Voice Assistant – Python

## Project Overview

This project is a simple Python-based Voice Assistant developed as part of the Oasis Infobyte Python Programming Internship.

The voice assistant listens to spoken commands through the microphone and responds using text-to-speech.

## Features

* Voice input using microphone
* Responds to "Hello"
* Tells the current time
* Tells the current date
* Performs Google searches
* Provides voice feedback using text-to-speech
* Handles speech recognition errors
* Supports exit commands such as "bye" and "stop"

## Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* datetime
* webbrowser

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command:

```bash
python voice_assistant.py
```

Speak clearly into the microphone when the assistant says "Listening...".

## Example Commands

* "Hello"
* "What is the time?"
* "What is today's date?"
* "Search Python Django"
* "Bye"

## Project Structure

```text
Python-Beginner-Task1-VoiceAssistant/
│
├── voice_assistant.py
├── requirements.txt
└── README.md
```

## Privacy Note

This project uses microphone input for speech recognition. Voice input is processed through the speech recognition service used by the `SpeechRecognition` library. Users should be aware of the network service involved when using voice recognition.

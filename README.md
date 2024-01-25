# Speech Recognition and Text Replacement Script

## Overview:

This Python script utilizes the SpeechRecognition library to continuously listen to the user's speech using a microphone. The recognized speech is then transcribed using Google Speech Recognition and saved to a text file named "speechRec.txt". The script runs until the user says "stop," at which point it terminates. Additionally, the script performs word replacements on the transcribed text based on a predefined dictionary.

## Dependencies:

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): A Python library for working with speech recognition APIs.
- [pyaudio](https://pypi.org/project/PyAudio/): Required by SpeechRecognition to work with microphones.

You can install these dependencies using the following commands:



pip install SpeechRecognition
pip install pyaudio


## Usage:

Run the script using Python:
python speech.py

The script will prompt you to start speaking. It continuously listens to your speech and transcribes it into text.

To stop the script, say "stop." The program will terminate, and the recognized speech will be saved to "speechRec.txt."








## Word Replacements:

The script includes a word replacement feature where certain words are replaced with predefined alternatives. The replacement dictionary is defined in the script and can be customized according to your needs.


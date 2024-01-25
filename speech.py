import speech_recognition

recognizer = speech_recognition.Recognizer()


def replace_words(text, replacement_dict):
    for old_word, new_word in replacement_dict.items():
        text = text.replace(old_word, new_word)
    return text


with open("speechRec.txt", "w") as file:
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"recognized: {text}")

                if "stop" in text:
                    print("Stopping the program as per user request.")
                    break

                # Write the recognized text to the file
                file.write(f"{text}\n")

        except speech_recognition.UnknownValueError:
            continue
        except speech_recognition.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break


replacement_dict = {
    "all": "*",
    "equal": "=",
    
    



    # Add more word replacements as needed
}

# Open the text file in read mode
with open("speechRec.txt", "r") as file:
    # Read the existing content
    lines = file.readlines()

# Apply word replacements to the text
modified_lines = [replace_words(line, replacement_dict) for line in lines]

# Open the same text file in write mode to overwrite the content
with open("speechRec.txt", "w") as file:
    # Write the modified content back to the file
    file.writelines(modified_lines)

print("Word replacements applied successfully.")

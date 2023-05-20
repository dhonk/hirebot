import os
import speech_recognition as sr

def transcribe_audio(file_path):
    r = sr.Recognizer()

    # Convert MP3 to WAV using FFmpeg
    wav_path = os.path.splitext(file_path)[0] + ".wav"
    os.system(f"ffmpeg -i {file_path} -vn -ar 44100 -ac 1 -f wav {wav_path}")

    # Transcribe the WAV file
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return None

def text():
    file_path = input("Enter the path to the MP3 file: ")

    if not os.path.isfile(file_path):
        print("Invalid file path.")
        return

    text = transcribe_audio(file_path)

    if text:
        print("Transcribed text:", text)

    return text

if __name__ == "__main__":
    pass

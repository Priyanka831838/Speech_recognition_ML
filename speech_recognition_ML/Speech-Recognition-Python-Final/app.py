from flask import Flask, render_template, request, redirect
import os
from moviepy.editor import AudioFileClip
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            mp3_file = "temp.mp3"
            file.save(mp3_file)

            wav_file = "temp.wav"
            clip = AudioFileClip(mp3_file)
            clip.write_audiofile(wav_file)

            
            recognizer = sr.Recognizer()
            with sr.AudioFile(wav_file) as source:
                audio = recognizer.record(source)
            transcript = recognizer.recognize_google(audio)

            
            os.remove(mp3_file)
            os.remove(wav_file)

    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

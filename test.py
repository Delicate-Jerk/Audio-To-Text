from flask import Flask, request, jsonify
import speech_recognition as sr
import subprocess
import os

app = Flask(__name__)

output_file_path = 'haha/single_file.wav'

@app.route('/audioToText', methods=['POST'])
def audio_to_text():
    uploaded_file = request.files['file']
    temp_file_path = 'hehe/temp_file.ogg'
    uploaded_file.save(temp_file_path)

    convert_audio_to_wav(temp_file_path, output_file_path)

    try:
        question1 = process_audio_file(output_file_path)
        return jsonify({
            'question': question1
        })
    except sr.UnknownValueError:
        return jsonify({
            'error': 'Speech recognition could not understand the audio'
        })

def process_audio_file(file_path):
    r = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)

    return text

def convert_audio_to_wav(input_file, output_file):
    subprocess.run(['/Users/arshitarora/Downloads/ffmpeg', '-y', '-i', input_file, '-acodec', 'pcm_s16le', '-ar', '44100', output_file])


if __name__ == '__main__':
    app.run(debug=True)

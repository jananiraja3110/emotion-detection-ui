# app.py
import os
from flask import Flask, render_template, request
from video_emotion import detect_video_emotion_file
from text_emotion import predict_text_emotion
from audio_emotion import predict_audio_emotion
from fusion_emotion import fusion_emotion_result

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    video_path = None
    if request.method == 'POST' and 'video' in request.files:
        video = request.files['video']
        if video:
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
            video.save(video_path)

            output_path = os.path.join(app.config['UPLOAD_FOLDER'], "output.avi")
            detect_video_emotion_file(video_path, output_path)
            return render_template("index.html", video_path="output.avi")
    return render_template("index.html", video_path=None)

@app.route('/text', methods=['POST'])
def text_emotion():
    text = request.form['text_input']
    emotion = predict_text_emotion(text)
    return f"<h2>Predicted Text Emotion: {emotion}</h2><br><a href='/'>Back</a>"

@app.route('/audio', methods=['POST'])
def audio_emotion():
    audio = request.files['audio']
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio.filename)
    audio.save(audio_path)
    emotion = predict_audio_emotion(audio_path)
    return f"<h2>Predicted Audio Emotion: {emotion}</h2><br><a href='/'>Back</a>"

@app.route('/fusion', methods=['POST'])
def fusion_emotion():
    video = request.files['video']
    audio = request.files['audio']
    text = request.form.get('text_input', '')

    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio.filename)

    video.save(video_path)
    audio.save(audio_path)

    result = fusion_emotion_result(video_path, audio_path, text)
    return f"<h2>Fusion Emotion Result: {result}</h2><br><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True)

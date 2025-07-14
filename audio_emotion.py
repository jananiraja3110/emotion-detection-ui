# audio_emotion.py

def predict_audio_emotion(audio_path):
    # Simulate based on file name or return random
    if "happy" in audio_path:
        return "Happy"
    elif "sad" in audio_path:
        return "Sad"
    else:
        return "Neutral"

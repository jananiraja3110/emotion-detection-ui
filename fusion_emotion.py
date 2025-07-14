# fusion_emotion.py

from text_emotion import predict_text_emotion
from audio_emotion import predict_audio_emotion

def fusion_emotion_result(video_path, audio_path, text):
    # Dummy fusion logic — later: average model scores
    video_emotion = "Happy"  # placeholder
    audio_emotion = predict_audio_emotion(audio_path)
    text_emotion = predict_text_emotion(text)

    if video_emotion == audio_emotion == text_emotion:
        return f"{video_emotion} (Agreed by all)"
    else:
        return f"Video: {video_emotion}, Audio: {audio_emotion}, Text: {text_emotion}"

# text_emotion.py

def predict_text_emotion(text):
    text = text.lower()
    if "happy" in text or "great" in text or "joy" in text:
        return "Happy"
    elif "sad" in text or "cry" in text:
        return "Sad"
    elif "angry" in text or "mad" in text:
        return "Angry"
    elif "fear" in text or "scared" in text:
        return "Fear"
    elif "surprise" in text:
        return "Surprise"
    else:
        return "Neutral"

# 🎭 Multimodal Emotion Detection System Using Deep Learning

This project is a **modern AI-based web application** that detects human emotions from:

- 🎥 **Video** (facial expressions)
- 🎧 **Audio** (voice tone)
- ✍️ **Text** (sentiment & emotion words)
- 🔀 **Fusion** (combines all three for higher accuracy)

It uses **Deep Learning models** (TensorFlow/Keras) for emotion classification and is built with a clean, interactive **Flask web interface**.  
Users can upload media or input text, and the system returns emotion predictions such as **Happy**, **Sad**, **Angry**, **Neutral**, etc.

---

## 🔧 Technologies Used

| Layer       | Tools/Tech                              |
|-------------|----------------------------------------  |
| 👩‍💻 Backend | Python, Flask                            |
| 🧠 AI/ML     | TensorFlow, Keras, OpenCV, librosa     |
| 🖼️ UI        | HTML5, CSS3, Responsive Layout         |
| 🎨 Theme     | Soft Modern UI (Poppins, Hover effects)|

---

## 🚀 Features

- 🎥 Upload a **video** to detect facial emotion frame-by-frame  
- 🎧 Upload an **audio file** to extract emotion from voice tone  
- ✍️ Type or paste **text** to analyze sentiment using NLP  
- 🔀 Run **Fusion Detection** by combining video, audio, and text  
- 🖼️ Displays the processed video with emotion labels  
- 💫 Soft UI, animated cards, and a responsive interface

---

## 📦 How to Run Locally


# 1. Clone the repo
git clone https://github.com/jananiraja3110/emotion-detection-ui.git
cd emotion-detection-ui

# 2. (Optional) Create virtual environment
python -m venv env
env\Scripts\activate      # on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py

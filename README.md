# 🎭 Multimodal Emotion Detection System Using Deep Learning

This project is a **modern AI-based web application** that detects human emotions from:

- 🎥 **Video** (facial expressions)
- 🎧 **Audio** (voice tone)
- ✍️ **Text** (sentiment & emotion words)
- 🔀 **Fusion** (combines all three for higher accuracy)

It uses **Deep Learning models** (TensorFlow/Keras) for emotion classification and is built with a clean, interactive **Flask web interface**.  
Users can upload media or input text, and the system returns emotion predictions such as **Happy**, **Sad**, **Angry**, **Neutral**, etc.

---

## 💡 Project Explanation

### 🧠 Goal
To build an AI system that can **detect human emotions** using input from:

- 🎥 Facial expressions (video)
- 🎧 Voice tone (audio)
- ✍️ Written text (text)
- 🔀 Fusion (all combined)

Each input is analyzed using deep learning models, and the result is shown via a **modern web UI**.

---

## 📘 Project Workflow Overview

### 1. **User Interface (HTML/CSS - Flask `templates/index.html`)**
- Users upload files (video/audio) or type text
- UI is modern, responsive, and interactive

### 2. **Backend (Flask - Python)**
- Flask routes handle each modality separately (`/`, `/audio`, `/text`, `/fusion`)
- Uploaded data is saved temporarily and passed to respective emotion detection functions

### 3. **Model Inference**
- Deep learning models (stored as `.h5`) are used for:
  - Video: Face detection + CNN classification
  - Audio: MFCC feature extraction + classifier
  - Text: Tokenization + LSTM/CNN/NLP model
- Output: Emotion like *Happy*, *Sad*, *Angry*, *Neutral*

### 4. **Fusion Logic**
- Combines results from all three modalities and gives final prediction (e.g., majority voting or weighted decision)

---

## 🔧 Technologies Used

| Layer       | Tools/Tech                             |
|-------------|----------------------------------------|
| 👩‍💻 Backend | Python, Flask                          |
| 🧠 AI/ML     | TensorFlow, Keras, OpenCV, librosa     |
| 🖼️ UI        | HTML5, CSS3, Responsive Layout         |
| 🎨 Theme     | Soft Modern UI (Poppins, Hover effects)|

---

## 📚 Libraries Used & Their Purpose

### 🧠 Machine Learning / Deep Learning
| Library        | Purpose |
|----------------|---------|
| `TensorFlow` / `Keras` | Load trained deep learning models (`.h5`), predict emotion |
| `OpenCV` (`cv2`) | Process video frames, detect face, draw emotion labels |
| `librosa` | Extract audio features (like MFCC) for emotion prediction |
| `numpy` | Numerical computations (arrays, matrices) |
| `sklearn` | Optional: preprocessing, metrics, model evaluation |

### 🌐 Web Application
| Library | Purpose |
|---------|---------|
| `Flask` | Main backend framework – handle routes, user inputs, serve pages |
| `Werkzeug` | Handle file uploads securely (via `request.files`) |
| `Jinja2` | Templating system used inside HTML for dynamic values |

### 🖼️ UI & Frontend
| Tool      | Purpose |
|-----------|---------|
| `HTML/CSS` | Build and style the frontend layout |
| `Google Fonts` | Custom fonts (like `Poppins`) for modern look |
| `Emoji Icons` | Make the interface fun and emotionally expressive |
| `CSS Transitions` | Hover effects, scaling cards, smooth animations |

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
```

🔗 Open browser at: [http://localhost:5000](http://localhost:5000)

---

## 👩‍💻 About the Author

**Janani R**  
AI & Deep Learning Enthusiast  
🌐 [GitHub](https://github.com/jananiraja3110)  
🔗 [LinkedIn](https://www.linkedin.com/in/jananiraja3110)

---

## 📌 Status

✅ Emotion detection working for all modalities  
🔄 More visualizations and charts coming soon  
📬 Suggestions & contributions welcome!

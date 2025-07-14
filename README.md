This project is a modern AI-based web application that detects human emotions from:

🎥 Video (facial expressions)

🎧 Audio (voice tone)

✍️ Text (sentiment & emotion words)

🔀 Fusion (combines all three for accuracy)

It uses Deep Learning models (TensorFlow/Keras) for classification and is built with a clean, interactive Flask web interface.
Users can upload media or input text, and the system will analyze and return emotion predictions like Happy, Sad, Angry, Neutral, etc.

🔧 Technologies Used:
Layer	Tools/Tech
👩‍💻 Backend	Python, Flask
🧠 AI/ML	TensorFlow, Keras, OpenCV, librosa
🖼️ UI	HTML5, CSS3, Responsive Layout
🎨 Theme	Soft Modern UI (Poppins Font, Touch UI, Hover Effects)

🚀 Features:
Upload a video, detect facial emotion frame by frame

Upload an audio file, extract tone-based emotion

Paste or type text, analyze sentiment/emotion using NLP

Run Fusion Detection by combining all three inputs

Display processed video result on the same page

Smooth, glowing, and responsive modern UI

📦 How to Run Locally:

# 1. Clone the repo

git clone https://github.com/jananiraja3110/emotion-detection-ui.git

cd emotion-detection-ui

# 2. Create virtual environment (optional)

python -m venv env

env\\Scripts\\activate    # on Windows

# 3. Install dependencies

pip install -r requirements.txt

# 4. Run the app
python app.py

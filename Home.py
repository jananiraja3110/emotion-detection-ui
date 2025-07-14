import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Background Setup
def set_bg(path):
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)

set_bg("background.jpg")

# Page Title
st.markdown("<h1 style='text-align:center; color:white;'>🎭 EmotionSense Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:white;'>Click a module below to detect emotions</h4><br>", unsafe_allow_html=True)

# Card-style Buttons
selected = option_menu(
    None,
    ["Text", "Audio", "Video", "Fusion"],
    icons=["file-text", "mic", "camera-video", "diagram-3"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "2rem", "background-color": "transparent"},
        "icon": {"color": "white", "font-size": "30px"},
        "nav-link": {
            "font-size": "24px",
            "color": "white",
            "text-align": "center",
            "--hover-color": "#6c757d"
        },
        "nav-link-selected": {"background-color": "#6f42c1"},
    },
)

# Navigate
if selected == "Text":
    st.switch_page("Text.py")
elif selected == "Audio":
    st.switch_page("Audio.py")
elif selected == "Video":
    st.switch_page("Video.py")
elif selected == "Fusion":
    st.switch_page("Fusion.py")

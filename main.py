# main.py
from video_emotion import detect_video_emotion, detect_live_video_emotion
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Hides info and warnings

if __name__ == "__main__":
    choice = input("Choose mode:\n1. Video file\n2. Live camera\nEnter 1 or 2: ")
    
    if choice == "1":
        video_path = input("Enter path to video file: ")
        detect_video_emotion(video_path)
    elif choice == "2":
        detect_live_video_emotion()
    else:
        print("Invalid choice.")

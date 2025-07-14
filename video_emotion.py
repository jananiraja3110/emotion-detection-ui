def detect_video_emotion_file(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = detect_emotion(frame)

        if out is None:
            height, width, _ = frame.shape
            out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))
        out.write(frame)

    cap.release()
    out.release()

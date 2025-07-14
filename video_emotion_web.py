import cv2
from deepface import DeepFace

def gen_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        try:
            results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            for result in results:
                x, y, w, h = result['region'].values()
                emotion = result['dominant_emotion']
                score = result['emotion'][emotion]

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                cv2.putText(frame, f"{emotion} ({score:.1f}%)", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        except:
            pass

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

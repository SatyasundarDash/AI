import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if (not ret): break

    try:
        res = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)[0]
        
        x, y, w, h = res['region']['x'], res['region']['y'], res['region']['w'], res['region']['h']
        emotion = res['dominant_emotion']
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    except:
        pass

    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
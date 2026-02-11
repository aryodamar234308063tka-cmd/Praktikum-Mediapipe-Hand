import cv2
import mediapipe as mp

capture = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

while True:
    success, img = capture.read()
    if not success:
        continue

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks and results.multi_handedness:

        for idx in range(len(results.multi_hand_landmarks)):

            hand_landmarks = results.multi_hand_landmarks[idx]
            handedness = results.multi_handedness[idx].classification[0].label

            thumb_x = hand_landmarks.landmark[4].x
            pinky_x = hand_landmarks.landmark[20].x

            if handedness == "Right":
                if thumb_x < pinky_x:
                    text = "Telapak"
                else:
                    text = "Punggung"

            elif handedness == "Left":
                if thumb_x > pinky_x:
                    text = "Telapak"
                else:
                    text = "Punggung"
            cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)

    cv2.imshow("webcam",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        continue

capture.release()
cv2.destroyAllWindows()
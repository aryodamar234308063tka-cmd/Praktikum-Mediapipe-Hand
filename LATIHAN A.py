import cv2
import mediapipe as mp

capture = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

while True:
    success, img = capture.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        for idx, handedness in enumerate(results.multi_handedness):

            if handedness.classification[0].index == 1:
                cv2.putText(img, "kiri",(200,50),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),3)

            elif handedness.classification[0].index == 0:
                cv2.putText(img, "kanan",(200,50),cv2.FONT_HERSHEY_PLAIN,5,(0,0,255),3)

    cv2.imshow("webcam",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
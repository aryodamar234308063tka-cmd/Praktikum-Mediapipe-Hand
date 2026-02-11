import cv2 #import module opencv
import mediapipe
capture = cv2.VideoCapture(0)
mediapipehand = mediapipe.solutions.hands
tangan = mediapipehand.Hands(max_num_hands=4)
mpdraw = mediapipe.solutions.drawing_utils

while True:
    success, img = capture.read() #Read vidio frame by frame
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = tangan.process(imgRGB)
    if results.multi_hand_landmarks:
        for titiktangan in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(img,titiktangan,mediapipehand.HAND_CONNECTIONS)
        for id, titik in enumerate(titiktangan.landmark):
                print (id)
                print (titik.x)
                print (titik.y)
    cv2.imshow("webcam",img)
    cv2.waitKey(10)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # Tutup webcam dan jendela tampilan saat q ditekan
capture.release()
cv2.destroyAllWindows()

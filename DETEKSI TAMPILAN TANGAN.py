import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import cv2 #import module cv2
import mediapipe as mp
capture = cv2.VideoCapture(0) #vidio capture pada devive kamera nomer 0
mp_hands = mp.solutions.hands #inisialisasi deteksi tengah
hands = mp_hands.Hands() #variable tangan untuk menyimpan konfigurasi deteksi tangan

while True:
    success, img = capture.read()

    if not success:
        print("Kamera tidak terbaca")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        print("tangan")
    else:
        print("tidak ada")

    cv2.imshow("webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release() #tutup webcam dan jendela tampilan saat q ditekan
cv2.destroyAllWindows()
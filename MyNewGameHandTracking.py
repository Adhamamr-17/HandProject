import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm



pTime = 0
cTime = 0
vid = cv2.VideoCapture(0)
detector = htm.handDetector()
while (True):
    success, img = vid.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img,draw = False)
    if len(lmlist) != 0:
        print(lmlist[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        vid.release()
        cv2.destroyAllWindows()

import face_recognition

import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    face_locations = face_recognition.face_locations(cv2.cvtColor( frame, cv2.COLOR_BGR2RGB))
    if(face_locations !=[]):
        cv2.rectangle(frame, (face_locations[0][3], face_locations[0][0]), (face_locations[0][1], face_locations[0][2]), (0, 0, 255), 2)
        cv2.putText(frame, "FACE FOUND!", (face_locations[0][3]+10,face_locations[0][2]+10), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)
    else:
        cv2.putText(frame, "NO FACE!", (20,450), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    
    cv2.imshow("video_feed", frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()

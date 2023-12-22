import face_recognition

import cv2
from os import listdir

font = cv2.FONT_HERSHEY_PLAIN
known_face_encodings = []
file_names = []
training_data = "training_data"

def encode_images(folder_path):
    for path in listdir(folder_path):
        image = face_recognition.load_image_file(folder_path + "\\"+path)
        data = face_recognition.face_encodings(image)
        if(data != []):
            face_encoding = data[0]
            file_names.append(path)
            known_face_encodings.append(face_encoding)


encode_images(training_data)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor( frame, cv2.COLOR_BGR2RGB)   
    face_locations = face_recognition.face_locations(rgb_frame)
    
    if(face_locations !=[]):
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        for i in range(len(face_locations)):
            matches = face_recognition.compare_faces(known_face_encodings, face_encodings[i])
            print(matches)
            j = 0
            location = face_locations[i]
            for j in range(len(matches)):
                if(matches[j]):
                    cv2.putText(frame, file_names[j], (location[3]+12,location[2]+12), font, 1, (0,255,0), 1)
                    break
            cv2.rectangle(frame, (location[3], location[0]), (location[1], location[2]), (0, 0, 255), 2)
           
    else:
        cv2.putText(frame, "NO FACE!", (20,450), font, 1, (0,255,255), 1)
    
    cv2.imshow("video_feed", frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()

import face_recognition
import cv2
import os
import datetime
def face_rec(frame):
    for student in encoded_face:
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
       
        face_location=face_recognition.face_locations(frame)
        if(len(face_location)>0 and len(face_location)<=1):
            face_encoding=face_recognition.face_encodings(frame,face_location)[0]
            if(face_recognition.compare_faces([student["encoded face"]],face_encoding)[0] and face_recognition.compare_faces([student["encoded face"]],face_encoding)[0]):
                return (student["name"])

student_data=[]
for student in os.listdir("student image"):
    student_img_add=os.path.join("student image",student)
    if(os.path.isdir(student_img_add)):
        student_img_add=os.path.join(student_img_add,os.listdir(student_img_add)[0])
        student_data.append({"name":student,"address":student_img_add})

encoded_face=[]
for student in student_data:
        known=cv2.imread(student["address"])
        known=cv2.cvtColor(known,cv2.COLOR_RGB2GRAY)
        known=cv2.cvtColor(known,cv2.COLOR_BGR2RGB)
       
        known_face_locations=face_recognition.face_locations(known)
        if(len(known_face_locations)>0):
            encoded_face.append({"encoded face":face_recognition.face_encodings(known,known_face_locations)[0],"name":student["name"]})
cap = cv2.VideoCapture(0)

name=""
while(True):
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()
    ret, frame = cap.read()
        
    key = cv2.waitKey(1) 
    if key == 97:
        break
    elif key==32:
        name=face_rec(frame)
        file=open('attendence.txt','a')
        file.write(str(name)+"  "+str(datetime.datetime.now())+" \n")
    # Font options (adjust font and size as desired)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    (text_width, text_height) = cv2.getTextSize(name, font, font_scale, font_thickness)[0]
    text_offset_x = 10  # Adjust horizontal offset from left edge
    text_offset_y = frame.shape[0] - 10  # Adjust vertical offset from bottom edge (frame.shape[0] gives frame height)
    # Put the text on the frame
    cv2.putText(frame, name, (text_offset_x, text_offset_y), font, font_scale, (255, 21, 0), font_thickness)  
    cv2.imshow('Captured Image', frame)
cap.release()
cv2.destroyAllWindows()

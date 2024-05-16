import cv2
import os
name="prashant"
parent_dir="E:\python\student image"
path = os.path.join(parent_dir,name)

os.mkdir(path,0o666) 
cap=cv2.VideoCapture(0)
count=0
while(True):
    if not cap.isOpened():
        print("can not open camera")
        exit()
    ret, frame = cap.read()
    key = cv2.waitKey(1) 
    if key == 97:
        break
    elif key==32:
        path.join(path,)
        cv2.imwrite('E:/python/student image/'+name+'/'+str(count)+'.jpg',frame)
        count=count+1
    cv2.imshow('Captured Image', frame)
cap.release()
cv2.destroyAllWindows()


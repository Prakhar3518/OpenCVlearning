import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    lineimg = cv2.line(frame,(0,0),(width,height),(0,255,0),2)
    lineimg = cv2.line(frame, (width, 0), (0,height), (0, 0, 255), 2)

    rect = cv2.rectangle(frame, (20,20) , (100,100), (255, 0, 0), 5)
    cir = cv2.circle(frame,(100,100),30,(0,0,255),-1)  #if we use -1 for thickness it will fill the shape


    font = cv2.FONT_HERSHEY_SIMPLEX
    texts = cv2.putText(frame,'And it is monday again' ,(200,height-10),font,1,(255,255,255),2,cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

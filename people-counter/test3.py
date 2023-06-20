import cv2
import numpy as np
from tracker import *

kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
# tracker = cv2.TrackerMOSSE_create()
tracker = EuclideanDistTracker()

# Filter out shadow with threshold
while True:
    ret, frame = cap.read()
    if ret == False: break
    
    frame = frame[0:320, 0:640]
    
    fgmask = fgbg.apply(frame)
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    thresh = cv2.threshold(opening,200,255,cv2.THRESH_BINARY)[1]
    dilation = cv2.dilate(thresh,kernel,iterations = 1)
    
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    
    detections = []
    for c in cnts:
        if cv2.contourArea(c) > 10000:
            x,y,w,h = cv2.boundingRect(c)
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,255), 2)
            detections.append([x, y, w, h])
       
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, idt = box_id
        cv2.putText(frame, str(idt), (x, y-15), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,255), 2)
       
    cv2.imshow('dilation', dilation)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
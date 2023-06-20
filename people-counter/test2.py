import cv2 as cv

cascade = cv.CascadeClassifier('./cascades/haarcascade_fullbody.xml')
capture = cv.VideoCapture(0)

while True:
    _, img = capture.read()
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.2, 5)
    
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x,y), (x + w, y + h), (0, 0, 255), 2)
        
    cv.imshow('img', img)
    if cv.waitKey(10) & 0xFF == 27:
        break

capture.release()
cv.destroyAllWindows()

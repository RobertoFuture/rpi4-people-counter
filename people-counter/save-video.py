import numpy as np
import cv2 as cv

# TODO: fix VLC viewer

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')

# TODO: figure out why at 60 fps videos saves sped up x2
out = cv.VideoWriter('./videos/test.avi', fourcc, 30.0, (640,  480))

while True:
    
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # write the flipped frame
    out.write(frame)
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished

cap.release()
# out.release()
cv.destroyAllWindows()

import numpy as np
import cv2
import imutils
from modules.nms import non_max_suppression_fast as nms

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# open webcam video stream
cap = cv2.VideoCapture(0)

# the output will be written to output.avi
out = cv2.VideoWriter(
    '../hasil-tes-images/hog_human_detection.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (480, 360))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resizing for faster detection
    frame = cv2.resize(frame, (480, 360))
    frame = imutils.resize(frame, width=min(480, frame.shape[1]))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8), padding=(32, 32), scale=1.05)
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    boxes = nms(boxes, 0.3)

    if len(weights) > 0:
        print(len(weights))

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

    # Write the output video
    out.write(frame.astype('uint8'))
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)

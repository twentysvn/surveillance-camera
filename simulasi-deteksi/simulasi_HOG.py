import numpy as np
import cv2

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# Capture frame-by-frame
path = "../test-images/5.jpg"
frame = cv2.imread(path)

# resizing for faster detection
#frame = cv2.resize(frame, (640, 480))
# using a greyscale picture, also for faster detection
gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# detect people in the image
# returns the bounding boxes for the detected objects
boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))

if len(weights) > 0:
    print("terdeteksi")
else:
    print("!!! tidak terdeteksi !!!")

boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

for (xA, yA, xB, yB) in boxes:
    # display the detected boxes in the colour picture
    cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

cv2.imwrite('../hasil-tes-images/hog_test.jpg', frame)

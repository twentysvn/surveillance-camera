import numpy as np
import cv2
import imutils
from modules.nms import non_max_suppression_fast as nms

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

path = "../test-images/5.jpg"
frame = cv2.imread(path)

# resizing for faster detection
#frame = cv2.resize(frame, (640, 480))
frame = imutils.resize(frame, width=min(480, frame.shape[1]))
# using a greyscale picture, also for faster detection
#gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# detect people in the image
# returns the bounding boxes for the detected objects
# akurasi tertinggi  = winStride=(8, 8), padding=(32, 32), scale=1.03
boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4), padding=(32, 32), scale=1.03)
boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

if len(boxes) > 0:
    print("Jumlah box sebelum NMS : "+str(len(boxes)))

boxes = nms(boxes, 0.3)
for (xA, yA, xB, yB) in boxes:
    # display the detected boxes in the colour picture
    cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

if len(boxes) > 0:
    print("terdeteksi")
    print("Setelah NMS : "+str(len(boxes)))
else:
    print("!!! tidak terdeteksi !!!")

cv2.imshow("HOG Test", frame)
cv2.waitKey()
#cv2.imwrite('../hasil-tes-images/hog_test.jpg', frame)

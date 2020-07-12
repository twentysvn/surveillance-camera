import numpy as np
import cv2

object_classifier = cv2.CascadeClassifier("../models/facial_recognition_model.xml")

cv2.startWindowThread()
cap = cv2.VideoCapture(0)

# the output will be written to output.avi
out = cv2.VideoWriter(
    '../hasil-tes-images/simulasi_human_detection.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (480, 360))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    weights = object_classifier.detectMultiScale(
        gray_image,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(30, 30)
    )

    if len(weights) > 0 :
        print(len(weights))

    for(x, y, w, h) in weights:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    # boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    # for (xA, yA, xB, yB) in boxes:
    #     # display the detected boxes in the colour picture
    #     cv2.rectangle(frame, (xA, yA), (xB, yB),
    #                   (0, 255, 0), 2)

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

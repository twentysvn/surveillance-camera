import cv2
from imutils.video import VideoStream
import time
import numpy as np
from modules.nms import non_max_suppression_fast as nms


class VideoCamera(object):
    def __init__(self, flip=False):
        self.vs = VideoStream().start()
        self.flip = flip
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def get_object(self, hog):
        found_objects = False
        frame = self.flip_if_needed(self.vs.read()).copy() 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # objects = classifier.detectMultiScale(
        #     gray,
        #     scaleFactor=1.1,
        #     minNeighbors=5,
        #     minSize=(30, 30),
        #     flags=cv2.CASCADE_SCALE_IMAGE
        # )

        boxes, objects = hog.detectMultiScale(gray, winStride=(8, 8), padding=(32, 32), scale=1.03)
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        boxes = nms(boxes, 0.3)

        if len(boxes) > 0:
            found_objects = True
            jmlobject = len(boxes)
        else:
            jmlobject = 0

        # kotak ijo
        # for (x, y, w, h) in objects:
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)

        return jmlobject, frame, jpeg.tobytes(), found_objects


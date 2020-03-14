import cv2

object_classifier = cv2.CascadeClassifier("../models/fullbody_recognition_model.xml")


def mulai_simulasi(classifier):
    path = "../test-images/5.jpg"
    file = cv2.imread(path)
    gray = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
    ret, frame = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)

    objects = classifier.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if len(objects) > 0:
        print("terdeteksi")
    else:
        print("!!!! tidak terdeteksi !!!!")

    for (x, y, w, h) in objects:
        cv2.rectangle(file, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for (x, y, w, h) in objects:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite('../hasil-tes-images/hasil_tes.jpg', file)
    cv2.imwrite('../hasil-tes-images/hasil_tes_gray.jpg', gray)
    cv2.imwrite('../hasil-tes-images/hasil_tes_gray_treshold.jpg', frame)


mulai_simulasi(object_classifier)

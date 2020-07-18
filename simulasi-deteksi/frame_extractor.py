import cv2
import os


video_path = "D:\\star.MP4"
save_path = '../hasil-tes-images/data'

cam = cv2.VideoCapture(video_path)
try:
    if not os.path.exists(save_path):
        os.makedirs(save_path)

except OSError:
    print('Error: Creating directory of data')


currentframe = 0

while True:
    ret, frame = cam.read()

    if ret:
        name = str(save_path)+'/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break


cam.release()
cv2.destroyAllWindows()

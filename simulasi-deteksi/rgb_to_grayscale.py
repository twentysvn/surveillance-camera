import cv2
import numpy as np
import time

img = cv2.imread("../test-images/1.jpg")

ts = time.time()
H, W = img.shape[:2]
gray = np.zeros((H, W), np.uint8)
for i in range(H):
    for j in range(W):
        # ini pake urutan BGR
        gray[i, j] = np.clip(0.299 * img[i, j, 0] + 0.587 * img[i, j, 1] + 0.144 * img[i, j, 2], 0, 255)

t = (time.time() - ts)
print("Loop: {:} ms".format(t * 1000))

cv2.imshow("Warna", img)
cv2.imshow("Grayscale", gray)
cv2.waitKey()

from skimage import exposure
from skimage import feature
import cv2

path = "../test-images/5.jpg"
frame = cv2.imread(path)
image = cv2.resize(frame, (640, 480))

(H, hogImage) = feature.hog(image, orientations=9, pixels_per_cell=(8, 8),
                            cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1",
                            visualize=True)
hogImage = exposure.rescale_intensity(hogImage, out_range=(0, 255))
hogImage = hogImage.astype("uint8")

cv2.imshow("HOG Feature", hogImage)
cv2.waitKey()
cv2.destroyAllWindows()

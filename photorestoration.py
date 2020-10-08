import cv2
import numpy

image = cv2.imread("abraham.jpg")
cv2.imshow("Original damaged image", image)
cv2.waitKey(0)

marked_damage = cv2.imread("mask.jpg", 0)
cv2.imshow("Damages marked image", marked_damage)
cv2.waitKey(0)
ret, thresh1 = cv2.threshold(marked_damage, 254, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded Binary", thresh1)
cv2.waitKey(0)

kernel = numpy.ones((7, 7), numpy.uint8)
mask = cv2.dilate(thresh1, kernel, iterations=1)
cv2.imshow("Dilated Mask", mask)
cv2.imwrite("abraham_mask.png", mask)
cv2.waitKey(0)
restore = cv2.inpaint(image, mask, 5, cv2.INPAINT_NS)
cv2.imshow("Restored", restore)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 100, 200)

cv2.imwrite("canny_image.jpg", canny)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Image", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

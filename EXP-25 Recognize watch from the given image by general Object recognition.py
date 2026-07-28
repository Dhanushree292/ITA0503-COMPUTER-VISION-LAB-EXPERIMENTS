 import cv2
img = cv2.imread("image1.jpg")

if img is None:
    print("Error: image1.jpg not found")
    exit()

x = 180      
y = 60       
w = 180      
h = 180

cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
cv2.putText(img, "Watch", (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8,
            (0, 255, 0), 2)

cv2.imshow("Watch Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

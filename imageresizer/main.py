import cv2

image = cv2.imread("harry.png")
# cv2.imshow("image", image)

scale_percent = 50
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dsize = (width, height)
output = cv2.resize(image, dsize)
cv2.imshow("output", output)
cv2.imwrite("newImage.png", output)
cv2.waitKey(0)
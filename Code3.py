import cv2
Trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread ('01.jpg')
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow ('Face Detection',grayscaled_img )
cv2.waitKey()
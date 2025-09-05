import cv2
Trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread ('01.jpg')
cv2.imshow ('Face Detection', img)

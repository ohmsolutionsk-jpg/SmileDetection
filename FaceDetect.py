import cv2
train_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('01.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_coordinates = train_face_data.detectMultiScale(img)
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Face Detector', img)
cv2.waitKey()





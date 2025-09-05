import cv2

# Face and Smile Classifier
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_detector = cv2.CascadeClassifier("haarcascade_smile.xml")

# To use Webcam
webcam = cv2.VideoCapture(0)

while True:

    # Read current frame from webcam
    successful_frame_read, frame = webcam.read()

    # If error occurs abort
    if not successful_frame_read:
        break
# Convert to Gray Scale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(frame_grayscale, 1.3, 5)

    for (x, y, w, h) in faces:

        # To draw rectangles for face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 200, 50),4)
        face = frame[y:y + h, x:x + w]

        # Convert to gray scale
        face_grayscale = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Detect smile
        smile = smile_detector.detectMultiScale(face_grayscale, 1.7,20)

        # To detect smile and display some text while smiling
        if len(smile) > 0:
            cv2.putText(frame, 'smiling', (x, y + h + 40),fontScale=3,
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, color=(255, 255, 255))

    # Display current frame
    cv2.imshow('Smile Detector', frame)

    # Quit from the output screen press q or Q
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break

# clean up
webcam.release()
cv2.destroyAllWindows()

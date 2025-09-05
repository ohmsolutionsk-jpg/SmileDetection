import cv2

# Importing pre-trained car Classifier File
classifier_file = 'cars.xml'

# Importing pre-trained Pedestrian Classifier File
pedestrian_file = 'harcascade_fullbody.xml'

# importing video
video = cv2.VideoCapture('Cars.mp4')

# Create Classifier
car_tracker = cv2.CascadeClassifier(classifier_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_file)

while True:
    (read_successful, frame) = video.read()

    if read_successful:

        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect cars
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrian = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    # Create rectangles for cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Create rectangles for Pedestrian
    for (x, y, w, h) in pedestrian:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.imshow('Car Detector', frame)
    cv2.waitKey(10)

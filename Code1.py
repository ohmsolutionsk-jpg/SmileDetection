import cv2

# Load the image
img = cv2.imread('01.jpg')

# Check if image was loaded
if img is None:
    print("Image not found!")
else:
    # Show the image
    cv2.imshow('Face Detection', img)

    # Keep window open until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()



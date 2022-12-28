import cv2
import pytello

# Connect to the Tello drone
drone = pytello.Tello()

# Start video streaming
drone.streamon()

# Set the frame rate for the video stream
drone.set_video_rate(pytello.VideoRate.RATE_30_FPS)

# Create a Haar cascade classifier for detecting humans
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Continuously capture frames from the Tello's video stream
while True:
    # Get the next frame from the video stream
    frame = drone.get_frame()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect humans in the frame using the Haar cascade classifier
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw a bounding box around each detected human
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Tello Camera', frame)

    # Check if the user has pressed the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop video streaming and close the window
drone.streamoff()
cv2.destroyAllWindows()

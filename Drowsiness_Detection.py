from scipy.spatial import distance
from imutils import face_utils
from pygame import mixer
import imutils
import dlib
import cv2
import os
import time

# Initialize the music player
mixer.init()

# Try loading the background music
music_file = "Alert.wav"
try:
    mixer.music.load(music_file)
except pygame.error as e:
    print(f"Failed to load the music file: {e}")
    exit()

# Function to calculate Eye Aspect Ratio (EAR)
# EAR is used to detect whether the eyes are closed or open
def calculate_eye_aspect_ratio(eye_points):
    dist_1 = distance.euclidean(eye_points[1], eye_points[5])  # Vertical distance 1
    dist_2 = distance.euclidean(eye_points[2], eye_points[4])  # Vertical distance 2
    dist_3 = distance.euclidean(eye_points[0], eye_points[3])  # Horizontal distance
    ear_value = (dist_1 + dist_2) / (2.0 * dist_3)
    return ear_value

# Threshold for EAR below which eyes are considered closed
ear_threshold = 0.25

# Number of consecutive frames required to trigger a drowsiness alert
frame_counter = 20

# Load dlib's face detector and the facial landmark predictor
face_detector = dlib.get_frontal_face_detector()
predictor_path = "face_landmarks.dat"
if not os.path.exists(predictor_path):
    print(f"Could not find the predictor file: {predictor_path}")
    exit()
landmark_predictor = dlib.shape_predictor(predictor_path)

# Define indices for left and right eyes in the 68-point facial landmark model
left_eye_start, left_eye_end = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
right_eye_start, right_eye_end = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

# Start video capture from the default camera
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Unable to access the camera")
    exit()

# Create a named window with resizable properties for display
cv2.namedWindow("Drowsiness Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Drowsiness Detection", 1024, 768)

# Flags for tracking drowsiness and sound status
drowsy_flag = 0
sound_played = False

try:
    while True:
        # Read the video frame from the camera
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture frame")
            break
        if frame is None:
            print("Captured frame is None")
            break
        frame = cv2.flip(frame, 1)
        frame = imutils.resize(frame, width=850)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_detector(gray_frame, 0)

        for face in faces:
            # Predict facial landmarks for the detected face
            landmarks = landmark_predictor(gray_frame, face)
            landmarks = face_utils.shape_to_np(landmarks)

            # Extract points corresponding to the left and right eyes
            left_eye_points = landmarks[left_eye_start:left_eye_end]
            right_eye_points = landmarks[right_eye_start:right_eye_end]

            # Calculate EAR for both eyes
            left_eye_ear = calculate_eye_aspect_ratio(left_eye_points)
            right_eye_ear = calculate_eye_aspect_ratio(right_eye_points)

            # Compute the average EAR
            average_ear = (left_eye_ear + right_eye_ear) / 2.0

            # Draw contours around the eyes on the frame
            left_eye_contour = cv2.convexHull(left_eye_points)
            right_eye_contour = cv2.convexHull(right_eye_points)
            cv2.drawContours(frame, [left_eye_contour], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [right_eye_contour], -1, (0, 255, 0), 1)

            # Check if EAR is below the threshold
            if average_ear < ear_threshold:
                drowsy_flag += 1
                if drowsy_flag >= frame_counter:
                    if not sound_played:
                        # Display drowsiness warning on the frame
                        cv2.putText(frame, "***** WARNING: DROWSINESS DETECTED *****", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        cv2.putText(frame, "***** WARNING: DROWSINESS DETECTED *****", (10, 325),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        # Show the frame with the warning
                        cv2.imshow("Drowsiness Detection", frame)
                        cv2.waitKey(500)  # Display the warning for 500 milliseconds
                        mixer.music.play()  # Play alert sound
                        sound_played = True
            else:
                # Reset flags if EAR is above the threshold
                drowsy_flag = 0
                sound_played = False

        # Display the current video frame
        cv2.imshow("Drowsiness Detection", frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    # Release resources and close all OpenCV windows
    cv2.destroyAllWindows()
    camera.release()

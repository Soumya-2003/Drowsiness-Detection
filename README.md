# Driver Drowsiness Detection
Driver Drowsiness Detection is a Python project that uses computer vision to detect driver drowsiness in real-time using a webcam. 
It sounds an alert when drowsiness is detected to help prevent accidents due to driver fatigue.


##   TABLE OF CONTENTS
1)  Installation
2)  Usage
3)  Dependencies
4)  How It Works


## INSTALLATION
To run this project, you need to have Python, OpenCV, Dlib, imutils, and pygame installed on your system. 
We installed the required packages using pip:
        'pip install {package_name}'

You also need to download the shape predictor model file ("shape_predictor_68_face_landmarks.dat") 
from the Dlib website and place it in the project directory.


## USAGE
1)  Run the Python script
2)  The webcam feed will open, and the program will start detecting drowsiness.
3)  If the driver's eyes remain closed for an extended period, an alert will be triggered, notifying the driver to stay awake.
4)  To exit the program, press the "q" key.


## DEPENDENCIES
This project relies on the following Python packages:

OpenCV: For capturing video frames and image processing.
Dlib: For facial landmark detection.
imutils: For resizing frames and other convenience functions.
pygame: For playing an alert sound.
winsound: for beep alerts.

## HOW IT WORKS
The program works by analyzing the driver's eye landmarks and calculating the Eye Aspect Ratio (EAR). 
When the EAR falls below a predefined threshold for a certain number of frames, an alert is triggered to wake up the driver. 
The program uses Dlib's facial landmark detection model to locate and track the eyes.


## ALGORITHM
1)  Initialize Libraries and Variables:
Import necessary libraries (OpenCV, imutils, dlib, etc.).
Initialize Pygame mixer for audio alerts.
Set parameters like thresh (EAR threshold), frame_check (frame counter for alert), and landmarks for left and right eyes.

2)  Initialize the Webcam:
    Use OpenCV to capture video from the webcam (usually the default camera).

3)  Main Loop:
Enter an infinite loop to continuously process frames from the webcam.
Frame Preprocessing:

4)  Read a frame from the webcam.
Resize the frame to a manageable width (e.g., 450 pixels).
Convert the frame to grayscale for face detection and landmark calculation.

5)  Face Detection:
Use a frontal face detector from dlib to detect faces in the grayscale frame.
For each detected face:
Calculate facial landmarks using a shape predictor.
Convert the shape points to NumPy arrays.
Extract left and right eye landmarks.

6)  Eye Aspect Ratio (EAR) Calculation:
Calculate the EAR for the left and right eyes using the Euclidean distances between eye landmarks.
Compute the average EAR for both eyes.

7)  Drowsiness Detection:
Check if the average EAR is below the predefined threshold (thresh).
If it is below the threshold, increment a "flag" counter.
If the flag counter exceeds a certain value (frame_check), trigger an alert.
The alert can be an audio alert using Pygame mixer or a beep sound using winsound.

8)  Visual Feedback:
Draw eye contours on the frame.
If drowsiness is detected, display an alert message on the frame.

9)  Display the Frame:
Show the processed frame with overlays and alerts.

10)  Exit Condition:
Check if the user presses the 'q' key. If so, exit the loop.

11)  Cleanup:
Release the webcam and close all OpenCV windows.
End the Pygame mixer.


_Feel free to customize the README to include additional information or details specific to your project. 
Providing clear instructions on installation, usage, and dependencies will make it easier for others to use and contribute to your project._

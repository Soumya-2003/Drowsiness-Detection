from turtle import bgcolor
import cv2
import imutils
from imutils import face_utils
import dlib
from scipy.spatial import distance
from pygame import mixer
import winsound
from gtts import gTTS
import pyttsx3
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
language = "en"


mixer.init()

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear
def start_detection():
    thresh = 0.25
    flag = 0
    frame_check = 50
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS['left_eye']
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS['right_eye']

    detect = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        subjects = detect(gray, 0)
        for subject in subjects:
            shape = predictor(gray, subject)  # Corrected usage here
            shape = face_utils.shape_to_np(shape)
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEar = eye_aspect_ratio(leftEye)
            rightEar = eye_aspect_ratio(rightEye)
            ear = (leftEar + rightEar) / 2.0

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
            if ear < thresh:
                flag += 1
                #print(flag)
                if flag >= frame_check:
                    cv2.putText(frame, "*ALERT*", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 225), 2)
                    cv2.putText(frame, "*WARNING*", (10, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 225), 2)
                    mixer.init()
                    #mixer.music.load("music.wav")
                    winsound.Beep(2500,1000)
                    engine = pyttsx3.init()
                    engine.say("Wake Up! Wake Up! Attention ") 
                    engine.runAndWait()
                    engine.stop
            else:
                flag = 0

        cv2.imshow("Frame", frame) 
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
    cap.release()
def ex_det():
    exit(0)
    

# Create a new thread for running the drowsiness detection
# import threading
# detection_thread = threading.Thread(target=detect_drowsiness)
# detection_thread.start()

# Create the main Tkinter window
root = tk.Tk()
root.title("Drowsiness Detection System")
root['background']='gray17'
root.geometry("650x500+0+0")
root.wm_iconbitmap("think.ico")

l1=tk.Label(root,text="Welcome to the Drowsiness Detection System",font=('arial',21,'bold'),bg='gray17',fg='snow')
l1.place(x=10,y=10)
l2=tk.Label(root,text="Developed by ThinkTECH",font=('arial',10,'bold'),bg='gray17',fg='skyblue')
l2.place(x=10,y=450)
def message():
    messagebox.showinfo('Attention !','Press:_Start Drowsiness Detection_botton to start \n\n\nPress:_q_botton in your keyboard to exit')

start1_button = tk.Button(root, text="CLICK HERE to know the steps",font=('arial',16,'bold'),bg='yellow3',fg='black', command = message)
start1_button.place(x=110,y=100)
# Create a button to start the drowsiness detection
start_button = tk.Button(root, text="START Drowsiness Detection",font=('arial',16,'bold'),bg='Green2',fg='black', command = start_detection)
start_button.place(x=117,y=200)

# Create a button to quit the application
quit_button = tk.Button(root,text="QUIT",font=('arial',16,'bold'),bg='DeepPink1',fg='black', command=root.destroy)
quit_button.place(x=240,y=300)

root.mainloop()
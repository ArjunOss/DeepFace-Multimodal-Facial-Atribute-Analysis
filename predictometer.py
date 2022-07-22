import time
from tkinter import *
from tkinter import ttk

import cv2
from deepface import DeepFace as df

def age():
    l1.delete(0, END)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    video = cv2.VideoCapture(0)

    while video.isOpened():
        _,frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for x,y,w,h in face:
            img = cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),1)

            try:
                analyze = df.analyze(frame, actions=["age"])
                s.set(analyze["age"])
                time.sleep(2)

            except:

                s.set("no face")
                time.sleep(2)

        cv2.imshow("video", frame)
        key = cv2.waitKey(1)
        if key==ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

def gender():
    l1.delete(0,END)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    video = cv2.VideoCapture(0)

    while video.isOpened():
        _,frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for x,y,w,h in face:
            img = cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),1)

            try:
                analyze = df.analyze(frame, actions=["gender"])
                time.sleep(2)
                s.set(analyze["gender"])

            except:
                time.sleep(2)
                s.set("no face")


        cv2.imshow("video", frame)
        key = cv2.waitKey(1)
        if key==ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def race():
    l1.delete(0,END)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    video = cv2.VideoCapture(0)

    while video.isOpened():
        _,frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for x,y,w,h in face:
            img = cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),1)

            try:
                analyze = df.analyze(frame, actions=["race"])

                s.set(analyze["race"])

            except:

                s.set("no face")


        cv2.imshow("video", frame)
        key = cv2.waitKey(1)
        if key==ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def facial_expression():
    l1.delete(0,END)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    video = cv2.VideoCapture(0)

    while video.isOpened():
        _,frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for x,y,w,h in face:
            img = cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),1)

            try:
                analyze = df.analyze(frame, actions=["emotion"])
                s.set(analyze["dominant_emotion"])

            except:

                s.set("no face")


        cv2.imshow("video", frame)
        key = cv2.waitKey(1)
        if key==ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()




root = Tk()
root.title("Predictometer")
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
xco = sw//3
yco = sh//3
# w = sw//2
# h = sh//2
root.geometry(f"332x200+{xco}+{yco}")
# root.geometry("332x200")

#menubar
menubar = Menu(root)
#add menubar to root
root.config(menu = menubar)

#create file_menu
file_name = Menu(menubar, tearoff = 0)

file_name.add_separator()
file_name.add_command(label = "Exit", command = root.destroy )
menubar.add_cascade(label = "File", menu = file_name, underline = 0)
#menubar end


s = StringVar()
l1 = Entry(root, relief = "raised", width = 20, bg = "white", textvariable=s)
l1.grid(row = 2, column = 0,columnspan=4)

b1 = ttk.Button(root, text = "Age", width = 12, command = age)
b2 = ttk.Button(root, text = "Gender", width = 12, command = gender)
b3 = ttk.Button(root, text = "Race", width = 12, command = race)
b4 = ttk.Button(root, text = "Emotion", width = 12, command = facial_expression)

b1.grid(row = 1, column = 0)
b2.grid(row = 1, column = 1)
b3.grid(row = 1, column = 2)
b4.grid(row = 1, column = 3)

root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from patient import Patient
from train import Train
from face_recognition import Face_Recognition
import os


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1000+0+0")
        self.root.title("СИСТЕМА РАСПОЗНАВАНИЯ ЛИЦА")


        # First image
        img=Image.open("img/img.jpg")
        img=img.resize((650,170),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=650,height=170)

        #Second image
        img1=Image.open("img/dee.png")
        img1=img1.resize((650,170),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=0,width=650,height=170)

        # Thirt image
        img2=Image.open("img/img3.jpg")
        img2=img2.resize((650,170),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1300,y=0,width=650,height=170)

        # Background image
        imgbg=Image.open("img/a.png")
        imgbg=imgbg.resize((1920,830),Image.ANTIALIAS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)
        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=170,width=1920,height=830)

        title_lbl=Label(bg_img,text="СИСТЕМА РАСПОЗНАВАНИЯ ЛИЦА ДЛЯ РЕГИСТРАЦИЯ ПАЦИЕНТА",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1920,height=45)


        # Button for register patient
        imgbtn1=Image.open("img/patient.jpg")
        imgbtn1=imgbtn1.resize((220,220),Image.ANTIALIAS)
        self.photoimgbtn1=ImageTk.PhotoImage(imgbtn1)
        b1=Button(bg_img,image=self.photoimgbtn1,command=self.patient_details,cursor="hand2")
        b1.place(x=300,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Данные пациента",command=self.patient_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=300,y=300,width=220,height=40)

        # Face detection
        imgbtn2=Image.open("img/detection.jpg")
        imgbtn2=imgbtn2.resize((220,220),Image.ANTIALIAS)
        self.photoimgbtn2=ImageTk.PhotoImage(imgbtn2)
        b2=Button(bg_img,image=self.photoimgbtn2,cursor="hand2",command=self.face_recognition)
        b2.place(x=650,y=100,width=220,height=220)
        b2_1=Button(bg_img,text="Распознавание лиц",cursor="hand2",command=self.face_recognition,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=650,y=300,width=220,height=40)


        # Attendance system
        imgbtn3=Image.open("img/attendance.jpg")
        imgbtn3=imgbtn3.resize((220,220),Image.ANTIALIAS)
        self.photoimgbtn3=ImageTk.PhotoImage(imgbtn3)
        b3=Button(bg_img,image=self.photoimgbtn3,cursor="hand2")
        b3.place(x=1000,y=100,width=220,height=220)
        b3_1=Button(bg_img,text="Посещение",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=1000,y=300,width=220,height=40)


        # Help Desk button
        imgbtn4=Image.open("img/help.jpg")
        imgbtn4=imgbtn4.resize((220,220),Image.ANTIALIAS)
        self.photoimgbtn4=ImageTk.PhotoImage(imgbtn4)
        b4=Button(bg_img,image=self.photoimgbtn4,cursor="hand2")
        b4.place(x=1350,y=100,width=220,height=220)
        b4_1=Button(bg_img,text="Служба поддержки",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1350,y=300,width=220,height=40)

###################################################################################################
######################################### Second row ##############################################
###################################################################################################

        # Button for Train data
        imgbtn1_1=Image.open("img/train.jpg")
        imgbtn1_1=imgbtn1_1.resize((220,220),Image.ANTIALIAS)
        self.photoimgbtn1_1=ImageTk.PhotoImage(imgbtn1_1)
        b5=Button(bg_img,image=self.photoimgbtn1_1,cursor="hand2",command=self.train_data)
        b5.place(x=300,y=450,width=220,height=220)
        b5_1=Button(bg_img,text="Составить данные",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=300,y=650,width=220,height=40)

        # Button for view Photos
        imgbtn2_1=Image.open("img/photos.png")
        imgbtn2_1=imgbtn2_1.resize((220,220),Image.ANTIALIAS)
        self.photoimgbtn2_1=ImageTk.PhotoImage(imgbtn2_1)
        b6=Button(bg_img,image=self.photoimgbtn2_1,cursor="hand2",command=self.open_img)
        b6.place(x=650,y=450,width=220,height=220)
        b6_1=Button(bg_img,text="Фото",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=650,y=650,width=220,height=40)


        # Button for developer
        imgbtn3_1=Image.open("img/developer.jpg")
        imgbtn3_1=imgbtn3_1.resize((220,220),Image.ANTIALIAS)
        self.photoimgbtn3_1=ImageTk.PhotoImage(imgbtn3_1)
        b7=Button(bg_img,image=self.photoimgbtn3_1,cursor="hand2")
        b7.place(x=1000,y=450,width=220,height=220)
        b7_1=Button(bg_img,text="Программист",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=1000,y=650,width=220,height=40)


        # Button for exit
        imgbtn4_1=Image.open("img/exit.png")
        imgbtn4_1=imgbtn4_1.resize((220,220),Image.ANTIALIAS)
        self.photoimgbtn4_1=ImageTk.PhotoImage(imgbtn4_1)
        b8=Button(bg_img,image=self.photoimgbtn4_1,cursor="hand2")
        b8.place(x=1350,y=450,width=220,height=220)
        b8_1=Button(bg_img,text="Выйти",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1350,y=650,width=220,height=40)


    # =========================Functions buttons =========================
    def open_img(self):
        os.startfile("data")

    def patient_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Patient(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
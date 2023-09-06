from sys import path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from patient import Patient
from train import Train
import psycopg2
import cv2
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1000+0+0")
        self.root.title("СИСТЕМА РАСПОЗНАВАНИЯ ЛИЦА")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1920,height=45)

        #   1st image
        img_top=Image.open("img/face_recog2.jpg")
        img_top=img_top.resize((850,930),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=55,width=850,height=930)
         
        
        #2nd image
        img_bottom=Image.open("img/face_recog1.jpg")
        img_bottom=img_bottom.resize((1150,930) ,Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_label=Label(self.root,image=self.photoimg_bottom)
        f_label.place(x=850,y=55,width=1150,height=930)


        b1_1=Button(f_label,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=445,y=830,width=250,height=50)

    def mark_attendance(self,n,r,p,k,l,m):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((n not in name_list)) and ((r not in name_list)) and ((p not in name_list)) and ((k not in name_list)) and ((l not in name_list)) and ((m not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n}, {r}, {p},{k},{l},{m},{dtString}, {d1}, Preset")

#======================= face recognition ===========================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
        
                conn = psycopg2.connect(database="postgres",user="postgres",password="2284161",host="localhost",port='5432')
                cur = conn.cursor()

                cur.execute("select fname from patient where patient_id="+str(id))
                n=cur.fetchone()
                n="+".join(n)

                cur.execute("select lname from patient where patient_id="+str(id))
                r=cur.fetchone()
                r="+".join(r)

                cur.execute("select sname from patient where patient_id="+str(id))
                p=cur.fetchone()
                p="+".join(p)

                cur.execute("select blood from patient where patient_id="+str(id))
                k=cur.fetchone()
                k="+".join(k)

                cur.execute("select bolezn from patient where patient_id="+str(id))
                l=cur.fetchone()
                l="+".join(l)
                
                cur.execute("select nogiron from patient where patient_id="+str(id))
                m=cur.fetchone()
                m="+".join(m)

                if confidence>77:
                    cv2.putText(img,f"Имя:{n}",(x,y-150),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Фамилия:{r}",(x,y-125),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Отчество:{p}",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Група крови:{k}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Болезнь:{l}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Болезнь:{m}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    self.mark_attendance(n,r,p,k,l,m)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
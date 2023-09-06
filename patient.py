from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import psycopg2
import cv2

class Patient:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1000+0+0")
        self.root.title("Face Recognition System")





        # ==================== varriables===================
        self.var_region=StringVar()
        self.var_blood=StringVar()
        self.var_year=StringVar()
        self.var_hospital=StringVar()
        self.var_nogiron=StringVar()
        self.var_mod=StringVar()
        self.var_id=StringVar()
        self.var_bolezn=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_adress=StringVar()
        self.var_phone=StringVar()
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_sname=StringVar()
        self.var_datebirth=StringVar()
        self.var_passports=StringVar()
        self.var_grajdanin=StringVar()

        # First image
        img=Image.open("img/patient_2.jpg")
        img=img.resize((650,170),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=650,height=170)

        #Second image
        img1=Image.open("img/patient_3.jpg")
        img1=img1.resize((650,170),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=0,width=650,height=170)

        # Thirt image
        img2=Image.open("img/patient_r.jpg")
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
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM FOR PATIENT",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1920,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=15,y=60,width=1860,height=760)
        
        # Left frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",bg="white", font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=830,height=730)
        
        img_left=Image.open("img/patient_r.jpg")
        img_left=img_left.resize((820,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=820,height=130)

        #current label
        current_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Данные о пациенте",bg="white", font=("times new roman",12,"bold"))
        current_frame.place(x=5,y=135,width=820,height=155)

        region_frame=Label(current_frame,text="Регион",bg="white", font=("times new roman",12,"bold"))
        region_frame.grid(row=0,column=0,padx=10,sticky=W)
        region_combo=ttk.Combobox(current_frame,textvariable=self.var_region, font=("times new roman",12,"bold"),state="readonly")
        region_combo["values"]=("Выбери регион","Андижан","Бухара","Самарканд","Жиззах","Ташкент","Кашкадарья","Навоий")
        region_combo.current(0)
        region_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        blood_frame=Label(current_frame,text="Группы крови",bg="white", font=("times new roman",12,"bold"))
        blood_frame.grid(row=0,column=2,padx=10,sticky=W)
        blood_combo=ttk.Combobox(current_frame,textvariable=self.var_blood,font=("times new roman",12,"bold"),state="readonly")
        blood_combo["values"]=("Выбери группу крови","I-группа","II-группа","III-группа",)
        blood_combo.current(0)
        blood_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        year_frame=Label(current_frame,text="Год лечение",bg="white", font=("times new roman",12,"bold"))
        year_frame.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Выбери год","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        hospital_frame=Label(current_frame,text="Больницы",bg="white", font=("times new roman",12,"bold"))
        hospital_frame.grid(row=1,column=2,padx=10,sticky=W)
        hospital_combo=ttk.Combobox(current_frame,textvariable=self.var_hospital,font=("times new roman",12,"bold"),state="readonly")
        hospital_combo["values"]=("Выбери больницы","Гор больница","Облатная больница","Глазной больница")
        hospital_combo.current(0)
        hospital_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        nogiron_frame=Label(current_frame,text="Инвалидность",bg="white", font=("times new roman",12,"bold"))
        nogiron_frame.grid(row=2,column=0,padx=10,sticky=W)
        nogiron_combo=ttk.Combobox(current_frame,textvariable=self.var_nogiron,font=("times new roman",12,"bold"),state="readonly")
        nogiron_combo["values"]=("Выбери Группу","Нет","I группа","II группа","III группа")
        nogiron_combo.current(0)
        nogiron_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        mod_frame=Label(current_frame,text="Махалля",bg="white", font=("times new roman",12,"bold"))
        mod_frame.grid(row=2,column=2,padx=10,sticky=W)
        mod_combo=ttk.Combobox(current_frame,textvariable=self.var_mod,font=("times new roman",12,"bold"),state="readonly")
        mod_combo["values"]=("Выбери махалля","Чашма МФЙ","Турон МФЙ","Темур Малик МФЙ")
        mod_combo.current(0)
        mod_combo.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Данные пациенте
        input_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Данные о пациенте",bg="white", font=("times new roman",12,"bold"))
        input_frame.place(x=5,y=290,width=820,height=410)
        #ID name entry
        id_name_label=Label(input_frame,text="ID:",bg="white",font=("times new roman",13,"bold"))
        id_name_label.grid(row=0,column=0,padx=20,pady=10,sticky=W)
        id_name_entry=ttk.Entry(input_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        id_name_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        #ID name entry
        bolezn_label=Label(input_frame,text="Болезнь:",bg="white",font=("times new roman",13,"bold"))
        bolezn_label.grid(row=1,column=0,padx=20,pady=5,sticky=W)
        bolezn_entry=ttk.Entry(input_frame,textvariable=self.var_bolezn,width=20,font=("times new roman",13,"bold"))
        bolezn_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #ID name entry
        gender_label=Label(input_frame,text="Пол:",bg="white",font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=0,padx=20,pady=5,sticky=W)
        gender_combo=ttk.Combobox(input_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Мужской","Женский","Другой")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        #ID name entry
        email_label=Label(input_frame,text="E-mail:",bg="white",font=("times new roman",13,"bold"))
        email_label.grid(row=3,column=0,padx=20,pady=5,sticky=W)
        email_entry=ttk.Entry(input_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #ID name entry
        adress_label=Label(input_frame,text="Адрес",bg="white",font=("times new roman",13,"bold"))
        adress_label.grid(row=4,column=0,padx=20,pady=5,sticky=W)
        adress_entry=ttk.Entry(input_frame,textvariable=self.var_adress,width=20,font=("times new roman",13,"bold"))
        adress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        #ID name entry
        phone_label=Label(input_frame,text="Телефон номер:",bg="white",font=("times new roman",13,"bold"))
        phone_label.grid(row=5,column=0,padx=20,pady=5,sticky=W)
        phone_entry=ttk.Entry(input_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)
        #ID name entry
        fname_label=Label(input_frame,text="Имя:",bg="white",font=("times new roman",13,"bold"))
        fname_label.grid(row=0,column=2,padx=20,pady=10,sticky=W)
        fname_entry=ttk.Entry(input_frame,textvariable=self.var_fname,width=20,font=("times new roman",13,"bold"))
        fname_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        #ID name entry
        lname_label=Label(input_frame,text="Фамилия:",bg="white",font=("times new roman",13,"bold"))
        lname_label.grid(row=1,column=2,padx=20,pady=5,sticky=W)
        lname_entry=ttk.Entry(input_frame,textvariable=self.var_lname,width=20,font=("times new roman",13,"bold"))
        lname_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #Sur name
        sname_label=Label(input_frame,text="Отчество:",bg="white",font=("times new roman",13,"bold"))
        sname_label.grid(row=2,column=2,padx=20,pady=5,sticky=W)
        sname_entry=ttk.Entry(input_frame,textvariable=self.var_sname,width=20,font=("times new roman",13,"bold"))
        sname_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #Data birthday entry
        datebirth_label=Label(input_frame,text="Дата рождения:",bg="white",font=("times new roman",13,"bold"))
        datebirth_label.grid(row=3,column=2,padx=20,pady=5,sticky=W)
        datebirth_entry=ttk.Entry(input_frame,textvariable=self.var_datebirth,width=20,font=("times new roman",13,"bold"))
        datebirth_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        # Passport entry
        passports_label=Label(input_frame,text="Серия пасспорта:",bg="white",font=("times new roman",13,"bold"))
        passports_label.grid(row=4,column=2,padx=20,pady=5,sticky=W)
        passports_entry=ttk.Entry(input_frame,textvariable=self.var_passports,width=20,font=("times new roman",13,"bold"))
        passports_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        #Grajdanin entry
        grajdanin_label=Label(input_frame,text="Гражданинство:",bg="white",font=("times new roman",13,"bold"))
        grajdanin_label.grid(row=5,column=2,padx=20,pady=5,sticky=W)
        grajdanin_entry=ttk.Entry(input_frame,textvariable=self.var_grajdanin,width=20,font=("times new roman",13,"bold"))
        grajdanin_entry.grid(row=5,column=3,padx=10,pady=5,sticky=W)
        # Radio button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(input_frame,variable=self.var_radio1,text="Сделать образец фото",value="Yes")
        radionbtn1.grid(row=7,column=0)

        radionbtn2=ttk.Radiobutton(input_frame,variable=self.var_radio1,text="Несделать образец фото",value="No")
        radionbtn2.grid(row=7,column=1)


        #Buttons frame
        btn_frame=Frame(input_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=815,height=70)

        save_btn=Button(btn_frame,text="Save",width=16,height=2,command=self.add_data, font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=16,height=2,command=self.update_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=16,height=2,command=self.delete_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=16,height=2,command=self.reset_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(input_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=320,width=815,height=60)
        
        take_photo_btn=Button(btn_frame1,text="Take a photo",width=33,height=2,command=self.generate_dataset,font=("times new roman",15,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Quit",width=33,height=2,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        # Right frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",bg="white", font=("times new roman",12,"bold"))
        right_frame.place(x=850,y=10,width=970,height=730)
        
        img_right=Image.open("img/patient_r.jpg")
        img_right=img_right.resize((960,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=960,height=130)

        # Search frame
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search system",bg="white", font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=960,height=70)

        # Search label
        search_label=Label(search_frame,text="Поиск пациента:",bg="red",font=("times new roman",13,"bold"),fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        self.var_searchTX=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Выбери поиск","По ID пациента","По номер телефона","По e-mail пациента")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,width=25,textvariable=self.var_search,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Поиск",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)
        show_search_btn=Button(search_frame,text="Показать все",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        show_search_btn.grid(row=0,column=4,padx=15)
        
        # Table frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=210,width=960,height=490)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.patient_table=ttk.Treeview(table_frame,column=("ID","fname","lname","sname","adress","region","datebirth","email","phone","year","blood","hospital","nogiron","mod","gender","bolezn","passports","grajdanin","photosample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.patient_table.xview)
        scroll_y.config(command=self.patient_table.yview)

        self.patient_table.heading("ID",text="ID пациента")
        self.patient_table.heading("fname",text="Имя")
        self.patient_table.heading("lname",text="Фамилия")
        self.patient_table.heading("sname",text="Отчество")
        self.patient_table.heading("adress",text="Адрес")
        self.patient_table.heading("region",text="Регион")
        self.patient_table.heading("datebirth",text="Дата рождения")
        self.patient_table.heading("email",text="Почта")
        self.patient_table.heading("phone",text="Телефон")
        self.patient_table.heading("year",text="Год")
        self.patient_table.heading("blood",text="Группа крови")
        self.patient_table.heading("hospital",text="Больницы")
        self.patient_table.heading("nogiron",text="Спеуиалист")
        self.patient_table.heading("mod",text="Region")
        self.patient_table.heading("gender",text="Пол")
        self.patient_table.heading("bolezn",text="Болезнь")
        self.patient_table.heading("passports",text="Серия пасспорт")
        self.patient_table.heading("grajdanin",text="Гражданство")
        self.patient_table.heading("photosample",text="Фото")
        self.patient_table["show"]="headings"

        
        self.patient_table.column("ID",width=150)
        self.patient_table.column("fname",width=150)
        self.patient_table.column("lname",width=150)
        self.patient_table.column("sname",width=150)
        self.patient_table.column("adress",width=150)
        self.patient_table.column("region",width=150)
        self.patient_table.column("datebirth",width=150)
        self.patient_table.column("email",width=150)
        self.patient_table.column("phone",width=150)
        self.patient_table.column("year",width=150)
        self.patient_table.column("blood",width=150)
        self.patient_table.column("hospital",width=150)
        self.patient_table.column("nogiron",width=150)
        self.patient_table.column("mod",width=150)
        self.patient_table.column("gender",width=150)
        self.patient_table.column("bolezn",width=150)
        self.patient_table.column("passports",width=150)
        self.patient_table.column("grajdanin",width=150)
        self.patient_table.column("photosample",width=150)

        self.patient_table.pack(fill=BOTH,expand=1)
        self.patient_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_region.get()=="" or self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_sname.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Ошибка","Заполните все поля!",parent=self.root)
        else:
            try:
                conn = psycopg2.connect(database="postgres",user="postgres",password="2284161",host="localhost",port='5432')
                cur = conn.cursor()
                cur.execute("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_id.get(),
                                                                                                                    self.var_fname.get(),
                                                                                                                    self.var_lname.get(),
                                                                                                                    self.var_sname.get(),
                                                                                                                    self.var_adress.get(),
                                                                                                                    self.var_region.get(),
                                                                                                                    self.var_datebirth.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_blood.get(),
                                                                                                                    self.var_hospital.get(),
                                                                                                                    self.var_nogiron.get(),
                                                                                                                    self.var_mod.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_bolezn.get(),
                                                                                                                    self.var_passports.get(),
                                                                                                                    self.var_grajdanin.get(),
                                                                                                                    self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Patient details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    def fetch_data(self):
        conn = psycopg2.connect(database="postgres",user="postgres",password="2284161",host="localhost",port='5432')
        cur = conn.cursor()
        cur.execute("select * from patient")
        data=cur.fetchall()

        if len(data)!=0:
            self.patient_table.delete(*self.patient_table.get_children())
            for i in data:
                self.patient_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event):
        cursor_focus=self.patient_table.focus()
        content=self.patient_table.item(cursor_focus)
        data=content["values"]
        self.var_id.set(data[0])
        self.var_fname.set(data[1])
        self.var_lname.set(data[2])
        self.var_sname.set(data[3])
        self.var_adress.set(data[4])
        self.var_region.set(data[5])
        self.var_datebirth.set(data[6])
        self.var_email.set(data[7])
        self.var_phone.set(data[8])
        self.var_year.set(data[9])
        self.var_blood.set(data[10])
        self.var_hospital.set(data[11])
        self.var_nogiron.set(data[12])
        self.var_mod.set(data[13])
        self.var_gender.set(data[14])
        self.var_bolezn.set(data[15])
        self.var_passports.set(data[16])
        self.var_grajdanin.set(data[17])
        self.var_radio1.set(data[18])

    def update_data(self):
        if self.var_region.get()=="Select Department" or self.var_blood.get()=="" or self.var_year.get()=="" or self.var_hospital.get()=="" or self.var_nogiron.get()=="" or self.var_mod.get()=="" or self.var_id.get()=="" or self.var_bolezn.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_adress.get()=="" or self.var_phone.get()=="" or self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_sname.get()=="" or self.var_datebirth.get()=="" or self.var_passports.get()=="" or self.var_grajdanin.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("Ошибка","Заполните все поля!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this patient details",parent=self.root)
                if Update>0:
                    conn = psycopg2.connect(database="postgres",user="postgres",password="2284161",host="localhost",port='5432')
                    cur = conn.cursor()
                    cur.execute(""" update patient set fname=%s,lname=%s,sname=%s,address=%s,region=%s,datebirth=%s,email=%s,phone=%s,
                                    year=%s,blood=%s,hospital=%s,nogiron=%s,mod=%s,gender=%s,bolezn=%s,passports=%s,grajdanin=%s,
                                    photosample=%s where patient_id=%s""", (
                                    self.var_fname.get(),
                                    self.var_lname.get(),
                                    self.var_sname.get(),
                                    self.var_adress.get(),
                                    self.var_region.get(),
                                    self.var_datebirth.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_year.get(),
                                    self.var_blood.get(),
                                    self.var_hospital.get(),
                                    self.var_nogiron.get(),
                                    self.var_mod.get(),
                                    self.var_gender.get(),
                                    self.var_bolezn.get(),
                                    self.var_passports.get(),
                                    self.var_grajdanin.get(),
                                    self.var_radio1.get(),
                                    self.var_id.get()))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Успешно","Сведения о пациенте успешно обновлены",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Ошибка",f"Из за:{str(es)}",parent=self.root)
            
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Ошибка","Требуется студенческий билет!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Удалить","Вы точно хотите удалить информацию этого пациента",parent=self.root)
                if delete>0:
                    conn = psycopg2.connect(user='postgres', password='2284161',host='localhost',database='postgres',port=5432)
                    cur = conn.cursor() 
                    sql="delete from patient where patient_id=%s"
                    val=(self.var_id.get(),)
                    cur.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Удалить","Успешно удалено!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Ошибка",f"Из за: {str(es)}",parent=self.root)    
    # Reset Function 
    def reset_data(self):
        self.var_id.set("")
        self.var_fname.set(""),
        self.var_lname.set(""),
        self.var_sname.set(""),
        self.var_adress.set(""),
        self.var_region.set(""),
        self.var_datebirth.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_year.set(""),
        self.var_blood.set(""),
        self.var_hospital.set(""),
        self.var_nogiron.set(""),
        self.var_mod.set(""),
        self.var_gender.set(""),
        self.var_bolezn.set(""),
        self.var_passports.set(""),
        self.var_grajdanin.set(""),
        self.var_radio1.set("")

    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Выбери поиск":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = psycopg2.connect(user='postgres', password='2284161',host='localhost',database='postgres',port=5432)
                cur = conn.cursor()
                sql = "SELECT patient_id,fname,lname,sname,address,region,datebirth,email,phone,year,blood,hospital,nogiron,mod,gender,bolezn,passports,grajdanin,photosample FROM patient where where patient_id='" +str(self.var_search.get()) + "'" 
                cur.execute(sql)
                cur.execute("select * from patient where patient_id= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=cur.fetchall()        
                if len(rows)!=0:
                    self.patient_table.delete(*self.patient_table.get_children())
                    for i in rows:
                        self.patient_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

# ======================= GENERATE DATASET =====================
    def generate_dataset(self):
        if self.var_region.get()=="Select Department" or self.var_blood.get()=="" or self.var_year.get()=="" or self.var_hospital.get()=="" or self.var_nogiron.get()=="" or self.var_mod.get()=="" or self.var_id.get()=="" or self.var_bolezn.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_adress.get()=="" or self.var_phone.get()=="" or self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_sname.get()=="" or self.var_datebirth.get()=="" or self.var_passports.get()=="" or self.var_grajdanin.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("Ошибка","Заполните все поля!",parent=self.root)
        else:
            try:
                conn = psycopg2.connect(user='postgres', password='2284161',host='localhost',database='postgres',port=5432)
                cur = conn.cursor()
                cur.execute("select * from patient")
                myreslut = cur.fetchall()
                id=0
                for x in myreslut:
                    id+=1
                cur.execute(""" update patient set fname=%s,lname=%s,sname=%s,address=%s,region=%s,datebirth=%s,email=%s,phone=%s,
                                    year=%s,blood=%s,hospital=%s,nogiron=%s,mod=%s,gender=%s,bolezn=%s,passports=%s,grajdanin=%s,
                                    photosample=%s where patient_id=%s""", (
                                    self.var_fname.get(),
                                    self.var_lname.get(),
                                    self.var_sname.get(),
                                    self.var_adress.get(),
                                    self.var_region.get(),
                                    self.var_datebirth.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_year.get(),
                                    self.var_blood.get(),
                                    self.var_hospital.get(),
                                    self.var_nogiron.get(),
                                    self.var_mod.get(),
                                    self.var_gender.get(),
                                    self.var_bolezn.get(),
                                    self.var_passports.get(),
                                    self.var_grajdanin.get(),
                                    self.var_radio1.get(),
                                    self.var_id.get()))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5, minSize=(200, 200), flags=cv2.CASCADE_SCALE_IMAGE) 
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        
                        face=cv2.resize(face_croped(my_frame),(600,600))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/patient."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Результат","Фотографии успешно сохранено",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Из за: {str(es)}",parent=self.root) 






if __name__=="__main__":
    root=Tk()
    obj=Patient(root)
    root.mainloop()
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import psycopg2

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Đăng Ký Tài Khoản")
        self.root.state('zoomed')
        self.root.configure(bg="#002B53")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file="img/a.png")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=300,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,highlightbackground="lightgray",highlightthickness=2,bg="#F2F2F2")
        frame.place(x=100,y=70,width=670,height=480)
        

        # img1=Image.open("Images_GUI/reg1.png")
        # img1=img1.resize((450,100),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        # lb1img1.place(x=350,y=100, width=500,height=100)
        

        get_str = Label(frame,text="Đăng Ký Tài Khoản Admin ",font=("times new roman",20,"bold"),fg="#F2F2F2",bg="#002B53")
        get_str.place(x=0,y=0,width=665,height=50)

        #label1 
        fname =lb1= Label(frame,text="Họ:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=50,y=90)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=50,y=120,width=270)


        #label2 
        lname =lb1= Label(frame,text="Tên:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=50,y=160)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=50,y=190,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Liên hệ:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=350,y=90)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=350,y=120,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=350,y=160)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=350,y=190,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Câu hỏi bảo mật:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=50,y=230)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Ngày tháng sinh","Nick Name","Sách yêu thích")
        self.combo_security.current(0)
        self.combo_security.place(x=50,y=260,width=270)


        #label2 
        sa =lb1= Label(frame,text="Câu trả lời:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=50,y=300)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=50,y=330,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="mật khẩu:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=350,y=230)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=350,y=260,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Nhắc lại mật khẩu:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=350,y=300)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=350,y=330,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="Đồng ý các điều khoản",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=40,y=370,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Đăng Ký",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=50,y=410,width=270,height=35)

        # Creating Button Login
        loginbtn=Button(frame,text="Đăng Nhập",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=350,y=410,width=270,height=35)




    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","Tất cả các trường bắt buộc!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Vui lòng nhập mật khẩu và xác nhận mật khẩu giống nhau!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Vui lòng kiểm tra các Điều khoản và Điều kiện đã Thỏa thuận!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = psycopg2.connect(user='postgres', password='2284161',host='localhost',database='postgres',port=5432)
                mycursor = conn.cursor()
                query=("select * from regteach where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Người dùng đã tồn tại, vui lòng thử một email khác")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_cnum.get(),
                    self.var_email.get(),
                    self.var_ssq.get(),
                    self.var_sa.get(),
                    self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Đăng ký thành công!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
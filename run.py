from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
total_bill = 0
class Login:

   def __init__(self,root):
      self.root=root
      self.root.title("Login and Registration")
      self.root.geometry("2000x1265+0+0")
      self.root.resizable(True,True)
      self.loginform()

   def loginform(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=1265,width=2000)

      self.img=ImageTk.PhotoImage(file=r"D:\Project Build A Thon\New folder\del.jpg")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=2000,height=1265)

      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=120,y=130,height=450,width=350)

      label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),fg="black",bg='white')
      label1.place(x=75,y=20)

      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='black',bg='white')
      label2.place(x=30,y=95)
      
      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      self.email_txt.place(x=30,y=145,width=270,height=35)

      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='black',bg='white')
      label3.place(x=30,y=195)
      self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      self.password.place(x=30,y=245,width=270,height=35)

      #btn1=Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg='bl',fg='black',bd=0)
      #btn1.place(x=125,y=305)

      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("times new roman",15),fg="white",bg="black",bd=0,width=15,height=1)
      btn2.place(x=90,y=340)

      btn3=Button(frame_input,command=self.Register,text="Not Registered?Register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      btn3.place(x=110,y=390)

   def login(self):

      if self.email_txt.get()=="" or self.password.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)

      else:
         try:
            con=pymysql.connect(host='localhost',user='root',password='Riya',database='frozenfood')
            cur=con.cursor()
            cur.execute('select * from register where emailid=%s and password=%s',(self.email_txt.get(),self.password.get()))
            row=cur.fetchone()

            if row==None:
               messagebox.showerror('Error','Invalid Username And Password',parent=self.root)
               self.loginclear()
               self.email_txt.focus()

            else:
               self.appscreen()
               con.close()

         except Exception as es:
            messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)

            
   def Register(self):
      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=1265,width=2000)
      self.img=ImageTk.PhotoImage(file=r"D:\Project Build A Thon\New folder\del.jpg")
      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=2000,height=1265)
      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=104,y=130,height=450,width=630)
      label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),fg="black",bg='white')
      label1.place(x=45,y=20)
      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),fg='black',bg='white')
      label2.place(x=30,y=95)
      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry.place(x=30,y=145,width=270,height=35)
      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),fg='black',bg='white')
      label3.place(x=30,y=195)
      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry2.place(x=30,y=245,width=270,height=35)
      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),fg='black',bg='white')
      label4.place(x=330,y=95)
      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry3.place(x=330,y=145,width=270,height=35)
      label5=Label(frame_input2,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='black',bg='white')
      label5.place(x=330,y=195)
      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry4.place(x=330,y=245,width=270,height=35)
         #btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="black",bg="black",bd=0)#width=15,height=1
         #btn2.place(x=30,y=195)
      btn4=Button(frame_input2,text="Register",command=self.register,cursor="hand2",font=("times new roman",15),fg="white",bg="black",bd=0,width=15,height=1)
      btn4.place(x=240,y=340)
      btn5=Button(frame_input2,command=self.loginform,text="Already Registered?Login",cursor="hand2",font=("times new roman",12),fg="black",bg="white",bd=0)
      btn5.place(x=242,y=390)
   
      
   def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      elif self.entry2.get()!=self.entry4.get():

         messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)

      else:

         try:

            con=pymysql.connect(host="localhost",user="root",password="Riya",database="frozenfood")

            cur=con.cursor()

            cur.execute("select * from register where emailid=%s",self.entry3.get())

            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)

               self.regclear()

               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)",(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get()))

               con.commit()

               con.close()

               messagebox.showinfo("Success","Register Succesfull",parent=self.root)

               self.regclear()

         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
   
   def appscreen(self):
      
      self.root.geometry("1500x1265+0+0")
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=1265,width=2000)
      
      label1=Label(Frame_login,text="Welcome to Frozen Foods..",font=('times new roman',30,'bold'),fg="black",bg='white')
      label1.place(x=375,y=15)
      
      self.img1=ImageTk.PhotoImage(file="berriesblue.jpg")
      img=Label(Frame_login,image=self.img1).place(x=10,y=70)
      
      l1=Label(Frame_login,text="Blueberries ₹1000/Kg",font=('times new roman',15,'bold'),fg="black",bg="lightgrey")
      l1.place(x=10,y=80)
      
      self.img2=ImageTk.PhotoImage(file="peas.jpg")
      img=Label(Frame_login,image=self.img2).place(x=300,y=70)
      
      l2=Label(Frame_login,text="Green-Peas ₹300/Kg",font=('times new roman',15,'bold'),fg="black",bg="lightgrey")
      l2.place(x=300,y=80)
      
      self.img3=ImageTk.PhotoImage(file="3.jpg")
      img=Label(Frame_login,image=self.img3).place(x=10,y=300)
      
      l3=Label(Frame_login,text="Blackberries ₹750/Kg",font=('times new roman',15,'bold'),fg="black",bg="lightgrey")
      l3.place(x=10,y=310)
      
      self.img4=ImageTk.PhotoImage(file="cranberries.jpg")
      img=Label(Frame_login,image=self.img4).place(x=300,y=300)
      
      l4=Label(Frame_login,text="Cranberries ₹1200/Kg",font=('times new roman',15,'bold'),fg="black",bg="lightgrey")
      l4.place(x=300,y=310)
      
      self.img5=ImageTk.PhotoImage(file="strawbeeries.jpg")
      img=Label(Frame_login,image=self.img5).place(x=10,y=530)
      
      l5=Label(Frame_login,text="Strawberries ₹350/Kg",font=('times new roman',15,'bold'),fg="black",bg="lightgrey")
      l5.place(x=10,y=540)
      
      self.img6=ImageTk.PhotoImage(file="raspberries.jpeg")
      img=Label(Frame_login,image=self.img6).place(x=300,y=530)
      
      l6=Label(Frame_login,text="Raspberries ₹1200/Kg",font=('times new roman',15,'bold'),fg="black",bg="lightgrey")
      l6.place(x=300,y=540)
      
      self.img7=ImageTk.PhotoImage(file="muscat.jpg")
      img=Label(Frame_login,image=self.img7).place(x=600,y=70)
      
      l7=Label(Frame_login,text="Muscat ₹500/Kg",font=('times new roman',15,'bold'),fg="black",bg="lightgrey")
      l7.place(x=600,y=80)
      
      btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",17),fg="white",bg="black",bd=0,width=9,height=1)
      btn2.place(x=1350,y=20)
      
      self.img8=ImageTk.PhotoImage(file="dragonfruit.jpg")
      img=Label(Frame_login,image=self.img8).place(x=600,y=300)
      
      l8=Label(Frame_login,text="Dragonfruit ₹1500/Kg",font=('times new roman',15,'bold'),fg="black",bg="lightgrey")
      l8.place(x=600,y=320)
      
      self.img9=ImageTk.PhotoImage(file="BlackCurrant.jpg")
      img=Label(Frame_login,image=self.img9).place(x=600,y=530)
      
      l9=Label(Frame_login,text="BlackCurrant ₹1000/Kg",font=('times new roman',15,'bold'),fg="black",bg="lightgrey")
      l9.place(x=600,y=540)
      
      f1 = Frame(self.root,bd=5,bg='lightgrey')
      f1.place(x=930,y=70,height=650,width=550)
      
      blueberries = StringVar()
      greenpeas  = StringVar()
      blackberries = StringVar()
      cranberries = StringVar()
      strawberries = StringVar()
      raspberries  = StringVar()
      muscat  = StringVar()
      dragonfruit= StringVar()
      blackcurrant  = StringVar()
      total_bill = IntVar()
      
      lbl_bb = Label(f1, font=('times new roman',15,'bold'),text='Blueberries',width=15,fg='black')
      lbl_bb.place(x=50,y=40)
      
      lbl_gp = Label(f1, font=('times new roman',15,'bold'),text='Green-peas',width=15,fg='black')
      lbl_gp.place(x=50,y=80)
      
      lbl_blb = Label(f1, font=('times new roman',15,'bold'),text='Blackberries',width=15,fg='black')
      lbl_blb.place(x=50,y=120)
      
      lbl_cb = Label(f1, font=('times new roman',15,'bold'),text='Cranberries',width=15,fg='black')
      lbl_cb.place(x=50,y=160)
      
      lbl_sb = Label(f1, font=('times new roman',15,'bold'),text='Strawberries',width=15,fg='black')
      lbl_sb.place(x=50,y=200)
      
      lbl_rb = Label(f1, font=('times new roman',15,'bold'),text='Raspberries',width=15,fg='black')
      lbl_rb.place(x=50,y=240)
      
      lbl_mu = Label(f1, font=('times new roman',15,'bold'),text='Muscat',width=15,fg='black')
      lbl_mu.place(x=50,y=280)
      
      lbl_db = Label(f1, font=('times new roman',15,'bold'),text='Dragon-Fruit',width=15,fg='black')
      lbl_db.place(x=50,y=320)
      
      lbl_bc = Label(f1, font=('times new roman',15,'bold'),text='Black Currant',width=15,fg='black')
      lbl_bc.place(x=50,y=360)
      
      
      
      
      self.entry_bb = Entry(f1,font=('times new roman',15,'bold'),textvariable = blueberries, bd = 4, width = 9, bg='lightgrey' )
      self.entry_bb.place(x=350,y=40,width=150,height=30)

      self.entry_gp = Entry(f1,font=('times new roman',15,'bold'),textvariable = greenpeas, bd = 4, width = 9, bg='lightgrey' )
      self.entry_gp.place(x=350,y=80,width=150,height=30)
      
      self.entry_blb = Entry(f1,font=('times new roman',15,'bold'),textvariable = blackberries, bd = 4, width = 9, bg='lightgrey' )
      self.entry_blb.place(x=350,y=120,width=150,height=30)
      
      self.entry_cb = Entry(f1,font=('times new roman',15,'bold'),textvariable = cranberries, bd = 4, width = 9, bg='lightgrey' )
      self.entry_cb.place(x=350,y=160,width=150,height=30)
      
      self.entry_sb = Entry(f1,font=('times new roman',15,'bold'),textvariable = strawberries, bd = 4, width = 9, bg='lightgrey' )
      self.entry_sb.place(x=350,y=200,width=150,height=30)
      
      self.entry_rb = Entry(f1,font=('times new roman',15,'bold'),textvariable = raspberries, bd = 4, width = 9, bg='lightgrey' )
      self.entry_rb.place(x=350,y=240,width=150,height=30)
      
      self.entry_mm = Entry(f1,font=('times new roman',15,'bold'),textvariable = muscat, bd = 4, width = 9, bg='lightgrey' )
      self.entry_mm.place(x=350,y=280,width=150,height=30)
      
      self.entry_df = Entry(f1,font=('times new roman',15,'bold'),textvariable = dragonfruit, bd = 4, width = 9, bg='lightgrey' )
      self.entry_df.place(x=350,y=320,width=150,height=30)
      
      self.entry_bc = Entry(f1,font=('times new roman',15,'bold'),textvariable = blackcurrant, bd = 4, width = 9, bg='lightgrey' )
      self.entry_bc.place(x=350,y=360,width=150,height=30)
      
      btn_reset = Button(f1,bd=3,fg='white',bg='black',font=('times new roman',12,'bold'),width=10,text="Reset",command=self.Reset)
      btn_reset.place(x=100,y=400)
      
      #btn_total = Button(f2,bd=3,fg='white',bg='black',font=('times new roman',12,'bold'),width=10,text="Total",command=self.Total)
      #btn_total.place(x=370,y=400)
      
      #Bill = Label(f1,text="Bill",font=('times new roman',25,'bold'),fg='black',bg ='lightgrey',highlightthickness=2)
      #Bill.place(x=245,y=450)
      
      btn_total = Button(f1,bd=7,fg='white',bg='black',font=('times new roman',12,'bold'),width=10,text="Total",command=self.Total)
      btn_total.place(x=300,y=400)
      
      lbl_totl = Label(f1, font=('times new roman',15,'bold'),text=('Total Bill Amount: ₹',total_bill),width=30,fg='black')
      lbl_totl.place(x=50,y=470)
      
      #lbl_total = Label(f2,font=('times new roman',20,'bold'),text="Total",width=10,fg='black',bg='lightgrey')
      #lbl_total.place(x=20,y=100)
      
      ''' string_bill="₹",str(self.totalcost.get())
      self.total_bill.set(string_bill)
      
      entry_total = Entry(self.f2,font=('times new roman',20,'bold'),textvariable=self.total_bill,bd=5,width=15,bg='lightgrey',fg='black')
      entry_total.place(x=120,y=100)'''
   
   def Reset(self):
      self.entry_bb.delete(0,END)
      self.entry_gp.delete(0,END)
      self.entry_blb.delete(0,END)
      self.entry_cb.delete(0,END)
      self.entry_sb.delete(0,END)
      self.entry_rb.delete(0,END)
      self.entry_mm.delete(0,END)
      self.entry_df.delete(0,END)
      self.entry_bc.delete(0,END)
      
      
   def Total(self):
      try:
         a1=int(self.entry_bb.get())
      except:
         a1=0
         
      try:
         a2=int(self.entry_gp.get())
      except:
         a2=0
         
      try:
         a3=int(self.entry_blb.get())
      except:
         a3=0
         
      try:
         a4=int(self.entry_cb.get())
      except:
         a4=0
         
      try:
         a5=int(self.entry_sb.get())
      except:
         a5=0
         
      try:
         a6=int(self.entry_rb.get())
      except:
         a6=0
         
      try:
         a7=int(self.entry_mm.get())
      except:
         a7=0
         
      try:
         a8=int(self.entry_df.get())
      except:
         a8=0
         
      try:
         a9=int(self.entry_bc.get())
      except:
         a9=0
         
      c1 = a1 * 1000
      c2 = a2 * 300
      c3 = a3 * 750
      c4 = a4 * 1200
      c5 = a5 * 350
      c6 = a6 * 1200
      c7 = a7 * 500
      c8 = a8 * 1500
      c9 = a9 * 1000
      
      total_cost = c1+c2+c3+c4+c5+c6+c7+c8+c9
      #string_bill="₹",str('%.2f' %total_cost)
      self.total_bill = total_cost
      
      
   
      
   
   def regclear(self):
      self.entry.delete(0,END)
      self.entry2.delete(0,END)
      self.entry3.delete(0,END)
      self.entry4.delete(0,END)

   def loginclear(self):
      self.email_txt.delete(0,END)
      self.password.delete(0,END)

root=Tk()
ob=Login(root)
root.mainloop()

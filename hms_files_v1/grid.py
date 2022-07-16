from cProfile import label
from cgitb import text
from ctypes import addressof
from distutils.cmd import Command
import tkinter as tk
from tkinter import Canvas, ttk
from tkinter.messagebox import NO
from turtle import width
from urllib import response
from PIL import Image, ImageTk

#private files are importing:
import login_check
#import main_page

class main_window():
    def __init__(self):
       self.root1 = tk.Tk()
       self.canvas=Canvas()
       self.screem_width=int(self.root1.winfo_screenwidth())
       self.screem_height=int(self.root1.winfo_screenheight())
       self.root1.geometry(f'{self.screem_width-40}x{self.screem_height-40}+0+0')
       self.root1.resizable(True,True)
       self.root1.title("HMS")
    def login_page(self):
        self.login_page_frame1= tk.Frame(self.root1,width=self.screem_width,height=self.screem_height)
        self.login_page_frame1.place(x=0,y=0)

        """
        self.bg = tk.PhotoImage(file = "home_image.png")
  
        # Show image using label
        self.label1 = ttk.Label( self.login_page_frame1, image = self.bg)
        self.label1.place(x = 0, y = 0)
        
        self.image = Image.open('home_image.png')
        self.resize_image = self.image.resize((self.screem_width, self.screem_height))        self.img = ImageTk.PhotoImage(self.resize_image)
        self.img = ImageTk.PhotoImage(self.resize_image)
        # create label and add resize image
        self.label1 = tk.Label(self.login_page_frame1,image=self.img)
        self.label1.image = self.img
        self.label1.place(x=1,y=1)
   
        self.img = tk.PhotoImage(file='home_image.png')
        self.label = tk.Label(self.login_page_frame1,image=self.img,width=self.screem_width,height=self.screem_height)

        self.label.place(x=0, y=0)
        """
        #declaring string variables to store role and reg_id and password
        self.value_inside = tk.StringVar(self.login_page_frame1)
        self.reg_id_var=tk.StringVar(self.login_page_frame1)
        self.password_var=tk.StringVar(self.login_page_frame1)

        self.home_title=tk.Label(self.login_page_frame1,text='HOSPITAL MANAGEMENT SYSTEM',font=('calibre',45,'italic'),fg='green')
        self.home_title.place(x=250, y=200)



        self.role = ttk.Label(self.login_page_frame1,text='user role',font=('calibre',15))
        self.role.place(x=600, y=430)
        self.reg_id = ttk.Label(self.login_page_frame1,text="Reg ID",font=('calibre',15))
        self.reg_id.place(x=600, y=470)
        self.password=ttk.Label(self.login_page_frame1,text='Password',font=('calibre',15))
        self.password.place(x=600, y=510)


        self.value_inside.set('select role')
        self.roles_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.role_entry = ttk.OptionMenu(self.login_page_frame1,self.value_inside , *self.roles_list)
        self.role_entry.configure(width=38)

        self.role_entry.place(x=720,y=430)
        print("the valuse on the roles:",self.value_inside.get())

        self.reg_id_entry = tk.Entry(self.login_page_frame1,textvariable= self.reg_id_var,font=('calibre',17)).place(x=720,y=470)
        self.password_entry = tk.Entry(self.login_page_frame1, textvariable = self.password_var, font=('calibre',17),show="*").place(x=720,y=510)
        
        
        
        self.submit_botton = tk.Button(self.login_page_frame1,text='submit',width=13,height=1,bg='red',command=self.login_check_fun)
        #,command=logincheck
        #submit_botton.config(width=50,height=5)
        self.submit_botton.place(x=690,y=570)
        self.reset_button = tk.Button(self.login_page_frame1,text='Reset',width=13,height=1,bg='red',command=self.reser_button_responce)
        #,command=logincheck
        self.reset_button.place(x=840,y=570)
        #role_entry = tk.Entry(root,textvariable=role_var,font=('calibre',17)).place(x=720,y=430)
        self.root1.mainloop()
        

    def reser_button_responce(self):
        self.value_inside.set('select role')
        self.reg_id_var.set('')
        self.password_var.set('')

    def login_check_fun(self):
              print(self.value_inside.get(),self.reg_id_var.get(),self.password_var.get())
              self.response = login_check.username_password_check(login_check.mydb,self.value_inside.get(),self.reg_id_var.get(),self.password_var.get())
              if self.response == 'true':
                       #return  self.response
                       self.login_page_frame1.destroy()
                       self.login_page_frame1 =None
                       self.main_page()
                       
              else:
                       #return  self.response
                       pass

    def main_page(self):

        #main_page_frame_view1------start-------------
        self.main_page_frame_view1=tk.Frame(self.root1,bg='red')
        self.main_page_frame_view1.pack(ipadx=770,ipady=20,side='top',fill='y')
        self.main_page_frame_view1['borderwidth']=0
        #main_page_frame_view1------end-------------

        
        
        #main_page_frame_view2------start-------------
        self.main_page_frame_view2=tk.Frame(self.root1,bg='yellow')
        self.main_page_frame_view2.pack(ipadx=10,ipady=100,side='left',fill='y')
        self.main_page_frame_view2['borderwidth']=0
        



        self.label1= tk.Button(self.main_page_frame_view2,text="patient_registration",command=self.patient_registration)
        self.label1.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label11= tk.Button(self.main_page_frame_view2,text="mp_button2",command=self.mp_button2)
        self.label11.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label12= tk.Button(self.main_page_frame_view2,text="mp_button3")
        self.label12.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label13= tk.Button(self.main_page_frame_view2,text="mp_button4")
        self.label13.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label14= tk.Button(self.main_page_frame_view2,text="mp_button5")
        self.label14.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label15= tk.Button(self.main_page_frame_view2,text="mp_button6")
        self.label15.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label16= tk.Button(self.main_page_frame_view2,text="mp_button8")
        self.label16.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label17= tk.Button(self.main_page_frame_view2,text="`mp_button9`")
        self.label17.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        #side='top',
        #main_page_frame_view2------end-------------

        #main_page_frame_view3------start-------------

        self.main_page_frame_view3=tk.Frame(self.root1,bg='blue')
        self.main_page_frame_view3.pack(ipadx=550,ipady=370,side='top')
        self.main_page_frame_view3['borderwidth']=0
 
        
        self.label2= tk.Label(self.main_page_frame_view3,text="main_page_frame_view3")
        self.label2.place(x=10,y=100)
        self.label21= tk.Label(self.main_page_frame_view3,text="main_page_frame_view3")
        self.label21.pack(side='bottom')
        self.label22= tk.Label(self.main_page_frame_view3,text="main_page_frame_view3")
        self.label22.pack(side='right')
        self.label23= tk.Label(self.main_page_frame_view3,text="main_page_frame_view3")
        self.label23.pack(side='top')
        
        """
        self.frame3_frame2_1=tk.Frame(self.main_page_frame_view3,bg='orange')
        label11111=tk.Label(self.frame3_frame2_1,text="self.frame3_frame2_1")
        self.frame3_frame2_1.place(x=0,y=0)
        """
        #main_page_frame_view3------end-------------



        #main_page_frame_view4------start------------- 
        self.main_page_frame_view4=tk.Frame(self.root1,bg='green')
        self.main_page_frame_view4['borderwidth']=0


        """
        self.label3= tk.Label(self.main_page_frame_view4,text="main_page_frame_view4")
        self.label3.pack(side='left')
        self.label31= tk.Label(self.main_page_frame_view4,text="main_page_frame_view4")
        self.label31.pack(side='bottom')
        self.label32= tk.Label(self.main_page_frame_view4,text="main_page_frame_view4")
        self.label32.pack(side='right')
        self.label33= tk.Label(self.main_page_frame_view4,text="main_page_frame_view4")
        self.label33.pack(side='top')
        #self.label1.config(command=self.destroy_main_page_frame_view3)
        """

        self.label31_patient_registration = tk.Label(self.main_page_frame_view4,text="patient registration",bg='blue')
        self.label31_patient_registration.place(x=5,y=5,width=1300,height=40)

        self.button1_save = tk.Button(self.main_page_frame_view4,text="save")
        self.button1_save.place(x=5,y=50,width=50,height=50)

        self.button1_update = tk.Button(self.main_page_frame_view4,text="update")
        self.button1_update.place(x=60,y=50,width=50,height=50)

        self.button1_delete = tk.Button(self.main_page_frame_view4,text="delete")
        self.button1_delete.place(x=115,y=50,width=50,height=50)

        self.button1_clear = tk.Button(self.main_page_frame_view4,text="clear")
        self.button1_clear.place(x=170,y=50,width=50,height=50)

        self.button1_exit = tk.Button(self.main_page_frame_view4,text="exit")
        self.button1_exit.place(x=225,y=50,width=50,height=50)

         # box1 objects ------start------------
        

        self.label33_uniqueid = tk.Label(self.main_page_frame_view4,text="Unique ID")
        self.label33_uniqueid.place(x=200,y=100,width=100,height=1)

        self.label34_regdate = tk.Label(self.main_page_frame_view4,text="Reg Date")
        self.label34_regdate.place(x=200,y=100,width=100,height=1)

        self.label35_entername = tk.Label(self.main_page_frame_view4,text="Enter Name")
        self.label35_entername.place(x=200,y=100,width=100,height=1)

        self.label36_birthdate = tk.Label(self.main_page_frame_view4,text="Birth Date")
        self.label36_birthdate.place(x=200,y=100,width=100,height=1)

        self.label37_age = tk.Label(self.main_page_frame_view4,text="Age")
        self.label37_age.place(x=200,y=100,width=100,height=1)

        self.label38_address = tk.Label(self.main_page_frame_view4,text="Address")
        self.label38_address.place(x=200,y=100,width=100,height=1)

        self.label39_city = tk.Label(self.main_page_frame_view4,text="City")
        self.label39_city.place(x=200,y=100,width=100,height=1)

        self.label311_phoneno1 = tk.Label(self.main_page_frame_view4,text="Phone NO1")
        self.label311_phoneno1.place(x=200,y=100,width=100,height=1)

        self.label312_phoneno2 = tk.Label(self.main_page_frame_view4,text="Phone NO2")
        self.label312_phoneno2.place(x=200,y=100,width=100,height=1)

        self.label313_gender = tk.Label(self.main_page_frame_view4,text="Gender")
        self.label313_gender.place(x=200,y=100,width=100,height=1)

        self.label314_bloodgroup = tk.Label(self.main_page_frame_view4,text="Blood Group")
        self.label314_bloodgroup.place(x=200,y=100,width=100,height=1)

        self.label315_emailid = tk.Label(self.main_page_frame_view4,text="Email ID")
        self.label315_emailid.place(x=200,y=100,width=100,height=1)

        self.label316_photo = tk.Label(self.main_page_frame_view4,text="Photo")
        self.label316_photo.place(x=200,y=100,width=100,height=1) 

        self.label317_companydetails = tk.Label(self.main_page_frame_view4,text="Company Details")
        self.label317_companydetails.place(x=200,y=100,width=100,height=1)
        # box1 objects ------end------------
        
        # box2 objects ------start------------
        self.button1_start = tk.Button(self.main_page_frame_view4,text="Start")
        self.button1_start.place(x=995,y=370,width=90,height=35)

        self.button1_capture = tk.Button(self.main_page_frame_view4,text="Capture")
        self.button1_capture.place(x=1095,y=370,width=90,height=35)

        self.button1_browse = tk.Button(self.main_page_frame_view4,text="Browse")
        self.button1_browse.place(x=995,y=415,width=90,height=35)

        self.button1_remove = tk.Button(self.main_page_frame_view4,text="Exit")
        self.button1_remove.place(x=1095,y=415,width=90,height=35)
        # box2 objects ------end------------

        # box3 objects ------start------------

        # box3 objects ------end------------

        # box4 objects ------start------------
        self.button1_companyname = tk.Label(self.main_page_frame_view4,text="Company Name")
        self.button1_companyname.place(x=930,y=560,width=100,height=25)
        
        self.box4_value_inside = tk.StringVar(self.main_page_frame_view4)
        self.box4_value_inside.set('---select---')
        self.box4_roles_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.box4_role_entry = ttk.OptionMenu(self.main_page_frame_view4,self.box4_value_inside , *self.box4_roles_list)
        self.box4_role_entry.configure(width=25)
        self.box4_role_entry.place(x=1070,y=560)
        #,width=100,height=25


        self.button1_isdependent = tk.Label(self.main_page_frame_view4,text="Is dependent")
        self.button1_isdependent.place(x=930,y=600,width=100,height=25)
        self.box4_Checkbutton1_yes = tk.Checkbutton(self.main_page_frame_view4,text="Yes")
        self.box4_Checkbutton1_yes.place(x=1070,y=600,width=50,height=25)
        self.box4_Checkbutton1_no = tk.Checkbutton(self.main_page_frame_view4,text="No")
        self.box4_Checkbutton1_no.place(x=1140,y=600,width=50,height=25)

        self.button1_relationto = tk.Label(self.main_page_frame_view4,text="Reletion To")
        self.button1_relationto.place(x=930,y=640,width=100,height=25)
        self.box4_relationto_entry = tk.Entry(self.main_page_frame_view4,text="No")
        self.box4_relationto_entry.place(x=1070,y=640,width=100,height=25)

        self.button1_emailid = tk.Label(self.main_page_frame_view4,text="Email ID")
        self.button1_emailid.place(x=930,y=680,width=100,height=25)
        self.box4_emailid_entry = tk.Entry(self.main_page_frame_view4,text="No")
        self.box4_emailid_entry.place(x=1070,y=680,width=100,height=25)

        # box4 objects ------end------------


                #box1
        self.label32_patient_details=tk.Label(self.main_page_frame_view4,text="patient details",bg='green')
        self.label32_patient_details.place(x=5,y=110,width=90,height=20)

        self.line1_box1_top = tk.Label(self.main_page_frame_view4,text="",bg='black')
        self.line1_box1_top.place(x=100,y=120,width=785,height=1)

        self.line2_box1_right=Canvas(self.main_page_frame_view4,width=1,height=200,bg='black')
        self.line2_box1_right.place(x=885,y=120,width=1,height=370)
        self.line2_box1_right.create_line(300, 35, 300, 200, dash = (5, 2))

        self.line3_box1_bottom = tk.Label(self.main_page_frame_view4,text="",bg='black')
        self.line3_box1_bottom.place(x=5,y=490,width=880,height=1)


        self.line4_box1_left=Canvas(self.main_page_frame_view4,width=1,height=200,bg='black')
        self.line4_box1_left.place(x=5,y=120,width=1,height=370)
        self.line4_box1_left.create_line(300, 35, 300, 200, dash = (5, 2))

                 #box2

        self.label32_photo=tk.Label(self.main_page_frame_view4,text="photo",bg='green')
        self.label32_photo.place(x=900,y=110,width=50,height=20)

        self.line5_box2_top = tk.Label(self.main_page_frame_view4,text="",bg='black')
        self.line5_box2_top.place(x=950,y=120,width=320,height=1)

        self.line6_box2_right=Canvas(self.main_page_frame_view4,width=1,height=200,bg='black')
        self.line6_box2_right.place(x=1270,y=120,width=1,height=370)
        self.line6_box2_right.create_line(300, 35, 300, 200, dash = (5, 2)) 

        self.line7_box2_bottom = tk.Label(self.main_page_frame_view4,text="",bg='black')
        self.line7_box2_bottom.place(x=900,y=490,width=370,height=1)

        self.line8_box2_left=Canvas(self.main_page_frame_view4,width=1,height=200,bg='black')
        self.line8_box2_left.place(x=900,y=120,width=1,height=370)
        self.line8_box2_left.create_line(300, 35, 300, 200, dash = (5, 2))

                  #box3
        
        self.line9_box3_top = tk.Label(self.main_page_frame_view4,text="",bg='black')
        self.line9_box3_top.place(x=5,y=505,width=880,height=1)

        self.line10_box3_right =Canvas(self.main_page_frame_view4,width=1,height=200,bg='black')
        self.line10_box3_right .place(x=885,y=505,width=1,height=240)
        self.line10_box3_right .create_line(300, 35, 300, 200, dash = (5, 2))

        self.line11_box3_bottom = tk.Label(self.main_page_frame_view4,text="",bg='black')
        self.line11_box3_bottom.place(x=5,y=745,width=880,height=1)

        self.line12_box3_left =Canvas(self.main_page_frame_view4,bg='black')
        #self.line12_box3_left.configure(bg='black') 
        self.line12_box3_left .place(x=5,y=505,width=1,height=240)
        self.line12_box3_left .create_line(300, 35, 300, 200, dash = (5, 2))

        

             #box 4

        self.label32_company_details=tk.Label(self.main_page_frame_view4,text="Company Details",bg='green')
        self.label32_company_details.place(x=900,y=495,width=100,height=20)

        self.line13_box4_top = tk.Label(self.main_page_frame_view4,text="",bg='black')
        self.line13_box4_top.place(x=1000,y=505,width=270,height=1)

        #creating vertical line of box4
        self.line14_box4_right =Canvas(self.main_page_frame_view4,width=1,height=200,bg='black')
        self.line14_box4_right .place(x=1270,y=505,width=1,height=240)
        self.line14_box4_right .create_line(300, 35, 300, 200, dash = (5, 2))

        

        self.line15_box4_bottom = tk.Label(self.main_page_frame_view4,text="",bg='black')
        self.line15_box4_bottom.place(x=900,y=745,width=370,height=1)

        #creating vertical line of box4 left
        self.line16_box4_left =Canvas(self.main_page_frame_view4,width=1,height=200,bg='black')
        self.line16_box4_left .place(x=900,y=505,width=1,height=240)
        self.line16_box4_left .create_line(300, 35, 300, 200, dash = (5, 2))

        #main_page_frame_view4-------end--------------





        #main_page_frame_view5------start-------------
        self.main_page_frame_view5=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view5['borderwidth']=0
        
        #self.label4= tk.Label(self.main_page_frame_view5,text="main_page_frame_view5",Command = self.loop_1)
        #self.label4.pack(side='left')
        self.label41= tk.Label(self.main_page_frame_view5,text="main_page_frame_view5")
        self.label41.pack(side='bottom')
        self.label42= tk.Label(self.main_page_frame_view5,text="main_page_frame_view5")
        self.label42.pack(side='right')
        self.label43= tk.Label(self.main_page_frame_view5,text="main_page_frame_view5")
        self.label43.pack(side='top')
        self.label44= tk.Label(self.main_page_frame_view5,text="main_page_frame_view5")
        self.label44.pack(side='left')

        #main_page_frame_view5------end-------------

        #main_page_frame_view6------start-------------
        self.main_page_frame_view6=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view6['borderwidth']=0

        self.label5= tk.Label(self.main_page_frame_view6,text="main_page_frame_view6")
        self.label5.pack(side='left')
        self.label51= tk.Label(self.main_page_frame_view6,text="main_page_frame_view6")
        self.label51.pack(side='bottom')
        self.label52= tk.Label(self.main_page_frame_view6,text="main_page_frame_view6")
        self.label52.pack(side='right')
        self.label53= tk.Label(self.main_page_frame_view6,text="main_page_frame_view6")
        self.label53.pack(side='top')
        #main_page_frame_view6------end-------------

        #main_page_frame_view7------start-------------
        self.main_page_frame_view7=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view7['borderwidth']=0

        self.label6= tk.Label(self.main_page_frame_view7,text="main_page_frame_view7")
        self.label6.pack(side='left')
        self.label61= tk.Label(self.main_page_frame_view7,text="main_page_frame_view7")
        self.label61.pack(side='bottom')
        self.label62= tk.Label(self.main_page_frame_view7,text="main_page_frame_view7")
        self.label62.pack(side='right')
        self.label63= tk.Label(self.main_page_frame_view7,text="main_page_frame_view7")
        self.label63.pack(side='top')
        #main_page_frame_view7------end-------------


    def loop_1(self):
            self.label456 = None
            self.x11,self.y11= 0
            for  self.a in range(0,10):
                self.label456= tk.Label(self.main_page_frame_view5,text="main_page_frame_view5")
                self.y11 = self.y11 + 20
                self.label456.place(x=self.x11,y=self.y11)

    def frames_status(self):
             pass
             #print("login_page_frame1 status:",self.login_page_frame1)
             #print("main_page_frame_view1 status:",self.main_page_frame_view1)
             #print("main_page_frame_view2 status:",self.main_page_frame_view2)
             #print("main_page_frame_view3 status:",self.main_page_frame_view3)
             #print("main_page_frame_view4 status:",self.main_page_frame_view4)
             #print("main_page_frame_view5 status:",self.main_page_frame_view5)
             #print("main_page_frame_view6 status:",self.main_page_frame_view6)
             #print("main_page_frame_view7 status:",self.main_page_frame_view7)
    


    def patient_registration(self):
             
             self.main_page_frame_view3_before_destroy = None
             self.main_page_frame_view4_before_destroy = None
             self.main_page_frame_view5_before_destroy = None
             print("+++++++++++++++++++++++++++++++++++++++++")
             print("destroy_main_page_frame_view3 function")
    
             self.frames_status()
             if self.main_page_frame_view3 == None:
                pass
             else:
                 print("destroy_main_page_frame_view3 destroyed")
                 #self.main_page_frame_view3_before_destroy = self.main_page_frame_view3
                 self.main_page_frame_view3.pack_forget()
                 #self.main_page_frame_view3 = self.main_page_frame_view3_before_destroy
             self.frames_status()
             #self.main_page_frame_view3 = None
             if self.main_page_frame_view5 == None:
                    pass
             else:
                 print("destroy_main_page_frame_view5 destroyed")
                 #self.main_page_frame_view5_before_destroy = self.main_page_frame_view5
                 self.main_page_frame_view5.pack_forget()
                 
                 #self.main_page_frame_view5 = self.main_page_frame_view5_before_destroy 
             self.frames_status()
             print("main_page_frame_view4 activated")
             #self.main_page_frame_view4_before_destroy = self.main_page_frame_view4
             self.main_page_frame_view4.pack(ipadx=670,ipady=390,side='top')
             self.frames_status()
             print("+++++++++++++++++++++++++++++++++++++++++")


    def mp_button2(self):
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("search_button function")
        self.frames_status()
        self.frames_status()
        if self.main_page_frame_view3 == None:
                pass
        else:
                 print("destroy_main_page_frame_view3 destroyed")
                 self.main_page_frame_view3.pack_forget()
                 #self.main_page_frame_view3 = self.main_page_frame_view3_before_destroy
                 #self.main_page_frame_view3 = None
        self.frames_status()
        if self.main_page_frame_view4 == None:
                pass
        else:
            print("destroy_main_page_frame_view4 destroyed")
            #self.main_page_frame_view4 = self.main_page_frame_view4_before_destroy
            self.main_page_frame_view4.pack_forget()
            #self.main_page_frame_view4 = None
        
        #self.main_page_frame_view4 = None
        #self.main_page_frame_view4.destroy()
        self.frames_status()
        print("main_page_frame_view5 before changing",self.main_page_frame_view5)
        #self.main_page_frame_view5 = self.main_page_frame_view5_before_destroy
        print("main_page_frame_view5 after changing",self.main_page_frame_view5)
        
        self.main_page_frame_view5.pack(ipadx=670,ipady=370,side='top')
        print("+++++++++++++++++++++++++++++++++++++++++")

        


    
           
             
    
    
        
        

  



x=main_window()
x.login_page()
my = login_check.mydb
my.close()

       
     
from cProfile import label
from cgitb import text
from ctypes import addressof
from distutils.cmd import Command
import tkinter as tk
from tkinter import Canvas, ttk
from tkinter.messagebox import NO
from turtle import bgcolor, width
from urllib import response
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


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
       self.root1.title("HOSPITAL MANAGEMENT SYSTEM BY PAVAN YENDLURI")
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
              #self.response = login_check.username_password_check(login_check.mydb,self.value_inside.get(),self.reg_id_var.get(),self.password_var.get())
              self.response = 'true'
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
        self.main_page_frame_view1.pack(ipadx=770,ipady=20,side='top')
        self.main_page_frame_view1['borderwidth']=0

        self.botton1_dialy_tasks = tk.Button(self.main_page_frame_view1,text="Dialy Tasks",command= self.main_page_frame_view1_dialy_tasks_default_frame_activate)
        self.botton1_dialy_tasks.place(x=650,y=5,width=100,height=32)

        #frames of  main_page_frame_view1 --> dialy tasks====start=============
        
        #frames of  main_page_frame_view1 --> dialy tasks-->default frame=========start==================
        self.main_page_frame_view1_dialy_tasks_default_frame=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view1_dialy_tasks_default_frame['borderwidth']=0

        self.main_page_frame_view1_dialy_tasks_default_frame_button1_dialy_attedence = tk.Button(self.main_page_frame_view1_dialy_tasks_default_frame,text= "dialy attdence",command = self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame_activate)
        self.main_page_frame_view1_dialy_tasks_default_frame_button1_dialy_attedence.place(x=200,y=100)
       
        self.main_page_frame_view1_dialy_tasks_default_frame_button2_view_dialy_attdence = tk.Button(self.main_page_frame_view1_dialy_tasks_default_frame,text= "View dialy attdence",command = self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_activate)
        self.main_page_frame_view1_dialy_tasks_default_frame_button2_view_dialy_attdence.place(x=200,y=100)

        self.main_page_frame_view1_dialy_tasks_default_frame_button3_add_dialy_work_done = tk.Button(self.main_page_frame_view1_dialy_tasks_default_frame,text= "Add dialy work done",command = self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_activate)
        self.main_page_frame_view1_dialy_tasks_default_frame_button3_add_dialy_work_done .place(x=300,y=100)
        
        self.main_page_frame_view1_dialy_tasks_default_frame_button4_update_work_done = tk.Button(self.main_page_frame_view1_dialy_tasks_default_frame,text= "Update Work Done",command = self.main_page_frame_view1_dialy_tasks_update_work_done_frame_activate)
        self.main_page_frame_view1_dialy_tasks_default_frame_button4_update_work_done.place(x=400,y=100)
        
        self.main_page_frame_view1_dialy_tasks_default_frame_button5_work_done = tk.Button(self.main_page_frame_view1_dialy_tasks_default_frame,text= "Work Done",command = self.main_page_frame_view1_dialy_tasks_work_done_frame_activate)
        self.main_page_frame_view1_dialy_tasks_default_frame_button5_work_done.place(x=500,y=100)
        

        #frames of  main_page_frame_view1 --> dialy tasks-->default frame=========start==================
        
        #frames of  main_page_frame_view1 --> dialy tasks-->dialy_attdence frame=========start==================
        self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame['borderwidth']=0
        tk.Button(self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame,text="")
        #frames of  main_page_frame_view1 --> dialy tasks-->dialy_attdence frame=========end==================

        #frames of  main_page_frame_view1 --> dialy tasks-->view_dialy_attdence frame=========start==================
        self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame['borderwidth']=0
        #frames of  main_page_frame_view1 --> dialy tasks-->view_dialy_attdence frame=========end==================

        #frames of  main_page_frame_view1 --> dialy tasks-->add_dialy_work_done frame=========start==================
        self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame['borderwidth']=0
        #frames of  main_page_frame_view1 --> dialy tasks-->add_dialy_work_done frame=========end==================

        #frames of  main_page_frame_view1 --> dialy tasks-->update_work_done frame=========start==================
        self.main_page_frame_view1_dialy_tasks_update_work_done_frame=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view1_dialy_tasks_update_work_done_frame['borderwidth']=0
        #frames of  main_page_frame_view1 --> dialy tasks-->update_work_done frame=========end==================

        #frames of  main_page_frame_view1 --> dialy tasks-->default frame=========start==================
        self.main_page_frame_view1_dialy_tasks_work_done_frame=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view1_dialy_tasks_work_done_frame['borderwidth']=0
        #frames of  main_page_frame_view1 --> dialy tasks-->default frame=========start==================

        #frames of  main_page_frame_view1 --> dialy tasks====end=============




        

        '''
        self.Menubar = tk.Menu(self.main_page_frame_view1)
        #self.Menubar.place(x=100,y=10)
        self.fileMenu  = tk.Menu(self.Menubar, tearoff=0)
        self.fileMenu .add_command(label="New", command=self.donothing)
        self.fileMenu .add_command(label="Open", command=self.donothing)
        self.fileMenu .add_command(label="Save", command=self.donothing)
        self.fileMenu .add_command(label="Save as...", command=self.donothing)
        self.fileMenu .add_command(label="Close", command=self.donothing)

        self.fileMenu .add_separator()
        self.fileMenu.add_command(label="Exit", command=self.main_page_frame_view1.quit)
        self.Menubar.add_cascade(label="File", menu=self.fileMenu )
        self.editMenu = tk.Menu(self.Menubar, tearoff=0)
        #self.editMenu.place(x=100,y=10)
        self.editMenu.add_command(label="Undo", command=self.donothing)

        self.editMenu.add_separator()

        self.editMenu.add_command(label="Cut", command=self.donothing)
        self.editMenu.add_command(label="Copy", command=self.donothing)
        self.editMenu.add_command(label="Paste", command=self.donothing)
        self.editMenu.add_command(label="Delete", command=self.donothing)
        self.editMenu.add_command(label="Select All", command=self.donothing)

        self.Menubar.add_cascade(label="Edit", Menu=self.editMenu)
        self.helpMenu = tk.Menu(self.Menubar, tearoff=0)
        #self.helpMenu.place(x=100,y=10)
        self.helpMenu.add_command(label="Help Index", command=self.donothing)
        self.helpMenu.add_command(label="About...", command=self.donothing)
        self.Menubar.add_cascade(label="Help", Menu=self.helpMenu)

        self.main_page_frame_view1.config(Menu=self.Menubar)
        '''
        
        #main_page_frame_view1------end-------------

        
        
        #main_page_frame_view2------start-------------

        self.main_page_frame_view2=tk.Frame(self.root1,bg='yellow')
        self.main_page_frame_view2.pack(ipadx=10,ipady=100,side='left',fill='y')
        self.main_page_frame_view2['borderwidth']=0
        



        self.label1= tk.Button(self.main_page_frame_view2,text="patient registration",command=self.patient_registration_default)
        self.label1.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label11= tk.Button(self.main_page_frame_view2,text="emergency registration",command=self.emergency_registration_default)
        self.label11.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label12= tk.Button(self.main_page_frame_view2,text="patient search",command=self.patient_search_default)
        self.label12.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label13= tk.Button(self.main_page_frame_view2,text="patient queue",command=self.patient_queue_default)
        self.label13.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label14= tk.Button(self.main_page_frame_view2,text="Lab queue",command=self.lab_queue_default)
        self.label14.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label15= tk.Button(self.main_page_frame_view2,text="opd queue",command=self.opd_queue_default)
        self.label15.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label16= tk.Button(self.main_page_frame_view2,text="physical management",command=self.physical_management_default)
        self.label16.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label17= tk.Button(self.main_page_frame_view2,text="`Dialy collection",command=self.dialy_collection_default)
        self.label17.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        #side='top',
        #main_page_frame_view2------end-------------

        #main_page_frame_view3------start-------------

        self.main_page_frame_view3_home_frame=tk.Frame(self.root1,bg='blue')
        self.main_page_frame_view3_home_frame.pack(ipadx=550,ipady=370,side='top')
        self.main_page_frame_view3_home_frame['borderwidth']=0
 
        
        self.label2= tk.Label(self.main_page_frame_view3_home_frame,text="main_page_frame_view3_home_frame")
        self.label2.place(x=10,y=100)
        self.label21= tk.Label(self.main_page_frame_view3_home_frame,text="main_page_frame_view3_home_frame")
        self.label21.pack(side='bottom')
        self.label22= tk.Label(self.main_page_frame_view3_home_frame,text="main_page_frame_view3_home_frame")
        self.label22.pack(side='right')
        self.label23= tk.Label(self.main_page_frame_view3_home_frame,text="main_page_frame_view3_home_frame")
        self.label23.pack(side='top')
        
        """
        self.frame3_frame2_1=tk.Frame(self.main_page_frame_view3,bg='orange')
        label11111=tk.Label(self.frame3_frame2_1,text="self.frame3_frame2_1")
        self.frame3_frame2_1.place(x=0,y=0)
        """
        #main_page_frame_view3------end-------------


       #main_page_frame_view3_patient_registration_default_frame------start------------- 
        self.main_page_frame_view3_patient_registration_default_frame=tk.Frame(self.root1,bg='green')
        self.main_page_frame_view3_patient_registration_default_frame['borderwidth']=0


        """
        self.label3= tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="main_page_frame_view3_patient_registration_default_frame")
        self.label3.pack(side='left')
        self.label31= tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="main_page_frame_view3_patient_registration_default_frame")
        self.label31.pack(side='bottom')
        self.label32= tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="main_page_frame_view3_patient_registration_default_frame")
        self.label32.pack(side='right')
        self.label33= tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="main_page_frame_view3_patient_registration_default_frame")
        self.label33.pack(side='top')
        #self.label1.config(command=self.destroy_main_page_frame_view3)
        """

        self.label31_patient_registration_default = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="patient registration",font=("lucida",15,"bold italic"),bg='blue')
        self.label31_patient_registration_default.place(x=5,y=5,width=1300,height=40)

        self.button1_save = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="save")
        self.button1_save.place(x=5,y=50,width=50,height=50)

        self.button1_update = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="update")
        self.button1_update.place(x=60,y=50,width=50,height=50)

        self.button1_delete = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="delete")
        self.button1_delete.place(x=115,y=50,width=50,height=50)

        self.button1_clear = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="clear")
        self.button1_clear.place(x=170,y=50,width=50,height=50)

        self.button1_exit = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="exit")
        self.button1_exit.place(x=225,y=50,width=50,height=50)

         # box1 objects ------start------------
        

        self.label33_uniqueid = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Unique ID")
        self.label33_uniqueid.place(x=200,y=100,width=100,height=1)

        self.label34_regdate = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Reg Date")
        self.label34_regdate.place(x=200,y=100,width=100,height=1)

        self.label35_entername = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Enter Name")
        self.label35_entername.place(x=200,y=100,width=100,height=1)

        self.label36_birthdate = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Birth Date")
        self.label36_birthdate.place(x=200,y=100,width=100,height=1)

        self.label37_age = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Age")
        self.label37_age.place(x=200,y=100,width=100,height=1)

        self.label38_address = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Address")
        self.label38_address.place(x=200,y=100,width=100,height=1)

        self.label39_city = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="City")
        self.label39_city.place(x=200,y=100,width=100,height=1)

        self.label311_phoneno1 = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Phone NO1")
        self.label311_phoneno1.place(x=200,y=100,width=100,height=1)

        self.label312_phoneno2 = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Phone NO2")
        self.label312_phoneno2.place(x=200,y=100,width=100,height=1)

        self.label313_gender = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Gender")
        self.label313_gender.place(x=200,y=100,width=100,height=1)

        self.label314_bloodgroup = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Blood Group")
        self.label314_bloodgroup.place(x=200,y=100,width=100,height=1)

        self.label315_emailid = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Email ID")
        self.label315_emailid.place(x=200,y=100,width=100,height=1)

        self.label316_photo = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Photo")
        self.label316_photo.place(x=200,y=100,width=100,height=1) 

        self.label317_companydetails = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Company Details")
        self.label317_companydetails.place(x=200,y=100,width=100,height=1)
        # box1 objects ------end------------
        
        # box2 objects ------start------------
        self.button1_start = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="Start")
        self.button1_start.place(x=995,y=370,width=90,height=35)

        self.button1_capture = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="Capture")
        self.button1_capture.place(x=1095,y=370,width=90,height=35)

        self.button1_browse = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="Browse")
        self.button1_browse.place(x=995,y=415,width=90,height=35)

        self.button1_remove = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="Exit")
        self.button1_remove.place(x=1095,y=415,width=90,height=35)
        # box2 objects ------end------------

        # box3 objects ------start------------

        # box3 objects ------end------------

        # box4 objects ------start------------
        self.button1_companyname = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Company Name")
        self.button1_companyname.place(x=930,y=560,width=100,height=25)
        
        self.box4_value_inside = tk.StringVar(self.main_page_frame_view3_patient_registration_default_frame)
        self.box4_value_inside.set('---select---')
        self.box4_roles_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.box4_role_entry = ttk.OptionMenu(self.main_page_frame_view3_patient_registration_default_frame,self.box4_value_inside , *self.box4_roles_list)
        self.box4_role_entry.configure(width=25)
        self.box4_role_entry.place(x=1070,y=560)
        #,width=100,height=25


        self.button1_isdependent = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Is dependent")
        self.button1_isdependent.place(x=930,y=600,width=100,height=25)
        self.box4_Checkbutton1_yes = tk.Checkbutton(self.main_page_frame_view3_patient_registration_default_frame,text="Yes")
        self.box4_Checkbutton1_yes.place(x=1070,y=600,width=50,height=25)
        self.box4_Checkbutton1_no = tk.Checkbutton(self.main_page_frame_view3_patient_registration_default_frame,text="No")
        self.box4_Checkbutton1_no.place(x=1140,y=600,width=50,height=25)

        self.button1_relationto = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Reletion To")
        self.button1_relationto.place(x=930,y=640,width=100,height=25)
        self.box4_relationto_entry = tk.Entry(self.main_page_frame_view3_patient_registration_default_frame)
        self.box4_relationto_entry.place(x=1070,y=640,width=100,height=25)

        self.button1_emailid = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Email ID")
        self.button1_emailid.place(x=930,y=680,width=100,height=25)
        self.box4_emailid_entry = tk.Entry(self.main_page_frame_view3_patient_registration_default_frame)
        self.box4_emailid_entry.place(x=1070,y=680,width=100,height=25)

        # box4 objects ------end------------


                #box1
        self.label32_patient_details=tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="patient details",bg='green')
        self.label32_patient_details.place(x=5,y=110,width=90,height=20)

        self.line1_box1_top = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line1_box1_top.place(x=100,y=120,width=785,height=1)

        self.line2_box1_right=Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black')
        self.line2_box1_right.place(x=885,y=120,width=1,height=370)
        self.line2_box1_right.create_line(300, 35, 300, 200, dash = (5, 2))

        self.line3_box1_bottom = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line3_box1_bottom.place(x=5,y=490,width=880,height=1)


        self.line4_box1_left=Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black')
        self.line4_box1_left.place(x=5,y=120,width=1,height=370)
        self.line4_box1_left.create_line(300, 35, 300, 200, dash = (5, 2))

                 #box2

        self.label32_photo=tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="photo",bg='green')
        self.label32_photo.place(x=900,y=110,width=50,height=20)

        self.line5_box2_top = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line5_box2_top.place(x=950,y=120,width=320,height=1)

        self.line6_box2_right=Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black')
        self.line6_box2_right.place(x=1270,y=120,width=1,height=370)
        self.line6_box2_right.create_line(300, 35, 300, 200, dash = (5, 2)) 

        self.line7_box2_bottom = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line7_box2_bottom.place(x=900,y=490,width=370,height=1)

        self.line8_box2_left=Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black')
        self.line8_box2_left.place(x=900,y=120,width=1,height=370)
        self.line8_box2_left.create_line(300, 35, 300, 200, dash = (5, 2))

                  #box3
        
        self.line9_box3_top = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line9_box3_top.place(x=5,y=505,width=880,height=1)

        self.line10_box3_right =Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black')
        self.line10_box3_right .place(x=885,y=505,width=1,height=240)
        self.line10_box3_right .create_line(300, 35, 300, 200, dash = (5, 2))

        self.line11_box3_bottom = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line11_box3_bottom.place(x=5,y=745,width=880,height=1)

        self.line12_box3_left =Canvas(self.main_page_frame_view3_patient_registration_default_frame,bg='black')
        #self.line12_box3_left.configure(bg='black') 
        self.line12_box3_left .place(x=5,y=505,width=1,height=240)
        self.line12_box3_left .create_line(300, 35, 300, 200, dash = (5, 2))

        

             #box 4

        self.label32_company_details=tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Company Details",bg='green')
        self.label32_company_details.place(x=900,y=495,width=100,height=20)

        self.line13_box4_top = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line13_box4_top.place(x=1000,y=505,width=270,height=1)

        #creating vertical line of box4
        self.line14_box4_right =Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black')
        self.line14_box4_right .place(x=1270,y=505,width=1,height=240)
        self.line14_box4_right .create_line(300, 35, 300, 200, dash = (5, 2))

        

        self.line15_box4_bottom = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line15_box4_bottom.place(x=900,y=745,width=370,height=1)

        #creating vertical line of box4 left
        self.line16_box4_left =Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black')
        self.line16_box4_left .place(x=900,y=505,width=1,height=240)
        self.line16_box4_left .create_line(300, 35, 300, 200, dash = (5, 2))

        #main_page_frame_view3_patient_registration_default_frame-------end--------------

     
        self.main_page_frame_view3_emergency_registration_default_frame=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view3_emergency_registration_default_frame['borderwidth']=0
        
        self.emergency_registration_mainheading1 = tk.Label(self.main_page_frame_view3_emergency_registration_default_frame,text="emergency registration",font=("lucida",15,"bold italic"),bg='blue')
        self.emergency_registration_mainheading1.place(x=5,y=5,width=1300,height=40)
     


        #patient_search_default_frame------start-------------
        self.main_page_frame_view3_patient_search_default_frame=tk.Frame(self.root1,bg='white')
        self.main_page_frame_view3_patient_search_default_frame['borderwidth']=0
        
        self.patient_search_mainheading1 = tk.Label(self.main_page_frame_view3_patient_search_default_frame,text="patient search",font=("lucida",15,"bold italic"),bg='blue')
        self.patient_search_mainheading1.place(x=5,y=5,width=1300,height=40)

        #main_buttons========================================start==========================================
        self.patient_search_button1_DISPLAY = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="DISPLAY")
        self.patient_search_button1_DISPLAY.place(x=5,y=50,width=100,height=30)

        self.patient_search_button1_PAQTIENT_QUEUE = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="PAQTIENT QUEUE")
        self.patient_search_button1_PAQTIENT_QUEUE.place(x=115,y=50,width=100,height=30)

        self.patient_search_button1_EDIT_PATIENT_QUEUE = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="EDIT")
        self.patient_search_button1_EDIT_PATIENT_QUEUE.place(x=225,y=50,width=100,height=30)

        self.patient_search_button1_DETAILS = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="DETAILS")
        self.patient_search_button1_DETAILS.place(x=335,y=50,width=100,height=30)

        self.patient_search_button1_EXIT = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="EXIT")
        self.patient_search_button1_EXIT.place(x=445,y=50,width=100,height=30)
        #main_buttons========================================end==========================================
        #patient_search_box1===========================start==================================================
        self.patient_search_heading1 = tk.Label(self.main_page_frame_view3_patient_search_default_frame,text="patient search",bg='white')
        self.patient_search_heading1.place(x=10,y=100,width=80,height=20)

        self.patient_search_box1_top = tk.Label(self.main_page_frame_view3_patient_search_default_frame,text="",bg='black')
        self.patient_search_box1_top.place(x=95,y=110,width=330,height=1)

        self.patient_search_box1_right =Canvas(self.main_page_frame_view3_patient_search_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.patient_search_box1_right .place(x=425,y=110,width=1,height=220)
        self.patient_search_box1_right .create_line(300, 35, 300, 200, dash = (5, 2))

        self.patient_search_box1_bottom = tk.Label(self.main_page_frame_view3_patient_search_default_frame,text="",bg='black')
        self.patient_search_box1_bottom.place(x=15,y=330,width=410,height=1)

        self.patient_search_box1_left =Canvas(self.main_page_frame_view3_patient_search_default_frame,bg='black',highlightthickness = 1, highlightbackground = 'black')
        #self.line12_box3_left.configure(bg='black') 
        self.patient_search_box1_left .place(x=15,y=125,width=1,height=205)
        self.patient_search_box1_left .create_line(300, 35, 300, 200, dash = (5, 2))
        #patient_search_box1===========================end==================================================

        #patient_search_input===========================================start====================================
        self.patient_search_input_label1=tk.Label(self.main_page_frame_view3_patient_search_default_frame,text="Reg ID",bg='white')
        self.patient_search_input_label1.place(x=25,y=140)
        self.patient_search_input_reg_id_var= tk.IntVar()
        self.patient_search_input_entry1=tk.Entry(self.main_page_frame_view3_patient_search_default_frame,text= self.patient_search_input_reg_id_var,font=('calibre',12))
        self.patient_search_input_entry1.place(x=150,y=140,width=250,height=20)

        self.patient_search_input_label2=tk.Label(self.main_page_frame_view3_patient_search_default_frame,text="Fname",bg='white')
        self.patient_search_input_label2.place(x=25,y=190)
        self.patient_search_input_Fname_var= tk.StringVar()
        self.patient_search_input_entry2=tk.Entry(self.main_page_frame_view3_patient_search_default_frame,text= self.patient_search_input_Fname_var,font=('calibre',12))
        self.patient_search_input_entry2.place(x=150,y=190,width=250,height=20)

        self.patient_search_input_label3=tk.Label(self.main_page_frame_view3_patient_search_default_frame,text="Lname",bg='white')
        self.patient_search_input_label3.place(x=25,y=240)
        self.patient_search_input_Lname_var= tk.StringVar()
        self.patient_search_input_entry3=tk.Entry(self.main_page_frame_view3_patient_search_default_frame,text= self.patient_search_input_Lname_var,font=('calibre',12))
        self.patient_search_input_entry3.place(x=150,y=240,width=250,height=20)

        self.patient_search_input_label4=tk.Label(self.main_page_frame_view3_patient_search_default_frame,text="Phone No",bg='white')
        self.patient_search_input_label4.place(x=25,y=290)
        self.patient_search_input_Phone_No_var= tk.IntVar()
        self.patient_search_input_entry4=tk.Entry(self.main_page_frame_view3_patient_search_default_frame,text= self.patient_search_input_Phone_No_var,font=('calibre',12))
        self.patient_search_input_entry4.place(x=150,y=290,width=250,height=20)

        #patient_search_input===========================================end====================================

        #patient_search_default_frame------end-------------


        #patient_queue-------------------------start-------------
        #patient_queue_default_frame------start-------------
        self.main_page_frame_view3_patient_queue_default_frame=tk.Frame(self.root1,bg='light blue')
        self.main_page_frame_view3_patient_queue_default_frame['borderwidth']=0

        self.patient_queue_mainheading1 = tk.Label(self.main_page_frame_view3_patient_queue_default_frame,text="patient queue",font=("lucida",15,"bold italic"),bg='blue')
        self.patient_queue_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.patient_queue_button1_Reload_Queue = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Reload Queue")
        self.patient_queue_button1_Reload_Queue.place(x=5,y=50,width=150,height=30)

        self.patient_queue_button2_Send_to_OPD = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Send to OPD")
        self.patient_queue_button2_Send_to_OPD.place(x=165,y=50,width=150,height=30)

        self.patient_queue_button3_Send_to_IPO = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Send to IPO")
        self.patient_queue_button3_Send_to_IPO.place(x=325,y=50,width=150,height=30)

        self.patient_queue_button4_Delete = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Delete")
        self.patient_queue_button4_Delete.place(x=485,y=50,width=150,height=30)

        self.patient_queue_button5_OPD_Patient_History = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="OPD Patient History")
        self.patient_queue_button5_OPD_Patient_History.place(x=645,y=50,width=150,height=30)

        self.patient_queue_button6_IPO_Patient_History = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="IPO Patient History")
        self.patient_queue_button6_IPO_Patient_History.place(x=805,y=50,width=150,height=30)

        self.patient_queue_button7_Exit = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Exit")
        self.patient_queue_button7_Exit.place(x=965,y=50,width=150,height=30)
        
        self.patient_queue_label_select_doctor= tk.Label(self.main_page_frame_view3_patient_queue_default_frame,text="Select Doctor*")
        self.patient_queue_label_select_doctor.place(x=20,y=100)

        self.patient_queue_value_inside = tk.StringVar(self.main_page_frame_view3_patient_queue_default_frame)
        self.patient_queue_value_inside.set('select role')
        self.patient_queue_roles_list = ["ALL"]
        self.patient_queue_role_entry = ttk.OptionMenu(self.main_page_frame_view3_patient_queue_default_frame,self.patient_queue_value_inside , *self.patient_queue_roles_list)
        self.patient_queue_role_entry.configure(width=20)

        self.patient_queue_role_entry.place(x=120,y=100)
        print("the valuse on the roles:",self.patient_queue_value_inside.get())
        #patient_queue_default_frame------end-------------
        #patient_queue-------------------------end-------------

        # #lab_queue=====================================end=========================
        #main_page_frame_view3_lab_queue_defaulte_frame------start-------------
        self.main_page_frame_view3_lab_queue_default_frame=tk.Frame(self.root1,bg='light cyan')
        self.main_page_frame_view3_lab_queue_default_frame['borderwidth']=0

        self.lab_queue_default_mainheading1 = tk.Label(self.main_page_frame_view3_lab_queue_default_frame,text="lab queue",font=("lucida",15,"bold italic"),bg='blue')
        self.lab_queue_default_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.main_page_frame_view3_lab_queue_default_frame_button1_lab_queue = tk.Button(self.main_page_frame_view3_lab_queue_default_frame,text="Lab Queue",command=self.lab_queue_default,bg='red')
        self.main_page_frame_view3_lab_queue_default_frame_button1_lab_queue.place(x=50,y=55)

        self.main_page_frame_view3_lab_queue_default_frame_button1_search_lab_queue = tk.Button(self.main_page_frame_view3_lab_queue_default_frame,text="Search Lab Report",command= self.search_lab_queue)
        self.main_page_frame_view3_lab_queue_default_frame_button1_search_lab_queue.place(x=200,y=55)

    
        self.main_page_frame_view3_lab_queue_default_frame_button1_view_lab_report= tk.Button(self.main_page_frame_view3_lab_queue_default_frame,text="View Lab Report",command=self.view_lab_report)
        self.main_page_frame_view3_lab_queue_default_frame_button1_view_lab_report.place(x=350,y=55)




        #main_page_frame_view3_lab_queue_defaulte_frame------end-------------
        #main_page_frame_view3_search_lab_queue_defaulte_frame------start-------------
        self.main_page_frame_view3_search_lab_queue_frame=tk.Frame(self.root1,bg='light cyan')
        self.main_page_frame_view3_search_lab_queue_frame['borderwidth']=0

        self.search_lab_queue_mainheading1 = tk.Label(self.main_page_frame_view3_search_lab_queue_frame,text="search lab queue",font=("lucida",15,"bold italic"),bg='blue')
        self.search_lab_queue_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.main_page_frame_view3_search_lab_queue_frame_button1_lab_queue = tk.Button(self.main_page_frame_view3_search_lab_queue_frame,text="Lab Queue",command=self.lab_queue_default)
        self.main_page_frame_view3_search_lab_queue_frame_button1_lab_queue.place(x=50,y=55)

        self.main_page_frame_view3_search_lab_queue_frame_button1_search_lab_queue = tk.Button(self.main_page_frame_view3_search_lab_queue_frame,text="Search Lab Report",command= self.search_lab_queue,bg='red')
        self.main_page_frame_view3_search_lab_queue_frame_button1_search_lab_queue.place(x=200,y=55)

    
        self.main_page_frame_view3_search_lab_queue_frame_button1_view_lab_report= tk.Button(self.main_page_frame_view3_search_lab_queue_frame,text="View Lab Report",command=self.view_lab_report)
        self.main_page_frame_view3_search_lab_queue_frame_button1_view_lab_report.place(x=350,y=55)



        #main_page_frame_view3_search_lab_queue_defaulte_frame------end-------------
        #main_page_frame_view3_view_lab_report_defaulte_frame------start-------------
        self.main_page_frame_view3_view_lab_report_frame=tk.Frame(self.root1,bg='light cyan')
        self.main_page_frame_view3_view_lab_report_frame['borderwidth']=0

        self.view_lab_report_mainheading1 = tk.Label(self.main_page_frame_view3_view_lab_report_frame,text="view lab report",font=("lucida",15,"bold italic"),bg='blue')
        self.view_lab_report_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.main_page_frame_view3_view_lab_report_frame_button1_lab_queue = tk.Button(self.main_page_frame_view3_view_lab_report_frame,text="Lab Queue",command=self.lab_queue_default)
        self.main_page_frame_view3_view_lab_report_frame_button1_lab_queue.place(x=50,y=55)

        self.main_page_frame_view3_view_lab_report_frame_button1_search_lab_queue = tk.Button(self.main_page_frame_view3_view_lab_report_frame,text="Search Lab Report",command= self.search_lab_queue)
        self.main_page_frame_view3_view_lab_report_frame_button1_search_lab_queue.place(x=200,y=55)

    
        self.main_page_frame_view3_view_lab_report_frame_button1_view_lab_report= tk.Button(self.main_page_frame_view3_view_lab_report_frame,text="View Lab Report",command=self.view_lab_report,bg='red')
        self.main_page_frame_view3_view_lab_report_frame_button1_view_lab_report.place(x=350,y=55)



        #main_page_frame_view3_view_lab_report_defaulte_frame------end-------------
        #lab_queue=====================================end=========================

        #main_page_frame_view3_opd_queue_defaulte_frame------start-------------
        self.main_page_frame_view3_opd_queue_default_frame=tk.Frame(self.root1,bg='magenta')
        self.main_page_frame_view3_opd_queue_default_frame['borderwidth']=0

        self.opd_queue_mainheading1 = tk.Label(self.main_page_frame_view3_opd_queue_default_frame,text="OPD queue",font=("lucida",15,"bold italic"),bg='blue')
        self.opd_queue_mainheading1.place(x=5,y=5,width=1300,height=40)
        

 
        #main_page_frame_view3_opd_queue_defaulte_frame------end-------------

        #main_page_frame_view3_physical_management_defaulte_frame------start-------------
        self.main_page_frame_view3_physical_management_default_frame=tk.Frame(self.root1,bg='cyan')
        self.main_page_frame_view3_physical_management_default_frame['borderwidth']=0

        self.physical_management_mainheading1 = tk.Label(self.main_page_frame_view3_physical_management_default_frame,text="physical management",font=("lucida",15,"bold italic"),bg='blue')
        self.physical_management_mainheading1.place(x=5,y=5,width=1300,height=40)


        #main_page_frame_view3_physical_management_defaulte_frame------end-------------

        #main_page_frame_view3_dialy_collection-------------start---------------------------
        #main_page_frame_view3_dialy_collection_default_frame---------start--------------------
        self.main_page_frame_view3_dialy_collection_default_frame = tk.Frame(self.root1,bg='pink')
        self.main_page_frame_view3_dialy_collection_default_frame['borderwidth']=0

        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both = tk.Button(self.main_page_frame_view3_dialy_collection_default_frame,text="dialy collection ",command=self.dialy_collection_default,bg='red')
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both.place(x=50,y=20)

        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipo = tk.Button(self.main_page_frame_view3_dialy_collection_default_frame,text="dialy collection ipo",command= self.dialy_collection_ipo)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipo.place(x=200,y=20)

    
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd = tk.Button(self.main_page_frame_view3_dialy_collection_default_frame,text="dialy collection opd",command=self.dialy_collection_opd)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd.place(x=350,y=20)

        self.mid_line =Canvas(self.main_page_frame_view3_dialy_collection_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.mid_line .place(x=590,y=100,width=1,height=1000)
        self.mid_line .create_line(300, 35, 300, 200, dash = (5, 2))

        self.right_heading_label1= tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Dialy Collection IPO",font= ("arial italic", 18))
        self.right_heading_label1.place(x=50,y=105,width=250,height=35)

        self.left_label1 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total consulting charge")
        self.left_label1.place(x=50,y=170,width=130,height=15)
        self.left_label1var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.left_label1var.set(000)
        self.left_label1var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.left_label1var)
        self.left_label1var_display.place(x=450,y=170,width=50,height=15)

        self.left_label2 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total miscellaneous charge")
        self.left_label2.place(x=50,y=210,width=145,height=15)
        self.left_label2var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.left_label2var.set(000)
        self.left_label2var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.left_label2var)
        self.left_label2var_display.place(x=450,y=210,width=50,height=15)

        self.left_label3 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total other charge")
        self.left_label3.place(x=50,y=250,width=100,height=15)
        self.left_label3var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.left_label3var.set(000)
        self.left_label3var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.left_label3var)
        self.left_label3var_display.place(x=450,y=250,width=50,height=15)

        self.left_label4 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total Lab Test Charges")
        self.left_label4.place(x=50,y=290,width=120,height=15)
        self.left_label4var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.left_label4var.set(000)
        self.left_label4var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.left_label4var)
        self.left_label4var_display.place(x=450,y=290,width=50,height=15)

        self.left_label5 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total Consumble charge")
        self.left_label5.place(x=50,y=330,width=130,height=15)
        self.left_label5var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.left_label5var.set(000)
        self.left_label5var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.left_label5var)
        self.left_label5var_display.place(x=450,y=330,width=50,height=15)

        self.left_label6 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="total procedure charge")
        self.left_label6.place(x=50,y=370,width=125,height=15)
        self.left_label6var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.left_label6var.set(000)
        self.left_label6var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.left_label6var)
        self.left_label6var_display.place(x=450,y=370,width=50,height=15)

        self.left_label7 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total Dialy Collection")
        self.left_label7.place(x=50,y=410,width=112,height=15)
        self.left_label7var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.left_label7var.set(000)
        self.left_label7var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.left_label7var)
        self.left_label7var_display.place(x=450,y=410,width=50,height=15)
        
        '''
        canvas1 = Canvas(main_window,width=100,height=100)
        canvas1.place(x=100,y=500)
        
        def createPieChart(PieV,colV):
          st = 0
          coord = 100, 100, 300, 300
          for val,col in zip(PieV,colV):    
                     canvas1.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                     st = st + val*3.6 

        PieV=[25,45,10,20]
        colV=["red","Blue","Yellow","Green"]
        createPieChart(PieV,colV) 
        '''
        '''
        stockListExp = [ 'AMZN' , 'AAPL', 'JETS', 'CCL', 'NCLH']
        stockSplitExp = [15,25,40,10,10]


        plt.pie(stockSplitExp, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True,) # 2 decimal points after plot

        figChart1 = plt.pie(stockSplitExp, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True)
        plt.axis("equal")
        chart1 = FigureCanvasTkAgg(figChart1,self.main_page_frame_view3_dialy_collection_default_frame)
        chart1.get_tk_widget().place(x=10,y=10)
        '''
        self.right_heading_label2= tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Dialy Collection OPD",font= ("arial italic", 18))
        self.right_heading_label2.place(x=680,y=105,width=250,height=35)

        self.right_label1 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total consulting charge")
        self.right_label1.place(x=680,y=170,width=130,height=15)
        self.right_label1var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.right_label1var.set(000)
        self.right_label1var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.right_label1var)
        self.right_label1var_display.place(x=1080,y=170,width=50,height=15)

        self.right_label2 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total miscellaneous charge")
        self.right_label2.place(x=680,y=210,width=145,height=15)
        self.right_label2var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.right_label2var.set(000)
        self.right_label2var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.right_label2var)
        self.right_label2var_display.place(x=1080,y=210,width=50,height=15)

        self.right_label3 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total other charge")
        self.right_label3.place(x=680,y=250,width=100,height=15)
        self.right_label3var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.right_label3var.set(000)
        self.right_label3var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.right_label3var)
        self.right_label3var_display.place(x=1080,y=250,width=50,height=15)

        self.right_label4 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total Lab Test Charges")
        self.right_label4.place(x=680,y=290,width=120,height=15)
        self.right_label4var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.right_label4var.set(000)
        self.right_label4var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.right_label4var)
        self.right_label4var_display.place(x=1080,y=290,width=50,height=15)

        self.right_label5 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total Consumble charge")
        self.right_label5.place(x=680,y=330,width=130,height=15)
        self.right_label5var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.right_label5var.set(000)
        self.right_label5var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.right_label5var)
        self.right_label5var_display.place(x=1080,y=330,width=50,height=15)

        self.right_label6 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="total procedure charge")
        self.right_label6.place(x=680,y=370,width=125,height=15)
        self.right_label6var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.right_label6var.set(000)
        self.right_label6var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.right_label6var)
        self.right_label6var_display.place(x=1080,y=370,width=50,height=15)

        self.right_label7 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Total Dialy Collection")
        self.right_label7.place(x=680,y=410,width=112,height=15)
        self.right_label7var = tk.IntVar(self.main_page_frame_view3_dialy_collection_default_frame)
        self.right_label7var.set(000)
        self.right_label7var_display = tk.Label( self.main_page_frame_view3_dialy_collection_default_frame, textvariable=self.right_label7var)
        self.right_label7var_display.place(x=1080,y=410,width=50,height=15)

        self.left_label8 = tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="")
        #main_page_frame_view3_dialy_collection_default_frame-----------------end----------------------

        #main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame-------------start----------
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame = tk.Frame(self.root1,bg='Light Blue')
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame['borderwidth']=0

        
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="dialy collection ",command=self.dialy_collection_default)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both.place(x=50,y=20)

        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipo = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="dialy collection ipo",command= self.dialy_collection_ipo,bg='red')
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipo.place(x=200,y=20)

    
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="dialy collection opd",command=self.dialy_collection_opd)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd.place(x=350,y=20)

        self.right_heading_label_ipo1 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="Dialy Collection IPO",font= ("arial italic", 18))
        self.right_heading_label_ipo1.place(x=50,y=105,width=250,height=35)

        self.left_label_ipo1 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="Total consulting charge")
        self.left_label_ipo1.place(x=50,y=170,width=130,height=15)
        self.left_label_ipo1var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame)
        self.left_label_ipo1var.set(000)
        self.left_label_ipo1var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame, textvariable=self.left_label_ipo1var)
        self.left_label_ipo1var_display.place(x=450,y=170,width=50,height=15)

        self.left_label_ipo2 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="Total miscellaneous charge")
        self.left_label_ipo2.place(x=50,y=210,width=145,height=15)
        self.left_label_ipo2var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame)
        self.left_label_ipo2var.set(000)
        self.left_label_ipo2var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame, textvariable=self.left_label_ipo2var)
        self.left_label_ipo2var_display.place(x=450,y=210,width=50,height=15)

        self.left_label_ipo3 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="Total other charge")
        self.left_label_ipo3.place(x=50,y=250,width=100,height=15)
        self.left_label_ipo3var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame)
        self.left_label_ipo3var.set(000)
        self.left_label_ipo3var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame, textvariable=self.left_label_ipo3var)
        self.left_label_ipo3var_display.place(x=450,y=250,width=50,height=15)

        self.left_label_ipo4 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="Total Lab Test Charges")
        self.left_label_ipo4.place(x=50,y=290,width=120,height=15)
        self.left_label_ipo4var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame)
        self.left_label_ipo4var.set(000)
        self.left_label_ipo4var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame, textvariable=self.left_label_ipo4var)
        self.left_label_ipo4var_display.place(x=450,y=290,width=50,height=15)

        self.left_label_ipo5 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="Total Consumble charge")
        self.left_label_ipo5.place(x=50,y=330,width=130,height=15)
        self.left_label_ipo5var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame)
        self.left_label_ipo5var.set(000)
        self.left_label_ipo5var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame, textvariable=self.left_label_ipo5var)
        self.left_label_ipo5var_display.place(x=450,y=330,width=50,height=15)

        self.left_label_ipo6 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="total procedure charge")
        self.left_label_ipo6.place(x=50,y=370,width=125,height=15)
        self.left_label_ipo6var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame)
        self.left_label_ipo6var.set(000)
        self.left_label_ipo6var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame, textvariable=self.left_label_ipo6var)
        self.left_label_ipo6var_display.place(x=450,y=370,width=50,height=15)

        self.left_label_ipo7 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame,text="Total Dialy Collection")
        self.left_label_ipo7.place(x=50,y=410,width=112,height=15)
        self.left_label_ipo7var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame)
        self.left_label_ipo7var.set(000)
        self.left_label_ipo7var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame, textvariable=self.left_label_ipo7var)
        self.left_label_ipo7var_display.place(x=450,y=410,width=50,height=15)
       


        #main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame-------------end------------

        #main_page_frame_view3_dialy_collection_dialy_collection_opd_frame------------start-------------
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame = tk.Frame(self.root1,bg='Orange')
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame['borderwidth']=0
        
         
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="dialy collection ",command=self.dialy_collection_default)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both.place(x=50,y=20)

        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipo = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="dialy collection ipo",command= self.dialy_collection_ipo)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipo.place(x=200,y=20)

    
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="dialy collection opd",command=self.dialy_collection_opd,bg='red')
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd.place(x=350,y=20)
        
        self.right_heading_label_opd1 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="Dialy Collection OPD",font= ("arial italic", 18))
        self.right_heading_label_opd1.place(x=50,y=105,width=250,height=35)


        self.right_label_opd1 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="Total consulting charge")
        self.right_label_opd1.place(x=50,y=170,width=130,height=15)
        self.right_label_opd1var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame)
        self.right_label_opd1var.set(000)
        self.right_label_opd1var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame, textvariable=self.right_label_opd1var)
        self.right_label_opd1var_display.place(x=450,y=170,width=50,height=15)

        self.right_label_opd2 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="Total miscellaneous charge")
        self.right_label_opd2.place(x=50,y=210,width=145,height=15)
        self.right_label_opd2var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame)
        self.right_label_opd2var.set(000)
        self.right_label_opd2var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame, textvariable=self.right_label_opd2var)
        self.right_label_opd2var_display.place(x=450,y=210,width=50,height=15)

        self.right_label_opd3 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="Total other charge")
        self.right_label_opd3.place(x=50,y=250,width=100,height=15)
        self.right_label_opd3var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame)
        self.right_label_opd3var.set(000)
        self.right_label_opd3var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame, textvariable=self.right_label_opd3var)
        self.right_label_opd3var_display.place(x=450,y=250,width=50,height=15)

        self.right_label_opd4 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="Total Lab Test Charges")
        self.right_label_opd4.place(x=50,y=290,width=120,height=15)
        self.right_label_opd4var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame)
        self.right_label_opd4var.set(000)
        self.right_label_opd4var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame, textvariable=self.right_label_opd4var)
        self.right_label_opd4var_display.place(x=450,y=290,width=50,height=15)

        self.right_label_opd5 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="Total Consumble charge")
        self.right_label_opd5.place(x=50,y=330,width=130,height=15)
        self.right_label_opd5var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame)
        self.right_label_opd5var.set(000)
        self.right_label_opd5var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame, textvariable=self.right_label_opd5var)
        self.right_label_opd5var_display.place(x=450,y=330,width=50,height=15)

        self.right_label_opd6 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="total procedure charge")
        self.right_label_opd6.place(x=50,y=370,width=125,height=15)
        self.right_label_opd6var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame)
        self.right_label_opd6var.set(000)
        self.right_label_opd6var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame, textvariable=self.right_label_opd6var)
        self.right_label_opd6var_display.place(x=450,y=370,width=50,height=15)

        self.right_label_opd7 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="Total Dialy Collection")
        self.right_label_opd7.place(x=50,y=410,width=112,height=15)
        self.right_label_opd7var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame)
        self.right_label_opd7var.set(000)
        self.right_label_opd7var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame, textvariable=self.right_label_opd7var)
        self.right_label_opd7var_display.place(x=450,y=410,width=50,height=15)



        #main_page_frame_view3_dialy_collection_dialy_collection_opd_frame------------end---------------

        #main_page_frame_view3_dialy_collection_dialy_collection_both_frame------------start-------------
       


        #main_page_frame_view3_dialy_collection_dialy_collection_opd_frame------------end---------------
        
        #main_page_frame_view3_dialy_collection-------------end---------------------------
        


        #frames status variables---------------------start----------------------------
        self.login_page_frame1_status= "None" 
        self.main_page_frame_view1_status= "None"
        self.main_page_frame_view1_dialy_tasks_default_frame_status="None"
        self.main_page_frame_view1_dialy_tasks_default_frame_status = "None"
        self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame_status = "None"
        self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_status = "None"
        self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_status = "None"
        self.main_page_frame_view1_dialy_tasks_update_work_done_frame_status = "None"
        self.main_page_frame_view1_dialy_tasks_work_done_frame_status = "None"
        self.main_page_frame_view2_status= "None"


        self.main_page_frame_view3_home_frame_status= "None"
        self.main_page_frame_view3_patient_registration_default_frame_status = "None"
        self.main_page_frame_view3_emergency_registration_default_frame_status = "None"
        self.main_page_frame_view3_patient_search_default_frame_status= "None"
        self.main_page_frame_view3_patient_queue_default_frame_status= "None"
        self.main_page_frame_view3_lab_queue_default_frame_status= "None"
        self.main_page_frame_view3_search_lab_queue_frame_status= "None"
        self.main_page_frame_view3_view_lab_report_frame_status = "None"

        self.main_page_frame_view3_opd_queue_default_frame_status= "None"
        self.main_page_frame_view3_physical_management_default_frame_status= "None"


   
        
        self.main_page_frame_view3_dialy_collection_default_frame_status = "None"
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_status = "None"
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_status = "None"
        
        
         #frames status variables---------------------end----------------------------

    #main_page_frame_view1_dialy_tasks_functions--------------start--------------------------------

    #activiate functions -----------------start---------------------
    

    def main_page_frame_view3_home_frame_activate(self):
        if self.main_page_frame_view3_home_frame_status  == "deactivated" or self.main_page_frame_view3_home_frame_status == "None" :
              self.main_page_frame_view3_home_frame_status = "activated"
              self.main_page_frame_view3_home_frame.pack(ipadx=670,ipady=390,side='top')



    def main_page_frame_view3_patient_registration_default_frame_activate(self):
        if self.main_page_frame_view3_patient_registration_default_frame_status  == "deactivated" or self.main_page_frame_view3_patient_registration_default_frame_status == "None" :
              self.main_page_frame_view3_patient_registration_default_frame_status = "activated"
              self.main_page_frame_view3_patient_registration_default_frame.pack(ipadx=670,ipady=390,side='top')


    def main_page_frame_view3_emergency_registration_default_frame_activate(self):
        if self.main_page_frame_view3_emergency_registration_default_frame_status  == "deactivated" or self.main_page_frame_view3_emergency_registration_default_frame_status == "None" :
              self.main_page_frame_view3_emergency_registration_default_frame_status = "activated"
              self.main_page_frame_view3_emergency_registration_default_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_patient_search_default_frame_activate(self):
        if self.main_page_frame_view3_patient_search_default_frame_status  == "deactivated" or self.main_page_frame_view3_patient_search_default_frame_status == "None" :
            self.main_page_frame_view3_patient_search_default_frame_status = "activated"
            self.main_page_frame_view3_patient_search_default_frame.pack(ipadx=670,ipady=390,side='top')
  
    def main_page_frame_view3_patient_queue_default_frame_activate(self):
        if self.main_page_frame_view3_patient_queue_default_frame_status  == "deactivated" or self.main_page_frame_view3_patient_queue_default_frame_status == "None" :
              self.main_page_frame_view3_patient_queue_default_frame_status = "activated"
              self.main_page_frame_view3_patient_queue_default_frame.pack(ipadx=670,ipady=390,side='top')
    
    def main_page_frame_view3_lab_queue_default_frame_activate(self):
        if self.main_page_frame_view3_lab_queue_default_frame_status  == "deactivated" or self.main_page_frame_view3_lab_queue_default_frame_status == "None" :
            self.main_page_frame_view3_lab_queue_default_frame_status = "activated"
            self.main_page_frame_view3_lab_queue_default_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_search_lab_queue_frame_activate(self):
        if self.main_page_frame_view3_search_lab_queue_frame_status  == "deactivated" or self.main_page_frame_view3_search_lab_queue_frame_status == "None" :
            self.main_page_frame_view3_search_lab_queue_frame_status = "activated"
            self.main_page_frame_view3_search_lab_queue_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_view_lab_report_frame_activate(self):
        if self.main_page_frame_view3_view_lab_report_frame_status  == "deactivated" or self.main_page_frame_view3_view_lab_report_frame_status == "None" :
            self.main_page_frame_view3_view_lab_report_frame_status = "activated"
            self.main_page_frame_view3_view_lab_report_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_opd_queue_default_frame_activate(self):
        if self.main_page_frame_view3_opd_queue_default_frame_status  == "deactivated" or self.main_page_frame_view3_opd_queue_default_frame_status == "None" :
              self.main_page_frame_view3_opd_queue_default_frame_status = "activated"
              self.main_page_frame_view3_opd_queue_default_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_physical_management_default_frame_activate(self):
        if self.main_page_frame_view3_physical_management_default_frame_status  == "deactivated" or self.main_page_frame_view3_physical_management_default_frame_status == "None" :
            self.main_page_frame_view3_physical_management_default_frame_status = "activated"
            self.main_page_frame_view3_physical_management_default_frame.pack(ipadx=670,ipady=390,side='top')

    






    def main_page_frame_view1_dialy_tasks_default_frame_activate(self):
        if self.main_page_frame_view1_dialy_tasks_default_frame_status  == "deactivated" or self.main_page_frame_view1_dialy_tasks_default_frame_status == "None" :
            self.main_page_frame_view1_dialy_tasks_default_frame_status = "activated"
            self.main_page_frame_view1_dialy_tasks_default_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view1_dialy_tasks_dialy_attdence_frame_activate(self):
        if self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame_status  == "deactivated" or self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame_status == "None" :
              self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame_status = "activated"
              self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_activate(self):
        if self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_status  == "deactivated" or self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_status == "None" :
              self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_status = "activated"
              self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_activate(self):
        if self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_status  == "deactivated" or self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_status == "None" :
              self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_status = "activated"
              self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view1_dialy_tasks_update_work_done_frame_activate(self):
        if self.main_page_frame_view1_dialy_tasks_update_work_done_frame_status  == "deactivated" or self.main_page_frame_view1_dialy_tasks_update_work_done_frame_status == "None" :
              self.main_page_frame_view1_dialy_tasks_update_work_done_frame_status = "activated"
              self.main_page_frame_view1_dialy_tasks_update_work_done_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view1_dialy_tasks_work_done_frame_activate(self):
        if self.main_page_frame_view1_dialy_tasks_work_done_frame_status  == "deactivated" or self.main_page_frame_view1_dialy_tasks_work_done_frame_status == "None" :
              self.main_page_frame_view1_dialy_tasks_work_done_frame_status = "activated"
              self.main_page_frame_view1_dialy_tasks_work_done_frame.pack(ipadx=670,ipady=390,side='top')



    def main_page_frame_view3_dialy_collection_default_frame_activate(self):
         if self.main_page_frame_view3_dialy_collection_default_frame_status  == "deactivated" or self.main_page_frame_view3_dialy_collection_default_frame_status == "None" :
              self.main_page_frame_view3_dialy_collection_default_frame_status = "activated"
              self.main_page_frame_view3_dialy_collection_default_frame.pack(ipadx=670,ipady=390,side='top')



    def main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_activate(self):
        if self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_status  == "deactivated" or self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_status == "None" :
              self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_status = "activated"
              self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_activate(self):
        if self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_status  == "deactivated" or self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_status == "None" :
              self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_status = "activated"
              self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame.pack(ipadx=670,ipady=390,side='top')

   
        
    #activiate functions -----------------end---------------------

    #deactiviate functions -----------------start---------------------
    def dialy_collection_frame_deactivate(self):
        pass

    def main_page_frame_view3_home_frame_deactivate(self):
        if self.main_page_frame_view3_home_frame_status  == "activated"  or self.main_page_frame_view3_home_frame_status == "None":
              self.main_page_frame_view3_home_frame_status = "deactivated"
              self.main_page_frame_view3_home_frame.pack_forget()

    def main_page_frame_view3_patient_registration_default_frame_deactivate(self):
         if self.main_page_frame_view3_patient_registration_default_frame_status  == "activated"  or self.main_page_frame_view3_patient_registration_default_frame_status == "None":
              self.main_page_frame_view3_patient_registration_default_frame_status = "deactivated"
              self.main_page_frame_view3_patient_registration_default_frame.pack_forget()
              
    def main_page_frame_view3_emergency_registration_default_frame_deactivate(self):
         if self.main_page_frame_view3_emergency_registration_default_frame_status  == "activated"  or self.main_page_frame_view3_emergency_registration_default_frame_status == "None":
              self.main_page_frame_view3_emergency_registration_default_frame_status = "deactivated"
              self.main_page_frame_view3_emergency_registration_default_frame.pack_forget()

    def main_page_frame_view3_patient_search_default_frame_deactivate(self):
        if self.main_page_frame_view3_patient_search_default_frame_status  == "activated" or self.main_page_frame_view3_patient_search_default_frame_status == "None" :
            self.main_page_frame_view3_patient_search_default_frame_status = "deactivated"
            self.main_page_frame_view3_patient_search_default_frame.pack_forget()
   
    def main_page_frame_view3_patient_queue_default_frame_deactivate(self):
        if self.main_page_frame_view3_patient_queue_default_frame_status  == "activated" or self.main_page_frame_view3_patient_queue_default_frame_status == "None" :
              self.main_page_frame_view3_patient_queue_default_frame_status = "deactivated"
              self.main_page_frame_view3_patient_queue_default_frame.pack_forget()

    def main_page_frame_view3_lab_queue_default_frame_deactivate(self):
         if self.main_page_frame_view3_lab_queue_default_frame_status  == "activated"  or self.main_page_frame_view3_lab_queue_default_frame_status == "None":
              self.main_page_frame_view3_lab_queue_default_frame_status = "deactivated"
              self.main_page_frame_view3_lab_queue_default_frame.pack_forget()

    def main_page_frame_view3_search_lab_queue_frame_deactivate(self):
         if self.main_page_frame_view3_search_lab_queue_frame_status  == "activated"  or self.main_page_frame_view3_search_lab_queue_frame_status == "None":
              self.main_page_frame_view3_search_lab_queue_frame_status = "deactivated"
              self.main_page_frame_view3_search_lab_queue_frame.pack_forget()

    def main_page_frame_view3_view_lab_report_frame_deactivate(self):
         if self.main_page_frame_view3_view_lab_report_frame_status  == "activated"  or self.main_page_frame_view3_view_lab_report_frame_status == "None":
              self.main_page_frame_view3_view_lab_report_frame_status = "deactivated"
              self.main_page_frame_view3_view_lab_report_frame.pack_forget()



    def main_page_frame_view3_opd_queue_default_frame_deactivate(self):
        if self.main_page_frame_view3_opd_queue_default_frame_status  == "activated" or self.main_page_frame_view3_opd_queue_default_frame_status == "None" :
            self.main_page_frame_view3_opd_queue_default_frame_status = "deactivated"
            self.main_page_frame_view3_opd_queue_default_frame.pack_forget()
   
    def main_page_frame_view3_physical_management_default_frame_deactivate(self):
        if self.main_page_frame_view3_physical_management_default_frame_status  == "activated" or self.main_page_frame_view3_physical_management_default_frame_status == "None" :
              self.main_page_frame_view3_physical_management_default_frame_status = "deactivated"
              self.main_page_frame_view3_physical_management_default_frame.pack_forget()


    


    def main_page_frame_view1_dialy_tasks_default_frame_deactivate(self):
        if self.main_page_frame_view1_dialy_tasks_default_frame_status  == "activated" or self.main_page_frame_view1_dialy_tasks_default_frame_status == "None" :
            self.main_page_frame_view1_dialy_tasks_default_frame_status = "deactivated"
            self.main_page_frame_view1_dialy_tasks_default_frame.pack_forget()

    def main_page_frame_view1_dialy_tasks_dialy_attdence_frame_deactivate(self):
        if self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame_status  == "activated" or self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame_status == "None" :
            self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame_status = "deactivated"
            self.main_page_frame_view1_dialy_tasks_dialy_attdence_frame.pack_forget()

    def main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_deactivate(self):
        if self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_status  == "activated"  or self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_status == "None" :
            self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame_status = "deactivated"
            self.main_page_frame_view1_dialy_tasks_view_dialy_attdence_frame.pack_forget()

    def main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_deactivate(self):
        if self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_status  == "activated" or self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_status == "None" :
            self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame_status = "deactivated"
            self.main_page_frame_view1_dialy_tasks_add_dialy_work_done_frame.pack_forget()

    def main_page_frame_view1_dialy_tasks_update_work_done_frame_deactivate(self):
        if self.main_page_frame_view1_dialy_tasks_update_work_done_frame_status  == "activated"  or self.main_page_frame_view1_dialy_tasks_update_work_done_frame_status == "None":
            self.main_page_frame_view1_dialy_tasks_update_work_done_frame_status = "deactivated"
            self.main_page_frame_view1_dialy_tasks_update_work_done_frame.pack_forget()

    def main_page_frame_view1_dialy_tasks_work_done_frame_deactivate(self):
        if self.main_page_frame_view1_dialy_tasks_work_done_frame_status  == "activated" or self.main_page_frame_view1_dialy_tasks_work_done_frame_status == "None" :
            self.main_page_frame_view1_dialy_tasks_work_done_frame_status = "deactivated"
            self.main_page_frame_view1_dialy_tasks_work_done_frame.pack_forget()
    

    def main_page_frame_view3_dialy_collection_default_frame_deactivate(self):
         if self.main_page_frame_view3_dialy_collection_default_frame_status  == "activated" or self.main_page_frame_view3_dialy_collection_default_frame_status == "None":
            self.main_page_frame_view3_dialy_collection_default_frame_status = "deactivated"
            self.main_page_frame_view3_dialy_collection_default_frame.pack_forget()



    def main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate(self):
        if self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_status  == "activated" or self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_status == "None" :
            self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_status = "deactivated"
            self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame.pack_forget()

    def main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate(self):
        if self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_status  == "activated" or self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_status == "None" :
            self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_status = "deactivated"
            self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame.pack_forget()

    
    
    #deactiviate functions -----------------end---------------------

    #main_page_frame_view1_dialy_tasks_functions--------------end--------------------------------

    '''
    def loop_1(self):
            self.label456 = None
            self.x11,self.y11= 0
            for  self.a in range(0,10):
                self.label456= tk.Label(self.patient_search_default_frame,text="patient_search_default_frame")
                self.y11 = self.y11 + 20
                self.label456.place(x=self.x11,y=self.y11)
    '''

    def frames_status(self):
             pass
    

     #functions_list====================================================start=====================================
    '''
    self.main_page_frame_view3_home_frame_deactivate()
    self.main_page_frame_view3_patient_registration_default_frame_deactivate()
    self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
    self.main_page_frame_view3_patient_search_default_frame_deactivate()
    self.main_page_frame_view3_patient_queue_default_frame_deactivate()
    self.main_page_frame_view3_lab_queue_default_frame_deactivate()
    self.main_page_frame_view3_search_lab_queue_frame_deactivate()
    self.main_page_frame_view3_view_lab_report_frame_deactivate()

    self.main_page_frame_view3_opd_queue_default_frame_deactivate()
    self.main_page_frame_view3_physical_management_default_frame_deactivate()

    self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
    self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
     
    
    
    '''
    #functions_list==================================================stop=====================================
        
    
    #main_page_view2_and_view3=======================================start=====================================

   


    #patient_registration==========================================start===========================================
    #patient_registration_default==========================================start===========================================

    def patient_registration_default(self):
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_activate()
             self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
             self.main_page_frame_view3_patient_search_default_frame_deactivate()
             self.main_page_frame_view3_patient_queue_default_frame_deactivate()
             
             
             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_physical_management_default_frame_deactivate()

             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
              
             
             '''
             print("+++++++++++++++++++++++++++++++++++++++++")
             print("destroy_main_page_frame_view3 function")
    
             self.frames_status()
             if self.main_page_frame_view3_status == None:
                pass
             else:
                 print("destroy_main_page_frame_view3 destroyed")
                 #self.main_page_frame_view3_before_destroy = self.main_page_frame_view3
                 self.main_page_frame_view3.pack_forget()
                 #self.main_page_frame_view3 = self.main_page_frame_view3_before_destroy
             self.frames_status()
             #self.main_page_frame_view3 = None
             if self.patient_search_default_frame == None:
                    pass
             else:
                 print("destroy_patient_search_default_frame destroyed")
                 #self.patient_search_default_frame_before_destroy = self.patient_search_default_frame
                 self.patient_search_default_frame.pack_forget()
                 
                 #self.patient_search_default_frame = self.patient_search_default_frame_before_destroy 
             self.frames_status()
             print("patient_search_default_frame activated")
             #self.patient_search_default_frame_before_destroy = self.patient_search_default_frame
             self.patient_search_default_frame.pack(ipadx=670,ipady=390,side='top')
             self.frames_status()
             print("+++++++++++++++++++++++++++++++++++++++++")
             '''
    #patient_registration_default==========================================end===========================================
    #patient_registration==========================================end===========================================
             

    
    ##emergency registration====================================start================================
    #emergency registration_default==============================start======================================
    def emergency_registration_default(self):
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_deactivate()
             self.main_page_frame_view3_emergency_registration_default_frame_activate()
             self.main_page_frame_view3_patient_search_default_frame_deactivate()
             self.main_page_frame_view3_patient_queue_default_frame_deactivate()

             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_physical_management_default_frame_deactivate()
             
             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
              
             self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()
             '''
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
        if self.patient_search_default_frame == None:
                pass
        else:
            print("destroy_patient_search_default_frame destroyed")
            #self.patient_search_default_frame = self.patient_search_default_frame_before_destroy
            self.patient_search_default_frame.pack_forget()
            #self.patient_search_default_frame = None
        
        #self.patient_search_default_frame = None
        #self.patient_search_default_frame.destroy()
        self.frames_status()
        print("patient_search_default_frame before changing",self.patient_search_default_frame)
        #self.patient_search_default_frame = self.patient_search_default_frame_before_destroy
        print("patient_search_default_frame after changing",self.patient_search_default_frame)
        
        self.patient_search_default_frame.pack(ipadx=670,ipady=370,side='top')
        print("+++++++++++++++++++++++++++++++++++++++++")
        '''

    #emergency registration_default===============================end========================================
    ##emergency registration=====================================start======================================

    #patient_search_default=====================================start========================================
    def patient_search_default(self):
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_deactivate()
             self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
             self.main_page_frame_view3_patient_search_default_frame_activate()
             self.main_page_frame_view3_patient_queue_default_frame_deactivate()

             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_physical_management_default_frame_deactivate()
             
             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
              
             self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #patient_search_default======================================end=========================================

    #patient_queue_default=====================================start========================================
    def patient_queue_default(self):
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_deactivate()
             self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
             self.main_page_frame_view3_patient_search_default_frame_deactivate()
             self.main_page_frame_view3_patient_queue_default_frame_activate()

             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_physical_management_default_frame_deactivate()
             
             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
              
             self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #patient_queue_default======================================end=========================================

    #lab_queue===========================================start=======================================
    #lab_queue_default=====================================start========================================
    def lab_queue_default(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_queue_default_frame_deactivate()

        self.main_page_frame_view3_lab_queue_default_frame_activate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_physical_management_default_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #lab_queue_default======================================end=========================================
    def search_lab_queue(self):
         self.main_page_frame_view3_home_frame_deactivate()
         self.main_page_frame_view3_patient_registration_default_frame_deactivate()
         self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
         self.main_page_frame_view3_patient_search_default_frame_deactivate()
         self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         self.main_page_frame_view3_lab_queue_default_frame_deactivate()
         self.main_page_frame_view3_search_lab_queue_frame_activate()
         self.main_page_frame_view3_view_lab_report_frame_deactivate()

         self.main_page_frame_view3_search_lab_queue_frame_activate()
         self.main_page_frame_view3_view_lab_report_frame_deactivate()

         self.main_page_frame_view3_opd_queue_default_frame_deactivate()
         self.main_page_frame_view3_physical_management_default_frame_deactivate()

    def view_lab_report(self):
         self.main_page_frame_view3_home_frame_deactivate()
         self.main_page_frame_view3_patient_registration_default_frame_deactivate()
         self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
         self.main_page_frame_view3_patient_search_default_frame_deactivate()
         self.main_page_frame_view3_patient_queue_default_frame_deactivate()

         self.main_page_frame_view3_lab_queue_default_frame_deactivate()
         self.main_page_frame_view3_search_lab_queue_frame_deactivate()
         self.main_page_frame_view3_view_lab_report_frame_activate()

         self.main_page_frame_view3_opd_queue_default_frame_deactivate()
         self.main_page_frame_view3_physical_management_default_frame_deactivate()

    #lab_queue===========================================end=======================================

    #opd_queue_default=====================================start========================================
    def opd_queue_default(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_activate()
        self.main_page_frame_view3_physical_management_default_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #opd_queue_default======================================end=========================================

    #physical_management_default=====================================start========================================
    def physical_management_default(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
        
        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_physical_management_default_frame_activate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #physical_management_default======================================end=========================================   

    #dialy_collection===============================================start=======================================
    def dialy_collection_default(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_queue_default_frame_deactivate()

        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_physical_management_default_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
         
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_default_frame_activate()
  
    def dialy_collection_ipo(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_physical_management_default_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
         
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_activate()

    def dialy_collection_opd(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_emergency_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_physical_management_default_frame_deactivate()
 
        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipo_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_activate()

    
    #dialy_collection===============================================end==========================================


    #main_page_view2_and_view3=======================================end=======================================


        


    
           
             
    
    
        
        

  



x=main_window()
x.login_page()
my = login_check.mydb
#my.close()

       
     
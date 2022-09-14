
from distutils.command.config import config
import tkinter as tk
from tkinter import *
from tkinter import ttk
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

        self.home_title=tk.Label(self.login_page_frame1,text='HOSPITAL MANAGEMENT SYSTEM',font=('calibre',45,''),fg='green')
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
        self.reset_button = tk.Button(self.login_page_frame1,text='Reset',width=13,height=1,bg='red',command=self.reset_button_responce)
        #,command=logincheck
        self.reset_button.place(x=840,y=570)
        #role_entry = tk.Entry(root,textvariable=role_var,font=('calibre',17)).place(x=720,y=430)
        self.root1.mainloop()
        

    def reset_button_responce(self):
        self.value_inside.set('select role')
        self.reg_id_var.set('')
        self.password_var.set('')

    def login_check_fun(self):
              print(self.value_inside.get(),self.reg_id_var.get(),self.password_var.get())
              self.response = login_check.username_password_check(login_check.mydb,self.value_inside.get(),self.reg_id_var.get(),self.password_var.get())
              # self.response = 'true'
              if self.response == 'true':
                       #return  self.response
                       self.login_page_frame1.place_forget()
                       #self.login_page_frame1 =None
                       self.main_page()
                       
              else:
                       #return  self.response
                       pass

    def main_page(self):

        #main_page_frame_view1------start-------------
        self.main_page_frame_view1=tk.Frame(self.root1,bg='red')
        self.main_page_frame_view1.pack(ipadx=770,ipady=20,side='top')
        self.main_page_frame_view1['borderwidth']=0

        self.botton1_dialy_tasks = tk.Button(self.main_page_frame_view1,text="Dialy Tasks",command= self.dialy_collection_default)
        self.botton1_dialy_tasks.place(x=650,y=5,width=100,height=32)

        self.main_page_frame_view1_logout_image =Image.open("G:\hms_v1\hms_files_v5\logout_img.png")
        #G:\hms_v1\hms_files_v3\main_page_home.jpeg
        # Show image using label
        
        self.logout_resized_image= self.main_page_frame_view1_logout_image.resize((40,32), Image.ANTIALIAS)
        self.logout_img=ImageTk.PhotoImage(self.logout_resized_image)
        self.button2_logout=tk.Button(self.main_page_frame_view1, image = self.logout_img,command= self.logout_default)#,command= self.logout_default
        self.button2_logout.place(x=1480,y=5,width=40,height=32)

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
        self.label11= tk.Button(self.main_page_frame_view2,text="patient visit",command=self.patient_visit_default)
        self.label11.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label12= tk.Button(self.main_page_frame_view2,text="patient search",command=self.patient_search_default)
        self.label12.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label13= tk.Button(self.main_page_frame_view2,text="patient queue",command=self.patient_queue_default)
        self.label13.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label14= tk.Button(self.main_page_frame_view2,text="Lab queue",command=self.lab_queue_default)
        self.label14.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label15= tk.Button(self.main_page_frame_view2,text="opd queue",command=self.opd_queue_default)
        self.label15.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label16= tk.Button(self.main_page_frame_view2,text="ipd queue",command=self.ipd_queue_default)
        self.label16.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label17= tk.Button(self.main_page_frame_view2,text="physical management",command=self.physical_management_book)
        self.label17.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label18= tk.Button(self.main_page_frame_view2,text="`Dialy collection",command=self.dialy_collection_default)
        self.label18.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        self.label19= tk.Button(self.main_page_frame_view2,text="Finance Details")
        self.label19.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
        #side='top',
        #main_page_frame_view2------end-------------

        #main_page_frame_view3------start-------------

        self.main_page_frame_view3_home_frame=tk.Frame(self.root1,bg='blue')
        self.main_page_frame_view3_home_frame.pack(ipadx=670,ipady=390,side='top')
        self.main_page_frame_view3_home_frame['borderwidth']=0
 
        
        
   

        #self.main_page_frame_view3_home_image = tk.PhotoImage( file = "main_page_home.jpeg")
        #self.main_page_frame_view3_home_image =Image.open("main_page_home.jpeg")
        self.main_page_frame_view3_home_image =Image.open("G:\hms_v1\hms_files_v3\main_page_home.jpeg")
        #G:\hms_v1\hms_files_v3\main_page_home.jpeg
        # Show image using label
        
        self.resized_image= self.main_page_frame_view3_home_image.resize((1300,770), Image.ANTIALIAS)
        self.my_img=ImageTk.PhotoImage(self.resized_image)

        self.main_page_frame_view3_home_label = tk.Label( self.main_page_frame_view3_home_frame, image = self.my_img)
        self.main_page_frame_view3_home_label.place(x=0,y=0,width=1300,height=770)
        
        """
        self.frame3_frame2_1=tk.Frame(self.main_page_frame_view3,bg='orange')
        label11111=tk.Label(self.frame3_frame2_1,text="self.frame3_frame2_1")
        self.frame3_frame2_1.place(x=0,y=0)
        """
        #main_page_frame_view3------end-------------


       #main_page_frame_view3_patient_registration_default_frame------start------------- 
        self.main_page_frame_view3_patient_registration_default_frame=tk.Frame(self.root1)
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

        self.label31_patient_registration_default = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="patient registration",font=("lucida",15,"bold "),bg='blue')
        self.label31_patient_registration_default.place(x=5,y=5,width=1300,height=40)

        self.button1_save = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="save")
        self.button1_save.place(x=5,y=50,width=50,height=50)

        self.button1_update = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="update")
        self.button1_update.place(x=60,y=50,width=50,height=50)

        self.button1_delete = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="delete")
        self.button1_delete.place(x=115,y=50,width=50,height=50)

        self.button1_clear = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="clear")
        self.button1_clear.place(x=170,y=50,width=50,height=50)

        self.button1_exit = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="exit",command=self.home_default)
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

        self.button1_remove = tk.Button(self.main_page_frame_view3_patient_registration_default_frame,text="Exit",command=self.home_default)
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
        self.label32_patient_details=tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="patient details")
        self.label32_patient_details.place(x=5,y=110,width=90,height=20)

        self.line1_box1_top = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line1_box1_top.place(x=100,y=120,width=785,height=1)

        self.line2_box1_right=Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.line2_box1_right.place(x=885,y=120,width=1,height=370)
        self.line2_box1_right.create_line(300, 35, 300, 200, dash = (5, 2))

        self.line3_box1_bottom = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line3_box1_bottom.place(x=5,y=490,width=880,height=1)


        self.line4_box1_left=Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.line4_box1_left.place(x=5,y=120,width=1,height=370)
        self.line4_box1_left.create_line(300, 35, 300, 200, dash = (5, 2))

                 #box2

        self.label32_photo=tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="photo")
        self.label32_photo.place(x=900,y=110,width=50,height=20)

        self.line5_box2_top = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line5_box2_top.place(x=950,y=120,width=320,height=1)

        self.line6_box2_right=Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.line6_box2_right.place(x=1270,y=120,width=1,height=370)
        self.line6_box2_right.create_line(300, 35, 300, 200, dash = (5, 2)) 

        self.line7_box2_bottom = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line7_box2_bottom.place(x=900,y=490,width=370,height=1)

        self.line8_box2_left=Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.line8_box2_left.place(x=900,y=120,width=1,height=370)
        self.line8_box2_left.create_line(300, 35, 300, 200, dash = (5, 2))

                  #box3
        
        self.line9_box3_top = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line9_box3_top.place(x=5,y=505,width=880,height=1)

        self.line10_box3_right =Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.line10_box3_right .place(x=885,y=505,width=1,height=240)
        self.line10_box3_right .create_line(300, 35, 300, 200, dash = (5, 2))

        self.line11_box3_bottom = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line11_box3_bottom.place(x=5,y=745,width=880,height=1)

        self.line12_box3_left =Canvas(self.main_page_frame_view3_patient_registration_default_frame,bg='black',highlightthickness = 1, highlightbackground = 'black')
        #self.line12_box3_left.configure(bg='black') 
        self.line12_box3_left .place(x=5,y=505,width=1,height=240)
        self.line12_box3_left .create_line(300, 35, 300, 200, dash = (5, 2))

        

             #box 4

        self.label32_company_details=tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="Company Details")
        self.label32_company_details.place(x=900,y=495,width=100,height=20)

        self.line13_box4_top = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line13_box4_top.place(x=1000,y=505,width=270,height=1)

        #creating vertical line of box4
        self.line14_box4_right =Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.line14_box4_right .place(x=1270,y=505,width=1,height=240)
        self.line14_box4_right .create_line(300, 35, 300, 200, dash = (5, 2))

        

        self.line15_box4_bottom = tk.Label(self.main_page_frame_view3_patient_registration_default_frame,text="",bg='black')
        self.line15_box4_bottom.place(x=900,y=745,width=370,height=1)

        #creating vertical line of box4 left
        self.line16_box4_left =Canvas(self.main_page_frame_view3_patient_registration_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.line16_box4_left .place(x=900,y=505,width=1,height=240)
        self.line16_box4_left .create_line(300, 35, 300, 200, dash = (5, 2))

        #main_page_frame_view3_patient_registration_default_frame-------end--------------

     
        self.main_page_frame_view3_patient_visit_default_frame=tk.Frame(self.root1,bg='black')
        self.main_page_frame_view3_patient_visit_default_frame['borderwidth']=0
        
        self.emergency_registration_mainheading1 = tk.Label(self.main_page_frame_view3_patient_visit_default_frame,text="patient visit",font=("lucida",15,"bold "),bg='blue')
        self.emergency_registration_mainheading1.place(x=5,y=5,width=1300,height=40)
     


        #patient_search_default_frame------start-------------
        self.main_page_frame_view3_patient_search_default_frame=tk.Frame(self.root1,bg='white')
        self.main_page_frame_view3_patient_search_default_frame['borderwidth']=0
        
        self.patient_search_mainheading1 = tk.Label(self.main_page_frame_view3_patient_search_default_frame,text="patient search",font=("lucida",15,"bold "),bg='blue')
        self.patient_search_mainheading1.place(x=5,y=5,width=1300,height=40)

        #main_buttons========================================start==========================================
        self.patient_search_button1_DISPLAY = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="DISPLAY",command=self.patient_search_default_display)
        self.patient_search_button1_DISPLAY.place(x=5,y=50,width=100,height=30)

        self.patient_search_button1_PAQTIENT_QUEUE = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="PAQTIENT QUEUE",command=self.patient_queue_default)
        self.patient_search_button1_PAQTIENT_QUEUE.place(x=115,y=50,width=100,height=30)

        self.patient_search_button1_EDIT_PATIENT_QUEUE = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="EDIT",command=self.patient_search_edit_fun)
        self.patient_search_button1_EDIT_PATIENT_QUEUE.place(x=225,y=50,width=100,height=30)

        self.patient_search_button1_DETAILS = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="DETAILS",command=self.patient_search_display_fun)
        self.patient_search_button1_DETAILS.place(x=335,y=50,width=100,height=30)

        self.patient_search_button1_EXIT = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="EXIT",command=self.home_default)
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

        
        self.patient_search_button7_tree_view_reset = tk.Button(self.main_page_frame_view3_patient_search_default_frame,text="RESET",command=self.patient_search_default_display_treeview_reset)
        self.patient_search_button7_tree_view_reset.place(x=450,y=300,width=70,height=25)

        #patient_search_input===========================================end====================================

        #patient_search_tree_view========================================start========================================
        # define columns
        self.patient_search_columns = ('id','fname','lname','phone_number','age','gender')

        self.patient_search_default_tree = ttk.Treeview(self.main_page_frame_view3_patient_search_default_frame, columns=self.patient_search_columns, show='headings')



        # define headings
        self.patient_search_default_tree.heading('id', text='Patient ID')
        self.patient_search_default_tree.heading('fname', text='First Name')
        self.patient_search_default_tree.heading('lname', text='Last Name')
        self.patient_search_default_tree.heading('phone_number', text='Phone Number')
        self.patient_search_default_tree.heading('age', text='Age')
        self.patient_search_default_tree.heading('gender', text='Gender')

        #patient_search_tree_view========================================end========================================
        #patient_table=====================================================start=======================================

        #patient_table=====================================================end=======================================
        #patient_search_edit_frame------start-------------
        self.main_page_frame_view3_patient_search_edit_frame=tk.Frame(self.root1,bg='white')
        self.main_page_frame_view3_patient_search_edit_frame['borderwidth']=0
        
        self.patient_search_edit_mainheading1 = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="patient info edit",font=("lucida",15,"bold "),bg='blue')
        self.patient_search_edit_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.patient_search_edit_Patient_ID_display_var=tk.StringVar()
        self.patient_search_edit_fname_display_var=tk.StringVar()
        self.patient_search_edit_mname_display_var=tk.StringVar()
        self.patient_search_edit_lname_display_var=tk.StringVar()
        self.patient_search_edit_dob_display_var=tk.StringVar()
        self.patient_search_edit_Phone_number1_display_var=tk.StringVar()
        self.patient_search_edit_Phone_number2_display_var=tk.StringVar()
        self.patient_search_edit_age_display_var=tk.StringVar()
        self.patient_search_edit_gender_display_var=tk.StringVar()
        self.patient_search_edit_adderess_display_var=tk.StringVar()
        self.patient_search_edit_city_display_var=tk.StringVar()
        self.patient_search_edit_emailid_display_var=tk.StringVar()
        self.patient_search_edit_blood_group_display_var=tk.StringVar()

        self.patient_search_edit_update_button = tk.Button(self.main_page_frame_view3_patient_search_edit_frame,text="UPDATE",command = self.patient_search_edit_update_button_fun)
        self.patient_search_edit_update_button.place(x=1200,y=55,width=50,height=25)

        self.patient_search_edit_Patient_ID = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Patient ID")
        self.patient_search_edit_Patient_ID.place(x=20,y=85,width=150,height=25)
        self.patient_search_edit_Patient_ID_display = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_Patient_ID_display_var ,font=("lucida",10,"bold "))
        self.patient_search_edit_Patient_ID_display.place(x=180,y=85,width=150,height=25)

        self.patient_search_edit_fname = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Fname ")
        self.patient_search_edit_fname.place(x=20,y=150,width=150,height=25)
        self.patient_search_edit_fname_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_fname_display_var)
        self.patient_search_edit_fname_display.place(x=180,y=150,width=150,height=25)

        self.patient_search_edit_mname = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Mname ")
        self.patient_search_edit_mname.place(x=490,y=150,width=150,height=25)
        self.patient_search_edit_mname_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_mname_display_var)
        self.patient_search_edit_mname_display.place(x=650,y=150,width=150,height=25)

        
        self.patient_search_edit_lname = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Lname ")
        self.patient_search_edit_lname.place(x=960,y=150,width=150,height=25)
        self.patient_search_edit_lname_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_lname_display_var)
        self.patient_search_edit_lname_display.place(x=1120,y=150,width=150,height=25)

        self.patient_search_edit_dob = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="DOB ")
        self.patient_search_edit_dob.place(x=20,y=215,width=150,height=25)
        self.patient_search_edit_dob_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_dob_display_var)
        self.patient_search_edit_dob_display.place(x=180,y=215,width=150,height=25)

        self.patient_search_edit_Phone_number1 = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Phone Number1")
        self.patient_search_edit_Phone_number1.place(x=20,y=280,width=150,height=25)
        self.patient_search_edit_Phone_number1_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_Phone_number1_display_var)
        self.patient_search_edit_Phone_number1_display.place(x=180,y=280,width=150,height=25)

        self.patient_search_edit_Phone_number2 = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Phone Number2")
        self.patient_search_edit_Phone_number2.place(x=490,y=280,width=150,height=25)
        self.patient_search_edit_Phone_number2_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_Phone_number2_display_var)
        self.patient_search_edit_Phone_number2_display.place(x=650,y=280,width=150,height=25)

        self.patient_search_edit_age = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Age")
        self.patient_search_edit_age.place(x=490,y=215,width=150,height=25)
        self.patient_search_edit_age_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_age_display_var)
        self.patient_search_edit_age_display.place(x=650,y=215,width=150,height=25)

        self.patient_search_edit_gender = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Gender")
        self.patient_search_edit_gender.place(x=960,y=215,width=150,height=25)
        self.patient_search_edit_gender_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_gender_display_var)
        self.patient_search_edit_gender_display.place(x=1120,y=215,width=150,height=25)

        self.patient_search_edit_adderess = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Address")
        self.patient_search_edit_adderess.place(x=20,y=345,width=150,height=25)
        self.patient_search_edit_adderess_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_adderess_display_var)
        self.patient_search_edit_adderess_display.place(x=180,y=345,width=150,height=25)

        self.patient_search_edit_city = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="City")
        self.patient_search_edit_city.place(x=490,y=345,width=150,height=25)
        self.patient_search_edit_city_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_city_display_var)
        self.patient_search_edit_city_display.place(x=650,y=345,width=150,height=25)

        self.patient_search_edit_emailid = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_Patient_ID_display_var)
        self.patient_search_edit_emailid.place(x=20,y=410,width=150,height=25)
        self.patient_search_edit_emailid_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_emailid_display_var)
        self.patient_search_edit_emailid_display.place(x=180,y=410,width=150,height=25)
        
        self.patient_search_edit_blood_group = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Blood Group")
        self.patient_search_edit_blood_group.place(x=20,y=410,width=150,height=25)
        self.patient_search_edit_blood_group_display = tk.Entry(self.main_page_frame_view3_patient_search_edit_frame,textvariable=self.patient_search_edit_blood_group_display_var)
        self.patient_search_edit_blood_group_display.place(x=180,y=410,width=150,height=25)

        self.patient_search_edit_ROOM_DETAILS = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="ROOM DETAILS")
        self.patient_search_edit_ROOM_DETAILS.place(x=5,y=468,width=100,height=25)
        self.patient_search_edit_line1 = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="",bg='black')
        self.patient_search_edit_line1.place(x=110,y=480,width=1160,height=1)

        self.patient_search_edit_ROOM_id = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="ROOM ID")
        self.patient_search_edit_ROOM_id.place(x=20,y=530,width=150,height=25)
        self.patient_search_edit_ROOM_id_display = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="ROOM ID Display")
        self.patient_search_edit_ROOM_id_display.place(x=180,y=530,width=150,height=25)
        self.patient_search_edit_ROOM_Floor = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="ROOM Floor")
        self.patient_search_edit_ROOM_Floor.place(x=490,y=530,width=150,height=25)
        self.patient_search_edit_ROOM_Floor_display = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="ROOM Floor Display")
        self.patient_search_edit_ROOM_Floor_display.place(x=650,y=530,width=150,height=25)
        self.patient_search_edit_ROOM_no = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="ROOM No")
        self.patient_search_edit_ROOM_no.place(x=960,y=530,width=150,height=25)
        self.patient_search_edit_ROOM_no_display = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="ROOM No Display")
        self.patient_search_edit_ROOM_no_display.place(x=1120,y=530,width=150,height=25)

        self.patient_search_edit_FINANCE_DETAILS = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="FINANCE DETAILS")
        self.patient_search_edit_FINANCE_DETAILS.place(x=5,y=588,width=100,height=25)
        self.patient_search_edit_line2 = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="",bg='black')
        self.patient_search_edit_line2.place(x=110,y=600,width=1160,height=1)

        self.patient_search_edit_FINANCE_Debit = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Debit")
        self.patient_search_edit_FINANCE_Debit.place(x=20,y=650,width=150,height=25)
        self.patient_search_edit_FINANCE_Debit_display = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Debit Display")
        self.patient_search_edit_FINANCE_Debit_display.place(x=180,y=650,width=150,height=25)
        self.patient_search_edit_FINANCE_Credit = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Credit")
        self.patient_search_edit_FINANCE_Credit.place(x=490,y=650,width=150,height=25)
        self.patient_search_edit_FINANCE_Credit_display = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Credit Display")
        self.patient_search_edit_FINANCE_Credit_display.place(x=650,y=650,width=150,height=25)
        self.patient_search_edit_FINANCE_Balance = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Balance")
        self.patient_search_edit_FINANCE_Balance.place(x=960,y=650,width=150,height=25)
        self.patient_search_edit_FINANCE_Balance_display = tk.Label(self.main_page_frame_view3_patient_search_edit_frame,text="Balance Display")
        self.patient_search_edit_FINANCE_Balance_display.place(x=1120,y=650,width=150,height=25)
        #patient_search_edit_frame------end-------------

        #patient_search_display_frame------start-------------
        self.main_page_frame_view3_patient_search_display_frame=tk.Frame(self.root1,bg='white')
        self.main_page_frame_view3_patient_search_display_frame['borderwidth']=0
        
        self.patient_search_display_mainheading1 = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="patient info display",font=("lucida",15,"bold "),bg='blue')
        self.patient_search_display_mainheading1.place(x=5,y=5,width=1300,height=40)

        

        self.patient_search_display_Patient_ID = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Patient ID")
        self.patient_search_display_Patient_ID.place(x=20,y=85,width=150,height=25)
        self.patient_search_display_Patient_ID_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Patient ID display",font=("lucida",10,"bold "))
        self.patient_search_display_Patient_ID_display.place(x=180,y=85,width=150,height=25)

        self.patient_search_display_fname = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Fname ")
        self.patient_search_display_fname.place(x=20,y=150,width=150,height=25)
        self.patient_search_display_fname_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Fname display")
        self.patient_search_display_fname_display.place(x=180,y=150,width=150,height=25)

        self.patient_search_display_mname = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Mname ")
        self.patient_search_display_mname.place(x=490,y=150,width=150,height=25)
        self.patient_search_display_mname_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Mname display")
        self.patient_search_display_mname_display.place(x=650,y=150,width=150,height=25)

        
        self.patient_search_display_lname = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Lname ")
        self.patient_search_display_lname.place(x=960,y=150,width=150,height=25)
        self.patient_search_display_lname_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Lname display")
        self.patient_search_display_lname_display.place(x=1120,y=150,width=150,height=25)

        self.patient_search_display_dob = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="DOB ")
        self.patient_search_display_dob.place(x=20,y=215,width=150,height=25)
        self.patient_search_display_dob_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="DOB display")
        self.patient_search_display_dob_display.place(x=180,y=215,width=150,height=25)

        self.patient_search_display_Phone_number1 = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Phone Number1")
        self.patient_search_display_Phone_number1.place(x=20,y=280,width=150,height=25)
        self.patient_search_display_Phone_number1_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Phone Number1 display")
        self.patient_search_display_Phone_number1_display.place(x=180,y=280,width=150,height=25)

        self.patient_search_display_Phone_number2 = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Phone Number2")
        self.patient_search_display_Phone_number2.place(x=490,y=280,width=150,height=25)
        self.patient_search_display_Phone_number2_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Phone Number2 display")
        self.patient_search_display_Phone_number2_display.place(x=650,y=280,width=150,height=25)

        self.patient_search_display_age = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Age")
        self.patient_search_display_age.place(x=490,y=215,width=150,height=25)
        self.patient_search_display_age_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Age display")
        self.patient_search_display_age_display.place(x=650,y=215,width=150,height=25)

        self.patient_search_display_gender = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Gender")
        self.patient_search_display_gender.place(x=960,y=215,width=150,height=25)
        self.patient_search_display_gender_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Gender display")
        self.patient_search_display_gender_display.place(x=1120,y=215,width=150,height=25)

        self.patient_search_display_adderess = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Address")
        self.patient_search_display_adderess.place(x=20,y=345,width=150,height=25)
        self.patient_search_display_adderess_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Address display")
        self.patient_search_display_adderess_display.place(x=180,y=345,width=150,height=25)

        self.patient_search_display_city = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="City")
        self.patient_search_display_city.place(x=490,y=345,width=150,height=25)
        self.patient_search_display_city_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="City display")
        self.patient_search_display_city_display.place(x=650,y=345,width=150,height=25)

        self.patient_search_display_emailid = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Email ID")
        self.patient_search_display_emailid.place(x=20,y=410,width=150,height=25)
        self.patient_search_display_emailid_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Email ID display")
        self.patient_search_display_emailid_display.place(x=180,y=410,width=150,height=25)

        self.patient_search_display_blood_group = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Blood Group")
        self.patient_search_display_blood_group.place(x=20,y=410,width=150,height=25)
        self.patient_search_display_blood_group_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="blood_group display")
        self.patient_search_display_blood_group_display.place(x=180,y=410,width=150,height=25)

        self.patient_search_display_ROOM_DETAILS = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="ROOM DETAILS")
        self.patient_search_display_ROOM_DETAILS.place(x=5,y=468,width=100,height=25)
        self.patient_search_display_line1 = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="",bg='black')
        self.patient_search_display_line1.place(x=110,y=480,width=1160,height=1)

        self.patient_search_display_ROOM_id = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="ROOM ID")
        self.patient_search_display_ROOM_id.place(x=20,y=530,width=150,height=25)
        self.patient_search_display_ROOM_id_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="ROOM ID Display")
        self.patient_search_display_ROOM_id_display.place(x=180,y=530,width=150,height=25)
        self.patient_search_display_ROOM_Floor = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="ROOM Floor")
        self.patient_search_display_ROOM_Floor.place(x=490,y=530,width=150,height=25)
        self.patient_search_display_ROOM_Floor_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="ROOM Floor Display")
        self.patient_search_display_ROOM_Floor_display.place(x=650,y=530,width=150,height=25)
        self.patient_search_display_ROOM_no = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="ROOM No")
        self.patient_search_display_ROOM_no.place(x=960,y=530,width=150,height=25)
        self.patient_search_display_ROOM_no_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="ROOM No Display")
        self.patient_search_display_ROOM_no_display.place(x=1120,y=530,width=150,height=25)

        self.patient_search_display_FINANCE_DETAILS = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="FINANCE DETAILS")
        self.patient_search_display_FINANCE_DETAILS.place(x=5,y=588,width=100,height=25)
        self.patient_search_display_line2 = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="",bg='black')
        self.patient_search_display_line2.place(x=110,y=600,width=1160,height=1)

        self.patient_search_display_FINANCE_Debit = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Debit")
        self.patient_search_display_FINANCE_Debit.place(x=20,y=650,width=150,height=25)
        self.patient_search_display_FINANCE_Debit_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Debit Display")
        self.patient_search_display_FINANCE_Debit_display.place(x=180,y=650,width=150,height=25)
        self.patient_search_display_FINANCE_Credit = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Credit")
        self.patient_search_display_FINANCE_Credit.place(x=490,y=650,width=150,height=25)
        self.patient_search_display_FINANCE_Credit_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Credit Display")
        self.patient_search_display_FINANCE_Credit_display.place(x=650,y=650,width=150,height=25)
        self.patient_search_display_FINANCE_Balance = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Balance")
        self.patient_search_display_FINANCE_Balance.place(x=960,y=650,width=150,height=25)
        self.patient_search_display_FINANCE_Balance_display = tk.Label(self.main_page_frame_view3_patient_search_display_frame,text="Balance Display")
        self.patient_search_display_FINANCE_Balance_display.place(x=1120,y=650,width=150,height=25)


        #finance details

        #patient_search_display_frame------end-------------
        #patient_search_default_frame------end-------------


        #patient_queue-------------------------start-------------
        #patient_queue_default_frame------start-------------
        
        self.main_page_frame_view3_patient_queue_default_frame=tk.Frame(self.root1,bg='light blue')
        self.main_page_frame_view3_patient_queue_default_frame['borderwidth']=0

        self.patient_queue_mainheading1 = tk.Label(self.main_page_frame_view3_patient_queue_default_frame,text="patient queue",font=("lucida",15,"bold "),bg='blue')
        self.patient_queue_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.patient_queue_button1_Reload_Queue = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Reload Queue",command=self.patient_queue_display)
        self.patient_queue_button1_Reload_Queue.place(x=5,y=50,width=150,height=30)

        self.patient_queue_button2_Send_to_OPD = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Send to OPD",command=self.patient_queue_send_to_OPD_fun)
        self.patient_queue_button2_Send_to_OPD.place(x=165,y=50,width=150,height=30)

       


        self.patient_queue_button3_Send_to_ipd = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Send to ipd",command=self.patient_queue_send_to_ipd_fun)
        self.patient_queue_button3_Send_to_ipd.place(x=325,y=50,width=150,height=30)

       

        self.patient_queue_button4_Delete = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Delete",command=self.patient_queue_Delete_fun)
        self.patient_queue_button4_Delete.place(x=485,y=50,width=150,height=30)

        self.patient_queue_button5_OPD_Patient_History = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="OPD Patient Queue",command=self.opd_queue_default)
        self.patient_queue_button5_OPD_Patient_History.place(x=645,y=50,width=150,height=30)

        self.patient_queue_button6_ipd_Patient_History = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="ipd Patient Queue",command=self.ipd_queue_default)
        self.patient_queue_button6_ipd_Patient_History.place(x=805,y=50,width=150,height=30)

        self.patient_queue_button7_Exit = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="Exit",command=self.home_default)
        self.patient_queue_button7_Exit.place(x=965,y=50,width=150,height=30)
        
        self.patient_queue_label_select_doctor= tk.Label(self.main_page_frame_view3_patient_queue_default_frame,text="Select Doctor*")
        self.patient_queue_label_select_doctor.place(x=20,y=100)

        self.patient_queue_value_inside = tk.StringVar(self.main_page_frame_view3_patient_queue_default_frame)
        self.patient_queue_value_inside.set('select role')
        self.patient_queue_roles_list = ["ALL"]
        self.patient_queue_role_entry = ttk.OptionMenu(self.main_page_frame_view3_patient_queue_default_frame,self.patient_queue_value_inside , *self.patient_queue_roles_list)
        self.patient_queue_role_entry.configure(width=30)
        self.patient_queue_role_entry.place(x=120,y=100)
        self.patient_queue_button7_tree_view_reset = tk.Button(self.main_page_frame_view3_patient_queue_default_frame,text="RESET",command=self.patient_queue_display_treeview_reset)
        self.patient_queue_button7_tree_view_reset.place(x=370,y=100,width=70,height=25)

        
        print("the valuse on the roles:",self.patient_queue_value_inside.get())


        #patient_queue_tree_view========================================start========================================
        # define columns
        self.patient_queue_columns = ('patinet_ID', 'First_name','Queue_Type','Queue_Status','Reason','doctor_Id','Doctor_name')
        """
        id
name
mname
lname
dob
age
gender
phone_number
phone_number2
queue_type
queue_status
reason
doctor_id
doctor_name
        """

        self.patient_queue_default_tree = ttk.Treeview(self.main_page_frame_view3_patient_queue_default_frame, columns=self.patient_queue_columns, show='headings')



        # define headings
        self.patient_queue_default_tree.heading('patinet_ID', text='patinet ID')
        self.patient_queue_default_tree.heading('First_name', text='First name')
        self.patient_queue_default_tree.heading('Last_name', text='Last name')
        self.patient_queue_default_tree.heading('Age', text='Age')
        self.patient_queue_default_tree.heading('Gender', text='Gender')
        self.patient_queue_default_tree.heading('Phone_Number1', text='Phone Number1')
        self.patient_queue_default_tree.heading('Phone_Number2', text='Phone Number2')
        self.patient_queue_default_tree.heading('Queue_Type', text='Queue Type')
        self.patient_queue_default_tree.heading('Queue_Status', text='Queue Status')
        self.patient_queue_default_tree.heading('Reason', text='Reason')
        self.patient_queue_default_tree.heading('doctor_Id', text='doctor Id')
        self.patient_queue_default_tree.heading('Doctor_name', text='Doctor name')



        #patient_search_tree_view========================================end========================================
        #patient_queue_default_frame-----------end-------------


        


        #patient_queue-------------------------end-------------

        # #lab_queue=====================================end=========================
        #main_page_frame_view3_lab_queue_defaulte_frame------start-------------
        self.main_page_frame_view3_lab_queue_default_frame=tk.Frame(self.root1,bg='light cyan')
        self.main_page_frame_view3_lab_queue_default_frame['borderwidth']=0

        self.lab_queue_default_mainheading1 = tk.Label(self.main_page_frame_view3_lab_queue_default_frame,text="lab queue",font=("lucida",15,"bold"),bg='blue')
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

        self.search_lab_queue_mainheading1 = tk.Label(self.main_page_frame_view3_search_lab_queue_frame,text="search lab queue",font=("lucida",15,"bold "),bg='blue')
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

        self.view_lab_report_mainheading1 = tk.Label(self.main_page_frame_view3_view_lab_report_frame,text="view lab report",font=("lucida",15,"bold "),bg='blue')
        self.view_lab_report_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.main_page_frame_view3_view_lab_report_frame_button1_lab_queue = tk.Button(self.main_page_frame_view3_view_lab_report_frame,text="Lab Queue",command=self.lab_queue_default)
        self.main_page_frame_view3_view_lab_report_frame_button1_lab_queue.place(x=50,y=55)

        self.main_page_frame_view3_view_lab_report_frame_button1_search_lab_queue = tk.Button(self.main_page_frame_view3_view_lab_report_frame,text="Search Lab Report",command= self.search_lab_queue)
        self.main_page_frame_view3_view_lab_report_frame_button1_search_lab_queue.place(x=200,y=55)

    
        self.main_page_frame_view3_view_lab_report_frame_button1_view_lab_report= tk.Button(self.main_page_frame_view3_view_lab_report_frame,text="View Lab Report",command=self.view_lab_report,bg='red')
        self.main_page_frame_view3_view_lab_report_frame_button1_view_lab_report.place(x=350,y=55)



        #main_page_frame_view3_view_lab_report_defaulte_frame------end-------------
        #lab_queue=====================================end=========================

        #main_page_frame_view3_opd_queue_default_frame----------------start-------------
        self.main_page_frame_view3_opd_queue_default_frame=tk.Frame(self.root1,bg='light blue')
        self.main_page_frame_view3_opd_queue_default_frame['borderwidth']=0

        self.opd_queue_mainheading1 = tk.Label(self.main_page_frame_view3_opd_queue_default_frame,text="OPD queue",font=("lucida",15,"bold"),bg='blue')
        self.opd_queue_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.opd_queue_button_reload=tk.Button(self.main_page_frame_view3_opd_queue_default_frame,text="Reload queue",command=self.opd_queue_display)
        self.opd_queue_button_reload.place(x=5,y=50,width=150,height=30)
        self.opd_queue_button_send_to_ipd=tk.Button(self.main_page_frame_view3_opd_queue_default_frame,text="Send to IPD",command=self.opd_queue_send_to_IPD_fun)
        self.opd_queue_button_send_to_ipd.place(x=165,y=50,width=150,height=30)
        self.opd_queue_button_completed=tk.Button(self.main_page_frame_view3_opd_queue_default_frame,text="Completed",command=self.opd_queue_completed_fun)
        self.opd_queue_button_completed.place(x=325,y=50,width=150,height=30)
        self.opd_queue_button_delete=tk.Button(self.main_page_frame_view3_opd_queue_default_frame,text="Delete",command=self.opd_queue_delete_fun)
        self.opd_queue_button_delete.place(x=485,y=50,width=150,height=30)
        self.opd_queue_button_exit=tk.Button(self.main_page_frame_view3_opd_queue_default_frame,text="Exit",command=self.home_default)
        self.opd_queue_button_exit.place(x=645,y=50,width=150,height=30)
        

        self.opd_queue_label_select_doctor= tk.Label(self.main_page_frame_view3_opd_queue_default_frame,text="Select Doctor*")
        self.opd_queue_label_select_doctor.place(x=20,y=100)




        self.opd_queue_value_inside = tk.StringVar(self.main_page_frame_view3_opd_queue_default_frame)
        self.opd_queue_value_inside.set('select role')
        self.opd_queue_roles_list = ["ALL"]
        self.opd_queue_role_entry = ttk.OptionMenu(self.main_page_frame_view3_opd_queue_default_frame,self.patient_queue_value_inside , *self.opd_queue_roles_list)
        self.opd_queue_role_entry.configure(width=30)
        self.opd_queue_role_entry.place(x=120,y=100)

        self.opd_queue_button_reset=tk.Button(self.main_page_frame_view3_opd_queue_default_frame,text="Reset",command=self.opd_queue_display_treeview_reset)
        self.opd_queue_button_reset.place(x=370,y=100,width=70,height=25)

        #opd_queue_tree_view========================================start========================================
        # define columns
        self.opd_queue_columns = ('first_name', 'last_name', 'email')

        self.opd_queue_default_tree = ttk.Treeview(self.main_page_frame_view3_opd_queue_default_frame, columns=self.opd_queue_columns, show='headings')



        # define headings
        self.opd_queue_default_tree.heading('first_name', text='First Name')
        self.opd_queue_default_tree.heading('last_name', text='Last Name')
        self.opd_queue_default_tree.heading('email', text='Email')
        #patient_search_tree_view========================================end========================================
        #opd_queue_default_frame-----------end-------------

        

 
        #main_page_frame_view3_opd_queue_default_frame-----------------------end-------------
        #main_page_frame_view3_ipo_queue_defaulte_frame----------------------start-------------
        self.main_page_frame_view3_ipd_queue_default_frame=tk.Frame(self.root1,bg='light blue')
        self.main_page_frame_view3_ipd_queue_default_frame['borderwidth']=0

        self.ipo_queue_mainheading1 = tk.Label(self.main_page_frame_view3_ipd_queue_default_frame,text="IPO queue",font=("lucida",15,"bold"),bg='blue')
        self.ipo_queue_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.ipd_queue_button_reload=tk.Button(self.main_page_frame_view3_ipd_queue_default_frame,text="Reload queue",command=self.ipd_queue_display)
        self.ipd_queue_button_reload.place(x=5,y=50,width=150,height=30)
        self.ipd_queue_button_send_to_ipo=tk.Button(self.main_page_frame_view3_ipd_queue_default_frame,text="Send to OPD",command=self.ipd_queue_send_to_OPD_fun)
        self.ipd_queue_button_send_to_ipo.place(x=165,y=50,width=150,height=30)
        self.ipd_queue_button_completed=tk.Button(self.main_page_frame_view3_ipd_queue_default_frame,text="Completed",command=self.ipd_queue_completed_fun)
        self.ipd_queue_button_completed.place(x=325,y=50,width=150,height=30)
        self.ipd_queue_button_delete=tk.Button(self.main_page_frame_view3_ipd_queue_default_frame,text="Delete",command=self.ipd_queue_delete_fun)
        self.ipd_queue_button_delete.place(x=485,y=50,width=150,height=30)
        self.ipd_queue_button_exit=tk.Button(self.main_page_frame_view3_ipd_queue_default_frame,text="Exit",command=self.home_default)
        self.ipd_queue_button_exit.place(x=645,y=50,width=150,height=30)
        

        self.ipd_queue_label_select_doctor= tk.Label(self.main_page_frame_view3_ipd_queue_default_frame,text="Select Doctor*")
        self.ipd_queue_label_select_doctor.place(x=20,y=100)




        self.ipd_queue_value_inside = tk.StringVar(self.main_page_frame_view3_ipd_queue_default_frame)
        self.ipd_queue_value_inside.set('select role')
        self.ipd_queue_roles_list = ["ALL"]
        self.ipd_queue_role_entry = ttk.OptionMenu(self.main_page_frame_view3_ipd_queue_default_frame,self.ipd_queue_value_inside , *self.ipd_queue_roles_list)
        self.ipd_queue_role_entry.configure(width=30)
        self.ipd_queue_role_entry.place(x=120,y=100)

        self.ipd_queue_button_reset=tk.Button(self.main_page_frame_view3_ipd_queue_default_frame,text="Reset",command=self.ipd_queue_display_treeview_reset)
        self.ipd_queue_button_reset.place(x=370,y=100,width=70,height=25)

        #ipd_queue_tree_view========================================start========================================
        # define columns
        self.ipd_queue_columns = ('first_name', 'last_name', 'email')

        self.ipd_queue_default_tree = ttk.Treeview(self.main_page_frame_view3_ipd_queue_default_frame, columns=self.ipd_queue_columns, show='headings')



        # define headings
        self.ipd_queue_default_tree.heading('first_name', text='First Name')
        self.ipd_queue_default_tree.heading('last_name', text='Last Name')
        self.ipd_queue_default_tree.heading('email', text='Email')
        #patient_search_tree_view========================================end========================================
        #ipd_queue_default_frame-----------end-------------

        #main_page_frame_view3_ipo_queue_defaulte_frame----------------------end-------------

        ##main_page_frame_view3_physical_management----------------------------start--------------------------
        #main_page_frame_view3_physical_management_book_frame---------------start-------------
        self.main_page_frame_view3_physical_management_book_frame=tk.Frame(self.root1,bg='cyan')
        self.main_page_frame_view3_physical_management_book_frame['borderwidth']=0

        self.main_page_frame_view3_physical_management_book_mainheading1 = tk.Label(self.main_page_frame_view3_physical_management_book_frame,text="Book Room",font=("lucida",15,"bold"),bg='blue')
        self.main_page_frame_view3_physical_management_book_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.main_page_frame_view3_physical_management_book_book_room = tk.Button(self.main_page_frame_view3_physical_management_book_frame,text="Book Room",bg='red',command= self.physical_management_book)
        self.main_page_frame_view3_physical_management_book_book_room.place(x=20,y=50,width=100,height=30)
        self.main_page_frame_view3_physical_management_book_Discharge_room = tk.Button(self.main_page_frame_view3_physical_management_book_frame,text="Discharge Room",command= self.physical_management_Discharge)
        self.main_page_frame_view3_physical_management_book_Discharge_room.place(x=130,y=50,width=100,height=30)
        self.main_page_frame_view3_physical_management_book_room_status = tk.Button(self.main_page_frame_view3_physical_management_book_frame,text="Room Status",command= self.physical_management_room_status)
        self.main_page_frame_view3_physical_management_book_room_status.place(x=240,y=50,width=100,height=30)

        self.main_page_frame_view3_physical_management_book_line_label= tk.Label(self.main_page_frame_view3_physical_management_book_frame,text="",bg='black')
        self.main_page_frame_view3_physical_management_book_line_label.place(x=5,y=85,width=1285,height=1)

        self.main_page_frame_view3_physical_management_book_book_room_refresh = tk.Button(self.main_page_frame_view3_physical_management_book_frame,text="Reload",command= self.physical_management_Book_room_fun)
        self.main_page_frame_view3_physical_management_book_book_room_refresh.place(x=20,y=90,width=150,height=30)
        self.main_page_frame_view3_physical_management_book_Discharge_room_book_room = tk.Button(self.main_page_frame_view3_physical_management_book_frame,text="Assign Room",command= self.physical_management_book_room_assaign_room_fun)
        self.main_page_frame_view3_physical_management_book_Discharge_room_book_room.place(x=180,y=90,width=150,height=30)
        self.main_page_frame_view3_physical_management_book_room_status_exit = tk.Button(self.main_page_frame_view3_physical_management_book_frame,text="Exit",command=self.home_default)
        self.main_page_frame_view3_physical_management_book_room_status_exit.place(x=340,y=90,width=150,height=30)
        self.main_page_frame_view3_physical_management_book_room_status_reset = tk.Button(self.main_page_frame_view3_physical_management_book_frame,text="Reset",command=self.physical_management_book_room_treeview_reset)
        self.main_page_frame_view3_physical_management_book_room_status_reset.place(x=500,y=90,width=150,height=30)
   

        #physical_management_book_room_tree_view========================================start========================================
        # define columns
        self.physical_management_book_room_columns = ('ROOM_ID', 'FLOOR_NO', 'ROOM_NO','ROOM_STATUS')

        self.physical_management_book_room_default_tree = ttk.Treeview(self.main_page_frame_view3_physical_management_book_frame, columns=self.physical_management_book_room_columns, show='headings')



        # define headings
        self.physical_management_book_room_default_tree.heading('ROOM_ID', text='ROOM ID')
        self.physical_management_book_room_default_tree.heading('FLOOR_NO', text='FLOOR NO')
        self.physical_management_book_room_default_tree.heading('ROOM_NO', text='ROOM NO')
        self.physical_management_book_room_default_tree.heading('ROOM_STATUS', text='ROOM STATUS')
        #patient_search_tree_view========================================end========================================
        #physical_management_book_room_default_frame-----------end-------------

        #main_page_frame_view3_physical_management_book_frame------------------end-------------
        #main_page_frame_view3_physical_management_Discharge_frame---------------start-------------
        self.main_page_frame_view3_physical_management_Discharge_frame=tk.Frame(self.root1,bg='LavenderBlush')
        self.main_page_frame_view3_physical_management_Discharge_frame['borderwidth']=0

        self.main_page_frame_view3_physical_management_Discharge_mainheading1 = tk.Label(self.main_page_frame_view3_physical_management_Discharge_frame,text="Discharge Room",font=("lucida",15,"bold"),bg='blue')
        self.main_page_frame_view3_physical_management_Discharge_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.main_page_frame_view3_physical_management_Discharge_book_room = tk.Button(self.main_page_frame_view3_physical_management_Discharge_frame,text="Book Room",command= self.physical_management_book)
        self.main_page_frame_view3_physical_management_Discharge_book_room.place(x=20,y=50,width=100,height=30)
        self.main_page_frame_view3_physical_management_Discharge_Discharge_room = tk.Button(self.main_page_frame_view3_physical_management_Discharge_frame,text="Discharge Room",bg='red' ,command= self.physical_management_Discharge)
        self.main_page_frame_view3_physical_management_Discharge_Discharge_room.place(x=130,y=50,width=100,height=30)
        self.main_page_frame_view3_physical_management_Discharge_room_status = tk.Button(self.main_page_frame_view3_physical_management_Discharge_frame,text="Room Status",command= self.physical_management_room_status)
        self.main_page_frame_view3_physical_management_Discharge_room_status.place(x=240,y=50,width=100,height=30)

        self.main_page_frame_view3_physical_management_Discharge_line_label= tk.Label(self.main_page_frame_view3_physical_management_Discharge_frame,text="",bg='black')
        self.main_page_frame_view3_physical_management_Discharge_line_label.place(x=5,y=85,width=1285,height=1)

        self.main_page_frame_view3_physical_management_Discharge_Discharge_room_refresh = tk.Button(self.main_page_frame_view3_physical_management_Discharge_frame,text="Reload",command=self.physical_management_Discharge_room_fun)
        self.main_page_frame_view3_physical_management_Discharge_Discharge_room_refresh.place(x=20,y=90,width=150,height=30)
        self.main_page_frame_view3_physical_management_Discharge_Discharge_room_discharge_room = tk.Button(self.main_page_frame_view3_physical_management_Discharge_frame,text="discharge Room",command= self.physical_management_Discharge_room_Discharge_room_fun)
        self.main_page_frame_view3_physical_management_Discharge_Discharge_room_discharge_room.place(x=180,y=90,width=150,height=30)
        self.main_page_frame_view3_physical_management_Discharge_room_status_exit = tk.Button(self.main_page_frame_view3_physical_management_Discharge_frame,text="Exit",command=self.home_default)
        self.main_page_frame_view3_physical_management_Discharge_room_status_exit.place(x=340,y=90,width=150,height=30)
        self.main_page_frame_view3_physical_management_Discharge_room_status_reset = tk.Button(self.main_page_frame_view3_physical_management_Discharge_frame,text="Reset",command= self.physical_management_Discharge_room_treeview_reset)
        self.main_page_frame_view3_physical_management_Discharge_room_status_reset.place(x=500,y=90,width=150,height=30)

        
        #physical_management_Discharge_room_tree_view========================================start========================================
        # define columns
        self.physical_management_Discharge_room_columns = ('ROOM_ID', 'FLOOR_NO', 'ROOM_NO','ROOM_STATUS')

        self.physical_management_Discharge_room_default_tree = ttk.Treeview(self.main_page_frame_view3_physical_management_Discharge_frame, columns=self.physical_management_Discharge_room_columns, show='headings')



        # define headings
        self.physical_management_Discharge_room_default_tree.heading('ROOM_ID', text='ROOM ID')
        self.physical_management_Discharge_room_default_tree.heading('FLOOR_NO', text='FLOOR NO')
        self.physical_management_Discharge_room_default_tree.heading('ROOM_NO', text='ROOM NO')
        self.physical_management_Discharge_room_default_tree.heading('ROOM_STATUS', text='ROOM STATUS')
        #patient_search_tree_view========================================end========================================
        #physical_management_Discharge_room_default_frame-----------end-------------

        #main_page_frame_view3_physical_management_Discharge_frame------------------end-------------
        #main_page_frame_view3_physical_management_room_status_frame---------------start-------------
        self.main_page_frame_view3_physical_management_room_status_frame=tk.Frame(self.root1,bg='gray85')
        self.main_page_frame_view3_physical_management_room_status_frame['borderwidth']=0

        self.main_page_frame_view3_physical_management_room_status_mainheading1 = tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="Room Status",font=("lucida",15,"bold"),bg='blue')
        self.main_page_frame_view3_physical_management_room_status_mainheading1.place(x=5,y=5,width=1300,height=40)



        self.main_page_frame_view3_physical_management_room_status_book_room = tk.Button(self.main_page_frame_view3_physical_management_room_status_frame,text="Book Room",command= self.physical_management_book)
        self.main_page_frame_view3_physical_management_room_status_book_room.place(x=20,y=50,width=100,height=30)
        self.main_page_frame_view3_physical_management_room_status_room_status_room = tk.Button(self.main_page_frame_view3_physical_management_room_status_frame,text="Discharge Room",command= self.physical_management_Discharge)
        self.main_page_frame_view3_physical_management_room_status_room_status_room.place(x=130,y=50,width=100,height=30)
        self.main_page_frame_view3_physical_management_room_status_room_status = tk.Button(self.main_page_frame_view3_physical_management_room_status_frame,text="Room Status",bg='red',command= self.physical_management_room_status)
        self.main_page_frame_view3_physical_management_room_status_room_status.place(x=240,y=50,width=100,height=30)

        self.main_page_frame_view3_physical_management_room_status_avaliable_color = tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text=" ",bg='green')
        self.main_page_frame_view3_physical_management_room_status_avaliable_color.place(x=820,y=50,width=20,height=20)
        self.main_page_frame_view3_physical_management_room_status_avaliable = tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="avaliable",bg='gray85')
        self.main_page_frame_view3_physical_management_room_status_avaliable.place(x=840,y=50,width=60,height=20)
        
        self.main_page_frame_view3_physical_management_room_status_unavaliable_color = tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text=" ",bg='red')
        self.main_page_frame_view3_physical_management_room_status_unavaliable_color.place(x=920,y=50,width=20,height=20)
        self.main_page_frame_view3_physical_management_room_status_unavaliable = tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="unavaliable",bg='gray85')
        self.main_page_frame_view3_physical_management_room_status_unavaliable.place(x=940,y=50,width=70,height=20)
         
        
        self.main_page_frame_view3_physical_management_room_status_maintenance_color = tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="",bg='yellow')
        self.main_page_frame_view3_physical_management_room_status_maintenance_color.place(x=1030,y=50,width=20,height=20)
        self.main_page_frame_view3_physical_management_room_status_maintenance = tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="maintenance",bg='gray85')
        self.main_page_frame_view3_physical_management_room_status_maintenance.place(x=1050,y=50,width=80,height=20)
        

        self.main_page_frame_view3_physical_management_room_status_Refresh = tk.Button(self.main_page_frame_view3_physical_management_room_status_frame,text="Refresh Room Status",command= self.physical_management_room_status_refresh)
        self.main_page_frame_view3_physical_management_room_status_Refresh.place(x=20,y=90,width=150,height=25)

        

        #floor1===========================start=====================================
        self.room_statusfloor1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="FLOOR1",bg='burlywood4')
        self.room_statusfloor1_label.place(x=50,y=125,width=200,height=80)

        self.room_statusfloor1_to_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor1_to_room1_label.place(x=250,y=140,width=50,height=50)

        self.room_statusfloor1_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room1",bg='white')
        self.room_statusfloor1_room1_label.place(x=300,y=140,width=150,height=50)

        self.room_statusfloor1_room1_to_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor1_room1_to_room2_label.place(x=450,y=140,width=50,height=50)

        self.room_statusfloor1_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room2",bg='white')
        self.room_statusfloor1_room2_label.place(x=500,y=140,width=150,height=50)

        self.room_statusfloor1_room2_to_room3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor1_room2_to_room3_label.place(x=650,y=140,width=50,height=50) 

        self.room_statusfloor1_room3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room3",bg='white')
        self.room_statusfloor1_room3_label.place(x=700,y=140,width=150,height=50)

        self.room_statusfloor1_room3_to_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor1_room3_to_room4_label.place(x=850,y=140,width=50,height=50)

        self.room_statusfloor1_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room4",bg='white')
        self.room_statusfloor1_room4_label.place(x=900,y=140,width=150,height=50)

        self.room_statusfloor1_room4_to_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor1_room4_to_room5_label.place(x=1050,y=140,width=50,height=50)

        self.room_statusfloor1_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room5",bg='white')
        self.room_statusfloor1_room5_label.place(x=1100,y=140,width=150,height=50)
        #floor1===========================end=====================================
        
        #floor2===========================start=====================================
        self.room_statusfloor2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="FLOOR2",bg='burlywood4')
        self.room_statusfloor2_label.place(x=50,y=255,width=200,height=80)

        self.room_statusfloor2_to_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor2_to_room1_label.place(x=250,y=270,width=50,height=50)

        self.room_statusfloor2_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room1",bg='white')
        self.room_statusfloor2_room1_label.place(x=300,y=270,width=150,height=50)

        self.room_statusfloor2_room1_to_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor2_room1_to_room2_label.place(x=450,y=270,width=50,height=50)

        self.room_statusfloor2_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room2",bg='white')
        self.room_statusfloor2_room2_label.place(x=500,y=270,width=150,height=50)

        self.room_statusfloor2_room2_to_room3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor2_room2_to_room3_label.place(x=650,y=270,width=50,height=50) 

        self.room_statusfloor2_room3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room3",bg='white')
        self.room_statusfloor2_room3_label.place(x=700,y=270,width=150,height=50)

        self.room_statusfloor2_room3_to_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor2_room3_to_room4_label.place(x=850,y=270,width=50,height=50)

        self.room_statusfloor2_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room4",bg='white')
        self.room_statusfloor2_room4_label.place(x=900,y=270,width=150,height=50)

        self.room_statusfloor2_room4_to_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor2_room4_to_room5_label.place(x=1050,y=270,width=50,height=50)

        self.room_statusfloor2_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room5",bg='white')
        self.room_statusfloor2_room5_label.place(x=1100,y=270,width=150,height=50)
        #floor2===========================end=====================================

        #floor3===========================start=====================================
        self.room_statusfloor3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="FLOOR3",bg='burlywood4')
        self.room_statusfloor3_label.place(x=50,y=385,width=200,height=80)

        self.room_statusfloor3_to_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor3_to_room1_label.place(x=250,y=400,width=50,height=50)

        self.room_statusfloor3_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room1",bg='white')
        self.room_statusfloor3_room1_label.place(x=300,y=400,width=150,height=50)

        self.room_statusfloor3_room1_to_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor3_room1_to_room2_label.place(x=450,y=400,width=50,height=50)

        self.room_statusfloor3_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room2",bg='white')
        self.room_statusfloor3_room2_label.place(x=500,y=400,width=150,height=50)

        self.room_statusfloor3_room2_to_room3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor3_room2_to_room3_label.place(x=650,y=400,width=50,height=50) 

        self.room_statusfloor3_room3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room3",bg='white')
        self.room_statusfloor3_room3_label.place(x=700,y=400,width=150,height=50)

        self.room_statusfloor3_room3_to_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor3_room3_to_room4_label.place(x=850,y=400,width=50,height=50)

        self.room_statusfloor3_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room4",bg='white')
        self.room_statusfloor3_room4_label.place(x=900,y=400,width=150,height=50)

        self.room_statusfloor3_room4_to_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor3_room4_to_room5_label.place(x=1050,y=400,width=50,height=50)

        self.room_statusfloor3_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room5",bg='white')
        self.room_statusfloor3_room5_label.place(x=1100,y=400,width=150,height=50)
        #floor3===========================end=====================================

        #floor4===========================start=====================================

        self.room_statusfloor4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="FLOOR4",bg='burlywood4')
        self.room_statusfloor4_label.place(x=50,y=515,width=200,height=80)

        self.room_statusfloor4_to_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor4_to_room1_label.place(x=250,y=530,width=50,height=50)

        self.room_statusfloor4_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room1",bg='white')
        self.room_statusfloor4_room1_label.place(x=300,y=530,width=150,height=50)

        self.room_statusfloor4_room1_to_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor4_room1_to_room2_label.place(x=450,y=530,width=50,height=50)

        self.room_statusfloor4_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room2",bg='white')
        self.room_statusfloor4_room2_label.place(x=500,y=530,width=150,height=50)
        
        self.room_statusfloor4_room2_to_room3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor4_room2_to_room3_label.place(x=650,y=530,width=50,height=50) 

        self.room_statusfloor4_room3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room3",bg='white')
        self.room_statusfloor4_room3_label.place(x=700,y=530,width=150,height=50)

        self.room_statusfloor4_room3_to_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor4_room3_to_room4_label.place(x=850,y=530,width=50,height=50)

        self.room_statusfloor4_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room4",bg='white')
        self.room_statusfloor4_room4_label.place(x=900,y=530,width=150,height=50)

        self.room_statusfloor4_room4_to_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor4_room4_to_room5_label.place(x=1050,y=530,width=50,height=50)

        self.room_statusfloor4_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room5",bg='white')
        self.room_statusfloor4_room5_label.place(x=1100,y=530,width=150,height=50)
        #floor4===========================end=====================================

        #floor5===========================start=====================================
        self.room_statusfloor5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="FLOOR5",bg='burlywood4')
        self.room_statusfloor5_label.place(x=50,y=645,width=200,height=80)

        self.room_statusfloor5_to_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor5_to_room1_label.place(x=250,y=660,width=50,height=50)

        self.room_statusfloor5_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room1",bg='white')
        self.room_statusfloor5_room1_label.place(x=300,y=660,width=150,height=50)

        self.room_statusfloor5_room1_to_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor5_room1_to_room2_label.place(x=450,y=660,width=50,height=50)

        self.room_statusfloor5_room2_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room2",bg='white')
        self.room_statusfloor5_room2_label.place(x=500,y=660,width=150,height=50)

        self.room_statusfloor5_room2_to_room1_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor5_room2_to_room1_label.place(x=650,y=660,width=50,height=50)

        self.room_statusfloor5_room3_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room3",bg='white')
        self.room_statusfloor5_room3_label.place(x=700,y=660,width=150,height=50)

        self.room_statusfloor5_room3_to_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor5_room3_to_room4_label.place(x=850,y=660,width=50,height=50)

        self.room_statusfloor5_room4_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room4",bg='white')
        self.room_statusfloor5_room4_label.place(x=900,y=660,width=150,height=50)

        self.room_statusfloor5_room4_to_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="-------->",bg='gray85')
        self.room_statusfloor5_room4_to_room5_label.place(x=1050,y=660,width=50,height=50)

        self.room_statusfloor5_room5_label= tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="room5",bg='white')
        self.room_statusfloor5_room5_label.place(x=1100,y=660,width=150,height=50)
        #floor5===========================end=====================================




        #main_page_frame_view3_physical_management_room_status_frame------------------end-------------
        
        ##main_page_frame_view3_physical_management-------------------------------end-----------------------

        #main_page_frame_view3_dialy_collection-------------start---------------------------
        #main_page_frame_view3_dialy_collection_default_frame---------start--------------------
        self.main_page_frame_view3_dialy_collection_default_frame = tk.Frame(self.root1,bg='pink')
        self.main_page_frame_view3_dialy_collection_default_frame['borderwidth']=0

        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both = tk.Button(self.main_page_frame_view3_dialy_collection_default_frame,text="dialy collection ",command=self.dialy_collection_default,bg='red')
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both.place(x=50,y=20)

        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipd = tk.Button(self.main_page_frame_view3_dialy_collection_default_frame,text="dialy collection ipd",command= self.dialy_collection_ipd)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipd.place(x=200,y=20)

    
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd = tk.Button(self.main_page_frame_view3_dialy_collection_default_frame,text="dialy collection opd",command=self.dialy_collection_opd)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd.place(x=350,y=20)

        self.mid_line =Canvas(self.main_page_frame_view3_dialy_collection_default_frame,width=1,height=200,bg='black',highlightthickness = 1, highlightbackground = 'black')
        self.mid_line .place(x=590,y=100,width=2,height=1000)
        self.mid_line .create_line(300, 35, 300, 200, dash = (5, 2))

        self.right_heading_label1= tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Dialy Collection ipd",font= ("arial ", 18))
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
        self.right_heading_label2= tk.Label(self.main_page_frame_view3_dialy_collection_default_frame,text="Dialy Collection OPD",font= ("arial ", 18))
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

        #main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame-------------start----------
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame = tk.Frame(self.root1,bg='Light Blue')
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame['borderwidth']=0

        
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="dialy collection ",command=self.dialy_collection_default)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both.place(x=50,y=20)

        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipd = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="dialy collection ipd",command= self.dialy_collection_ipd,bg='red')
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipd.place(x=200,y=20)

    
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="dialy collection opd",command=self.dialy_collection_opd)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd.place(x=350,y=20)

        self.right_heading_label_ipd1 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="Dialy Collection ipd",font= ("arial ", 18))
        self.right_heading_label_ipd1.place(x=50,y=105,width=250,height=35)

        self.left_label_ipd1 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="Total consulting charge")
        self.left_label_ipd1.place(x=50,y=170,width=130,height=15)
        self.left_label_ipd1var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame)
        self.left_label_ipd1var.set(000)
        self.left_label_ipd1var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame, textvariable=self.left_label_ipd1var)
        self.left_label_ipd1var_display.place(x=450,y=170,width=50,height=15)

        self.left_label_ipd2 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="Total miscellaneous charge")
        self.left_label_ipd2.place(x=50,y=210,width=145,height=15)
        self.left_label_ipd2var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame)
        self.left_label_ipd2var.set(000)
        self.left_label_ipd2var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame, textvariable=self.left_label_ipd2var)
        self.left_label_ipd2var_display.place(x=450,y=210,width=50,height=15)

        self.left_label_ipd3 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="Total other charge")
        self.left_label_ipd3.place(x=50,y=250,width=100,height=15)
        self.left_label_ipd3var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame)
        self.left_label_ipd3var.set(000)
        self.left_label_ipd3var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame, textvariable=self.left_label_ipd3var)
        self.left_label_ipd3var_display.place(x=450,y=250,width=50,height=15)

        self.left_label_ipd4 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="Total Lab Test Charges")
        self.left_label_ipd4.place(x=50,y=290,width=120,height=15)
        self.left_label_ipd4var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame)
        self.left_label_ipd4var.set(000)
        self.left_label_ipd4var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame, textvariable=self.left_label_ipd4var)
        self.left_label_ipd4var_display.place(x=450,y=290,width=50,height=15)

        self.left_label_ipd5 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="Total Consumble charge")
        self.left_label_ipd5.place(x=50,y=330,width=130,height=15)
        self.left_label_ipd5var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame)
        self.left_label_ipd5var.set(000)
        self.left_label_ipd5var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame, textvariable=self.left_label_ipd5var)
        self.left_label_ipd5var_display.place(x=450,y=330,width=50,height=15)

        self.left_label_ipd6 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="total procedure charge")
        self.left_label_ipd6.place(x=50,y=370,width=125,height=15)
        self.left_label_ipd6var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame)
        self.left_label_ipd6var.set(000)
        self.left_label_ipd6var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame, textvariable=self.left_label_ipd6var)
        self.left_label_ipd6var_display.place(x=450,y=370,width=50,height=15)

        self.left_label_ipd7 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame,text="Total Dialy Collection")
        self.left_label_ipd7.place(x=50,y=410,width=112,height=15)
        self.left_label_ipd7var = tk.IntVar(self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame)
        self.left_label_ipd7var.set(000)
        self.left_label_ipd7var_display = tk.Label( self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame, textvariable=self.left_label_ipd7var)
        self.left_label_ipd7var_display.place(x=450,y=410,width=50,height=15)
       


        #main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame-------------end------------

        #main_page_frame_view3_dialy_collection_dialy_collection_opd_frame------------start-------------
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame = tk.Frame(self.root1,bg='Orange')
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame['borderwidth']=0
        
         
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="dialy collection ",command=self.dialy_collection_default)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_both.place(x=50,y=20)

        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipd = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="dialy collection ipd",command= self.dialy_collection_ipd)
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_ipd.place(x=200,y=20)

    
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd = tk.Button(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="dialy collection opd",command=self.dialy_collection_opd,bg='red')
        self.main_page_frame_view3_dialy_collection_default_frame_button1_dialy_collection_opd.place(x=350,y=20)
        
        self.right_heading_label_opd1 = tk.Label(self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame,text="Dialy Collection OPD",font= ("arial ", 18))
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
        self.main_page_frame_view3_patient_visit_default_frame_status = "None"

        self.main_page_frame_view3_patient_search_default_frame_status= "None"
        self.main_page_frame_view3_patient_search_edit_frame_status = "None"
        self.main_page_frame_view3_patient_search_display_frame_status = "None"

        self.main_page_frame_view3_patient_queue_default_frame_status= "None"
        

        self.main_page_frame_view3_lab_queue_default_frame_status= "None"
        self.main_page_frame_view3_search_lab_queue_frame_status= "None"
        self.main_page_frame_view3_view_lab_report_frame_status = "None"

        self.main_page_frame_view3_opd_queue_default_frame_status= "None"
        self.main_page_frame_view3_ipo_queue_default_frame_status= "None"

        self.main_page_frame_view3_physical_management_book_frame_status= "None"
        self.main_page_frame_view3_physical_management_Discharge_frame_status= "None"
        self.main_page_frame_view3_physical_management_room_status_frame_status= "None"


   
        
        self.main_page_frame_view3_dialy_collection_default_frame_status = "None"
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_status = "None"
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_status = "None"
        
        
         #frames status variables---------------------end----------------------------
    #search_patient_functions==============================start==================================
    def patient_search_default_display(self):
        self.patient_search_default_display_just_treeview_reset() 
        self.patient_search_input_reg_id_var_str=None
        self.patient_search_input_Fname_var_str=None
        self.patient_search_input_Lname_var_str=None
        self.patient_search_input_Phone_No_var_str=None
        
        
        
        if self.patient_search_input_reg_id_var.get() == 0:
            pass
        else :
            print("self.patient_search_input_reg_id_var.get():",self.patient_search_input_reg_id_var.get())
            self.patient_search_input_reg_id_var_str = str(self.patient_search_input_reg_id_var.get())
            print("self.patient_search_input_reg_id_var_str:",self.patient_search_input_reg_id_var_str)
        if self.patient_search_input_Fname_var.get() == '':
            pass
        else :
            print("self.patient_search_input_Fname_var.get():",self.patient_search_input_Fname_var.get())
            self.patient_search_input_Fname_var_str = str(self.patient_search_input_Fname_var.get())
            print("self.patient_search_input_Fname_var_str:",self.patient_search_input_Fname_var_str)
        if self.patient_search_input_Lname_var.get() == '':
            pass
        else :
            print("self.patient_search_input_Lname_var.get():",self.patient_search_input_Lname_var.get())
            self.patient_search_input_Lname_var_str = str(self.patient_search_input_Lname_var.get())
            print("self.patient_search_input_Lname_var_str:",self.patient_search_input_Lname_var_str)
        if self.patient_search_input_Phone_No_var.get() == 0:
            pass
        else :
            print("self.patient_search_input_Phone_No_var.get():",self.patient_search_input_Phone_No_var.get())
            self.patient_search_input_Phone_No_var_str = str(self.patient_search_input_Phone_No_var.get())
            print("self.patient_search_input_Phone_No_var_str:",self.patient_search_input_Phone_No_var_str)
        self.patient_search_table_command =" select id,name,lname,phone_number,age,gender from patient_details where "
        self.patient_search_command = None
        if self.patient_search_input_reg_id_var.get() != 0 and self.patient_search_input_Fname_var.get() == '' and self.patient_search_input_Lname_var.get() == '' and self.patient_search_input_Phone_No_var.get() == 0:
            #1
            self.patient_search_command= self.patient_search_table_command + "id = " + self.patient_search_input_reg_id_var_str 
        elif self.patient_search_input_reg_id_var.get() == 0 and self.patient_search_input_Fname_var.get() != '' and self.patient_search_input_Lname_var.get() == '' and self.patient_search_input_Phone_No_var.get() == 0:
            #2
            self.patient_search_command= self.patient_search_table_command + " name like '%" + self.patient_search_input_Fname_var_str + "%'"          
        elif self.patient_search_input_reg_id_var.get() == 0 and self.patient_search_input_Fname_var.get() == '' and self.patient_search_input_Lname_var.get() != '' and self.patient_search_input_Phone_No_var.get() == 0:
            #3
            self.patient_search_command= self.patient_search_table_command  + " lname like '%" + self.patient_search_input_Lname_var_str  + "%' "        
        elif self.patient_search_input_reg_id_var.get() == 0 and self.patient_search_input_Fname_var.get() == '' and self.patient_search_input_Lname_var.get() == '' and self.patient_search_input_Phone_No_var.get() != 0:
            #4
            self.patient_search_command= self.patient_search_table_command + " phone_number = " +  self.patient_search_input_Phone_No_var_str
        elif self.patient_search_input_reg_id_var.get() != 0 and self.patient_search_input_Fname_var.get() != '' and self.patient_search_input_Lname_var.get() == '' and self.patient_search_input_Phone_No_var.get() == 0:
            #12
            self.patient_search_command= self.patient_search_table_command + " id = " + self.patient_search_input_reg_id_var_str + "  or name like '%" + self.patient_search_input_Fname_var_str + "%'"          
        elif self.patient_search_input_reg_id_var.get() != 0 and self.patient_search_input_Fname_var.get() == '' and self.patient_search_input_Lname_var.get() != '' and self.patient_search_input_Phone_No_var.get() == 0:
            #13
            self.patient_search_command= self.patient_search_table_command + " id = " + self.patient_search_input_reg_id_var_str + " or  lname like '%" + self.patient_search_input_Lname_var_str  + "%' "        
        elif self.patient_search_input_reg_id_var.get() != 0 and self.patient_search_input_Fname_var.get() == '' and self.patient_search_input_Lname_var.get() == '' and self.patient_search_input_Phone_No_var.get() != 0:
            #14
            self.patient_search_command= self.patient_search_table_command + " id = " + self.patient_search_input_reg_id_var_str + " or  phone_number = " +  self.patient_search_input_Phone_No_var_str
        elif self.patient_search_input_reg_id_var.get() == 0 and self.patient_search_input_Fname_var.get() != '' and self.patient_search_input_Lname_var.get() != '' and self.patient_search_input_Phone_No_var.get() == 0:
            #23
            self.patient_search_command= self.patient_search_table_command +  " name like '%" + self.patient_search_input_Fname_var_str + "%'"  + " or  lname like '%" + self.patient_search_input_Lname_var_str  + "%' "        
        elif self.patient_search_input_reg_id_var.get() == 0 and self.patient_search_input_Fname_var.get() != '' and self.patient_search_input_Lname_var.get() == '' and self.patient_search_input_Phone_No_var.get() != 0:
            #24
            self.patient_search_command= self.patient_search_table_command + " name like '%" + self.patient_search_input_Fname_var_str + "%'"  + " or phone_number = " +  self.patient_search_input_Phone_No_var_str
        elif self.patient_search_input_reg_id_var.get() == 0 and self.patient_search_input_Fname_var.get() == '' and self.patient_search_input_Lname_var.get() != '' and self.patient_search_input_Phone_No_var.get() != 0:
            #34
            self.patient_search_command= self.patient_search_table_command +" lname like '%" + self.patient_search_input_Lname_var_str  + "%' " + " or phone_number = " +  self.patient_search_input_Phone_No_var_str
        elif self.patient_search_input_reg_id_var.get() != 0 and self.patient_search_input_Fname_var.get() != '' and self.patient_search_input_Lname_var.get() != '' and self.patient_search_input_Phone_No_var.get() == 0:
            #123
            self.patient_search_command= self.patient_search_table_command + " id = " + self.patient_search_input_reg_id_var_str + "  or name like '%" + self.patient_search_input_Fname_var_str + "%'"  + " or  lname like '%" + self.patient_search_input_Lname_var_str  + "%' "        
        elif self.patient_search_input_reg_id_var.get() != 0 and self.patient_search_input_Fname_var.get() != '' and self.patient_search_input_Lname_var.get() == '' and self.patient_search_input_Phone_No_var.get() != 0:
            #124
            self.patient_search_command= self.patient_search_table_command + " id = " + self.patient_search_input_reg_id_var_str + "  or name like '%" + self.patient_search_input_Fname_var_str + "%'"  + " or phone_number = " +  self.patient_search_input_Phone_No_var_str       
        elif self.patient_search_input_reg_id_var.get() != 0 and self.patient_search_input_Fname_var.get() == '' and self.patient_search_input_Lname_var.get() != '' and self.patient_search_input_Phone_No_var.get() != 0:
            #134
            self.patient_search_command= self.patient_search_table_command + "id = " + self.patient_search_input_reg_id_var_str + " or  lname like '%" + self.patient_search_input_Lname_var_str  + "%' " + " or phone_number = " +  self.patient_search_input_Phone_No_var_str       
        elif self.patient_search_input_reg_id_var.get() == 0 and self.patient_search_input_Fname_var.get() != '' and self.patient_search_input_Lname_var.get() != '' and self.patient_search_input_Phone_No_var.get() != 0:
            #243
            self.patient_search_command= self.patient_search_table_command + " name like '%" + self.patient_search_input_Fname_var_str + "%'"  + " or  lname like '%" + self.patient_search_input_Lname_var_str  + "%' " + " or phone_number = " +  self.patient_search_input_Phone_No_var_str
        elif self.patient_search_input_reg_id_var.get() != 0 and self.patient_search_input_Fname_var.get() != '' and self.patient_search_input_Lname_var.get() != '' and self.patient_search_input_Phone_No_var.get() != 0:
            #1234
            self.patient_search_command= self.patient_search_table_command + "id = " + self.patient_search_input_reg_id_var_str + "  or name like '%" + self.patient_search_input_Fname_var_str + "%'"  + " or  lname like '%" + self.patient_search_input_Lname_var_str  + "%' " + " or phone_number = " +  self.patient_search_input_Phone_No_var_str       
        print("self.patient_search_command:",self.patient_search_command)
        self.patient_search_command_result= None    
        if self.patient_search_command != None:
            self.patient_search_command_result = login_check.get_execution_result(self.patient_search_command)
        print("self.patient_search_command_result:",self.patient_search_command_result)
        #self.patient_search_selectItem()
        #adding the values into contact list 
        self.patient_search_contacts = []
        if self.patient_search_command_result != None:
              for i in self.patient_search_command_result:
                    self.patient_search_contacts.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}', f'{i[4]}',f'{i[5]}'))
            #self.patient_search_contacts.append((f'patient_search_first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview 
        if self.patient_search_contacts != None:
            for contact in self.patient_search_contacts:
                 self.patient_search_default_tree.insert('', tk.END, values=contact)

        self.patient_search_default_tree.place(x=15,y=340,width=1150,height=400)
        #tree.grid(row=0, column=0, sticky='nsew')

        #ading the scroll baar 
        self.patient_search_scrollbar = ttk.Scrollbar(self.main_page_frame_view3_patient_search_default_frame, orient=tk.VERTICAL, command=self.patient_search_default_tree.yview)
        self.patient_search_default_tree.configure(yscroll=self.patient_search_scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        self.patient_search_scrollbar.place(x=1165, y=340,width=15,height=400)
        

    def patient_search_selectItem(self):
        #curItem = tree.focus()
        #print(curItem, a)
        self.patient_search_selected = self.patient_search_default_tree.focus()
        print("self.patient_search_selected in selectitem" + self.patient_search_selected)
        if (self.patient_search_selected != ''):
             self.patient_search_temp = self.patient_search_default_tree.item(self.patient_search_selected, 'values')
             print(self.patient_search_temp)

    def patient_search_default_display_treeview_reset(self):
        self.patient_search_input_reg_id_var.set(0)
        self.patient_search_input_Fname_var.set('')
        self.patient_search_input_Lname_var.set('')
        self.patient_search_input_Phone_No_var.set(0)

        for item in self.patient_search_default_tree.get_children():
            self.patient_search_default_tree.delete(item)
    def patient_search_default_display_just_treeview_reset(self):
        for item in self.patient_search_default_tree.get_children():
            self.patient_search_default_tree.delete(item)

    def patient_search_edit_fun(self):
        self.patient_search_selected = self.patient_search_default_tree.focus()
        print("patient_search_edit_fun : self.patient_search_selected in selectitem:" + self.patient_search_selected)
        if (self.patient_search_selected != ''):
             self.patient_search_temp = self.patient_search_default_tree.item(self.patient_search_selected, 'values')
             print("patient_search_edit_fun : self.patient_search_temp:",self.patient_search_temp)
        if  len(self.patient_search_selected)!=0:
                  print("self.patient_search_selected in patient_search_edit ",self.patient_search_selected)
                  self.patient_search_edit_details_update_in_ui_fun()
                  self.patient_search_edit()
                  #self.patient_search_edit_details_update_in_ui_fun()
        else:

            
                   print("main_page_frame_view3_patient_search_default_frame_activate because len(self.patient_search_selected)!=0:len(self.patient_search_selected)=",len(self.patient_search_selected))
                   #self.main_page_frame_view3_patient_search_default_frame_activate()
    def patient_search_edit_details_update_in_ui_fun(self):
        self.patient_search_treeview_select_responce = self.patient_search_default_tree.focus()
        print("patient_search_treeview_selected :",self.patient_search_treeview_select_responce)
        print("patient_search_treeview_selected type:",type(self.patient_search_treeview_select_responce))
        self.patient_search_treeview_selected1 = self.patient_search_default_tree.item(self.patient_search_treeview_select_responce)
        print("values are ",self.patient_search_treeview_selected1['values'])
        self.patient_search_treeview_selected=self.patient_search_treeview_selected1['values']
        print("self.patient_search_treeview_selected type:",type(self.patient_search_treeview_selected))
        print("patient_search_treeview_selected ID:",self.patient_search_treeview_selected[0])
        self.patient_search_treeview_selected_id = tk.IntVar()
        self.patient_search_treeview_selected_id=  self.patient_search_treeview_selected[0]
        self.patient_search_treeview_selected_id_char = str(self.patient_search_treeview_selected_id)
        self.edit_details_update_command1 = "select id,name,mname,lname,dob,bloodgroup,phone_number,phone_number2,age,gender,address,city,emailid   from patient_details where id = " + self.patient_search_treeview_selected_id_char
        self.edit_details_update_login_database = login_check.get_execution_result(self.edit_details_update_command1 )
        print("self.edit_details_update_login_database:",self.edit_details_update_login_database)
        self.edit_details_edit_store=[]
        for i in self.edit_details_update_login_database:
            #print(" for loop i[0]",i[0])
            #self.book_room_assain_contact.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            self.edit_details_edit_store.append(f'{i[0]}')
            self.edit_details_edit_store.append(f'{i[1]}')
            self.edit_details_edit_store.append(f'{i[2]}')
            self.edit_details_edit_store.append(f'{i[3]}')
            self.edit_details_edit_store.append(f'{i[4]}')
            self.edit_details_edit_store.append(f'{i[5]}')
            self.edit_details_edit_store.append(f'{i[6]}')
            self.edit_details_edit_store.append(f'{i[7]}')
            self.edit_details_edit_store.append(f'{i[8]}')
            self.edit_details_edit_store.append(f'{i[9]}')
            self.edit_details_edit_store.append(f'{i[10]}')
            self.edit_details_edit_store.append(f'{i[11]}')
            self.edit_details_edit_store.append(f'{i[12]}')
        self.patient_search_edit_Patient_ID_display_var.set(str(self.edit_details_edit_store[0]))
        self.patient_search_edit_fname_display_var.set(str(self.edit_details_edit_store[1]))
        self.patient_search_edit_mname_display_var.set(str(self.edit_details_edit_store[2]))
        self.patient_search_edit_lname_display_var.set(str(self.edit_details_edit_store[3]))
        self.patient_search_edit_dob_display_var.set(str(self.edit_details_edit_store[4]))
        self.patient_search_edit_blood_group_display_var.set(str(self.edit_details_edit_store[5]))
        self.patient_search_edit_Phone_number1_display_var.set(str(self.edit_details_edit_store[6]))
        self.patient_search_edit_Phone_number2_display_var.set(str(self.edit_details_edit_store[7]))
        self.patient_search_edit_age_display_var.set(str(self.edit_details_edit_store[8]))
        self.patient_search_edit_gender_display_var.set(str(self.edit_details_edit_store[9]))
        self.patient_search_edit_adderess_display_var.set(str(self.edit_details_edit_store[10]))
        self.patient_search_edit_city_display_var.set(str(self.edit_details_edit_store[11]))
        self.patient_search_edit_emailid_display_var.set(str(self.edit_details_edit_store[12]))
        self.edit_details_update_room_details = None
        self.edit_details_update_room_details = login_check.get_execution_result("select room_ID,room_floor,room_no from rooms_details where  booked_person_id = " + str(self.edit_details_edit_store[0]) + " and rooms_status='occupied'  LIMIT 1; ")
        self.edit_details_edit_room_details=[]
        for i in self.edit_details_update_room_details:
            #print(" for loop i[0]",i[0])
            #self.book_room_assain_contact.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            if  self.edit_details_update_room_details != '':
                 self.edit_details_edit_room_details.append(f'{i[0]}')
                 self.edit_details_edit_room_details.append(f'{i[1]}')
                 self.edit_details_edit_room_details.append(f'{i[2]}')
        print("self.edit_details_edit_room_details:",self.edit_details_edit_room_details)
        if self.edit_details_edit_room_details != []:
            self.patient_search_edit_ROOM_id_display.config(text = str(self.edit_details_edit_room_details[0]),width=len(self.edit_details_edit_room_details[0]))
            self.patient_search_edit_ROOM_Floor_display.config(text = str(self.edit_details_edit_room_details[1]),width=len(self.edit_details_edit_room_details[1]))
            self.patient_search_edit_ROOM_no_display.config(text = str(self.edit_details_edit_room_details[2]),width=len(self.edit_details_edit_room_details[2]))
        else:
            self.patient_search_edit_ROOM_id_display.config(text = "None",width=len("None"))
            self.patient_search_edit_ROOM_Floor_display.config(text = "None",width=len("None"))
            self.patient_search_edit_ROOM_no_display.config(text = "None",width=len("None"))

        self.edit_details_update_finance_details = None
        self.edit_details_update_finance_details = login_check.get_execution_result("select sum(Debit),sum(credit) from finance_details  where  patient_id = " + str(self.edit_details_edit_store[0]) + "   LIMIT 1; ")
        self.edit_details_edit_finance_details=[]
        self.edit_details_edit_finance_details_balance= None
        print("self.edit_details_update_finance_details :",self.edit_details_update_finance_details )
        for i in self.edit_details_update_finance_details:
            #print(" for loop i[0]",i[0])
            #self.book_room_assain_contact.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            if  self.edit_details_update_finance_details != None:
                 self.edit_details_edit_finance_details.append(i[0])
                 print("self.edit_details_edit_finance_details[0]",self.edit_details_edit_finance_details[0])
                 self.edit_details_edit_finance_details.append(i[1])
                 print("self.edit_details_edit_finance_details[1]",self.edit_details_edit_finance_details[1])
                 if self.edit_details_edit_finance_details[0]  != None:
                      self.edit_details_edit_finance_details_balance=self.edit_details_edit_finance_details[0] - self.edit_details_edit_finance_details[1]

          
        if self.edit_details_edit_finance_details != []:
            self.patient_search_edit_FINANCE_Debit_display.config(text = str(self.edit_details_edit_finance_details[0]))
            self.patient_search_edit_FINANCE_Credit_display.config(text = str(self.edit_details_edit_finance_details[1]))
            self.patient_search_edit_FINANCE_Balance_display.config(text = str(self.edit_details_edit_finance_details_balance))
        else:
            self.patient_search_edit_FINANCE_Debit_display.config(text = "0",width=len("0"))
            self.patient_search_edit_FINANCE_Credit_display.config(text = "0",width=len("0"))
            self.patient_search_edit_FINANCE_Balance_display.config(text = "0",width=len("0"))
        
        
    def patient_search_edit_update_button_fun(self):
        self.patient_search_edit_update_button_command1 = "UPDATE patient_details set "
        self.patient_search_edit_update_button_command2  = " where id = " + self.patient_search_edit_Patient_ID_display_var.get()
        
        self.patient_search_edit_update_button_command_name= self.patient_search_edit_update_button_command1 + " name = '" + self.patient_search_edit_fname_display_var.get() + "'" +  self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_mname=self.patient_search_edit_update_button_command1 + " mname = '" + self.patient_search_edit_mname_display_var.get() + "'" +  self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_lname=self.patient_search_edit_update_button_command1 + " lname = '" + self.patient_search_edit_lname_display_var.get() + "'" +  self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_dob=self.patient_search_edit_update_button_command1 + " dob = '" + self.patient_search_edit_dob_display_var.get() + "'" +  self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_bloodgroup=self.patient_search_edit_update_button_command1 + " bloodgroup = '" + self.patient_search_edit_blood_group_display_var.get() + "'" + self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_phone_number=self.patient_search_edit_update_button_command1 + " phone_number = " + self.patient_search_edit_Phone_number1_display_var.get() + self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_phone_number2=self.patient_search_edit_update_button_command1 + " phone_number2 = " + self.patient_search_edit_Phone_number2_display_var.get() + self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_age=self.patient_search_edit_update_button_command1 + " age = " + self.patient_search_edit_age_display_var.get() + self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_gender=self.patient_search_edit_update_button_command1 + " gender = '" + self.patient_search_edit_gender_display_var.get() + "'" +  self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_address=self.patient_search_edit_update_button_command1 + " address = '" + self.patient_search_edit_adderess_display_var.get() + "'" +  self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_city=self.patient_search_edit_update_button_command1 + " city = '" + self.patient_search_edit_city_display_var.get() + "'" +  self.patient_search_edit_update_button_command2
        self.patient_search_edit_update_button_command_emailid=self.patient_search_edit_update_button_command1 + " emailid = '" + self.patient_search_edit_emailid_display_var.get() + "'" +  self.patient_search_edit_update_button_command2
        print("self.patient_search_edit_update_button_command_name:",self.patient_search_edit_update_button_command_name)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_name)
        #print("successfully_completed")
        login_check.get_execution_result(self.patient_search_edit_update_button_command_mname)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_lname)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_dob)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_bloodgroup)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_phone_number)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_phone_number2)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_age)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_gender)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_address)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_city)
        login_check.get_execution_result(self.patient_search_edit_update_button_command_emailid)
    

        
        
        
        
        
        
        
        
        
        
        
        

    def patient_search_display_fun(self):
        self.patient_search_selected = self.patient_search_default_tree.focus()
        self.patient_search_treeview_select_responce = self.patient_search_default_tree.focus()
        print("patient_search_treeview_selected :",self.patient_search_treeview_select_responce)
        print("patient_search_treeview_selected type:",type(self.patient_search_treeview_select_responce))
        
        
        print("patient_search_display_fun: self.patient_search_selected in selectitem:" + self.patient_search_selected)
        if (self.patient_search_selected != ''):
             self.patient_search_temp = self.patient_search_default_tree.item(self.patient_search_selected, 'values')
             print("patient_search_display_fun: self.patient_search_temp:",self.patient_search_temp)
        if  len(self.patient_search_selected)!=0:
                  print("self.patient_search_selected in patient_search_edit ",self.patient_search_selected)
                  self.patient_search_display_data_update()
                  self.patient_search_display()
                  

        else:
            
                   print("main_page_frame_view3_patient_search_default_frame_activate because len(self.patient_search_selected)!=0:len(self.patient_search_selected)=",len(self.patient_search_selected))
                   #self.main_page_frame_view3_patient_search_default_frame_activate()

    def patient_search_display_data_update(self):
        self.patient_search_treeview_select_responce = self.patient_search_default_tree.focus()
        print("patient_search_treeview_selected :",self.patient_search_treeview_select_responce)
        print("patient_search_treeview_selected type:",type(self.patient_search_treeview_select_responce))
        self.patient_search_treeview_selected1 = self.patient_search_default_tree.item(self.patient_search_treeview_select_responce)
        print("values are ",self.patient_search_treeview_selected1['values'])
        self.patient_search_treeview_selected=self.patient_search_treeview_selected1['values']
        print("self.patient_search_treeview_selected type:",type(self.patient_search_treeview_selected))
        print("patient_search_treeview_selected ID:",self.patient_search_treeview_selected[0])
        self.patient_search_treeview_selected_id = tk.IntVar()
        self.patient_search_treeview_selected_id=  self.patient_search_treeview_selected[0]
        self.patient_search_treeview_selected_id_char = str(self.patient_search_treeview_selected_id)
        self.display_details_update_command1 = "select id,name,mname,lname,dob,bloodgroup,phone_number,phone_number2,age,gender,address,city,emailid   from patient_details where id = " + self.patient_search_treeview_selected_id_char
        self.display_details_update_login_database = login_check.get_execution_result(self.display_details_update_command1 )
        self.display_details_display_store=[]
        for i in self.display_details_update_login_database:
            #print(" for loop i[0]",i[0])
            #self.book_room_assain_contact.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            self.display_details_display_store.append(f'{i[0]}')
            self.display_details_display_store.append(f'{i[1]}')
            self.display_details_display_store.append(f'{i[2]}')
            self.display_details_display_store.append(f'{i[3]}')
            self.display_details_display_store.append(f'{i[4]}')
            self.display_details_display_store.append(f'{i[5]}')
            self.display_details_display_store.append(f'{i[6]}')
            self.display_details_display_store.append(f'{i[7]}')
            self.display_details_display_store.append(f'{i[8]}')
            self.display_details_display_store.append(f'{i[9]}')
            self.display_details_display_store.append(f'{i[10]}')
            self.display_details_display_store.append(f'{i[11]}')
            self.display_details_display_store.append(f'{i[12]}')

        print("self.display_details_display_store:",self.display_details_display_store)
        print("self.display_details_display_store type:",type(self.display_details_display_store))
        

        self.patient_search_display_Patient_ID_display.config(text = str( self.display_details_display_store[0]))
        self.patient_search_display_fname_display.config(text = str(self.display_details_display_store[1]))
        self.patient_search_display_mname_display.config(text = str(self.display_details_display_store[2]))
        self.patient_search_display_lname_display.config(text = str(self.display_details_display_store[3]))
        self.patient_search_display_dob_display.config(text = str(self.display_details_display_store[4]))
        self.patient_search_display_blood_group_display.config(text = str(self.display_details_display_store[5]))
        self.patient_search_display_Phone_number1_display.config(text = str( self.display_details_display_store[6]))
        self.patient_search_display_Phone_number2_display.config(text = str(self.display_details_display_store[7]))
        self.patient_search_display_age_display.config(text = str(self.display_details_display_store[8]))
        self.patient_search_display_gender_display.config(text = str(self.display_details_display_store[9]))
        self.patient_search_display_adderess_display.config(text = str(self.display_details_display_store[10]))
        self.patient_search_display_city_display.config(text = str(self.display_details_display_store[11]))
        self.patient_search_display_emailid_display.config(text = str(self.display_details_display_store[12]))

        self.display_details_update_room_details = None
        self.display_details_update_room_details = login_check.get_execution_result("select room_ID,room_floor,room_no from rooms_details where  booked_person_id = " + str(self.display_details_display_store[0]) + " and rooms_status='occupied'  LIMIT 1; ")
        self.display_details_display_room_details=[]
        for i in self.display_details_update_room_details:
            #print(" for loop i[0]",i[0])
            #self.book_room_assain_contact.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            if  self.display_details_update_room_details != '':
                 self.display_details_display_room_details.append(f'{i[0]}')
                 self.display_details_display_room_details.append(f'{i[1]}')
                 self.display_details_display_room_details.append(f'{i[2]}')
        print("self.display_details_display_room_details:",self.display_details_display_room_details)
        if self.display_details_display_room_details != []:
            self.patient_search_display_ROOM_id_display.config(text = str(self.display_details_display_room_details[0]),width=len(self.display_details_display_room_details[0]))
            self.patient_search_display_ROOM_Floor_display.config(text = str(self.display_details_display_room_details[1]),width=len(self.display_details_display_room_details[1]))
            self.patient_search_display_ROOM_no_display.config(text = str(self.display_details_display_room_details[2]),width=len(self.display_details_display_room_details[2]))
        else:
            self.patient_search_display_ROOM_id_display.config(text = "None",width=len("None"))
            self.patient_search_display_ROOM_Floor_display.config(text = "None",width=len("None"))
            self.patient_search_display_ROOM_no_display.config(text = "None",width=len("None"))

        self.display_details_update_finance_details = None
        self.display_details_update_finance_details = login_check.get_execution_result("select sum(Debit),sum(credit) from finance_details  where  patient_id = " + str(self.display_details_display_store[0]) + "   LIMIT 1; ")
        self.display_details_display_finance_details=[]
        self.display_details_display_finance_details_balance= None
        print("self.display_details_update_finance_details :",self.display_details_update_finance_details )
        for i in self.display_details_update_finance_details:
            #print(" for loop i[0]",i[0])
            #self.book_room_assain_contact.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            if  self.display_details_update_finance_details != None:
                 self.display_details_display_finance_details.append(i[0])
                 print("self.display_details_display_finance_details[0]",self.display_details_display_finance_details[0])
                 self.display_details_display_finance_details.append(i[1])
                 print("self.display_details_display_finance_details[1]",self.display_details_display_finance_details[1])
                 if self.display_details_display_finance_details[0]  != None:
                      self.display_details_display_finance_details_balance=self.display_details_display_finance_details[0] - self.display_details_display_finance_details[1]
                 
        print("self.display_details_display_room_details:",self.display_details_display_room_details)
        #self.display_details_display_finance_details_balance=self.display_details_display_finance_details[0] - self.display_details_display_finance_details[1]
        if self.display_details_display_finance_details != []:
            self.patient_search_display_FINANCE_Debit_display.config(text = str(self.display_details_display_finance_details[0]))
            self.patient_search_display_FINANCE_Credit_display.config(text = str(self.display_details_display_finance_details[1]))
            self.patient_search_display_FINANCE_Balance_display.config(text = str(self.display_details_display_finance_details_balance))
        else:
            self.patient_search_display_FINANCE_Debit_display.config(text = "0",width=len("0"))
            self.patient_search_display_FINANCE_Credit_display.config(text = "0",width=len("0"))
            self.patient_search_display_FINANCE_Balance_display.config(text = "0",width=len("0"))

    


    
    #search_patient_functions=============================end=================================

    #patient_queue_functions==============================start==================================
    def patient_queue_display(self): 
        #adding the values into contact list 
        self.patient_queue_contacts = []
        for n in range(1, 200):
            self.patient_queue_contacts.append((f'id{n}', f'first {n}',f'last {n}',f'age {n}',f'gender {n}', f'ph1 {n}',f'ph2 {n}',f'queue_type {n}',f'queue_status {n}',f'reason {n}',f'doctorid {n}',f'doctor_name {n}'))

        # add data to the treeview 
        for contact in self.patient_queue_contacts:
            self.patient_queue_default_tree.insert('', tk.END, values=contact)

        self.patient_queue_default_tree.place(x=15,y=150,width=1200,height=600)
        #tree.grid(row=0, column=0, sticky='nsew')

        #ading the scroll baar 
        self.patient_queue_scrollbar = ttk.Scrollbar(self.main_page_frame_view3_patient_queue_default_frame, orient=tk.VERTICAL, command=self.patient_queue_default_tree.yview)
        self.patient_queue_default_tree.configure(yscroll=self.patient_queue_scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        self.patient_queue_scrollbar.place(x=1215, y=150,width=15,height=600)

        self.patient_queue_selected = self.patient_queue_default_tree.focus()
        print("self.patient_queue_selected in display" + self.patient_queue_selected)

    def patient_queue_selectItem(self):
        #curItem = tree.focus()
        #print(curItem, a)
        self.patient_queue_selected = self.patient_queue_default_tree.focus()
        print("self.patient_queue_selected in selected" + self.patient_queue_selected)
        if (self.patient_queue_selected != ''):
             self.patient_queue_temp = self.patient_queue_default_tree.item(self.patient_queue_selected, 'values')
             print(self.patient_queue_temp)

    def patient_queue_display_treeview_reset(self):
        for item in self.patient_queue_default_tree.get_children():
            self.patient_queue_default_tree.delete(item)

    def  patient_queue_send_to_OPD_fun(self):
        self.patient_queue_selectItem()
        self.patient_queue_send_to_OPD = Toplevel(self.main_page_frame_view3_patient_queue_default_frame)
        self.patient_queue_send_to_OPD.title("SEND TO OPD")
        self.main_window_geometry_x = self.root1.winfo_x()
        self.main_window_geometry_y = self.root1.winfo_y()
        self.patient_queue_send_to_OPD.geometry("600x300+500+300")

        self.patient_queue_send_to_OPD_id_label=tk.Label(self.patient_queue_send_to_OPD,text="Patient ID :")
        self.patient_queue_send_to_OPD_id_label.place(x=20,y=20,width=100,height=15)
        self.patient_queue_send_to_OPD_id_label_display=tk.Label(self.patient_queue_send_to_OPD,text="Patient ID display")
        self.patient_queue_send_to_OPD_id_label_display.place(x=172,y=20,width=112,height=15)

        self.patient_queue_send_to_OPD_name_label=tk.Label(self.patient_queue_send_to_OPD,text="Name :")
        self.patient_queue_send_to_OPD_name_label.place(x=300,y=20,width=102,height=15)
        self.patient_queue_send_to_OPD_name_label_display=tk.Label(self.patient_queue_send_to_OPD,text="Name display")
        self.patient_queue_send_to_OPD_name_label_display.place(x=424,y=20,width=112,height=15)
        
        self.patient_queue_send_to_OPD_phoneno_label=tk.Label(self.patient_queue_send_to_OPD,text="Phone NO :")
        self.patient_queue_send_to_OPD_phoneno_label.place(x=20,y=60,width=100,height=15)
        self.patient_queue_send_to_OPD_phoneno_label_display=tk.Label(self.patient_queue_send_to_OPD,text="phone_no_display")
        self.patient_queue_send_to_OPD_phoneno_label_display.place(x=172,y=60,width=112,height=15)
        
        self.patient_queue_send_to_OPD_gender_label=tk.Label(self.patient_queue_send_to_OPD,text="Gender:")
        self.patient_queue_send_to_OPD_gender_label.place(x=300,y=60,width=100,height=15)
        self.patient_queue_send_to_OPD_gender_label_display=tk.Label(self.patient_queue_send_to_OPD,text="gender_display")
        self.patient_queue_send_to_OPD_gender_label_display.place(x=424,y=60,width=112,height=15)

        self.patient_queue_send_to_OPD_age_label=tk.Label(self.patient_queue_send_to_OPD,text="Age :")
        self.patient_queue_send_to_OPD_age_label.place(x=20,y=100,width=100,height=15)
        self.patient_queue_send_to_OPD_age_label_display=tk.Label(self.patient_queue_send_to_OPD,text="age display")
        self.patient_queue_send_to_OPD_age_label_display.place(x=172,y=100,width=112,height=15)
        
        self.patient_queue_send_to_OPD_specialization_label=tk.Label(self.patient_queue_send_to_OPD,text="Specialization ")
        self.patient_queue_send_to_OPD_specialization_label.place(x=20,y=140,width=100,height=15)
        self.patient_queue_send_to_OPD_specialization_value_inside=tk.StringVar()
        self.patient_queue_send_to_OPD_specialization_value_inside.set('select role')
        self.patient_queue_send_to_OPD_specialization_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.patient_queue_send_to_OPD_specialization = ttk.OptionMenu(self.patient_queue_send_to_OPD,self.patient_queue_send_to_OPD_specialization_value_inside , *self.patient_queue_send_to_OPD_specialization_list)
        self.patient_queue_send_to_OPD_specialization.configure(width=38)
        self.patient_queue_send_to_OPD_specialization.place(x=170,y=140)
        print("the valuse on the roles:",self.patient_queue_send_to_OPD_specialization_value_inside.get())
        
        self.patient_queue_send_to_OPD_refresh_image =Image.open("refresh_img.png")
        #G:\hms_v1\hms_files_v3\main_page_home.jpeg
        # Show image using label
        
        self.patient_queue_send_to_OPD_refresh_resized_image= self.patient_queue_send_to_OPD_refresh_image.resize((20,22), Image.ANTIALIAS)
        self.patient_queue_send_to_OPD_refresh_img=ImageTk.PhotoImage(self.patient_queue_send_to_OPD_refresh_resized_image)
        self.patient_queue_send_to_OPD_button2_refresh=tk.Button(self.patient_queue_send_to_OPD, image = self.patient_queue_send_to_OPD_refresh_img)#,command= self.refresh_default
        self.patient_queue_send_to_OPD_button2_refresh.place(x=460,y=150,width=25,height=25)

        self.patient_queue_send_to_OPD_doctor_label=tk.Label(self.patient_queue_send_to_OPD,text="Doctor ")
        self.patient_queue_send_to_OPD_doctor_label.place(x=20,y=180,width=100,height=15)
        self.patient_queue_send_to_OPD_doctor_value_inside=tk.StringVar()
        self.patient_queue_send_to_OPD_doctor_value_inside.set('select role')
        self.patient_queue_send_to_OPD_doctor_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.patient_queue_send_to_OPD_doctor= ttk.OptionMenu(self.patient_queue_send_to_OPD,self.patient_queue_send_to_OPD_doctor_value_inside , *self.patient_queue_send_to_OPD_doctor_list)
        self.patient_queue_send_to_OPD_doctor.configure(width=38)
        self.patient_queue_send_to_OPD_doctor.place(x=170,y=180)
        print("the valuse on the roles:",self.patient_queue_send_to_OPD_doctor_value_inside.get())

        self.patient_queue_send_to_OPD_warning_label=tk.Label(self.patient_queue_send_to_OPD,text=" ",font=('calibre',13,'bold'))
        self.patient_queue_send_to_OPD_warning_label.place(x=70,y=220,width=400,height=15)

        self.patient_queue_send_to_OPD_yes_button=tk.Button(self.patient_queue_send_to_OPD,text="YES")
        self.patient_queue_send_to_OPD_yes_button.pack_forget()
        self.patient_queue_send_to_OPD_no_button=tk.Button(self.patient_queue_send_to_OPD,text="NO",command=self.patient_queue_send_to_OPD__deactivate)
        self.patient_queue_send_to_OPD_no_button.pack_forget()


        if(self.patient_queue_selected == ''):
            self.patient_queue_send_to_OPD_warning_label.config(text="WARNING!:please select patient in patient queue")
        else:
            self.patient_queue_send_to_OPD_yes_button.place(x=70,y=250,width=112,height=25)
            self.patient_queue_send_to_OPD_no_button.place(x=370,y=250,width=112,height=25)


        self.patient_queue_send_to_OPD.wm_transient(self.root1)
        self.patient_queue_send_to_OPD.mainloop()
    def patient_queue_send_to_OPD__deactivate(self):
        self.patient_queue_send_to_OPD.destroy()

    def  patient_queue_send_to_ipd_fun(self):
        self.patient_queue_send_to_ipd = Toplevel()
        self.patient_queue_send_to_ipd.title("SEND TO IPD")
        self.patient_queue_send_to_ipd.geometry("600x300+500+300")
        self.patient_queue_selectItem()

        self.patient_queue_send_to_ipd_id_label=tk.Label(self.patient_queue_send_to_ipd,text="Patient ID :")
        self.patient_queue_send_to_ipd_id_label.place(x=20,y=20,width=100,height=15)
        self.patient_queue_send_to_ipd_id_label_display=tk.Label(self.patient_queue_send_to_ipd,text="Patient ID display")
        self.patient_queue_send_to_ipd_id_label_display.place(x=172,y=20,width=112,height=15)

        self.patient_queue_send_to_ipd_name_label=tk.Label(self.patient_queue_send_to_ipd,text="Name :")
        self.patient_queue_send_to_ipd_name_label.place(x=300,y=20,width=102,height=15)
        self.patient_queue_send_to_ipd_name_label_display=tk.Label(self.patient_queue_send_to_ipd,text="Name display")
        self.patient_queue_send_to_ipd_name_label_display.place(x=424,y=20,width=112,height=15)
        
        self.patient_queue_send_to_ipd_phoneno_label=tk.Label(self.patient_queue_send_to_ipd,text="Phone NO :")
        self.patient_queue_send_to_ipd_phoneno_label.place(x=20,y=60,width=100,height=15)
        self.patient_queue_send_to_ipd_phoneno_label_display=tk.Label(self.patient_queue_send_to_ipd,text="phone_no_display")
        self.patient_queue_send_to_ipd_phoneno_label_display.place(x=172,y=60,width=112,height=15)
        
        self.patient_queue_send_to_ipd_gender_label=tk.Label(self.patient_queue_send_to_ipd,text="Gender:")
        self.patient_queue_send_to_ipd_gender_label.place(x=300,y=60,width=100,height=15)
        self.patient_queue_send_to_ipd_gender_label_display=tk.Label(self.patient_queue_send_to_ipd,text="gender_display")
        self.patient_queue_send_to_ipd_gender_label_display.place(x=424,y=60,width=112,height=15)

        self.patient_queue_send_to_ipd_age_label=tk.Label(self.patient_queue_send_to_ipd,text="Age :")
        self.patient_queue_send_to_ipd_age_label.place(x=20,y=100,width=100,height=15)
        self.patient_queue_send_to_ipd_age_label_display=tk.Label(self.patient_queue_send_to_ipd,text="age display")
        self.patient_queue_send_to_ipd_age_label_display.place(x=172,y=100,width=112,height=15)
        
        self.patient_queue_send_to_ipd_specialization_label=tk.Label(self.patient_queue_send_to_ipd,text="Specialization ")
        self.patient_queue_send_to_ipd_specialization_label.place(x=20,y=140,width=100,height=15)
        self.patient_queue_send_to_ipd_specialization_value_inside=tk.StringVar()
        self.patient_queue_send_to_ipd_specialization_value_inside.set('select role')
        self.patient_queue_send_to_ipd_specialization_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.patient_queue_send_to_ipd_specialization = ttk.OptionMenu(self.patient_queue_send_to_ipd,self.patient_queue_send_to_ipd_specialization_value_inside , *self.patient_queue_send_to_ipd_specialization_list)
        self.patient_queue_send_to_ipd_specialization.configure(width=38)
        self.patient_queue_send_to_ipd_specialization.place(x=170,y=140)
        print("the valuse on the roles:",self.patient_queue_send_to_ipd_specialization_value_inside.get())
        
        self.patient_queue_send_to_ipd_doctor_label=tk.Label(self.patient_queue_send_to_ipd,text="Doctor ")
        self.patient_queue_send_to_ipd_doctor_label.place(x=20,y=180,width=100,height=15)
        self.patient_queue_send_to_ipd_doctor_value_inside=tk.StringVar()
        self.patient_queue_send_to_ipd_doctor_value_inside.set('select role')
        self.patient_queue_send_to_ipd_doctor_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.patient_queue_send_to_ipd_doctor= ttk.OptionMenu(self.patient_queue_send_to_ipd,self.patient_queue_send_to_ipd_doctor_value_inside , *self.patient_queue_send_to_ipd_doctor_list)
        self.patient_queue_send_to_ipd_doctor.configure(width=38)
        self.patient_queue_send_to_ipd_doctor.place(x=170,y=180)
        print("the valuse on the roles:",self.patient_queue_send_to_ipd_doctor_value_inside.get())

        self.patient_queue_send_to_ipd_warning_label=tk.Label(self.patient_queue_send_to_ipd,text=" ",font=('calibre',13,'bold'))
        self.patient_queue_send_to_ipd_warning_label.place(x=70,y=220,width=400,height=15)

        self.patient_queue_send_to_ipd_yes_button=tk.Button(self.patient_queue_send_to_ipd,text="YES")
        self.patient_queue_send_to_ipd_yes_button.pack_forget()
        self.patient_queue_send_to_ipd_no_button=tk.Button(self.patient_queue_send_to_ipd,text="NO",command=self.patient_queue_send_to_ipd_deactivate)
        self.patient_queue_send_to_ipd_no_button.pack_forget()


        if(self.patient_queue_selected == ''):
            self.patient_queue_send_to_ipd_warning_label.config(text="WARNING!:please select patient in patient queue")
        else:
            self.patient_queue_send_to_ipd_yes_button.place(x=70,y=250,width=112,height=25)
            self.patient_queue_send_to_ipd_no_button.place(x=370,y=250,width=112,height=25)

        self.patient_queue_send_to_ipd.mainloop()
    def patient_queue_send_to_ipd_deactivate(self):
        self.patient_queue_send_to_ipd.destroy()


    def  patient_queue_Delete_fun(self):
        self.patient_queue_selectItem()
        self.patient_queue_Delete_page = Toplevel(self.main_page_frame_view3_patient_queue_default_frame)
        self.patient_queue_Delete_page.title("DELETE FROM PATIENT QUEUE")
        self.main_window_geometry_x = self.root1.winfo_x()
        self.main_window_geometry_y = self.root1.winfo_y()
        self.patient_queue_Delete_page.geometry("600x205+500+300")

        self.patient_queue_Delete_page_label=tk.Label(self.patient_queue_Delete_page,text="Patient ID :")
        self.patient_queue_Delete_page_label.place(x=20,y=20,width=100,height=15)
        self.patient_queue_Delete_page_label_display=tk.Label(self.patient_queue_Delete_page,text="Patient ID display")
        self.patient_queue_Delete_page_label_display.place(x=172,y=20,width=112,height=15)

        self.patient_queue_Delete_page_name_label=tk.Label(self.patient_queue_Delete_page,text="Name :")
        self.patient_queue_Delete_page_name_label.place(x=300,y=20,width=102,height=15)
        self.patient_queue_Delete_page_name_label_display=tk.Label(self.patient_queue_Delete_page,text="Name display")
        self.patient_queue_Delete_page_name_label_display.place(x=424,y=20,width=112,height=15)
        
        self.patient_queue_Delete_page_phoneno_label=tk.Label(self.patient_queue_Delete_page,text="Phone NO :")
        self.patient_queue_Delete_page_phoneno_label.place(x=20,y=60,width=100,height=15)
        self.patient_queue_Delete_page_phoneno_label_display=tk.Label(self.patient_queue_Delete_page,text="phone_no_display")
        self.patient_queue_Delete_page_phoneno_label_display.place(x=172,y=60,width=112,height=15)
        
        self.patient_queue_Delete_page_gender_label=tk.Label(self.patient_queue_Delete_page,text="Gender:")
        self.patient_queue_Delete_page_gender_label.place(x=300,y=60,width=100,height=15)
        self.patient_queue_Delete_page_gender_label_display=tk.Label(self.patient_queue_Delete_page,text="gender_display")
        self.patient_queue_Delete_page_gender_label_display.place(x=424,y=60,width=112,height=15)

        self.patient_queue_Delete_page_age_label=tk.Label(self.patient_queue_Delete_page,text="Age :")
        self.patient_queue_Delete_page_age_label.place(x=20,y=100,width=100,height=15)
        self.patient_queue_Delete_page_age_label_display=tk.Label(self.patient_queue_Delete_page,text="age display")
        self.patient_queue_Delete_page_age_label_display.place(x=172,y=100,width=112,height=15)
        
        self.patient_queue_Delete_page_warning_label=tk.Label(self.patient_queue_Delete_page,text=" ",font=('calibre',13,'bold'))
        self.patient_queue_Delete_page_warning_label.place(x=70,y=130,width=400,height=15)

        
        self.patient_queue_Delete_page_yes_button=tk.Button(self.patient_queue_Delete_page,text="YES")
        self.patient_queue_Delete_page_yes_button.pack_forget()
        self.patient_queue_Delete_page_no_button=tk.Button(self.patient_queue_Delete_page,text="NO",command=self.patient_queue_Delete_page_deactivate)
        self.patient_queue_Delete_page_no_button.pack_forget()

        if(self.patient_queue_selected == ''):
            self.patient_queue_Delete_page_warning_label.config(text="WARNING!:please select patient in patient queue")
        else:
            #self.patient_queue_Delete_page_yes_button = tk.Button(self.patient_queue_Delete_page,text="YES",font=('calibre',20,'bold'))
            self.patient_queue_Delete_page_yes_button.place(x=70,y=170,width=112,height=25)
            #self.patient_queue_Delete_page_no_button = tk.Button(self.patient_queue_Delete_page,text="NO",font=('calibre',20,'bold'))
            self.patient_queue_Delete_page_no_button.place(x=370,y=170,width=112,height=25)

        self.patient_queue_Delete_page.mainloop()
    def patient_queue_Delete_page_deactivate(self):
        self.patient_queue_Delete_page.destroy()
    
    
    #patient_queue_functions=============================end=================================

    #opd_queue_functions==============================start==================================
    def opd_queue_display(self): 
        #adding the values into contact list 
        self.opd_queue_contacts = []
        for n in range(1, 200):
            self.opd_queue_contacts.append((f'opd_queue_first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview 
        for contact in self.opd_queue_contacts:
            self.opd_queue_default_tree.insert('', tk.END, values=contact)

        self.opd_queue_default_tree.place(x=15,y=150,width=1200,height=600)
        #tree.grid(row=0, column=0, sticky='nsew')

        #ading the scroll baar 
        self.opd_queue_scrollbar = ttk.Scrollbar(self.main_page_frame_view3_opd_queue_default_frame, orient=tk.VERTICAL, command=self.opd_queue_default_tree.yview)
        self.opd_queue_default_tree.configure(yscroll=self.opd_queue_scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        self.opd_queue_scrollbar.place(x=1215, y=150,width=15,height=600)

        self.opd_queue_selected = self.opd_queue_default_tree.focus()
        print("self.opd_queue_selected in display" + self.opd_queue_selected)

    def opd_queue_selectItem(self):
        #curItem = tree.focus()
        #print(curItem, a)
        self.opd_queue_selected = self.opd_queue_default_tree.focus()
        print("self.opd_queue_selected in selected" + self.opd_queue_selected)
        if (self.opd_queue_selected != ''):
             self.opd_queue_temp = self.opd_queue_default_tree.item(self.opd_queue_selected, 'values')
             print(self.opd_queue_temp)

    def opd_queue_display_treeview_reset(self):
        for item in self.opd_queue_default_tree.get_children():
            self.opd_queue_default_tree.delete(item)

    def  opd_queue_send_to_IPD_fun(self):
        self.opd_queue_selectItem()
        self.opd_queue_send_to_OPD = Toplevel(self.main_page_frame_view3_opd_queue_default_frame)
        self.opd_queue_send_to_OPD.title("SEND TO IPD")
        self.opd_queue_send_to_OPD.geometry("600x300+500+300")

        self.opd_queue_send_to_OPD_id_label=tk.Label(self.opd_queue_send_to_OPD,text="Patient ID :")
        self.opd_queue_send_to_OPD_id_label.place(x=20,y=20,width=100,height=15)
        self.opd_queue_send_to_OPD_id_label_display=tk.Label(self.opd_queue_send_to_OPD,text="Patient ID display")
        self.opd_queue_send_to_OPD_id_label_display.place(x=172,y=20,width=112,height=15)

        self.opd_queue_send_to_OPD_name_label=tk.Label(self.opd_queue_send_to_OPD,text="Name :")
        self.opd_queue_send_to_OPD_name_label.place(x=300,y=20,width=102,height=15)
        self.opd_queue_send_to_OPD_name_label_display=tk.Label(self.opd_queue_send_to_OPD,text="Name display")
        self.opd_queue_send_to_OPD_name_label_display.place(x=424,y=20,width=112,height=15)
        
        self.opd_queue_send_to_OPD_phoneno_label=tk.Label(self.opd_queue_send_to_OPD,text="Phone NO :")
        self.opd_queue_send_to_OPD_phoneno_label.place(x=20,y=60,width=100,height=15)
        self.opd_queue_send_to_OPD_phoneno_label_display=tk.Label(self.opd_queue_send_to_OPD,text="phone_no_display")
        self.opd_queue_send_to_OPD_phoneno_label_display.place(x=172,y=60,width=112,height=15)
        
        self.opd_queue_send_to_OPD_gender_label=tk.Label(self.opd_queue_send_to_OPD,text="Gender:")
        self.opd_queue_send_to_OPD_gender_label.place(x=300,y=60,width=100,height=15)
        self.opd_queue_send_to_OPD_gender_label_display=tk.Label(self.opd_queue_send_to_OPD,text="gender_display")
        self.opd_queue_send_to_OPD_gender_label_display.place(x=424,y=60,width=112,height=15)

        self.opd_queue_send_to_OPD_age_label=tk.Label(self.opd_queue_send_to_OPD,text="Age :")
        self.opd_queue_send_to_OPD_age_label.place(x=20,y=100,width=100,height=15)
        self.opd_queue_send_to_OPD_age_label_display=tk.Label(self.opd_queue_send_to_OPD,text="age display")
        self.opd_queue_send_to_OPD_age_label_display.place(x=172,y=100,width=112,height=15)
        
        self.opd_queue_send_to_OPD_specialization_label=tk.Label(self.opd_queue_send_to_OPD,text="Specialization ")
        self.opd_queue_send_to_OPD_specialization_label.place(x=20,y=140,width=100,height=15)
        self.opd_queue_send_to_OPD_specialization_value_inside=tk.StringVar()
        self.opd_queue_send_to_OPD_specialization_value_inside.set('select role')
        self.opd_queue_send_to_OPD_specialization_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.opd_queue_send_to_OPD_specialization = ttk.OptionMenu(self.opd_queue_send_to_OPD,self.opd_queue_send_to_OPD_specialization_value_inside , *self.opd_queue_send_to_OPD_specialization_list)
        self.opd_queue_send_to_OPD_specialization.configure(width=38)
        self.opd_queue_send_to_OPD_specialization.place(x=170,y=140)
        print("the valuse on the roles:",self.opd_queue_send_to_OPD_specialization_value_inside.get())
        
        self.opd_queue_send_to_OPD_doctor_label=tk.Label(self.opd_queue_send_to_OPD,text="Doctor ")
        self.opd_queue_send_to_OPD_doctor_label.place(x=20,y=180,width=100,height=15)
        self.opd_queue_send_to_OPD_doctor_value_inside=tk.StringVar()
        self.opd_queue_send_to_OPD_doctor_value_inside.set('select role')
        self.opd_queue_send_to_OPD_doctor_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.opd_queue_send_to_OPD_doctor= ttk.OptionMenu(self.opd_queue_send_to_OPD,self.opd_queue_send_to_OPD_doctor_value_inside , *self.opd_queue_send_to_OPD_doctor_list)
        self.opd_queue_send_to_OPD_doctor.configure(width=38)
        self.opd_queue_send_to_OPD_doctor.place(x=170,y=180)
        print("the valuse on the roles:",self.opd_queue_send_to_OPD_doctor_value_inside.get())

        self.opd_queue_send_to_OPD_warning_label=tk.Label(self.opd_queue_send_to_OPD,text=" ",font=('calibre',13,'bold'))
        self.opd_queue_send_to_OPD_warning_label.place(x=70,y=220,width=400,height=15)

        self.opd_queue_send_to_OPD_yes_button=tk.Button(self.opd_queue_send_to_OPD,text="YES")
        self.opd_queue_send_to_OPD_yes_button.pack_forget()
        self.opd_queue_send_to_OPD_no_button=tk.Button(self.opd_queue_send_to_OPD,text="NO",command=self.opd_queue_send_to_OPD_deactivate)
        self.opd_queue_send_to_OPD_no_button.pack_forget()


        if(self.opd_queue_selected == ''):
            self.opd_queue_send_to_OPD_warning_label.config(text="WARNING!:please select patient in patient queue")
        else:
            self.opd_queue_send_to_OPD_yes_button.place(x=70,y=250,width=112,height=25)
            self.opd_queue_send_to_OPD_no_button.place(x=370,y=250,width=112,height=25)


        self.opd_queue_send_to_OPD.wm_transient(self.root1)
        self.opd_queue_send_to_OPD.mainloop()
    def opd_queue_send_to_OPD_deactivate(self):
        self.opd_queue_send_to_OPD.destroy()
    
    def  opd_queue_completed_fun(self):
        self.opd_queue_selectItem()
        self.opd_queue_completed = Toplevel(self.main_page_frame_view3_opd_queue_default_frame)
        self.opd_queue_completed.title("OPD COMPLETED")
        self.opd_queue_completed.geometry("600x300+500+300")

        self.opd_queue_completed_id_label=tk.Label(self.opd_queue_completed,text="Patient ID :")
        self.opd_queue_completed_id_label.place(x=20,y=20,width=100,height=15)
        self.opd_queue_completed_id_label_display=tk.Label(self.opd_queue_completed,text="Patient ID display")
        self.opd_queue_completed_id_label_display.place(x=172,y=20,width=112,height=15)

        self.opd_queue_completed_name_label=tk.Label(self.opd_queue_completed,text="Name :")
        self.opd_queue_completed_name_label.place(x=300,y=20,width=102,height=15)
        self.opd_queue_completed_name_label_display=tk.Label(self.opd_queue_completed,text="Name display")
        self.opd_queue_completed_name_label_display.place(x=424,y=20,width=112,height=15)
        
        self.opd_queue_completed_phoneno_label=tk.Label(self.opd_queue_completed,text="Phone NO :")
        self.opd_queue_completed_phoneno_label.place(x=20,y=60,width=100,height=15)
        self.opd_queue_completed_phoneno_label_display=tk.Label(self.opd_queue_completed,text="phone_no_display")
        self.opd_queue_completed_phoneno_label_display.place(x=172,y=60,width=112,height=15)
        
        self.opd_queue_completed_gender_label=tk.Label(self.opd_queue_completed,text="Gender:")
        self.opd_queue_completed_gender_label.place(x=300,y=60,width=100,height=15)
        self.opd_queue_completed_gender_label_display=tk.Label(self.opd_queue_completed,text="gender_display")
        self.opd_queue_completed_gender_label_display.place(x=424,y=60,width=112,height=15)

        self.opd_queue_completed_age_label=tk.Label(self.opd_queue_completed,text="Age :")
        self.opd_queue_completed_age_label.place(x=20,y=100,width=100,height=15)
        self.opd_queue_completed_age_label_display=tk.Label(self.opd_queue_completed,text="age display")
        self.opd_queue_completed_age_label_display.place(x=172,y=100,width=112,height=15)
        
        self.opd_queue_completed_specialization_label=tk.Label(self.opd_queue_completed,text="Specialization ")
        self.opd_queue_completed_specialization_label.place(x=20,y=140,width=100,height=15)
        self.opd_queue_completed_specialization_value_inside=tk.StringVar()
        self.opd_queue_completed_specialization_value_inside.set('select role')
        self.opd_queue_completed_specialization_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.opd_queue_completed_specialization = ttk.OptionMenu(self.opd_queue_completed,self.opd_queue_completed_specialization_value_inside , *self.opd_queue_completed_specialization_list)
        self.opd_queue_completed_specialization.configure(width=38)
        self.opd_queue_completed_specialization.place(x=170,y=140)
        print("the valuse on the roles:",self.opd_queue_completed_specialization_value_inside.get())
        
        self.opd_queue_completed_doctor_label=tk.Label(self.opd_queue_completed,text="Doctor ")
        self.opd_queue_completed_doctor_label.place(x=20,y=180,width=100,height=15)
        self.opd_queue_completed_doctor_value_inside=tk.StringVar()
        self.opd_queue_completed_doctor_value_inside.set('select role')
        self.opd_queue_completed_doctor_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.opd_queue_completed_doctor= ttk.OptionMenu(self.opd_queue_completed,self.opd_queue_completed_doctor_value_inside , *self.opd_queue_completed_doctor_list)
        self.opd_queue_completed_doctor.configure(width=38)
        self.opd_queue_completed_doctor.place(x=170,y=180)
        print("the valuse on the roles:",self.opd_queue_completed_doctor_value_inside.get())

        self.opd_queue_completed_warning_label=tk.Label(self.opd_queue_completed,text=" ",font=('calibre',13,'bold'))
        self.opd_queue_completed_warning_label.place(x=70,y=220,width=400,height=15)

        self.opd_queue_completed_yes_button=tk.Button(self.opd_queue_completed,text="YES")
        self.opd_queue_completed_yes_button.pack_forget()
        self.opd_queue_completed_no_button=tk.Button(self.opd_queue_completed,text="NO",command=self.opd_queue_completed_deactivate)
        self.opd_queue_completed_no_button.pack_forget()


        if(self.opd_queue_selected == ''):
            self.opd_queue_completed_warning_label.config(text="WARNING!:please select patient in patient queue")
        else:
            self.opd_queue_completed_yes_button.place(x=70,y=250,width=112,height=25)
            self.opd_queue_completed_no_button.place(x=370,y=250,width=112,height=25)


        self.opd_queue_completed.wm_transient(self.root1)
        self.opd_queue_completed.mainloop()

    def opd_queue_completed_deactivate(self):
        self.opd_queue_completed.destroy()

    def  opd_queue_delete_fun(self):
        self.opd_queue_selectItem()
        self.opd_queue_delete = Toplevel(self.main_page_frame_view3_opd_queue_default_frame)
        self.opd_queue_delete.title("OPD DELETE")
        self.main_window_geometry_x = self.root1.winfo_x()
        self.main_window_geometry_y = self.root1.winfo_y()
        self.opd_queue_delete.geometry("600x300+500+300")

        self.opd_queue_delete_id_label=tk.Label(self.opd_queue_delete,text="Patient ID :")
        self.opd_queue_delete_id_label.place(x=20,y=20,width=100,height=15)
        self.opd_queue_delete_id_label_display=tk.Label(self.opd_queue_delete,text="Patient ID display")
        self.opd_queue_delete_id_label_display.place(x=172,y=20,width=112,height=15)

        self.opd_queue_delete_name_label=tk.Label(self.opd_queue_delete,text="Name :")
        self.opd_queue_delete_name_label.place(x=300,y=20,width=102,height=15)
        self.opd_queue_delete_name_label_display=tk.Label(self.opd_queue_delete,text="Name display")
        self.opd_queue_delete_name_label_display.place(x=424,y=20,width=112,height=15)
        
        self.opd_queue_delete_phoneno_label=tk.Label(self.opd_queue_delete,text="Phone NO :")
        self.opd_queue_delete_phoneno_label.place(x=20,y=60,width=100,height=15)
        self.opd_queue_delete_phoneno_label_display=tk.Label(self.opd_queue_delete,text="phone_no_display")
        self.opd_queue_delete_phoneno_label_display.place(x=172,y=60,width=112,height=15)
        
        self.opd_queue_delete_gender_label=tk.Label(self.opd_queue_delete,text="Gender:")
        self.opd_queue_delete_gender_label.place(x=300,y=60,width=100,height=15)
        self.opd_queue_delete_gender_label_display=tk.Label(self.opd_queue_delete,text="gender_display")
        self.opd_queue_delete_gender_label_display.place(x=424,y=60,width=112,height=15)

        self.opd_queue_delete_age_label=tk.Label(self.opd_queue_delete,text="Age :")
        self.opd_queue_delete_age_label.place(x=20,y=100,width=100,height=15)
        self.opd_queue_delete_age_label_display=tk.Label(self.opd_queue_delete,text="age display")
        self.opd_queue_delete_age_label_display.place(x=172,y=100,width=112,height=15)
        
        self.opd_queue_delete_specialization_label=tk.Label(self.opd_queue_delete,text="Specialization ")
        self.opd_queue_delete_specialization_label.place(x=20,y=140,width=100,height=15)
        self.opd_queue_delete_specialization_value_inside=tk.StringVar()
        self.opd_queue_delete_specialization_value_inside.set('select role')
        self.opd_queue_delete_specialization_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.opd_queue_delete_specialization = ttk.OptionMenu(self.opd_queue_delete,self.opd_queue_delete_specialization_value_inside , *self.opd_queue_delete_specialization_list)
        self.opd_queue_delete_specialization.configure(width=38)
        self.opd_queue_delete_specialization.place(x=170,y=140)
        print("the valuse on the roles:",self.opd_queue_delete_specialization_value_inside.get())
        
        self.opd_queue_delete_doctor_label=tk.Label(self.opd_queue_delete,text="Doctor ")
        self.opd_queue_delete_doctor_label.place(x=20,y=180,width=100,height=15)
        self.opd_queue_delete_doctor_value_inside=tk.StringVar()
        self.opd_queue_delete_doctor_value_inside.set('select role')
        self.opd_queue_delete_doctor_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.opd_queue_delete_doctor= ttk.OptionMenu(self.opd_queue_delete,self.opd_queue_delete_doctor_value_inside , *self.opd_queue_delete_doctor_list)
        self.opd_queue_delete_doctor.configure(width=38)
        self.opd_queue_delete_doctor.place(x=170,y=180)
        print("the valuse on the roles:",self.opd_queue_delete_doctor_value_inside.get())

        self.opd_queue_delete_warning_label=tk.Label(self.opd_queue_delete,text=" ",font=('calibre',13,'bold'))
        self.opd_queue_delete_warning_label.place(x=70,y=220,width=400,height=15)

        self.opd_queue_delete_yes_button=tk.Button(self.opd_queue_delete,text="YES")
        self.opd_queue_delete_yes_button.pack_forget()
        self.opd_queue_delete_no_button=tk.Button(self.opd_queue_delete,text="NO",command=self.opd_queue_delete_deactivate)
        self.opd_queue_delete_no_button.pack_forget()


        if(self.opd_queue_selected == ''):
            self.opd_queue_delete_warning_label.config(text="WARNING!:please select patient in patient queue")
        else:
            self.opd_queue_delete_yes_button.place(x=70,y=250,width=112,height=25)
            self.opd_queue_delete_no_button.place(x=370,y=250,width=112,height=25)


        self.opd_queue_delete.wm_transient(self.root1)
        self.opd_queue_delete.mainloop()
    
    def opd_queue_delete_deactivate(self):
        self.opd_queue_delete.destroy()
    
    #opd_queue_functions==============================end==================================


    #ipd_queue_functions==============================start==================================
    def ipd_queue_display(self): 
        #adding the values into contact list 
        self.ipd_queue_contacts = []
        for n in range(1, 200):
            self.ipd_queue_contacts.append((f'ipd_queue_first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview 
        for contact in self.ipd_queue_contacts:
            self.ipd_queue_default_tree.insert('', tk.END, values=contact)

        self.ipd_queue_default_tree.place(x=15,y=150,width=1200,height=600)
        #tree.grid(row=0, column=0, sticky='nsew')

        #ading the scroll baar 
        self.ipd_queue_scrollbar = ttk.Scrollbar(self.main_page_frame_view3_ipd_queue_default_frame, orient=tk.VERTICAL, command=self.ipd_queue_default_tree.yview)
        self.ipd_queue_default_tree.configure(yscroll=self.ipd_queue_scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        self.ipd_queue_scrollbar.place(x=1215, y=150,width=15,height=600)

        self.ipd_queue_selected = self.ipd_queue_default_tree.focus()
        print("self.ipd_queue_selected in display" + self.ipd_queue_selected)

    def ipd_queue_selectItem(self):
        #curItem = tree.focus()
        #print(curItem, a)
        self.ipd_queue_selected = self.ipd_queue_default_tree.focus()
        print("self.ipd_queue_selected in selected" + self.ipd_queue_selected)
        if (self.ipd_queue_selected != ''):
             self.ipd_queue_temp = self.ipd_queue_default_tree.item(self.ipd_queue_selected, 'values')
             print(self.ipd_queue_temp)

    def ipd_queue_display_treeview_reset(self):
        for item in self.ipd_queue_default_tree.get_children():
            self.ipd_queue_default_tree.delete(item)

    def  ipd_queue_send_to_OPD_fun(self):
        self.ipd_queue_selectItem()
        self.ipd_queue_send_to_OPD = Toplevel(self.main_page_frame_view3_ipd_queue_default_frame)
        self.ipd_queue_send_to_OPD.title("SEND TO OPD")
        self.ipd_queue_send_to_OPD.geometry("600x300+500+300")

        self.ipd_queue_send_to_OPD_id_label=tk.Label(self.ipd_queue_send_to_OPD,text="Patient ID :")
        self.ipd_queue_send_to_OPD_id_label.place(x=20,y=20,width=100,height=15)
        self.ipd_queue_send_to_OPD_id_label_display=tk.Label(self.ipd_queue_send_to_OPD,text="Patient ID display")
        self.ipd_queue_send_to_OPD_id_label_display.place(x=172,y=20,width=112,height=15)

        self.ipd_queue_send_to_OPD_name_label=tk.Label(self.ipd_queue_send_to_OPD,text="Name :")
        self.ipd_queue_send_to_OPD_name_label.place(x=300,y=20,width=102,height=15)
        self.ipd_queue_send_to_OPD_name_label_display=tk.Label(self.ipd_queue_send_to_OPD,text="Name display")
        self.ipd_queue_send_to_OPD_name_label_display.place(x=424,y=20,width=112,height=15)
        
        self.ipd_queue_send_to_OPD_phoneno_label=tk.Label(self.ipd_queue_send_to_OPD,text="Phone NO :")
        self.ipd_queue_send_to_OPD_phoneno_label.place(x=20,y=60,width=100,height=15)
        self.ipd_queue_send_to_OPD_phoneno_label_display=tk.Label(self.ipd_queue_send_to_OPD,text="phone_no_display")
        self.ipd_queue_send_to_OPD_phoneno_label_display.place(x=172,y=60,width=112,height=15)
        
        self.ipd_queue_send_to_OPD_gender_label=tk.Label(self.ipd_queue_send_to_OPD,text="Gender:")
        self.ipd_queue_send_to_OPD_gender_label.place(x=300,y=60,width=100,height=15)
        self.ipd_queue_send_to_OPD_gender_label_display=tk.Label(self.ipd_queue_send_to_OPD,text="gender_display")
        self.ipd_queue_send_to_OPD_gender_label_display.place(x=424,y=60,width=112,height=15)

        self.ipd_queue_send_to_OPD_age_label=tk.Label(self.ipd_queue_send_to_OPD,text="Age :")
        self.ipd_queue_send_to_OPD_age_label.place(x=20,y=100,width=100,height=15)
        self.ipd_queue_send_to_OPD_age_label_display=tk.Label(self.ipd_queue_send_to_OPD,text="age display")
        self.ipd_queue_send_to_OPD_age_label_display.place(x=172,y=100,width=112,height=15)
        
        self.ipd_queue_send_to_OPD_specialization_label=tk.Label(self.ipd_queue_send_to_OPD,text="Specialization ")
        self.ipd_queue_send_to_OPD_specialization_label.place(x=20,y=140,width=100,height=15)
        self.ipd_queue_send_to_OPD_specialization_value_inside=tk.StringVar()
        self.ipd_queue_send_to_OPD_specialization_value_inside.set('select role')
        self.ipd_queue_send_to_OPD_specialization_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.ipd_queue_send_to_OPD_specialization = ttk.OptionMenu(self.ipd_queue_send_to_OPD,self.ipd_queue_send_to_OPD_specialization_value_inside , *self.ipd_queue_send_to_OPD_specialization_list)
        self.ipd_queue_send_to_OPD_specialization.configure(width=38)
        self.ipd_queue_send_to_OPD_specialization.place(x=170,y=140)
        print("the valuse on the roles:",self.ipd_queue_send_to_OPD_specialization_value_inside.get())
        
        self.ipd_queue_send_to_OPD_doctor_label=tk.Label(self.ipd_queue_send_to_OPD,text="Doctor ")
        self.ipd_queue_send_to_OPD_doctor_label.place(x=20,y=180,width=100,height=15)
        self.ipd_queue_send_to_OPD_doctor_value_inside=tk.StringVar()
        self.ipd_queue_send_to_OPD_doctor_value_inside.set('select role')
        self.ipd_queue_send_to_OPD_doctor_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.ipd_queue_send_to_OPD_doctor= ttk.OptionMenu(self.ipd_queue_send_to_OPD,self.ipd_queue_send_to_OPD_doctor_value_inside , *self.ipd_queue_send_to_OPD_doctor_list)
        self.ipd_queue_send_to_OPD_doctor.configure(width=38)
        self.ipd_queue_send_to_OPD_doctor.place(x=170,y=180)
        print("the valuse on the roles:",self.ipd_queue_send_to_OPD_doctor_value_inside.get())

        self.ipd_queue_send_to_OPD_warning_label=tk.Label(self.ipd_queue_send_to_OPD,text=" ",font=('calibre',13,'bold'))
        self.ipd_queue_send_to_OPD_warning_label.place(x=70,y=220,width=400,height=15)

        self.ipd_queue_send_to_OPD_yes_button=tk.Button(self.ipd_queue_send_to_OPD,text="YES")
        self.ipd_queue_send_to_OPD_yes_button.pack_forget()
        self.ipd_queue_send_to_OPD_no_button=tk.Button(self.ipd_queue_send_to_OPD,text="NO",command=self.ipd_queue_send_to_OPD_deactivate)
        self.ipd_queue_send_to_OPD_no_button.pack_forget()


        if(self.ipd_queue_selected == ''):
            self.ipd_queue_send_to_OPD_warning_label.config(text="WARNING!:please select patient in patient queue")
        else:
            self.ipd_queue_send_to_OPD_yes_button.place(x=70,y=250,width=112,height=25)
            self.ipd_queue_send_to_OPD_no_button.place(x=370,y=250,width=112,height=25)


        self.ipd_queue_send_to_OPD.wm_transient(self.root1)
        self.ipd_queue_send_to_OPD.mainloop()

    def ipd_queue_send_to_OPD_deactivate(self):
        self.ipd_queue_send_to_OPD.destroy()

    def  ipd_queue_completed_fun(self):
        self.ipd_queue_selectItem()
        self.ipd_queue_completed = Toplevel(self.main_page_frame_view3_ipd_queue_default_frame)
        self.ipd_queue_completed.title("IPD COMPLETED")
        self.ipd_queue_completed.geometry("600x300+500+300")

        self.ipd_queue_completed_id_label=tk.Label(self.ipd_queue_completed,text="Patient ID :")
        self.ipd_queue_completed_id_label.place(x=20,y=20,width=100,height=15)
        self.ipd_queue_completed_id_label_display=tk.Label(self.ipd_queue_completed,text="Patient ID display")
        self.ipd_queue_completed_id_label_display.place(x=172,y=20,width=112,height=15)

        self.ipd_queue_completed_name_label=tk.Label(self.ipd_queue_completed,text="Name :")
        self.ipd_queue_completed_name_label.place(x=300,y=20,width=102,height=15)
        self.ipd_queue_completed_name_label_display=tk.Label(self.ipd_queue_completed,text="Name display")
        self.ipd_queue_completed_name_label_display.place(x=424,y=20,width=112,height=15)
        
        self.ipd_queue_completed_phoneno_label=tk.Label(self.ipd_queue_completed,text="Phone NO :")
        self.ipd_queue_completed_phoneno_label.place(x=20,y=60,width=100,height=15)
        self.ipd_queue_completed_phoneno_label_display=tk.Label(self.ipd_queue_completed,text="phone_no_display")
        self.ipd_queue_completed_phoneno_label_display.place(x=172,y=60,width=112,height=15)
        
        self.ipd_queue_completed_gender_label=tk.Label(self.ipd_queue_completed,text="Gender:")
        self.ipd_queue_completed_gender_label.place(x=300,y=60,width=100,height=15)
        self.ipd_queue_completed_gender_label_display=tk.Label(self.ipd_queue_completed,text="gender_display")
        self.ipd_queue_completed_gender_label_display.place(x=424,y=60,width=112,height=15)

        self.ipd_queue_completed_age_label=tk.Label(self.ipd_queue_completed,text="Age :")
        self.ipd_queue_completed_age_label.place(x=20,y=100,width=100,height=15)
        self.ipd_queue_completed_age_label_display=tk.Label(self.ipd_queue_completed,text="age display")
        self.ipd_queue_completed_age_label_display.place(x=172,y=100,width=112,height=15)
        
        self.ipd_queue_completed_specialization_label=tk.Label(self.ipd_queue_completed,text="Specialization ")
        self.ipd_queue_completed_specialization_label.place(x=20,y=140,width=100,height=15)
        self.ipd_queue_completed_specialization_value_inside=tk.StringVar()
        self.ipd_queue_completed_specialization_value_inside.set('select role')
        self.ipd_queue_completed_specialization_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.ipd_queue_completed_specialization = ttk.OptionMenu(self.ipd_queue_completed,self.ipd_queue_completed_specialization_value_inside , *self.ipd_queue_completed_specialization_list)
        self.ipd_queue_completed_specialization.configure(width=38)
        self.ipd_queue_completed_specialization.place(x=170,y=140)
        print("the valuse on the roles:",self.ipd_queue_completed_specialization_value_inside.get())
        
        self.ipd_queue_completed_doctor_label=tk.Label(self.ipd_queue_completed,text="Doctor ")
        self.ipd_queue_completed_doctor_label.place(x=20,y=180,width=100,height=15)
        self.ipd_queue_completed_doctor_value_inside=tk.StringVar()
        self.ipd_queue_completed_doctor_value_inside.set('select role')
        self.ipd_queue_completed_doctor_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.ipd_queue_completed_doctor= ttk.OptionMenu(self.ipd_queue_completed,self.ipd_queue_completed_doctor_value_inside , *self.ipd_queue_completed_doctor_list)
        self.ipd_queue_completed_doctor.configure(width=38)
        self.ipd_queue_completed_doctor.place(x=170,y=180)
        print("the valuse on the roles:",self.ipd_queue_completed_doctor_value_inside.get())

        self.ipd_queue_completed_warning_label=tk.Label(self.ipd_queue_completed,text=" ",font=('calibre',13,'bold'))
        self.ipd_queue_completed_warning_label.place(x=70,y=220,width=400,height=15)

        self.ipd_queue_completed_yes_button=tk.Button(self.ipd_queue_completed,text="YES")
        self.ipd_queue_completed_yes_button.pack_forget()
        self.ipd_queue_completed_no_button=tk.Button(self.ipd_queue_completed,text="NO",command=self.ipd_queue_completed_deactivate)
        self.ipd_queue_completed_no_button.pack_forget()


        if(self.ipd_queue_selected == ''):
            self.ipd_queue_completed_warning_label.config(text="WARNING!:please select patient in patient queue")
        else:
            self.ipd_queue_completed_yes_button.place(x=70,y=250,width=112,height=25)
            self.ipd_queue_completed_no_button.place(x=370,y=250,width=112,height=25)


        self.ipd_queue_completed.wm_transient(self.root1)
        self.ipd_queue_completed.mainloop()

    def ipd_queue_completed_deactivate(self):
        self.ipd_queue_completed.destroy()

    def  ipd_queue_delete_fun(self):
        self.ipd_queue_selectItem()
        self.ipd_queue_delete = Toplevel(self.main_page_frame_view3_ipd_queue_default_frame)
        self.ipd_queue_delete.title("IPD DELETE")
        self.ipd_queue_delete.geometry("600x300+500+300")

        self.ipd_queue_delete_id_label=tk.Label(self.ipd_queue_delete,text="Patient ID :")
        self.ipd_queue_delete_id_label.place(x=20,y=20,width=100,height=15)
        self.ipd_queue_delete_id_label_display=tk.Label(self.ipd_queue_delete,text="Patient ID display")
        self.ipd_queue_delete_id_label_display.place(x=172,y=20,width=112,height=15)

        self.ipd_queue_delete_name_label=tk.Label(self.ipd_queue_delete,text="Name :")
        self.ipd_queue_delete_name_label.place(x=300,y=20,width=102,height=15)
        self.ipd_queue_delete_name_label_display=tk.Label(self.ipd_queue_delete,text="Name display")
        self.ipd_queue_delete_name_label_display.place(x=424,y=20,width=112,height=15)
        
        self.ipd_queue_delete_phoneno_label=tk.Label(self.ipd_queue_delete,text="Phone NO :")
        self.ipd_queue_delete_phoneno_label.place(x=20,y=60,width=100,height=15)
        self.ipd_queue_delete_phoneno_label_display=tk.Label(self.ipd_queue_delete,text="phone_no_display")
        self.ipd_queue_delete_phoneno_label_display.place(x=172,y=60,width=112,height=15)
        
        self.ipd_queue_delete_gender_label=tk.Label(self.ipd_queue_delete,text="Gender:")
        self.ipd_queue_delete_gender_label.place(x=300,y=60,width=100,height=15)
        self.ipd_queue_delete_gender_label_display=tk.Label(self.ipd_queue_delete,text="gender_display")
        self.ipd_queue_delete_gender_label_display.place(x=424,y=60,width=112,height=15)

        self.ipd_queue_delete_age_label=tk.Label(self.ipd_queue_delete,text="Age :")
        self.ipd_queue_delete_age_label.place(x=20,y=100,width=100,height=15)
        self.ipd_queue_delete_age_label_display=tk.Label(self.ipd_queue_delete,text="age display")
        self.ipd_queue_delete_age_label_display.place(x=172,y=100,width=112,height=15)
        
        self.ipd_queue_delete_specialization_label=tk.Label(self.ipd_queue_delete,text="Specialization ")
        self.ipd_queue_delete_specialization_label.place(x=20,y=140,width=100,height=15)
        self.ipd_queue_delete_specialization_value_inside=tk.StringVar()
        self.ipd_queue_delete_specialization_value_inside.set('select role')
        self.ipd_queue_delete_specialization_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.ipd_queue_delete_specialization = ttk.OptionMenu(self.ipd_queue_delete,self.ipd_queue_delete_specialization_value_inside , *self.ipd_queue_delete_specialization_list)
        self.ipd_queue_delete_specialization.configure(width=38)
        self.ipd_queue_delete_specialization.place(x=170,y=140)
        print("the valuse on the roles:",self.ipd_queue_delete_specialization_value_inside.get())
        
        self.ipd_queue_delete_doctor_label=tk.Label(self.ipd_queue_delete,text="Doctor ")
        self.ipd_queue_delete_doctor_label.place(x=20,y=180,width=100,height=15)
        self.ipd_queue_delete_doctor_value_inside=tk.StringVar()
        self.ipd_queue_delete_doctor_value_inside.set('select role')
        self.ipd_queue_delete_doctor_list = ["Accountant","Clerical Staff","Admin","Doctor","House Keeping","Janitorial Staff","Nurse","Physician","Receptionist"]
        self.ipd_queue_delete_doctor= ttk.OptionMenu(self.ipd_queue_delete,self.ipd_queue_delete_doctor_value_inside , *self.ipd_queue_delete_doctor_list)
        self.ipd_queue_delete_doctor.configure(width=38)
        self.ipd_queue_delete_doctor.place(x=170,y=180)
        print("the valuse on the roles:",self.ipd_queue_delete_doctor_value_inside.get())

        self.ipd_queue_delete_warning_label=tk.Label(self.ipd_queue_delete,text=" ",font=('calibre',13,'bold'))
        self.ipd_queue_delete_warning_label.place(x=70,y=220,width=400,height=15)

        self.ipd_queue_delete_yes_button=tk.Button(self.ipd_queue_delete,text="YES")
        self.ipd_queue_delete_yes_button.pack_forget()
        self.ipd_queue_delete_no_button=tk.Button(self.ipd_queue_delete,text="NO",command=self.ipd_queue_delete_deactivate)
        self.ipd_queue_delete_no_button.pack_forget()


        if(self.ipd_queue_selected == ''):
            self.ipd_queue_delete_warning_label.config(text="WARNING!:please select patient in patient queue")
        else:
            self.ipd_queue_delete_yes_button.place(x=70,y=250,width=112,height=25)
            self.ipd_queue_delete_no_button.place(x=370,y=250,width=112,height=25)


        self.ipd_queue_delete.wm_transient(self.root1)
        self.ipd_queue_delete.mainloop()

    def ipd_queue_delete_deactivate(self):
        self.ipd_queue_delete.destroy()
    
    #ipd_queue_functions==============================end==================================
    #physical_management_functions==============================start==================================
    def physical_management_Book_room_fun(self):
        self.physical_management_book_room_treeview_reset()
        self.avaliable_room_list = None
        self.avaliable_room_list = login_check.get_execution_result("select room_ID,room_floor, room_no,rooms_status from rooms_details where rooms_status = 'unoccupied'")
        print("avaliable_room_list type:",self.avaliable_room_list)
        #adding the values into contact list 
        self.physical_management_book_room_contacts = []
        for i in self.avaliable_room_list:
            #self.physical_management_book_room_contacts.append(i[0],i[1],i[2],i[3])
            self.physical_management_book_room_contacts.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}'))
            #(f'patient_search_first {n}', f'last {n}', f'email{n}@example.com')

        # add data to the treeview 
        for i in self.physical_management_book_room_contacts:
            self.physical_management_book_room_default_tree.insert('', tk.END, values=i)

        self.physical_management_book_room_default_tree.place(x=130,y=200,width=1000,height=400)
        #tree.grid(row=0, column=0, sticky='nsew')

        #ading the scroll baar 
        self.physical_management_book_room_scrollbar = ttk.Scrollbar(self.main_page_frame_view3_physical_management_book_frame, orient=tk.VERTICAL, command=self.physical_management_book_room_default_tree.yview)
        self.physical_management_book_room_default_tree.configure(yscroll=self.physical_management_book_room_scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        self.physical_management_book_room_scrollbar.place(x=1130, y=200,width=15,height=400)
        
        self.physical_management_book_room_selected = self.physical_management_book_room_default_tree.focus()
        print("self.physical_management_book_room_selected in display",self.physical_management_book_room_selected)

    def physical_management_book_room_treeview_reset(self):
        for item in self.physical_management_book_room_default_tree.get_children():
            self.physical_management_book_room_default_tree.delete(item)
    def physical_management_book_room_assaign_room_fun(self):
         self.physical_management_book_room_treeview_select_responce = self.physical_management_book_room_default_tree.focus()
         print("physical_management_book_room_treeview_selected :",self.physical_management_book_room_treeview_select_responce)
         self.physical_management_book_room_treeview_selected1 = self.physical_management_book_room_default_tree.item(self.physical_management_book_room_treeview_select_responce)
         print("values are ",self.physical_management_book_room_treeview_selected1['values'])
         self.physical_management_book_room_treeview_selected=self.physical_management_book_room_treeview_selected1['values']
         print("self.physical_management_book_room_treeview_selected type:",type(self.physical_management_book_room_treeview_selected))
         self.physical_management_book_room_assaign_room_id = self.physical_management_book_room_treeview_selected[0]
         self.physical_management_book_room_assaign_room_floor_no =self.physical_management_book_room_treeview_selected[1]
         self.physical_management_book_room_assaign_room_room_no =self.physical_management_book_room_treeview_selected[2]
         self.physical_management_book_room_assaign_room_patient_id_input_var=tk.IntVar()
         self.physical_management_book_room_assaign_room = Toplevel(self.main_page_frame_view3_physical_management_book_frame)
         self.physical_management_book_room_assaign_room.title("ASSIGN ROOM")
         self.physical_management_book_room_assaign_room.geometry("600x300+500+300")
         
         #self.physical_management_book_room_assaign_room

         self.physical_management_book_room_assaign_room_assign_room_label=tk.Label(self.physical_management_book_room_assaign_room,text="Assign Room")
         self.physical_management_book_room_assaign_room_assign_room_label.place(x=250,y=20,width=100,height=25)
         self.physical_management_book_room_assaign_room_floor_label=tk.Label(self.physical_management_book_room_assaign_room,text="Floor :")
         self.physical_management_book_room_assaign_room_floor_label.place(x=220,y=40,width=50,height=25)
         self.physical_management_book_room_assaign_room_floor_no_label=tk.Label(self.physical_management_book_room_assaign_room,text=self.physical_management_book_room_assaign_room_floor_no)
         self.physical_management_book_room_assaign_room_floor_no_label.place(x=270,y=40,width=10,height=25)
         self.physical_management_book_room_assaign_room_room_label=tk.Label(self.physical_management_book_room_assaign_room,text="Room :")
         self.physical_management_book_room_assaign_room_room_label.place(x=320,y=40,width=50,height=25)
         self.physical_management_book_room_assaign_room_room_no_label=tk.Label(self.physical_management_book_room_assaign_room,text=self.physical_management_book_room_assaign_room_room_no)
         self.physical_management_book_room_assaign_room_room_no_label.place(x=370,y=40,width=10,height=25)
         self.physical_management_book_room_assaign_room_to_label=tk.Label(self.physical_management_book_room_assaign_room,text="to",font=("lucida",15,"bold"))
         self.physical_management_book_room_assaign_room_to_label.place(x=295,y=70,width=30,height=25)
         self.physical_management_book_room_assaign_room_patient_id=tk.Label(self.physical_management_book_room_assaign_room,text="Patient ID :")
         self.physical_management_book_room_assaign_room_patient_id.place(x=100,y=100,width=100,height=25)
         self.physical_management_book_room_assaign_room_patient_id_input=tk.Entry(self.physical_management_book_room_assaign_room,textvariable= self.physical_management_book_room_assaign_room_patient_id_input_var)
         self.physical_management_book_room_assaign_room_patient_id_input.place(x=205,y=100,width=100,height=25)
         self.physical_management_book_room_assaign_room_get_details_button=tk.Button(self.physical_management_book_room_assaign_room,text="Get Details",command=self.physical_management_book_room_assaign_room_get_details)
         self.physical_management_book_room_assaign_room_get_details_button.place(x=350,y=100,width=100,height=25)

         
         self.physical_management_book_room_assaign_room_id_label=tk.Label(self.physical_management_book_room_assaign_room,text="Patient ID :")
         self.physical_management_book_room_assaign_room_id_label.place(x=20,y=140,width=100,height=25)
         self.physical_management_book_room_assaign_room_id_label_display=tk.Label(self.physical_management_book_room_assaign_room,text="Patient ID display")
         self.physical_management_book_room_assaign_room_id_label_display.place(x=172,y=140,width=112,height=25)

         self.physical_management_book_room_assaign_room_name_label=tk.Label(self.physical_management_book_room_assaign_room,text="Name :")
         self.physical_management_book_room_assaign_room_name_label.place(x=300,y=140,width=102,height=25)
         self.physical_management_book_room_assaign_room_name_label_display=tk.Label(self.physical_management_book_room_assaign_room,text="patient name")
         self.physical_management_book_room_assaign_room_name_label_display.place(x=424,y=140,width=112,height=25)
        
         self.physical_management_book_room_assaign_room_phoneno_label=tk.Label(self.physical_management_book_room_assaign_room,text="Phone NO :")
         self.physical_management_book_room_assaign_room_phoneno_label.place(x=20,y=180,width=160,height=25)
         self.physical_management_book_room_assaign_room_phoneno_label_display=tk.Label(self.physical_management_book_room_assaign_room,text="phone_no_display")
         self.physical_management_book_room_assaign_room_phoneno_label_display.place(x=172,y=180,width=112,height=25)
        
         self.physical_management_book_room_assaign_room_gender_label=tk.Label(self.physical_management_book_room_assaign_room,text="Gender:")
         self.physical_management_book_room_assaign_room_gender_label.place(x=300,y=180,width=160,height=25)
         self.physical_management_book_room_assaign_room_gender_label_display=tk.Label(self.physical_management_book_room_assaign_room,text="gender_display")
         self.physical_management_book_room_assaign_room_gender_label_display.place(x=424,y=180,width=112,height=25)

         self.physical_management_book_room_assaign_room_age_label=tk.Label(self.physical_management_book_room_assaign_room,text="Age :")
         self.physical_management_book_room_assaign_room_age_label.place(x=20,y=220,width=100,height=25)
         self.physical_management_book_room_assaign_room_age_label_display=tk.Label(self.physical_management_book_room_assaign_room,text="age display")
         self.physical_management_book_room_assaign_room_age_label_display.place(x=172,y=220,width=112,height=25)

         self.physical_management_book_room_assaign_room_yes_button = tk.Button(self.physical_management_book_room_assaign_room,text='YES',command=self.physical_management_book_room_assaign_room_yes_button_fun)
         self.physical_management_book_room_assaign_room_no_button = tk.Button(self.physical_management_book_room_assaign_room,text='NO',command=self.physical_management_book_room_assaign_room_no_button_fun)

         
        
         
    def physical_management_book_room_assaign_room_get_details(self):
         self.physical_management_book_room_assaign_room_patient_id_in_int =self.physical_management_book_room_assaign_room_patient_id_input_var.get()
         print("self.physical_management_book_room_assaign_room_patient_id_in_int:",self.physical_management_book_room_assaign_room_patient_id_in_int)
         self.physical_management_book_room_assaign_room_patient_id_in_string = str(self.physical_management_book_room_assaign_room_patient_id_in_int)
         self.physical_management_book_room_assaign_room_get_details_database_command = "select id,name,phone_number,age,gender from patient_details where id = " + self.physical_management_book_room_assaign_room_patient_id_in_string
         print("get details command :",self.physical_management_book_room_assaign_room_get_details_database_command)
         self.physical_management_book_room_assaign_room_patient_details_from_patient_id = login_check.get_execution_result(self.physical_management_book_room_assaign_room_get_details_database_command)
         self.book_room_assain_contact=[]
         for i in self.physical_management_book_room_assaign_room_patient_details_from_patient_id:
            #print(" for loop i[0]",i[0])
            #self.book_room_assain_contact.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            self.book_room_assain_contact.append(f'{i[0]}')
            self.book_room_assain_contact.append(f'{i[1]}')
            self.book_room_assain_contact.append(f'{i[2]}')
            self.book_room_assain_contact.append(f'{i[3]}')
            self.book_room_assain_contact.append(f'{i[4]}')

         print("self.book_room_assain_contact:",self.book_room_assain_contact)
         print("type self.book_room_assain_contact:",type(self.book_room_assain_contact))

         print("physical_management_book_room_assaign_room_patient_details_from_patient_id:",type(self.physical_management_book_room_assaign_room_patient_details_from_patient_id))
         print("self.physical_management_book_room_assaign_room_patient_details_from_patient_id=i[0]=",self.physical_management_book_room_assaign_room_patient_details_from_patient_id)
        
         self.physical_management_book_room_assaign_room_id_label_display_var=self.book_room_assain_contact[0]
         self.physical_management_book_room_assaign_room_name_label_display_var=self.book_room_assain_contact[1]
         self.physical_management_book_room_assaign_room_phoneno_label_display_var=self.book_room_assain_contact[2]
         self.physical_management_book_room_assaign_room_gender_label_display_var=self.book_room_assain_contact[4]
         self.physical_management_book_room_assaign_room_age_label_display_var=self.book_room_assain_contact[3]
         print("self.physical_management_book_room_assaign_room_name_label_display_var:",self.physical_management_book_room_assaign_room_name_label_display_var)

         if self.physical_management_book_room_assaign_room_patient_details_from_patient_id != "":
            self.physical_management_book_room_assaign_room_id_label_display.config(text=self.physical_management_book_room_assaign_room_id_label_display_var)
            self.physical_management_book_room_assaign_room_name_label_display.config(text=self.physical_management_book_room_assaign_room_name_label_display_var)
            self.physical_management_book_room_assaign_room_phoneno_label_display.config(text=self.physical_management_book_room_assaign_room_phoneno_label_display_var)
            self.physical_management_book_room_assaign_room_gender_label_display.config(text=self.physical_management_book_room_assaign_room_gender_label_display_var)
            self.physical_management_book_room_assaign_room_age_label_display.config(text=self.physical_management_book_room_assaign_room_age_label_display_var)

         if self.physical_management_book_room_treeview_select_responce != " ":
            self.physical_management_book_room_assaign_room_yes_button.place(x=70,y=270,width=112,height=25)
            self.physical_management_book_room_assaign_room_no_button.place(x=370,y=270,width=112,height=25)
         
         print("self.physical_management_book_room_assaign_room_patient_details_from_patient_id=i[0]=",self.physical_management_book_room_assaign_room_patient_details_from_patient_id)
        
    def physical_management_book_room_assaign_room_yes_button_fun(self):
        self.physical_management_book_room_assaign_person_id_str= str(self.physical_management_book_room_assaign_room_id_label_display_var )
        self.physical_management_book_room_assaign_room_id_str=str(self.physical_management_book_room_assaign_room_id)
        self.physical_management_book_room_assaign_room_command1 = "update rooms_details set  rooms_status = 'occupied',"
        self.physical_management_book_room_assaign_room_command2 = "booked_person_id = " +  self.physical_management_book_room_assaign_person_id_str
        self.physical_management_book_room_assaign_room_command3= "  where room_ID = " + self.physical_management_book_room_assaign_room_id_str
        self.physical_management_book_room_assaign_room_command_main = self.physical_management_book_room_assaign_room_command1 + self.physical_management_book_room_assaign_room_command2 + self.physical_management_book_room_assaign_room_command3
        print("self.physical_management_book_room_assaign_room_command_main:",self.physical_management_book_room_assaign_room_command_main)
        self.physical_management_book_room_assaign_yes_responce = login_check.get_execution_result(self.physical_management_book_room_assaign_room_command_main)
        if self.physical_management_book_room_assaign_yes_responce == []:
            self.physical_management_book_room_assaign_room.destroy()

    def physical_management_book_room_assaign_room_no_button_fun(self):
        self.physical_management_book_room_assaign_room.destroy()



    def physical_management_Discharge_room_fun(self):
        self.physical_management_Discharge_room_treeview_reset()
        self.unavaliable_room_list = None
        self.unavaliable_room_list = login_check.get_execution_result("select room_ID,room_floor, room_no,rooms_status from rooms_details where rooms_status = 'occupied'")
        print("avaliable_room_list type:",self.unavaliable_room_list)
        #adding the values into contact list 
        self.physical_management_Discharge_room_contacts = []
        for i in self.unavaliable_room_list:
            #self.physical_management_Discharge_room_contacts.append(i[0],i[1],i[2],i[3])
            self.physical_management_Discharge_room_contacts.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}'))
            #(f'patient_search_first {n}', f'last {n}', f'email{n}@example.com')

        # add data to the treeview 
        for i in self.physical_management_Discharge_room_contacts:
            self.physical_management_Discharge_room_default_tree.insert('', tk.END, values=i)

        self.physical_management_Discharge_room_default_tree.place(x=130,y=200,width=1000,height=400)
        #tree.grid(row=0, column=0, sticky='nsew')

        #ading the scroll baar 
        self.physical_management_Discharge_room_scrollbar = ttk.Scrollbar(self.main_page_frame_view3_physical_management_Discharge_frame, orient=tk.VERTICAL, command=self.physical_management_Discharge_room_default_tree.yview)
        self.physical_management_Discharge_room_default_tree.configure(yscroll=self.physical_management_Discharge_room_scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        self.physical_management_Discharge_room_scrollbar.place(x=1130, y=200,width=15,height=400)
        
        self.physical_management_Discharge_room_selected = self.physical_management_Discharge_room_default_tree.focus()
        print("self.physical_management_Discharge_room_selected in display",self.physical_management_Discharge_room_selected)

    def physical_management_Discharge_room_treeview_reset(self):
        for item in self.physical_management_Discharge_room_default_tree.get_children():
            self.physical_management_Discharge_room_default_tree.delete(item)
    def physical_management_Discharge_room_Discharge_room_fun(self):
         self.physical_management_Discharge_room_treeview_select_responce = self.physical_management_Discharge_room_default_tree.focus()
         print("physical_management_Discharge_room_treeview_selected :",self.physical_management_Discharge_room_treeview_select_responce)
         self.physical_management_Discharge_room_treeview_selected1 = self.physical_management_Discharge_room_default_tree.item(self.physical_management_Discharge_room_treeview_select_responce)
         print("values are ",self.physical_management_Discharge_room_treeview_selected1['values'])
         self.physical_management_Discharge_room_treeview_selected=self.physical_management_Discharge_room_treeview_selected1['values']
         print("self.physical_management_Discharge_room_treeview_selected type:",type(self.physical_management_Discharge_room_treeview_selected))
         self.physical_management_Discharge_room_Discharge_room_id = self.physical_management_Discharge_room_treeview_selected[0]
         self.physical_management_Discharge_room_Discharge_room_floor_no =self.physical_management_Discharge_room_treeview_selected[1]
         self.physical_management_Discharge_room_Discharge_room_room_no =self.physical_management_Discharge_room_treeview_selected[2]
         self.physical_management_Discharge_room_Discharge_room_patient_id_input_var=tk.IntVar()
         self.physical_management_Discharge_room_Discharge_room = Toplevel(self.main_page_frame_view3_physical_management_Discharge_frame)
         self.physical_management_Discharge_room_Discharge_room.title("DISCHARGE ROOM")
         self.physical_management_Discharge_room_Discharge_room.geometry("600x300+500+300")
         
         #self.physical_management_Discharge_room_Discharge_room

         self.physical_management_Discharge_room_Discharge_room_assign_room_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Discharge Room")
         self.physical_management_Discharge_room_Discharge_room_assign_room_label.place(x=250,y=20,width=100,height=25)
         self.physical_management_Discharge_room_Discharge_room_floor_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Floor :")
         self.physical_management_Discharge_room_Discharge_room_floor_label.place(x=220,y=40,width=50,height=25)
         self.physical_management_Discharge_room_Discharge_room_floor_no_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text=self.physical_management_Discharge_room_Discharge_room_floor_no)
         self.physical_management_Discharge_room_Discharge_room_floor_no_label.place(x=270,y=40,width=10,height=25)
         self.physical_management_Discharge_room_Discharge_room_room_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Room :")
         self.physical_management_Discharge_room_Discharge_room_room_label.place(x=320,y=40,width=50,height=25)
         self.physical_management_Discharge_room_Discharge_room_room_no_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text=self.physical_management_Discharge_room_Discharge_room_room_no)
         self.physical_management_Discharge_room_Discharge_room_room_no_label.place(x=370,y=40,width=10,height=25)
         self.physical_management_Discharge_room_Discharge_room_by_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="by",font=("lucida",15,"bold"))
         self.physical_management_Discharge_room_Discharge_room_by_label.place(x=295,y=70,width=30,height=25)
         self.physical_management_Discharge_room_Discharge_room_patient_id=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Patient ID :")
         self.physical_management_Discharge_room_Discharge_room_patient_id.place(x=100,y=100,width=100,height=25)
         self.physical_management_Discharge_room_Discharge_room_patient_id_input=tk.Entry(self.physical_management_Discharge_room_Discharge_room,textvariable= self.physical_management_Discharge_room_Discharge_room_patient_id_input_var)
         self.physical_management_Discharge_room_Discharge_room_patient_id_input.place(x=205,y=100,width=100,height=25)
         self.physical_management_Discharge_room_Discharge_room_get_details_button=tk.Button(self.physical_management_Discharge_room_Discharge_room,text="Get Details",command=self.physical_management_Discharge_room_Discharge_room_get_details)
         self.physical_management_Discharge_room_Discharge_room_get_details_button.place(x=350,y=100,width=100,height=25)

         
         self.physical_management_Discharge_room_Discharge_room_id_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Patient ID :")
         self.physical_management_Discharge_room_Discharge_room_id_label.place(x=20,y=140,width=100,height=25)
         self.physical_management_Discharge_room_Discharge_room_id_label_display=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Patient ID display")
         self.physical_management_Discharge_room_Discharge_room_id_label_display.place(x=172,y=140,width=112,height=25)

         self.physical_management_Discharge_room_Discharge_room_name_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Name :")
         self.physical_management_Discharge_room_Discharge_room_name_label.place(x=300,y=140,width=102,height=25)
         self.physical_management_Discharge_room_Discharge_room_name_label_display=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="patient name")
         self.physical_management_Discharge_room_Discharge_room_name_label_display.place(x=424,y=140,width=112,height=25)
        
         self.physical_management_Discharge_room_Discharge_room_phoneno_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Phone NO :")
         self.physical_management_Discharge_room_Discharge_room_phoneno_label.place(x=20,y=180,width=160,height=25)
         self.physical_management_Discharge_room_Discharge_room_phoneno_label_display=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="phone_no_display")
         self.physical_management_Discharge_room_Discharge_room_phoneno_label_display.place(x=172,y=180,width=112,height=25)
        
         self.physical_management_Discharge_room_Discharge_room_gender_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Gender:")
         self.physical_management_Discharge_room_Discharge_room_gender_label.place(x=300,y=180,width=160,height=25)
         self.physical_management_Discharge_room_Discharge_room_gender_label_display=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="gender_display")
         self.physical_management_Discharge_room_Discharge_room_gender_label_display.place(x=424,y=180,width=112,height=25)

         self.physical_management_Discharge_room_Discharge_room_age_label=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="Age :")
         self.physical_management_Discharge_room_Discharge_room_age_label.place(x=20,y=220,width=100,height=25)
         self.physical_management_Discharge_room_Discharge_room_age_label_display=tk.Label(self.physical_management_Discharge_room_Discharge_room,text="age display")
         self.physical_management_Discharge_room_Discharge_room_age_label_display.place(x=172,y=220,width=112,height=25)

         self.physical_management_Discharge_room_Discharge_room_yes_button = tk.Button(self.physical_management_Discharge_room_Discharge_room,text='YES',command=self.physical_management_Discharge_room_Discharge_room_yes_button_fun)
         self.physical_management_Discharge_room_Discharge_room_no_button = tk.Button(self.physical_management_Discharge_room_Discharge_room,text='NO',command=self.physical_management_Discharge_room_Discharge_room_no_button_fun)

         
        
         
    def physical_management_Discharge_room_Discharge_room_get_details(self):
         self.physical_management_Discharge_room_Discharge_room_patient_id_in_int =self.physical_management_Discharge_room_Discharge_room_patient_id_input_var.get()
         print("self.physical_management_Discharge_room_Discharge_room_patient_id_in_int:",self.physical_management_Discharge_room_Discharge_room_patient_id_in_int)
         self.physical_management_Discharge_room_Discharge_room_patient_id_in_string = str(self.physical_management_Discharge_room_Discharge_room_patient_id_in_int)
         self.physical_management_Discharge_room_Discharge_room_get_details_database_command = "select id,name,phone_number,age,gender from patient_details where id = " + self.physical_management_Discharge_room_Discharge_room_patient_id_in_string
         print("get details command :",self.physical_management_Discharge_room_Discharge_room_get_details_database_command)
         self.physical_management_Discharge_room_Discharge_room_patient_details_from_patient_id = login_check.get_execution_result(self.physical_management_Discharge_room_Discharge_room_get_details_database_command)
         self.Discharge_room_assain_contact=[]
         for i in self.physical_management_Discharge_room_Discharge_room_patient_details_from_patient_id:
            #print(" for loop i[0]",i[0])
            #self.Discharge_room_assain_contact.append((f'{i[0]}', f'{i[1]}', f'{i[2]}',f'{i[3]}',f'{i[4]}'))
            self.Discharge_room_assain_contact.append(f'{i[0]}')
            self.Discharge_room_assain_contact.append(f'{i[1]}')
            self.Discharge_room_assain_contact.append(f'{i[2]}')
            self.Discharge_room_assain_contact.append(f'{i[3]}')
            self.Discharge_room_assain_contact.append(f'{i[4]}')

         print("self.Discharge_room_assain_contact:",self.Discharge_room_assain_contact)
         print("type self.Discharge_room_assain_contact:",type(self.Discharge_room_assain_contact))

         print("physical_management_Discharge_room_Discharge_room_patient_details_from_patient_id:",type(self.physical_management_Discharge_room_Discharge_room_patient_details_from_patient_id))
         print("self.physical_management_Discharge_room_Discharge_room_patient_details_from_patient_id=i[0]=",self.physical_management_Discharge_room_Discharge_room_patient_details_from_patient_id)
        
         self.physical_management_Discharge_room_Discharge_room_id_label_display_var=self.Discharge_room_assain_contact[0]
         self.physical_management_Discharge_room_Discharge_room_name_label_display_var=self.Discharge_room_assain_contact[1]
         self.physical_management_Discharge_room_Discharge_room_phoneno_label_display_var=self.Discharge_room_assain_contact[2]
         self.physical_management_Discharge_room_Discharge_room_gender_label_display_var=self.Discharge_room_assain_contact[4]
         self.physical_management_Discharge_room_Discharge_room_age_label_display_var=self.Discharge_room_assain_contact[3]
         print("self.physical_management_Discharge_room_Discharge_room_name_label_display_var:",self.physical_management_Discharge_room_Discharge_room_name_label_display_var)

         if self.physical_management_Discharge_room_Discharge_room_patient_details_from_patient_id != "":
            self.physical_management_Discharge_room_Discharge_room_id_label_display.config(text=self.physical_management_Discharge_room_Discharge_room_id_label_display_var)
            self.physical_management_Discharge_room_Discharge_room_name_label_display.config(text=self.physical_management_Discharge_room_Discharge_room_name_label_display_var)
            self.physical_management_Discharge_room_Discharge_room_phoneno_label_display.config(text=self.physical_management_Discharge_room_Discharge_room_phoneno_label_display_var)
            self.physical_management_Discharge_room_Discharge_room_gender_label_display.config(text=self.physical_management_Discharge_room_Discharge_room_gender_label_display_var)
            self.physical_management_Discharge_room_Discharge_room_age_label_display.config(text=self.physical_management_Discharge_room_Discharge_room_age_label_display_var)

         if self.physical_management_Discharge_room_treeview_select_responce != " ":
            self.physical_management_Discharge_room_Discharge_room_yes_button.place(x=70,y=270,width=112,height=25)
            self.physical_management_Discharge_room_Discharge_room_no_button.place(x=370,y=270,width=112,height=25)
         
         print("self.physical_management_Discharge_room_Discharge_room_patient_details_from_patient_id=i[0]=",self.physical_management_Discharge_room_Discharge_room_patient_details_from_patient_id)
        
    def physical_management_Discharge_room_Discharge_room_yes_button_fun(self):
        self.physical_management_Discharge_room_Discharge_person_id_str= str(self.physical_management_Discharge_room_Discharge_room_id_label_display_var )
        self.physical_management_Discharge_room_Discharge_room_id_str=str(self.physical_management_Discharge_room_Discharge_room_id)
        self.physical_management_Discharge_room_Discharge_room_command1 = "update rooms_details set  rooms_status = 'unoccupied',"
        self.physical_management_Discharge_room_Discharge_room_command2 = "booked_person_id = " +  self.physical_management_Discharge_room_Discharge_person_id_str
        self.physical_management_Discharge_room_Discharge_room_command3= "  where room_ID = " + self.physical_management_Discharge_room_Discharge_room_id_str
        self.physical_management_Discharge_room_Discharge_room_command_main = self.physical_management_Discharge_room_Discharge_room_command1 + self.physical_management_Discharge_room_Discharge_room_command2 + self.physical_management_Discharge_room_Discharge_room_command3
        print("self.physical_management_Discharge_room_Discharge_room_command_main:",self.physical_management_Discharge_room_Discharge_room_command_main)
        self.physical_management_Discharge_room_Discharge_yes_responce = login_check.get_execution_result(self.physical_management_Discharge_room_Discharge_room_command_main)
        if self.physical_management_Discharge_room_Discharge_yes_responce == []:
            self.physical_management_Discharge_room_Discharge_room.destroy()

    def physical_management_Discharge_room_Discharge_room_no_button_fun(self):
        self.physical_management_Discharge_room_Discharge_room.destroy()

    def physical_management_room_status_refresh(self):
        self.room_details_data=None
        self.room_details_data = login_check.get_execution_result("select * from rooms_details")
        print(self.room_details_data)
        for i in self.room_details_data:
            self.id_var=i[0]
            self.room_status = i[3]
            if self.id_var == 11  and self.room_status == "occupied":
                   self.room_statusfloor1_room1_label.config(bg='red')
            elif self.id_var == 11 and self.room_status ==  "unoccupied":
                   self.room_statusfloor1_room1_label.config(bg='green')
            elif self.id_var == 11 and self.room_status ==  "maintenance":
                   self.room_statusfloor1_room1_label.config(bg='yellow')

            if self.id_var == 12 and self.room_status == "occupied":
                   self.room_statusfloor1_room2_label.config(bg='red')
            elif self.id_var == 12 and self.room_status ==  "unoccupied":
                   self.room_statusfloor1_room2_label.config(bg='green')
            elif self.id_var == 12 and self.room_status ==  "maintenance":
                   self.room_statusfloor1_room2_label.config(bg='yellow')

            if self.id_var == 13  and self.room_status == "occupied":
               self.room_statusfloor1_room3_label.config(bg='red')
            elif self.id_var ==13  and self.room_status ==  "unoccupied":
               self.room_statusfloor1_room3_label.config(bg='green')
            elif self.id_var ==13  and self.room_status ==  "maintenance":
               self.room_statusfloor1_room3_label.config(bg='yellow')

            if self.id_var == 14 and self.room_status == "occupied":
               self.room_statusfloor1_room4_label.config(bg='red')
            elif self.id_var == 14 and self.room_status ==  "unoccupied":
               self.room_statusfloor1_room4_label.config(bg='green')
            elif self.id_var == 14 and self.room_status ==  "maintenance":
               self.room_statusfloor1_room4_label.config(bg='yellow')

            if self.id_var == 15 and self.room_status == "occupied":
               self.room_statusfloor1_room5_label.config(bg='red')
            elif self.id_var == 15 and self.room_status ==  "unoccupied":
               self.room_statusfloor1_room5_label.config(bg='green')
            elif self.id_var ==15  and self.room_status ==  "maintenance":
               self.room_statusfloor1_room5_label.config(bg='yellow')

            if self.id_var == 21  and self.room_status == "occupied":
               self.room_statusfloor2_room1_label.config(bg='red')
            elif self.id_var == 21 and self.room_status ==  "unoccupied":
               self.room_statusfloor2_room1_label.config(bg='green')
            elif self.id_var == 21 and self.room_status ==  "maintenance":
               self.room_statusfloor2_room1_label.config(bg='yellow')

            if self.id_var == 22 and self.room_status == "occupied":
               self.room_statusfloor2_room2_label.config(bg='red')
            elif self.id_var == 22 and self.room_status ==  "unoccupied":
               self.room_statusfloor2_room2_label.config(bg='green')
            elif self.id_var == 22 and self.room_status ==  "maintenance":
               self.room_statusfloor2_room2_label.config(bg='yellow')

            if self.id_var == 23  and self.room_status == "occupied":
               self.room_statusfloor2_room3_label.config(bg='red')
            elif self.id_var ==23  and self.room_status ==  "unoccupied":
               self.room_statusfloor2_room3_label.config(bg='green')
            elif self.id_var ==23  and self.room_status ==  "maintenance":
               self.room_statusfloor2_room3_label.config(bg='yellow')

            if self.id_var == 24 and self.room_status == "occupied":
               self.room_statusfloor2_room4_label.config(bg='red')
            elif self.id_var == 24 and self.room_status ==  "unoccupied":
               self.room_statusfloor2_room4_label.config(bg='green')
            elif self.id_var == 24 and self.room_status ==  "maintenance":
               self.room_statusfloor2_room4_label.config(bg='yellow')

            if self.id_var == 25 and self.room_status == "occupied":
               self.room_statusfloor2_room5_label.config(bg='red')
            elif self.id_var == 25 and self.room_status ==  "unoccupied":
               self.room_statusfloor2_room5_label.config(bg='green')
            elif self.id_var ==25  and self.room_status ==  "maintenance":
               self.room_statusfloor2_room5_label.config(bg='yellow')

            if self.id_var == 31  and self.room_status == "occupied":
               self.room_statusfloor3_room1_label.config(bg='red')
            elif self.id_var == 31 and self.room_status ==  "unoccupied":
               self.room_statusfloor3_room1_label.config(bg='green')
            elif self.id_var == 31 and self.room_status ==  "maintenance":
               self.room_statusfloor3_room1_label.config(bg='yellow')

            if self.id_var == 32 and self.room_status == "occupied":
               self.room_statusfloor3_room2_label.config(bg='red')
            elif self.id_var == 32 and self.room_status ==  "unoccupied":
               self.room_statusfloor3_room2_label.config(bg='green')
            elif self.id_var == 32 and self.room_status ==  "maintenance":
               self.room_statusfloor3_room2_label.config(bg='yellow')

            if self.id_var == 33  and self.room_status == "occupied":
               self.room_statusfloor3_room3_label.config(bg='red')
            elif self.id_var ==33  and self.room_status ==  "unoccupied":
               self.room_statusfloor3_room3_label.config(bg='green')
            elif self.id_var ==33  and self.room_status ==  "maintenance":
               self.room_statusfloor3_room3_label.config(bg='yellow')

            if self.id_var == 34 and self.room_status == "occupied":
               self.room_statusfloor3_room4_label.config(bg='red')
            elif self.id_var == 34 and self.room_status ==  "unoccupied":
               self.room_statusfloor3_room4_label.config(bg='green')
            elif self.id_var == 34 and self.room_status ==  "maintenance":
               self.room_statusfloor3_room4_label.config(bg='yellow')

            if self.id_var == 35 and self.room_status == "occupied":
               self.room_statusfloor3_room5_label.config(bg='red')
            elif self.id_var == 35 and self.room_status ==  "unoccupied":
               self.room_statusfloor3_room5_label.config(bg='green')
            elif self.id_var == 35  and self.room_status ==  "maintenance":
               self.room_statusfloor3_room5_label.config(bg='yellow')

            if self.id_var == 41  and self.room_status == "occupied":
               self.room_statusfloor4_room1_label.config(bg='red')
            elif self.id_var == 41 and self.room_status ==  "unoccupied":
               self.room_statusfloor4_room1_label.config(bg='green')
            elif self.id_var == 41 and self.room_status ==  "maintenance":
               self.room_statusfloor4_room1_label.config(bg='yellow')

            if self.id_var == 42 and self.room_status == "occupied":
               self.room_statusfloor4_room2_label.config(bg='red')
            elif self.id_var == 42 and self.room_status ==  "unoccupied":
               self.room_statusfloor4_room2_label.config(bg='green')
            elif self.id_var == 42 and self.room_status ==  "maintenance":
               self.room_statusfloor4_room2_label.config(bg='yellow')

            if self.id_var == 43  and self.room_status == "occupied":
               self.room_statusfloor4_room3_label.config(bg='red')
            elif self.id_var ==43  and self.room_status ==  "unoccupied":
               self.room_statusfloor4_room3_label.config(bg='green')
            elif self.id_var ==43  and self.room_status ==  "maintenance":
               self.room_statusfloor4_room3_label.config(bg='yellow')

            if self.id_var == 44 and self.room_status == "occupied":
               self.room_statusfloor4_room4_label.config(bg='red')
            elif self.id_var == 44 and self.room_status ==  "unoccupied":
               self.room_statusfloor4_room4_label.config(bg='green')
            elif self.id_var == 44 and self.room_status ==  "maintenance":
               self.room_statusfloor4_room4_label.config(bg='yellow')

            if self.id_var == 45 and self.room_status == "occupied":
               self.room_statusfloor4_room5_label.config(bg='red')
            elif self.id_var == 45 and self.room_status ==  "unoccupied":
               self.room_statusfloor4_room5_label.config(bg='green')
            elif self.id_var ==45  and self.room_status ==  "maintenance":
               self.room_statusfloor4_room5_label.config(bg='yellow')



            if self.id_var == 51  and self.room_status == "occupied":
               self.room_statusfloor5_room1_label.config(bg='red')
            elif self.id_var == 51 and self.room_status ==  "unoccupied":
               self.room_statusfloor5_room1_label.config(bg='green')
            elif self.id_var == 51 and self.room_status ==  "maintenance":
               self.room_statusfloor5_room1_label.config(bg='yellow')

            if self.id_var == 52 and self.room_status == "occupied":
               self.room_statusfloor5_room2_label.config(bg='red')
            elif self.id_var == 52 and self.room_status ==  "unoccupied":
               self.room_statusfloor5_room2_label.config(bg='green')
            elif self.id_var == 52 and self.room_status ==  "maintenance":
               self.room_statusfloor5_room2_label.config(bg='yellow')

            if self.id_var == 53  and self.room_status == "occupied":
               self.room_statusfloor5_room3_label.config(bg='red')
            elif self.id_var ==53  and self.room_status ==  "unoccupied":
               self.room_statusfloor5_room3_label.config(bg='green')
            elif self.id_var ==53  and self.room_status ==  "maintenance":
               self.room_statusfloor5_room3_label.config(bg='yellow')

            if self.id_var == 54 and self.room_status == "occupied":
               self.room_statusfloor5_room4_label.config(bg='red')
            elif self.id_var == 54 and self.room_status ==  "unoccupied":
               self.room_statusfloor5_room4_label.config(bg='green')
            elif self.id_var == 54 and self.room_status ==  "maintenance":
               self.room_statusfloor5_room4_label.config(bg='yellow')

            if self.id_var == 55 and self.room_status == "occupied":
               self.room_statusfloor5_room5_label.config(bg='red')
            elif self.id_var == 55 and self.room_status ==  "unoccupied":
               self.room_statusfloor5_room5_label.config(bg='green')
            elif self.id_var ==55  and self.room_status ==  "maintenance":
               self.room_statusfloor5_room5_label.config(bg='yellow')
        
     


    #physical_management_functions==============================end==================================

    
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


    def main_page_frame_view3_patient_visit_default_frame_activate(self):
        if self.main_page_frame_view3_patient_visit_default_frame_status  == "deactivated" or self.main_page_frame_view3_patient_visit_default_frame_status == "None" :
              self.main_page_frame_view3_patient_visit_default_frame_status = "activated"
              self.main_page_frame_view3_patient_visit_default_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_patient_search_default_frame_activate(self):
        if self.main_page_frame_view3_patient_search_default_frame_status  == "deactivated" or self.main_page_frame_view3_patient_search_default_frame_status == "None" :
            self.main_page_frame_view3_patient_search_default_frame_status = "activated"
            self.main_page_frame_view3_patient_search_default_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_patient_search_edit_frame_activate(self):
        if self.main_page_frame_view3_patient_search_edit_frame_status  == "deactivated" or self.main_page_frame_view3_patient_search_edit_frame_status == "None" :
            self.main_page_frame_view3_patient_search_edit_frame_status = "activated"
            self.main_page_frame_view3_patient_search_edit_frame.pack(ipadx=670,ipady=390,side='top')


    def main_page_frame_view3_patient_search_display_frame_activate(self):
        if self.main_page_frame_view3_patient_search_display_frame_status  == "deactivated" or self.main_page_frame_view3_patient_search_display_frame_status == "None" :
            self.main_page_frame_view3_patient_search_display_frame_status = "activated"
            self.main_page_frame_view3_patient_search_display_frame.pack(ipadx=670,ipady=390,side='top')

  


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

    def main_page_frame_view3_ipo_queue_default_frame_activate(self):
        if self.main_page_frame_view3_ipo_queue_default_frame_status  == "deactivated" or self.main_page_frame_view3_ipo_queue_default_frame_status == "None" :
              self.main_page_frame_view3_ipo_queue_default_frame_status = "activated"
              self.main_page_frame_view3_ipd_queue_default_frame.pack(ipadx=670,ipady=390,side='top')


    def main_page_frame_view3_physical_management_book_frame_activate(self):
        if self.main_page_frame_view3_physical_management_book_frame_status  == "deactivated" or self.main_page_frame_view3_physical_management_book_frame_status == "None" :
            self.main_page_frame_view3_physical_management_book_frame_status = "activated"
            self.main_page_frame_view3_physical_management_book_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_physical_management_Discharge_frame_activate(self):
        if self.main_page_frame_view3_physical_management_Discharge_frame_status  == "deactivated" or self.main_page_frame_view3_physical_management_Discharge_frame_status == "None" :
            self.main_page_frame_view3_physical_management_Discharge_frame_status = "activated"
            self.main_page_frame_view3_physical_management_Discharge_frame.pack(ipadx=670,ipady=390,side='top')

    def main_page_frame_view3_physical_management_room_status_frame_activate(self):
        if self.main_page_frame_view3_physical_management_room_status_frame_status  == "deactivated" or self.main_page_frame_view3_physical_management_room_status_frame_status == "None" :
            self.main_page_frame_view3_physical_management_room_status_frame_status = "activated"
            self.main_page_frame_view3_physical_management_room_status_frame.pack(ipadx=670,ipady=390,side='top')

    






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



    def main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_activate(self):
        if self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_status  == "deactivated" or self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_status == "None" :
              self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_status = "activated"
              self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame.pack(ipadx=670,ipady=390,side='top')

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
              
    def main_page_frame_view3_patient_visit_default_frame_deactivate(self):
         if self.main_page_frame_view3_patient_visit_default_frame_status  == "activated"  or self.main_page_frame_view3_patient_visit_default_frame_status == "None":
              self.main_page_frame_view3_patient_visit_default_frame_status = "deactivated"
              self.main_page_frame_view3_patient_visit_default_frame.pack_forget()

    def main_page_frame_view3_patient_search_default_frame_deactivate(self):
        if self.main_page_frame_view3_patient_search_default_frame_status  == "activated" or self.main_page_frame_view3_patient_search_default_frame_status == "None" :
            self.main_page_frame_view3_patient_search_default_frame_status = "deactivated"
            self.main_page_frame_view3_patient_search_default_frame.pack_forget()
    
    def main_page_frame_view3_patient_search_edit_frame_deactivate(self):
        if self.main_page_frame_view3_patient_search_edit_frame_status  == "activated" or self.main_page_frame_view3_patient_search_edit_frame_status == "None" :
            self.main_page_frame_view3_patient_search_edit_frame_status = "deactivated"
            self.main_page_frame_view3_patient_search_edit_frame.pack_forget()

    def main_page_frame_view3_patient_search_display_frame_deactivate(self):
        if self.main_page_frame_view3_patient_search_display_frame_status  == "activated" or self.main_page_frame_view3_patient_search_display_frame_status == "None" :
            self.main_page_frame_view3_patient_search_display_frame_status = "deactivated"
            self.main_page_frame_view3_patient_search_display_frame.pack_forget()


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

    def main_page_frame_view3_ipo_queue_default_frame_deactivate(self):
        if self.main_page_frame_view3_ipo_queue_default_frame_status  == "activated" or self.main_page_frame_view3_ipo_queue_default_frame_status == "None" :
            self.main_page_frame_view3_ipo_queue_default_frame_status = "deactivated"
            self.main_page_frame_view3_ipd_queue_default_frame.pack_forget()
   
    def main_page_frame_view3_physical_management_book_frame_deactivate(self):
        if self.main_page_frame_view3_physical_management_book_frame_status  == "activated" or self.main_page_frame_view3_physical_management_book_frame_status == "None" :
              self.main_page_frame_view3_physical_management_book_frame_status = "deactivated"
              self.main_page_frame_view3_physical_management_book_frame.pack_forget()

    def main_page_frame_view3_physical_management_Discharge_frame_deactivate(self):
        if self.main_page_frame_view3_physical_management_Discharge_frame_status  == "activated" or self.main_page_frame_view3_physical_management_Discharge_frame_status == "None" :
            self.main_page_frame_view3_physical_management_Discharge_frame_status = "deactivated"
            self.main_page_frame_view3_physical_management_Discharge_frame.pack_forget()

    def main_page_frame_view3_physical_management_room_status_frame_deactivate(self):
        if self.main_page_frame_view3_physical_management_room_status_frame_status  == "activated" or self.main_page_frame_view3_physical_management_room_status_frame_status == "None" :
            self.main_page_frame_view3_physical_management_room_status_frame_status = "deactivated"
            self.main_page_frame_view3_physical_management_room_status_frame.pack_forget()


    


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



    def main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate(self):
        if self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_status  == "activated" or self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_status == "None" :
            self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_status = "deactivated"
            self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame.pack_forget()

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
    self.main_page_frame_view3_patient_visit_default_frame_deactivate()


    self.main_page_frame_view3_patient_search_default_frame_deactivate()
    self.main_page_frame_view3_patient_search_edit_frame_deactivate()
    self.main_page_frame_view3_patient_search_display_frame_deactivate()

    self.main_page_frame_view3_patient_queue_default_frame_deactivate()
     
     


    self.main_page_frame_view3_lab_queue_default_frame_deactivate()
    self.main_page_frame_view3_search_lab_queue_frame_deactivate()
    self.main_page_frame_view3_view_lab_report_frame_deactivate()

    self.main_page_frame_view3_opd_queue_default_frame_deactivate()

    self.main_page_frame_view3_physical_management_book_frame_deactivate()
    self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
    self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

    self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
    self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
     
    
    
    '''
    #functions_list==================================================stop=====================================
        
    
    #main_page_view2_and_view3=======================================start=====================================

   


    #patient_registration==========================================start===========================================
    #patient_registration_default==========================================start===========================================
    def home_default(self):
             self.main_page_frame_view3_home_frame_activate()
             self.main_page_frame_view3_patient_registration_default_frame_deactivate()
             self.main_page_frame_view3_patient_visit_default_frame_deactivate()

             self.main_page_frame_view3_patient_search_default_frame_deactivate()
             self.main_page_frame_view3_patient_search_edit_frame_deactivate()
             self.main_page_frame_view3_patient_search_display_frame_deactivate()

             self.main_page_frame_view3_patient_queue_default_frame_deactivate()
              
              
             
             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

             self.main_page_frame_view3_physical_management_book_frame_deactivate()
             self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
             self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()


    def patient_registration_default(self):
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_activate()
             self.main_page_frame_view3_patient_visit_default_frame_deactivate()

             self.main_page_frame_view3_patient_search_default_frame_deactivate()
             self.main_page_frame_view3_patient_search_edit_frame_deactivate()
             self.main_page_frame_view3_patient_search_display_frame_deactivate()

             self.main_page_frame_view3_patient_queue_default_frame_deactivate()
              
              
             
             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

             self.main_page_frame_view3_physical_management_book_frame_deactivate()
             self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
             self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
              
             
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
    def patient_visit_default(self):
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_deactivate()
             self.main_page_frame_view3_patient_visit_default_frame_activate()

             self.main_page_frame_view3_patient_search_default_frame_deactivate()
             self.main_page_frame_view3_patient_search_edit_frame_deactivate()
             self.main_page_frame_view3_patient_search_display_frame_deactivate()

             self.main_page_frame_view3_patient_queue_default_frame_deactivate()
              
              


             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

             self.main_page_frame_view3_physical_management_book_frame_deactivate()
             self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
             self.main_page_frame_view3_physical_management_room_status_frame_deactivate()
             
             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
              
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
    def logout_default(self):
         
         self.main_page_frame_view1.pack_forget()
         self.main_page_frame_view2.pack_forget()
         self.main_page_frame_view3_home_frame_deactivate()
         self.main_page_frame_view3_patient_registration_default_frame_deactivate()
         self.main_page_frame_view3_patient_visit_default_frame_deactivate()


         self.main_page_frame_view3_patient_search_default_frame_deactivate()
         self.main_page_frame_view3_patient_search_edit_frame_deactivate()
         self.main_page_frame_view3_patient_search_display_frame_deactivate()

         self.main_page_frame_view3_patient_queue_default_frame_deactivate()
     
     


         self.main_page_frame_view3_lab_queue_default_frame_deactivate()
         self.main_page_frame_view3_search_lab_queue_frame_deactivate()
         self.main_page_frame_view3_view_lab_report_frame_deactivate()

         self.main_page_frame_view3_opd_queue_default_frame_deactivate()

         self.main_page_frame_view3_physical_management_book_frame_deactivate()
         self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
         self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

         self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
         self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
         self.login_page_frame1.place(x=0,y=0)
    def patient_search_default(self):
             self.patient_search_default_display()
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_deactivate()
             self.main_page_frame_view3_patient_visit_default_frame_deactivate()

             self.main_page_frame_view3_patient_search_default_frame_activate()
             self.main_page_frame_view3_patient_search_edit_frame_deactivate()
             self.main_page_frame_view3_patient_search_display_frame_deactivate()

             self.main_page_frame_view3_patient_queue_default_frame_deactivate()
              
              

             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

             self.main_page_frame_view3_physical_management_book_frame_deactivate()
             self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
             self.main_page_frame_view3_physical_management_room_status_frame_deactivate()
             
             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
              
             self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    def patient_search_edit(self):
             self.patient_search_default_display()
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_deactivate()
             self.main_page_frame_view3_patient_visit_default_frame_deactivate()

             self.main_page_frame_view3_patient_search_default_frame_deactivate()
             self.main_page_frame_view3_patient_search_edit_frame_activate()
             self.main_page_frame_view3_patient_search_display_frame_deactivate()
             

             self.main_page_frame_view3_patient_queue_default_frame_deactivate()
              
              

             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

             self.main_page_frame_view3_physical_management_book_frame_deactivate()
             self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
             self.main_page_frame_view3_physical_management_room_status_frame_deactivate()
             
             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
              
             self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    def patient_search_display(self):
             self.patient_search_default_display()
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_deactivate()
             self.main_page_frame_view3_patient_visit_default_frame_deactivate()

             self.main_page_frame_view3_patient_search_default_frame_deactivate()
             self.main_page_frame_view3_patient_search_edit_frame_deactivate()
             self.main_page_frame_view3_patient_search_display_frame_activate()
             
              
              

             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

             self.main_page_frame_view3_physical_management_book_frame_deactivate()
             self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
             self.main_page_frame_view3_physical_management_room_status_frame_deactivate()
             
             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
              
             self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #patient_search_default======================================end=========================================


    #patient_queue=====================================start========================================
    #patient_queue_default=====================================start========================================
    def patient_queue_default(self):
             self.patient_queue_display()
             self.main_page_frame_view3_home_frame_deactivate()
             self.main_page_frame_view3_patient_registration_default_frame_deactivate()
             self.main_page_frame_view3_patient_visit_default_frame_deactivate()

             self.main_page_frame_view3_patient_search_default_frame_deactivate()
             self.main_page_frame_view3_patient_search_edit_frame_deactivate()
             self.main_page_frame_view3_patient_search_display_frame_deactivate()

             self.main_page_frame_view3_patient_queue_default_frame_activate()
              
              

             self.main_page_frame_view3_lab_queue_default_frame_deactivate()
             self.main_page_frame_view3_search_lab_queue_frame_deactivate()
             self.main_page_frame_view3_view_lab_report_frame_deactivate()

             self.main_page_frame_view3_opd_queue_default_frame_deactivate()
             self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

             self.main_page_frame_view3_physical_management_book_frame_deactivate()
             self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
             self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

             self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
             self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
              
             self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #patient_queue_default======================================end=========================================
   
    #patient_queue=====================================end========================================


    #lab_queue===========================================start=======================================
    #lab_queue_default=====================================start========================================
    def lab_queue_default(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_visit_default_frame_deactivate()

        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_edit_frame_deactivate()
        self.main_page_frame_view3_patient_search_display_frame_deactivate()

        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         

        self.main_page_frame_view3_lab_queue_default_frame_activate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

        self.main_page_frame_view3_physical_management_book_frame_deactivate()
        self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
        self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #lab_queue_default======================================end=========================================
    def search_lab_queue(self):
         self.main_page_frame_view3_home_frame_deactivate()
         self.main_page_frame_view3_patient_registration_default_frame_deactivate()
         self.main_page_frame_view3_patient_visit_default_frame_deactivate()

         self.main_page_frame_view3_patient_search_default_frame_deactivate()
         self.main_page_frame_view3_patient_search_edit_frame_deactivate()
         self.main_page_frame_view3_patient_search_display_frame_deactivate()

         self.main_page_frame_view3_patient_queue_default_frame_deactivate()
          
          

         
         self.main_page_frame_view3_lab_queue_default_frame_deactivate()
         self.main_page_frame_view3_search_lab_queue_frame_activate()
         self.main_page_frame_view3_view_lab_report_frame_deactivate()

         self.main_page_frame_view3_search_lab_queue_frame_activate()
         self.main_page_frame_view3_view_lab_report_frame_deactivate()

         self.main_page_frame_view3_opd_queue_default_frame_deactivate()
         self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

         self.main_page_frame_view3_physical_management_book_frame_deactivate()
         self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
         self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

         self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
         self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
         self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    def view_lab_report(self):
         self.main_page_frame_view3_home_frame_deactivate()
         self.main_page_frame_view3_patient_registration_default_frame_deactivate()
         self.main_page_frame_view3_patient_visit_default_frame_deactivate()

         self.main_page_frame_view3_patient_search_default_frame_deactivate()
         self.main_page_frame_view3_patient_search_edit_frame_deactivate()
         self.main_page_frame_view3_patient_search_display_frame_deactivate()

         self.main_page_frame_view3_patient_queue_default_frame_deactivate()
          
          


         self.main_page_frame_view3_lab_queue_default_frame_deactivate()
         self.main_page_frame_view3_search_lab_queue_frame_deactivate()
         self.main_page_frame_view3_view_lab_report_frame_activate()

         self.main_page_frame_view3_opd_queue_default_frame_deactivate()
         self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

         self.main_page_frame_view3_physical_management_book_frame_deactivate()
         self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
         self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

         self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
         self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
         self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #lab_queue===========================================end=======================================

    #opd_queue_default=====================================start========================================
    def opd_queue_default(self):
        self.opd_queue_display()
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_visit_default_frame_deactivate()

        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_edit_frame_deactivate()
        self.main_page_frame_view3_patient_search_display_frame_deactivate()

        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         

        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_activate()
        self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

        self.main_page_frame_view3_physical_management_book_frame_deactivate()
        self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
        self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #opd_queue_default======================================end=========================================

    #ipo_queue_default=====================================start========================================
    def ipd_queue_default(self):
        self.ipd_queue_display()
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_visit_default_frame_deactivate()
        
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_edit_frame_deactivate()
        self.main_page_frame_view3_patient_search_display_frame_deactivate()

        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         

        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_ipo_queue_default_frame_activate()

        self.main_page_frame_view3_physical_management_book_frame_deactivate()
        self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
        self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #ipo_queue_default======================================end=========================================

    #physical_management_book=====================================start========================================
    def physical_management_book(self):
        self.physical_management_Book_room_fun()
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_visit_default_frame_deactivate()
        
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_edit_frame_deactivate()
        self.main_page_frame_view3_patient_search_display_frame_deactivate()



        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         

        
        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

        self.main_page_frame_view3_physical_management_book_frame_activate()
        self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
        self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    def physical_management_Discharge(self):
        self.physical_management_Discharge_room_fun()
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_visit_default_frame_deactivate()
        
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_edit_frame_deactivate()
        self.main_page_frame_view3_patient_search_display_frame_deactivate()



        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         

        
        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

        self.main_page_frame_view3_physical_management_book_frame_deactivate()
        self.main_page_frame_view3_physical_management_Discharge_frame_activate()
        self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    def physical_management_room_status(self):
        #self.physical_management_room_status_refresh()
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_visit_default_frame_deactivate()
        
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_edit_frame_deactivate()
        self.main_page_frame_view3_patient_search_display_frame_deactivate()



        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         

        
        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

        self.main_page_frame_view3_physical_management_book_frame_deactivate()
        self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
        self.main_page_frame_view3_physical_management_room_status_frame_activate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()

    #physical_management_book======================================end=========================================   

    #dialy_collection===============================================start=======================================
    def dialy_collection_default(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_visit_default_frame_deactivate()
        
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_edit_frame_deactivate()
        self.main_page_frame_view3_patient_search_display_frame_deactivate()



        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         


        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

        self.main_page_frame_view3_physical_management_book_frame_deactivate()
        self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
        self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_default_frame_activate()
  
    def dialy_collection_ipd(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_visit_default_frame_deactivate()
        
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_edit_frame_deactivate()
        self.main_page_frame_view3_patient_search_display_frame_deactivate()



        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         

        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

        self.main_page_frame_view3_physical_management_book_frame_deactivate()
        self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
        self.main_page_frame_view3_physical_management_room_status_frame_deactivate()

        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_activate()

    def dialy_collection_opd(self):
        self.main_page_frame_view3_home_frame_deactivate()
        self.main_page_frame_view3_patient_registration_default_frame_deactivate()
        self.main_page_frame_view3_patient_visit_default_frame_deactivate()
        
        self.main_page_frame_view3_patient_search_default_frame_deactivate()
        self.main_page_frame_view3_patient_search_edit_frame_deactivate()
        self.main_page_frame_view3_patient_search_display_frame_deactivate()



        self.main_page_frame_view3_patient_queue_default_frame_deactivate()
         
         

        
        self.main_page_frame_view3_lab_queue_default_frame_deactivate()
        self.main_page_frame_view3_search_lab_queue_frame_deactivate()
        self.main_page_frame_view3_view_lab_report_frame_deactivate()

        self.main_page_frame_view3_opd_queue_default_frame_deactivate()
        self.main_page_frame_view3_ipo_queue_default_frame_deactivate()

        self.main_page_frame_view3_physical_management_book_frame_deactivate()
        self.main_page_frame_view3_physical_management_Discharge_frame_deactivate()
        self.main_page_frame_view3_physical_management_room_status_frame_deactivate()
 
        self.main_page_frame_view3_dialy_collection_default_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_ipd_frame_deactivate()
        self.main_page_frame_view3_dialy_collection_dialy_collection_opd_frame_activate()

    
    #dialy_collection===============================================end==========================================


    #main_page_view2_and_view3=======================================end=======================================


        


    
           
             
    
    
        
        

  



x=main_window()
#x.loginge()
my = login_check.mydb
#my.close()

       
     
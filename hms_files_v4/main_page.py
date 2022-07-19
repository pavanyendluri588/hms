import tkinter as tk

"""

root1= tk.Tk()
root1.geometry('500x600')
#root1.columnconfigure(0,weight=10)
#root1.rowconfigure(0,weight=20)

"""

root1= tk.Tk()
frame_view1=tk.Frame(root1,bg='red')
frame_view1.pack(ipadx=770,ipady=20,side='top',fill='y')
frame_view1['borderwidth']=0
#frame_view1['relief']=''



frame_view2=tk.Frame(root1,bg='yellow')
frame_view2.pack(ipadx=70,ipady=100,side='left',fill='y')
frame_view2['borderwidth']=0



label1= tk.Button(frame_view2,text="destroy1")
label1.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
label11= tk.Button(frame_view2,text="destroy2")
label11.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
label12= tk.Button(frame_view2,text="destroy3")
label12.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
label13= tk.Button(frame_view2,text="destroy4")
label13.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
label14= tk.Button(frame_view2,text="destroy5")
label14.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
label15= tk.Button(frame_view2,text="destroy6")
label15.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
label16= tk.Button(frame_view2,text="destroy7")
label16.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
label17= tk.Button(frame_view2,text="destroy8")
label17.pack(padx=5,pady=3,ipadx=40,ipady=10,fill='x')
#side='top',


frame_view3=tk.Frame(root1,bg='blue')
frame_view3.pack(ipadx=550,ipady=100,side='top',fill='y')
frame_view3['borderwidth']=0

label2= tk.Label(frame_view3,text="frame_view3")
label2.pack(side='left')
label21= tk.Label(frame_view3,text="frame_view3")
label21.pack(side='bottom')
label22= tk.Label(frame_view3,text="frame_view3")
label22.pack(side='right')
label23= tk.Label(frame_view3,text="frame_view3")
label23.pack(side='top')


frame_view4=tk.Frame(root1,bg='green')
frame_view4['borderwidth']=0

label3= tk.Label(frame_view4,text="frame_view4")
label3.pack(side='left')
label31= tk.Label(frame_view4,text="frame_view4")
label31.pack(side='bottom')
label32= tk.Label(frame_view4,text="frame_view4")
label32.pack(side='right')
label33= tk.Label(frame_view4,text="frame_view4")
label33.pack(side='top')

def frames_status():

     print("frame_view1 status:",frame_view1)
     print("frame_view2 status:",frame_view2)
     print("frame_view3 status:",frame_view3)
     print("frame_view3 status:",frame_view3)

def destroy_frame_view3():
    global frame_view1,frame_view2,frame_view3,frame_view4
    #frame_view3.destroy()
    frame_view3 = None
    frames_status()
    frame_view4.pack(ipadx=670,ipady=250,side='top')

label1.config(command=destroy_frame_view3)
root1.mainloop()
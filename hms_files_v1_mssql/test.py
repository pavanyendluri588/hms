#main_page_frame_view3_physical_management_room_status_frame---------------start-------------
        self.main_page_frame_view3_physical_management_room_status_frame=tk.Frame(self.root1,bg='cyan')
        self.main_page_frame_view3_physical_management_room_status_frame['borderwidth']=0

        self.main_page_frame_view3_physical_management_room_status_mainheading1 = tk.Label(self.main_page_frame_view3_physical_management_room_status_frame,text="physical management",font=("lucida",15,"bold"),bg='blue')
        self.main_page_frame_view3_physical_management_room_status_mainheading1.place(x=5,y=5,width=1300,height=40)

        self.main_page_frame_view3_physical_management_room_status_book_room = tk.Button(self.main_page_frame_view3_physical_management_room_status_frame,text="Book Room")
        self.main_page_frame_view3_physical_management_room_status_book_room.place(x=20,y=50,width=100,height=30)
        self.main_page_frame_view3_physical_management_room_status_room_status_room = tk.Button(self.main_page_frame_view3_physical_management_room_status_frame,text="Empty Room")
        self.main_page_frame_view3_physical_management_room_status_room_status_room.place(x=130,y=50,width=100,height=30)
        self.main_page_frame_view3_physical_management_room_status_room_status = tk.Button(self.main_page_frame_view3_physical_management_room_status_frame,text="Room Status")
        self.main_page_frame_view3_physical_management_room_status_room_status.place(x=240,y=50,width=100,height=30)


        #main_page_frame_view3_physical_management_room_status_frame------------------end-------------
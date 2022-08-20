self.main_page_frame_view1_logout_image =Image.open("G:\hms_v1\hms_files_v3\main_page_home.jpeg")
        #G:\hms_v1\hms_files_v3\main_page_home.jpeg
        # Show image using label
        
        self.logout_resized_image= self.main_page_frame_view1_logout_image.resize((1300,770), Image.ANTIALIAS)
        self.logout_img=ImageTk.PhotoImage(self.logout_resized_image)

        self.logout_main_page_frame_view3_home_label = tk.Label( self.main_page_frame_view3_home_frame,)
        self.main_page_frame_view3_ = tk.Label( self.main_page_frame_view3_home_frame, image = self.my_img)
        self.main_page_frame_view3_home_label.place(x=0,y=0,width=1300,height=770)
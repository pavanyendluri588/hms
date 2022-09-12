self.patient_queue_send_to_OPD_refresh_image =Image.open("G:\hms_v1\hms_files_v5\refresh_img.png")
        #G:\hms_v1\hms_files_v3\main_page_home.jpeg
        # Show image using label
        
        self.patient_queue_send_to_OPD_refresh_resized_image= self.patient_queue_send_to_OPD_refresh_image.resize((40,32), Image.ANTIALIAS)
        self.patient_queue_send_to_OPD_refresh_img=ImageTk.PhotoImage(self.patient_queue_send_to_OPD_refresh_resized_image)
        self.patient_queue_send_to_OPD_button2_refresh=tk.Button(self.patient_queue_send_to_OPD, image = self.patient_queue_send_to_OPD_refresh_img)#,command= self.refresh_default
        self.patient_queue_send_to_OPD_button2_refresh.place(x=1480,y=5,width=40,height=32)
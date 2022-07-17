def physical_management_book_room_display(self): 
        self.avaliable_room_list = login_check.get_execution_result("select room_ID,room_floor, room_no,rooms_status from rooms_details where rooms_status = 'occupied'")
        #adding the values into contact list 
        self.physical_management_book_room_contacts = []
        for n in self.avaliable_room_list:
            self.physical_management_book_room_contacts.append((f'physical_management_book_room_first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview 
        for contact in self.physical_management_book_room_contacts:
            self.physical_management_book_room_default_tree.insert('', tk.END, values=contact)

        self.physical_management_book_room_default_tree.place(x=15,y=340,width=1150,height=400)
        #tree.grid(row=0, column=0, sticky='nsew')

        #ading the scroll baar 
        self.physical_management_book_room_scrollbar = ttk.Scrollbar(self.main_page_frame_view3_physical_management_book_room_default_frame, orient=tk.VERTICAL, command=self.physical_management_book_room_default_tree.yview)
        self.physical_management_book_room_default_tree.configure(yscroll=self.physical_management_book_room_scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        self.physical_management_book_room_scrollbar.place(x=1165, y=340,width=15,height=400)
        
        self.physical_management_book_room_selected = self.physical_management_book_room_default_tree.focus()
        print("self.physical_management_book_room_selected in display" + self.physical_management_book_room_selected)
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
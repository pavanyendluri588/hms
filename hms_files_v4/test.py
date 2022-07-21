self.patient_search_treeview_select_responce = self.patient_search_default_tree.focus()
         print("patient_search_treeview_selected :",self.patient_search_treeview_select_responce)
         self.patient_search_treeview_selected1 = self.patient_search_default_tree.item(self.patient_search_treeview_select_responce)
         print("values are ",self.patient_search_treeview_selected1['values'])
         self.patient_search_treeview_selected=self.patient_search_treeview_selected1['values']
         print("self.patient_search_treeview_selected type:",type(self.patient_search_treeview_selected))
         
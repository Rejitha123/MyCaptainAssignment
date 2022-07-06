#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["NAME","AGE","PHONE NUMBER","EMail ID"])
        writer.writerow(info_list)

if __name__=='__main__':
    condition =True
    student_num=1
    
    while(condition):
        student_info=input("Enter student information for student #{} in the format(Name Age Contact_number Email_id): ".format(student_num))
        print("Entered information: " + student_info)
        #split
        student_info_list=student_info.split(' ')
        print("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail id: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        
        choice_check=input("Is the information correct?[yes/no]:")
        
        if choice_check=="yes":
            write_into_csv(student_info_list)
            
            condition_info=input("enter yes/n0 if you want to enter more information")
            if condition_info=="yes":
                condition=True
                student_num=student_num+1
            elif condition_info=="no":
                condition=False
        elif choice_check=="no":
            print("\nKindly re-enter the values!")


# In[ ]:





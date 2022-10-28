from tkinter import *
import tkinter
import pymysql
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
windo = tkinter.Tk()
windo.geometry("1000x800")
windo.config(bg="gray")
windo.title('Online Addmission form')

L =Label(windo, text = "First Name: ",font =('arial',30),fg='blue',bg="gray")
L.grid(row=2,column=0)
E=Entry(windo, bd=5, width=50)
E.grid(row=2, column=1)

L1 =Label(windo, text = "last Name: ",font =('arial',30),fg='blue',bg="gray")
L1.grid(row=3,column=0)
E1=Entry(windo, bd=5, width=50)
E1.grid(row=3, column=1)

L2 =Label(windo, text = "Date of Birth: ",font =('arial',30),fg='blue',bg="gray")
L2.grid(row=4,column=0)
E2=Entry(windo, bd=5, width=50)
E2.grid(row=4, column=1)

L3 =Label(windo, text = "Email ID : ",font =('arial',30),fg='blue',bg="gray")
L3.grid(row=5,column=0)
E3=Entry(windo, bd=5, width=50)
E3.grid(row=5, column=1)

L4 =Label(windo, text = "Contact No : ",font =('arial',30),fg='blue',bg="gray")
L4.grid(row=6,column=0)
E4=Entry(windo, bd=5, width=50)
E4.grid(row=6, column=1)


L6 =Label(windo, text = "City : ",font =('arial',30),fg='blue',bg="gray")
L6.grid(row=7,column=0)
E6=Entry(windo, bd=5, width=50)
E6.grid(row=7, column=1)

L7 =Label(windo, text = "S.S.C : ",font =('arial',30),fg='blue',bg="gray")
L7.grid(row=12,column=0)
E7=Entry(windo, bd=5, width=50)
E7.grid(row=12, column=1)

L8 =Label(windo, text = "H.S.C: ",font =('arial',30),fg='blue',bg="gray")
L8.grid(row=13,column=0)
E8=Entry(windo, bd=5, width=50)
E8.grid(row=13, column=1)

L9 =Label(windo, text = "Student Information : ",font =('arial',30),fg='blue',bg="gray")
L9.grid(row=1,column=1)

L10 =Label(windo, text = "Acadamic Information :",font =('arial',30),fg='blue',bg="gray")
L10.grid(row=9,column=1)

L11 =Label(windo, text = "Courses :",font =('arial',30),fg='blue',bg="gray")
L11.grid(row=14,column=1)

L12 =Label(windo, text = "Branch : ",font =('arial',30),fg='blue',bg="gray")
L12.grid(row=15,column=0)
E12=Entry(windo, bd=5, width=50)
E12.grid(row=15, column=1)



def myButtonEvent(selection):
    print("First Name  : ",E.get())
    print("last Name : ",E1.get())
    print("Date of Birth : ",E2.get())
    print("Email ID : ",E3.get())
    print("Mobile No : ",E4.get())
    #print("Dist : ",E5.get())
    print("City : ",E6.get())
  
    
    firstname=E.get()
    lastname=E1.get()
    DOB=E2.get()
    Emailid=E3.get()
    Mobileno=E4.get()
    city=E.get()
    ssc=E.get()
    hsc=E.get()
    Studentinformation=E.get()
    Acadamicinformation=E.get()

    if selection in ('Insert'):    
   
            con = mysql.connector.connect(host="localhost",user="root",passwd="123",database="test")
            print(con)
            cur = con.cursor()
       

            insQuery="insert into std (id,name,address) values ('%s','%s','%s')"%(id,name,address)
            cur.execute(insQuery)
            con.commit()
    elif selection in ('Submit'):
           
            con = mysql.connector.connect(host="localhost",user="root",passwd="123",database="test")
            print(con)
            cur = con.cursor()
             
            query="update std set name ='%s'"%(name)+",address='%s'"%(address)+"where id ='%s'"%(id)
           
            cur.execute(query)
            con.commit()


    elif selection in ('Delete'):
           
            con = mysql.connector.connect(host="localhost",user="root",passwd="123",database="test")
            print(con)
            cur = con.cursor()
             
            query="delete from std where id ='%s'"%(id)
           
            cur.execute(query)
            con.commit()


    elif selection in ('Select'):
           
            con = mysql.connector.connect(host="localhost",user="root",passwd="123",database="test")
            print(con)
            cur = con.cursor()
             
            query="select * from std where id ='%s'"%(id)
           
            cur.execute(query)
            rows = cur.fetchall()
            address1 = ''
            name1 = ''
            id1 = ''
            for row in rows:
                id1 = row[0]
                name1 = row[1]
                address1 = row[2]
                E.delete(0,END)
                E1.delete(0,END)
                E2.delete(0,END)

                E.insert(0,id1)
                E1.insert(0,name1)
                E2.insert(0,address1)
           




BInsert = tkinter.Button(text='Insert',fg='Yellow',bg='black',font=('arial',20,'bold'),command=lambda:myButtonEvent('Insert'))
BInsert.grid(row=16,column=0)

BUpdate = tkinter.Button(text='Update',fg='Yellow',bg='black',font=('arial',20,'bold'),command=lambda:myButtonEvent('Update'))
BUpdate.grid(row=16,column=1)   
                                                         
BSelect = tkinter.Button(text='Select',fg='Yellow',bg='black',font=('arial',20,'bold'),command=lambda:myButtonEvent('Select'))
BSelect.grid(row=17,column=0)      
                                                      
BDelete = tkinter.Button(text='Delete',fg='Yellow',bg='black',font=('arial',20,'bold'),command=lambda:myButtonEvent('Delete'))
BDelete.grid(row=17,column=1)                                                            


windo.mainloop()




'''BStudant_Information = tkinter.Button(text='Studant_Information',fg='blue',bg='Yellow',font=('arial',20,'bold'),command=lambda:myButtonEvent('Studant_Information'))
BStudant_Information.grid(row=1,column=1)'''  
   

'''BSubmit = tkinter.Button(text='Submit',fg='blue',bg='Yellow',font=('arial',20,'bold'),command=lambda:myButtonEvent('Submit'))
BSubmit.grid(row=17,column=1)    '''                                                                

'''BAcadamic_Record = tkinter.Button(text='Acadamic_Record',fg='black',bg='orange',font=('arial',20,'bold'),command=lambda:myButtonEvent('Acadamic_Record'))
BAcadamic_Record.grid(row=10,column=1)'''

#  '%s','%s','%d','%s%d','%d','%s'
#  first name, last name, date of Birth, Email Id, Contact no,City
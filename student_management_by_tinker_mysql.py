
from cProfile import label
from cgitb import text
from tkinter import *
import mysql.connector as connector

con = connector.connect(user = "root", password = "12345", database = "student_tinker")
cursor= con.cursor()
window = Tk() # object of Tk class will create GUI window
window.geometry("700x700")
window.configure(background="powder blue")
window.title("Student Management")

def add_student():
         
        try:
            name1= name.get()
            rollnum1= roll_num.get()
            mark= marks.get()

            query = f"""insert into student (rollnum, name, marks) 
            values ({rollnum1},'{name1}',{mark})"""

            name.delete(0, END)
            roll_num.delete(0,END)
            marks.delete(0,END)

            cursor.execute(query)
            con.commit()
        
        except Exception as e:

            if con:
                con.rollback()
                print('There is some error', e)
        
        else:
            label1 = Label(window , text=f"User {name1} is registered successfully.", font=('time',15) , fg='red')
            label1.place(x=150 ,y=450)
            

        finally:

            if con:
                con.close()
            
            if cursor:
                cursor.close()
# def get_all_student(rollnum=None):

#     if rollnum == None:

#       query= "select * from student"

#       data= cursor.fetchall() 

#     elif rollnum == data[1]:



def list_of_students():

    show_window = Tk()
    show_window.geometry("900x900")
    show_window.configure(background="powder blue")
    show_window.title("Student Management System")

    main_label= Label(show_window, text= "List Of Student", font=("Arial Black", 20, "italic"),fg= "black", bg="powder blue")
    main_label.grid(row=0, column=0, padx=100, pady=20, ipadx=120, ipady=30, columnspan=5)
    
    name_label= Label(show_window, text= "Name", font=("Arial Black", 15),fg="black",bg="powder blue")
    name_label.grid(row=2, column=1)
    rollnum_label= Label(show_window, text= "Roll Number", font=("Arial Black", 15),fg="black",bg="powder blue")
    rollnum_label.grid(row=2, column=2)
    marks_label= Label(show_window, text= "Marks", font=("Arial Black", 15),fg="black",bg="powder blue")
    marks_label.grid(row=2, column=3)
    update_label= Label(show_window, text= "Update", font=("Arial Black", 15),fg="black",bg="powder blue")
    update_label.grid(row=2, column=4)
    delete_label= Label(show_window, text= "Delete", font=("Arial Black", 15),fg="black",bg="powder blue")
    delete_label.grid(row=2, column=5)
    try:        
        query = f"select * from student"
        cursor.execute(query)
        
        data = cursor.fetchall() 
        print(data)
        r=3
        for x in data: 
             e = Label(window,width=100, text=f"=> Student name is {x[1]} Student Roll number {x[0]} and Marks is {x[2]}",fg="black") 
             e.grid(row=r, column=0) 
             r= r+1
             
        #e.insert(END, student[j])
        
        
    except Exception as e:
        if con:
            con.rollback()
            print("There is some problem: " , e)
        
    finally:
        if con:
            con.close()
        if cursor:
            cursor.close()
               

main_label= Label( window, text="Student Managemt System",fg="blue", bg="yellow", font=("Arial Black",20,"bold"))
main_label.pack(fill=X)

label_1 = Label(window , text="Enter Student Name: " , font=("Arial Black" , 12))
label_1.place(x=50 , y=250)
name = Entry(window , width=20 , bd=5 , font=("Arial Black" , 15))
name.place(x=350 , y=250)

label_2 = Label(window , text="Enter Student Roll Number: " , font=("Arial Black" , 12))
label_2.place(x=50 , y=300)
roll_num= Entry(window , width=20 , bd=5 , font=("Arial Black" , 15))
roll_num.place(x=350 , y=300)

label_3 = Label(window , text="Enter Student Marks: " , font=("Arial Black" , 12))
label_3.place(x=50 , y=350)
marks = Entry(window , width=20 , bd=5 , font=("Arial Black" , 15))
marks.place(x=350 , y=350)


button = Button(window , text = "add student" , fg = "white" , bg = "black" ,
                width=20 , font=("time" , 15) , command=add_student)
button.place(x=100 , y=400 )

button1 = Button(window , text = "Show student" , fg = "white" , bg = "black" ,
                width=20 , font=("time" , 15) , command=list_of_students)
button1.place(x=390 , y=400 )



window.mainloop()






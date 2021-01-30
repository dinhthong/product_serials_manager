#!/usr/bin/python

# import Tkinter
# top = Tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()

#30Jan21 11h50 login to database url: https://www.geeksforgeeks.org/create-mysql-database-login-page-in-python-using-tkinter/
import Tkinter as tk
import mysql.connector 
from Tkinter import *
#from Tkinter import ttk
  
table_name ="main"
def descb_table():
    # A Table in the database
    show_table_query = "DESCRIBE " +table_name

    try:
        cursor.execute(show_table_query)
        myresult = cursor.fetchall()
         
        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Excecuted successfully")
         
    except:
        db.rollback()
        print("Error occured")
  
def show_table():
    print("*Show table's content:")
    select_movies_query = "SELECT * FROM "+table_name+" LIMIT 10"

    try:
        cursor.execute(select_movies_query)
        myresult = cursor.fetchall()
        
        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Excecuted successfully")
         
    except:
        db.rollback()
        print("Error occured")
    # #print(select_movies_query)
    # with conn.cursor() as cursor:
    #     cursor.execute(select_movies_query)
    #     result = cursor.fetchall()
    #     for row in result:
    #         print(row)


 
def submitact():
    user = Username.get()
    passw = password.get()
 #   print(f"The name entered by you is {user} {passw}")
    logintodb(user, passw)
    

def logintodb(user, passw):
    global db
    global cursor
    # If paswword is enetered by the 
    # user
    if passw:
        db = mysql.connector.connect(host='127.0.0.1', #host ="localhost",
                                     user = user,
                                     password = passw,
                                     db ="m3_knan")
         
    # If no password is enetered by the
    # user
    else:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     db ="m3_knan")
    cursor = db.cursor()
    

root = tk.Tk()
root.geometry("500x500")
root.title("DINH THONG EXPERIMENT")
  
# Definging the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login", 
                      bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 100, width = 55)
 
descbButton = tk.Button(root, text ="descb", 
                      bg ='blue', command = descb_table)
descbButton.place(x = 10, y = 150, width = 55)

showButton = tk.Button(root, text ="SHOW", 
                      bg ='blue', command = show_table)
showButton.place(x = 100, y = 150, width = 55)

root.mainloop()
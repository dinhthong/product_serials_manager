#youtube link: https://www.youtube.com/watch?v=i4qLI9lmkqw&ab_channel=CodeWorked
# Work with Tkinter Treeview Table with Search Feature | All Together in 1 Video | Worth Watching
from Tkinter import *
import Tkinter as tk
import Tkinter
import tkMessageBox
import ttk
import mysql.connector

table_name ="main"
displayed_columns="id, device, pcb_main, c_oled"
def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i )


def search():
    q2 = q.get()
    query = "SELECT "+displayed_columns+" FROM "+table_name+" WHERE device LIKE '%"+q2+"%' OR pcb_main LIKE '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

mydb = mysql.connector.connect(host="localhost", user="root", passwd="cxzzxcCC", database="m3_knan", auth_plugin="mysql_native_password")
cursor = mydb.cursor() 

root = Tk()
q=StringVar()

wrapper1 = LabelFrame(root, text="Customer List")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame (root, text="Customer Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv=ttk.Treeview(wrapper1, column=(1,2,3,4), show="headings", height="6")
trv.pack() 

trv.heading(1, text="Customer ID")
trv.heading(2, text="First Name")
trv.heading(3, text="Last Name")
trv.heading(4, text="Age") 
#query = "SELECT id, first_name, last_name, age from "+table_name\
query = "SELECT "+displayed_columns+" from "+table_name
cursor.execute(query)
rows = cursor.fetchall()
update(rows) 

#Search selection
lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6) 



root.title("My Application")
root.geometry("800x700")
root.mainloop()


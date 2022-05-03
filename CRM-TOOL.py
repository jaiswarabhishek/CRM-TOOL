from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root = Tk()
#Code for Title of screen and Icon of screen
root.title('CRM TOOL')

image_icon=PhotoImage(file="crm.png")
root.iconphoto(False,image_icon)
# Dimension of Screen
root.geometry("1000x500")

def query_database():
    for record in my_tree.get_children():
        my_tree.delete(record)
    
    conn = sqlite3.connect('CUSTOMER.db')



# create a cursor instance
    c = conn.cursor()

    
    #rowid is the primary key which is assignd and set by sql
    c.execute("SELECT rowid,* FROM customers")
    records = c.fetchall()

    #Add data to the screen
    global count
    count = 0

    

    

    for record in records:
        
        if count % 2==0:
            
             my_tree.insert(parent='',index='end',iid=count,text='',values = (record[1],record[2],record[0],record[4],record[5],record[6],record[7]),tags= ('evenrow',))
        else:
            my_tree.insert(parent='',index='end',iid=count,text='',values = (record[1],record[2],record[0],record[4],record[5],record[6],record[7]),tags= ('oddrow',))
        count=count+1
    

    #commit changes
    conn.commit()
    #close Connection
    conn.close()


def search_records():
    search_record_entry = search_entry.get()
    for record in my_tree.get_children():
        my_tree.delete(record)
    conn = sqlite3.connect('CUSTOMER.db')



# create a cursor instance
    c = conn.cursor()

    
    #rowid is the primary key which is assignd and set by sql
    c.execute("SELECT rowid,* FROM customers WHERE last_name = ?",(search_record_entry,))
    records = c.fetchall()

    #Add data to the screen
    global count
    count = 0

    

    

    for record in records:
        
        if count % 2==0:
            
             my_tree.insert(parent='',index='end',iid=count,text='',values = (record[1],record[2],record[0],record[4],record[5],record[6],record[7]),tags= ('evenrow',))
        else:
            my_tree.insert(parent='',index='end',iid=count,text='',values = (record[1],record[2],record[0],record[4],record[5],record[6],record[7]),tags= ('oddrow',))
        count=count+1
    

    #commit changes
    conn.commit()
    #close Connection
    conn.close()

    
   
        
    

    search.destroy()
    

def lookup_records():
    global search_entry ,search
    search = Toplevel(root)
    search.title("Search Customer")
    search.geometry("300x300")
    image_icon=PhotoImage(file="crm.png")
    root.iconphoto(False,image_icon)

    #Create label Frame
    search_frame = LabelFrame(search,text = "Last Name")
    search_frame.pack(padx = 10,pady = 10)

    #Add entry Box
    
    search_entry = Entry(search_frame,font = ("Helvet",15))
    search_entry.pack(pady=20,padx = 20)

    #Add Button
    search_button = Button(search,text = "Search Records" ,command =search_records )
    search_button.pack(padx = 20, pady = 20)

    
    
    

#Add Menu
my_menu = Menu(root)
root.config(menu = my_menu)

#Search Menu
search_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label = "Search",menu=search_menu)

search_menu.add_command(label="Search",command = lookup_records)
search_menu.add_separator()
search_menu.add_command(label = "Reset",command = query_database)

#Add Data Into Table and connecting with database

#data = [ ["Abhishek","Jaiswar",1,"123 WGL","Mumbai","Maharashtra",12345],["Vijay","Gupta",2,"1T St.Road","Mumbai","Mahrashtra",123647],["Mohak","Singh",3,"321 WGL Krp.","Pune","Maharashtra",12365],["Aakash","Gupta",4,"111 PGL","Devas","MP",22345],["Anil","Yadav",5,"144 KGL","Jaunpur","UP",32345],["Anshuman","Pandey",6,"537 KKR","Gandhi Nagar","Delhi",22345],["Vinayak","Singh",7,"543 PKL","Chandani Chawk","Delhi",43256],["Mayur","Kumar",8,"113 HIV","Tithe Nagar","Goa",12145],["Sumedh","Gupta",9,"223 SSG","Machhli Sahar","Punjab",54345],["Govind","Gupta",10,"823 JHU","Dhule","Harayana",1215]] 

#Databse Stuff
#create A Database or connect to one that exists
conn = sqlite3.connect('CUSTOMER.db')



# create a cursor instance
c = conn.cursor()

#Create Table
c.execute(""" CREATE TABLE if not exists customers (
first_name text,
last_name text,
id integer,
address text,
city text,
state text,
pincode text
)
    """)

# Add the data to table
'''
for record in data:
	c.execute("INSERT INTO customers VALUES (:first_name, :last_name, :id, :address, :city, :state, :pincode)", 
		{
		'first_name': record[0],
		'last_name': record[1],
		'id': record[2],
		'address': record[3],
		'city': record[4],
		'state': record[5],
		'pincode': record[6]
		}
		)

'''
# commit changes
conn.commit()
#Close connection
conn.close()




#Add some Style
style=ttk.Style()

#Pick A theme
style.theme_use('default')

#Configure the Treeview colors

style.configure("Treeview",background="#D3D3D3",foreground="black",rowheight=25,fieldbackground="#D3D3D3")


#change selected color
style.map('Treeview',background=[('selected',"#347083")])

#Create A treeview frame
tree_frame=Frame(root)
tree_frame.pack(pady=10)

#create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

#Create The Treeview
my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
my_tree.pack()


#Configure The Scrollbar
tree_scroll.config(command=my_tree.yview)

#Define Columns using Tuple
my_tree['columns']=("First Name","Last Name","ID","Address","City","State","Pincode")

#Formate Our Columns this for columns stuff
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("First Name",anchor=W,width=140)
my_tree.column("Last Name",anchor=W,width=140)
my_tree.column("ID",anchor=CENTER,width=100)
my_tree.column("Address",anchor=CENTER,width=140)
my_tree.column("City",anchor=CENTER,width=140)
my_tree.column("State",anchor=CENTER,width=140)
my_tree.column("Pincode",anchor=CENTER,width=140)

#Create Headings
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("First Name",text="First Name",anchor=W)
my_tree.heading("Last Name",text="Last Name",anchor=W)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("Address",text="Address",anchor=CENTER)
my_tree.heading("City",text="City",anchor=CENTER)
my_tree.heading("State",text="State",anchor=CENTER)
my_tree.heading("Pincode",text="Pincode",anchor=CENTER)


#Create Striped Row Tags
my_tree.tag_configure('oddrow',background="#7c7cf0")
my_tree.tag_configure('evenrow',background="white")

'''#Add data to the screen
global count
count = 0

for record in data:
    if count % 2==0:
        my_tree.insert(parent='',index='end',iid=count,text='',values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags= ('evenrow',))
    else:
        my_tree.insert(parent='',index='end',iid=count,text='',values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags= ('oddrow',))
    count=count+1
'''

#Add Record Entry Boxes

data_frame = LabelFrame(root, text= "Record")
data_frame.pack(fill='x',expand="yes",padx=20)

fn_label = Label(data_frame,text="First Name ")
fn_label.grid(row=0,column=0,padx=10,pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0,column=1,padx=10,pady=10)

ln_label = Label(data_frame,text="Last Name ")
ln_label.grid(row=0,column=2,padx=10,pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0,column=3,padx=10,pady=10)

id_label = Label(data_frame,text="ID")
id_label.grid(row=0,column=4,padx=10,pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0,column=5,padx=10,pady=10)

address_label = Label(data_frame,text="Address")
address_label.grid(row=1,column=0,padx=10,pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1,column=1,padx=10,pady=10)

city_label = Label(data_frame,text="City")
city_label.grid(row=1,column=2,padx=10,pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1,column=3,padx=10,pady=10)

state_label = Label(data_frame,text="State")
state_label.grid(row=1,column=4,padx=10,pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1,column=5,padx=10,pady=10)

pincode_label = Label(data_frame,text="Pincode")
pincode_label.grid(row=1,column=6,padx=10,pady=10)
pincode_entry = Entry(data_frame)
pincode_entry.grid(row=1,column=7,padx=10,pady=10)

# Move Row Up

def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)-1)

# Move Row Down

def down():
    rows=my_tree.selection()
    for row in rows:
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)+1)

        
#clear Entries Function
def clear_entries():
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    pincode_entry.delete(0,END)

# Remove One Selected Row Record data

def selected_one_row_record():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    #Let's Delete the record from database

    #connect to the database
    conn = sqlite3.connect("CUSTOMER.db")
    #Creating Cursor
    c = conn.cursor()

    c.execute( " DELETE FROM customers WHERE oid=" + id_entry.get())


    #commit the changes

    conn.commit()

    #close
    conn.close()
        #Clear Entry Boxes
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    pincode_entry.delete(0,END)

    #show messagebox to delete the record

    messagebox.showinfo("Deleted","Rocord has been deleted!")

# Remove Many Selected Row Record data

def selected_many_row_record():
    x = my_tree.selection()
    delete_many=[]
    for record in x:
        delete_many.append(my_tree.item(record,'values')[2])
        
        my_tree.delete(record)
    
    conn=sqlite3.connect("CUSTOMER.db")

    c=conn.cursor()

    c.executemany(" DELETE FROM customers WHERE oid= ?",[(a,) for a in delete_many])

    conn.commit()
    conn.close()

#Remove All Records
def remove_record():

    rensponse = messagebox.askyesno("Warning!!","Are you sure to delete all the records?")
    if rensponse ==1:
        for record in my_tree.get_children():
            my_tree.delete(record)

        conn = sqlite3.connect("CUSTOMER.db")

        c = conn.cursor()

        c.execute("""DROP TABLE customers""")

        conn.commit()
        conn.close()

    

#Update Record
def update_record():
    #Take the record number
    selected = my_tree.focus()
    my_tree.item(selected,text="",values=(fn_entry.get(),ln_entry.get(),id_entry.get(),address_entry.get(),city_entry.get(),state_entry.get(),pincode_entry.get(),))

    
    #update the data into Database
    conn = sqlite3.connect('CUSTOMER.db')



# create a cursor instance
    c = conn.cursor()

    
    #rowid is the primary key which is assignd and set by sql
    c.execute("""UPDATE customers SET

              first_name=:first,
              last_name=:last,
              address=:address,
              city=:city,
              state=:state,
              pincode=:pincode

              WHERE oid=:oid

              """,
              

              {
                  'first':fn_entry.get(),
                  'last':ln_entry.get(),
                  'address':address_entry.get(),
                  'city':city_entry.get(),
                  'state':state_entry.get(),
                  'pincode':pincode_entry.get(),
                  'oid':id_entry.get()
                  

               }
              )

    #commit changes
    conn.commit()
    #close Connection
    conn.close()

    #Clear Entry Boxes
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    pincode_entry.delete(0,END)

# Add Record

def add_record():
    
    #Connect to the database
    conn= sqlite3.connect("CUSTOMER.db")
    #Create A cursor
    c = conn.cursor()

    #Let's add the data into the table

    c.execute("""INSERT INTO customers VALUES(:first,:last,:id,:address,:city,:state,:pincode)""",


              {
                  'first':fn_entry.get(),
                  'last':ln_entry.get(),
                  'id':id_entry.get(),
                  'address':address_entry.get(),
                  'city':city_entry.get(),
                  'state':state_entry.get(),
                  'pincode':pincode_entry.get(),
                  
               }

             )


    #commit
    conn.commit()
    #close
    conn.close()
    #Clear Entry Boxes
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    pincode_entry.delete(0,END)
   #clear the treeview screen
    my_tree.delete(*my_tree.get_children())
    query_database()

# Select Record Function
def select_record(e):
    #Clear Entry Boxes
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    pincode_entry.delete(0,END)

    #Take The Record Number
    selected = my_tree.focus()

    # Take The Record Values
    values = my_tree.item(selected,'values')

    #output to entry boxes
    fn_entry.insert(0,values[0])
    ln_entry.insert(0,values[1])
    id_entry.insert(0,values[2])
    address_entry.insert(0,values[3])
    city_entry.insert(0,values[4])
    state_entry.insert(0,values[5])
    pincode_entry.insert(0,values[6])



    

#Add Some Buttons

button_frame = LabelFrame(root, text= "Command")
button_frame.pack(fill='x',expand="yes",padx=20)

update_record=Button(button_frame,text="Upadate Record",bg='#7c7cf0',fg='white',bd=1,borderwidth=3,command=update_record)
update_record.grid(row=1,column=1,padx=10,pady=10)

add_record=Button(button_frame,text="Add Record",bg='#7c7cf0',fg='white',bd=1,borderwidth=3,command=add_record)
add_record.grid(row=1,column=2,padx=10,pady=10)


remove_all_records=Button(button_frame,text="Remove All Records",fg='white',bg='#7c7cf0',bd=1,borderwidth=3,command=remove_record)
remove_all_records.grid(row=1,column=3,padx=10,pady=10)

remove_one_selected=Button(button_frame,text="Remove One Selected",fg='white', bg='#7c7cf0',bd=1,borderwidth=3,command=selected_one_row_record)
remove_one_selected.grid(row=1,column=4,padx=10,pady=10)

remove_many_selected=Button(button_frame,text="Remove Many Selected",fg='white',bg='#7c7cf0',bd=1,borderwidth=3,command=selected_many_row_record)
remove_many_selected.grid(row=1,column=5,padx=10,pady=10)

move_up=Button(button_frame,text="Move Up" ,bg='#7c7cf0',fg='white',bd=1,borderwidth=3, command=up)
move_up.grid(row=1,column=6,padx=10,pady=10)

move_down=Button(button_frame,text="Move Down",bg='#7c7cf0',fg='white',bd=1,borderwidth=3,command=down)
move_down.grid(row=1,column=7,padx=10,pady=10)

Clear_record_button=Button(button_frame,text="Clear Entry",bg='#7c7cf0',fg='white',bd=1,borderwidth=3,command=clear_entries)
Clear_record_button.grid(row=1,column=8,padx=10,pady=10)


#Bind The TreeView When click and release the button the function fire

my_tree.bind("<ButtonRelease-1>",select_record)
query_database()

root.mainloop()

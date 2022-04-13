from tkinter import *
from tkinter import ttk

root = Tk()
#Code for Title of screen and Icon of screen
root.title('CRM TOOL')
image_icon=PhotoImage(file="crm.png")
root.iconphoto(False,image_icon)
# Dimension of Screen
root.geometry("1000x500")

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
my_tree['columns']=("First Name","Last Name","ID","Address","City","State","Zipcode")

#Formate Our Columns this for columns stuff
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("First Name",anchor=W,width=140)
my_tree.column("Last Name",anchor=W,width=140)
my_tree.column("ID",anchor=CENTER,width=100)
my_tree.column("Address",anchor=CENTER,width=140)
my_tree.column("City",anchor=CENTER,width=140)
my_tree.column("State",anchor=CENTER,width=140)
my_tree.column("Zipcode",anchor=CENTER,width=140)

#Create Headings
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("First Name",text="First Name",anchor=W)
my_tree.heading("Last Name",text="Last Name",anchor=W)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("Address",text="Address",anchor=CENTER)
my_tree.heading("City",text="City",anchor=CENTER)
my_tree.heading("State",text="State",anchor=CENTER)
my_tree.heading("Zipcode",text="Zipcode",anchor=CENTER)

#Add Data Into Table and connecting with database

data = [ ["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345],["Abhishek","Jaiswar",1,"123 WGL","Mumbai","UP",12345]] 

#Create Striped Row Tags
my_tree.tag_configure('oddrow',background="white")
my_tree.tag_configure('evenrow',background="lightblue")

#Add data to the screen
global count
count = 0

for record in data:
    if count % 2==0:
        my_tree.insert(parent='',index='end',iid=count,text='',values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags= ('evenrow',))
    else:
        my_tree.insert(parent='',index='end',iid=count,text='',values = (record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags= ('oddrow',))
    count=count+1

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

zipcode_label = Label(data_frame,text="Zipcode")
zipcode_label.grid(row=1,column=6,padx=10,pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1,column=7,padx=10,pady=10)

#Add Some Buttons

button_frame = LabelFrame(root, text= "Command")
button_frame.pack(fill='x',expand="yes",padx=20)

update_record=Button(button_frame,text="Upadate Record")
update_record.grid(row=1,column=1,padx=10,pady=10)

add_record=Button(button_frame,text="Add Record")
add_record.grid(row=1,column=2,padx=10,pady=10)


remove_all_records=Button(button_frame,text="Remove All Records")
remove_all_records.grid(row=1,column=3,padx=10,pady=10)

remove_one_selected=Button(button_frame,text="Remove One Selected")
remove_one_selected.grid(row=1,column=4,padx=10,pady=10)

remove_many_selected=Button(button_frame,text="Remove Many Selected")
remove_many_selected.grid(row=1,column=5,padx=10,pady=10)

move_up=Button(button_frame,text="Move Up")
move_up.grid(row=1,column=6,padx=10,pady=10)

move_down=Button(button_frame,text="Move Down")
move_down.grid(row=1,column=7,padx=10,pady=10)

select_record=Button(button_frame,text="Select Record")
select_record.grid(row=1,column=8,padx=10,pady=10)




root.mainloop()

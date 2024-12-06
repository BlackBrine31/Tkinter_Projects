import tkinter as tk 
import random
import tkinter.messagebox
root=tk.Tk()
root.title("To-Do List")
root.config(bg="white")
root.geometry("500x275")
tasks=[]
label_title=tk.Label(root, text="To-Do List", bg="white")
label_title.grid(row=0,column=0)
lbl_display=tk.Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1)
txt_input=tk.Entry(root, width=15)
txt_input.grid(row=1,column=1)
global number_of_task
number_of_task=len(tasks)
def update_listbox():
    clear_listbox()
    for task in tasks:
        listbox_task.insert("end",task)
def clear_listbox():
    listbox_task.delete(0,"end")
def add_task():
    task=txt_input.get()
    if task!="":
        tasks.append(task)
        update_listbox()
    else:
        tk.messagebox.showwarning(title="Warning",message="You must enter a task")
    txt_input.delete(0,"end")
def delete_all():
    if number_of_task==0:
        tk.messagebox.showwarning(title="Warning",message="There is no task to delete!")
    else:
         confirmed=tk.messagebox.askyesno("Please Confirm","do you really want to delete all?")
    try:
        if confirmed==True:
            global tasks
            tasks=[]
            update_listbox()
        else:
            tk.messagebox.showwarning(title="Approved",message="Ok I wont delete all of them")
    except:
        pass
def delete_one():
    task=listbox_task.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()
def sort_asc():
    tasks.sort()
    update_listbox()
def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()
def choose_random():
    try:
       task=random.choice(tasks)
       lbl_display["text"]=task
    except:
        tk.messagebox.showwarning(title="Warning",message="Cannot choose from an empty sequence")
def number_of_tasks():
    global number_of_task
    number_of_task=len(tasks)
    msg="Number of tasks: %s"%number_of_task
    lbl_display["text"]=msg
def exit_button():
    root.destroy()
listbox_task=tk.Listbox(root)
listbox_task.grid(row=2,column=1,rowspan=7)
button_add_task=tk.Button(root, text="Add Task",width=48,bg="white",fg="green",command=add_task)
button_add_task.grid(row=1,column=0)

button_del_all=tk.Button(root, text="Delete All Task",width=48,bg="white",fg="green",command=delete_all)
button_del_all.grid(row=2,column=0)

button_del_one=tk.Button(root, text="Delete One Task",width=48,bg="white",fg="green",command=delete_one)
button_del_one.grid(row=3,column=0)

button_sort_asc=tk.Button(root, text="Sort(ASC)",width=48,bg="white",fg="green",command=sort_asc)
button_sort_asc.grid(row=4,column=0)

button_sort_desc=tk.Button(root, text="Sort(DESC)",width=48,bg="white",fg="green",command=sort_desc)
button_sort_desc.grid(row=5,column=0)

button_choose_random=tk.Button(root, text="Choose Random",width=48,bg="white",fg="green",command=choose_random)
button_choose_random.grid(row=6,column=0)

button_number_of_tasks=tk.Button(root, text="Number Of Tasks",width=48,bg="white",fg="green",command=number_of_tasks)
button_number_of_tasks.grid(row=7,column=0)

button_exit=tk.Button(root, text="Exit",width=48,bg="white",fg="green",command=exit_button)
button_exit.grid(row=8,column=0)
root.mainloop()
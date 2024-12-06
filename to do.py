import tkinter as tk 
import tkinter.messagebox
import pickle
root=tk.Tk()
root.title("To-Do List")
def add_task():
    task=entry.get()
    if task!="":
        listbox_task.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        tk.messagebox.showwarning(title="Warning",message="You must enter a task")
def delete_task():
    try:
        task_index=listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tk.messagebox.showwarning(title="Warning",message="You must select a task")
def save_task():
    tasks=listbox_task.get(0,listbox_task.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
def load_task():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listbox_task.delete(0,tk.END)
        for task in tasks:
            listbox_task.insert(tk.END, task)
    except:
        tk.messagebox.showwarning(title="Warning",message="Cannot find tasks.dat")
frame=tk.Frame(root)
frame.pack()
listbox_task=tk.Listbox(frame, height=10, width=50)
listbox_task.pack(side=tk.LEFT)
scrollbar=tk.Scrollbar(frame)
listbox_task.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_task)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
entry=tk.Entry(root, width=50)
entry.pack()
button_add_task=tk.Button(root, text="Add Task",width=48,command=add_task)
button_add_task.pack()
button_delete_task=tk.Button(root, text="Delete Task",width=48,command=delete_task)
button_delete_task.pack()
button_save_task=tk.Button(root, text="Save Task",width=48,command=save_task)
button_save_task.pack()
button_load_task=tk.Button(root, text="Load Task",width=48,command=load_task)
button_load_task.pack()
root.mainloop()
import tkinter as tk 

root=tk.Tk()
root.title("caclulator")
root.configure(background="purple")
global operator
def button_work(number):
    evvelki_reqem=entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(evvelki_reqem)+str(number))
def button_clear(): 
    entry.delete(0, tk.END)
def button_ustegel(): 
    global operator 
    global num1 
    operator="ustegel"
    num1=int(entry.get())
    entry.delete(0, tk.END)
def button_cixma(): 
    global operator 
    global num1 
    operator="cixma"
    num1=int(entry.get())
    entry.delete(0, tk.END)
def button_vurma(): 
    global operator 
    global num1 
    operator="vurma"
    num1=int(entry.get())
    entry.delete(0, tk.END)
def button_bolme(): 
    global operator 
    global num1 
    operator="bolme"
    num1=int(entry.get())
    entry.delete(0, tk.END)
def beraber():
    global operator 
    global num1
    global num2
    num2=int(entry.get())
    entry.delete(0, tk.END)
    if operator=="ustegel": 
        entry.insert(0, num1+num2)
    if operator=="cixma":
        entry.insert(0, num1-num2)
    if operator=="vurma":
        entry.insert(0, num1*num2)
    if operator=="bolme":
        try:
            entry.insert(0, num1/num2)
        except:
            entry.insert(0, "ZeroDivisionError")
entry=tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
button_1=tk.Button(root, text="1", padx=40, pady=20, command= lambda: button_work(1))
button_2=tk.Button(root, text="2", padx=40, pady=20, command= lambda: button_work(2))
button_3=tk.Button(root, text="3", padx=40, pady=20, command= lambda: button_work(3))
button_4=tk.Button(root, text="4", padx=40, pady=20, command= lambda: button_work(4))
button_5=tk.Button(root, text="5", padx=40, pady=20, command= lambda: button_work(5))
button_6=tk.Button(root, text="6", padx=40, pady=20, command= lambda: button_work(6))
button_7=tk.Button(root, text="7", padx=40, pady=20, command= lambda: button_work(7))
button_8=tk.Button(root, text="8", padx=40, pady=20, command= lambda: button_work(8))
button_9=tk.Button(root, text="9", padx=40, pady=20, command= lambda: button_work(9))
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_ustegel=tk.Button(root, text="+", padx=40, pady=20, command=button_ustegel)
button_0=tk.Button(root, text="0", padx=40, pady=20, command= lambda: button_work(0))
button_beraber=tk.Button(root, text="=", padx=40, pady=20, command=beraber)
button_cixma=tk.Button(root, text="-", padx=40, pady=20,command=button_cixma)
button_vurma=tk.Button(root, text="*", padx=40, pady=20,command=button_vurma)
button_bolme=tk.Button(root, text="/", padx=40, pady=20,command=button_bolme)
button_clear=tk.Button(root, text="Clear", padx=130, pady=10, command=button_clear)
button_0.grid(row=4, column=1)
button_ustegel.grid(row=4, column=0)
button_beraber.grid(row=4, column=2)
button_cixma.grid(row=5, column=1)
button_vurma.grid(row=5, column=0)
button_bolme.grid(row=5, column=2)
button_clear.grid(row=6,column=0, columnspan=3)
root.mainloop()
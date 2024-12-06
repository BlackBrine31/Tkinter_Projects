import tkinter as tk 

root= tk.Tk()
root.title("Convertor")
def convert_selsi():
    farengeyt=entry1.get()
    selsi=round((5/9)*(float(farengeyt)-32),3)
    t1.delete("1.0",tk.END)
    t1.insert(tk.END, selsi)
label1=tk.Label(root, text="FARENGEYT DAXIL EDIN: ")
entry1=tk.Entry(root, width=35)
label2=tk.Label(root, text="SELSI")

t1=tk.Text(root, height=1, width =20)
button1=tk.Button(root, text="convert",command=convert_selsi)

label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
button1.grid(row=0, column=2)
label2.grid(row=1, column=0)
t1.grid(row=2, column=0)

root.mainloop()

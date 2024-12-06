import tkinter as tk
from tkinter import messagebox 
questions=[("What is capital city of UK?", "Paris", "London", "Copenhagen", "Brussels", "B"),
          ("What is capital city of France?", "Paris", "London", "Copenhagen", "Brussels", "A"),
          ("What is capital city of Belgium?", "Paris", "London", "Copenhagen", "Brussels", "D"),
          ("What is capital city of Denmark?", "Paris", "London", "Copenhagen", "Brussels", "C")
     ]
current_question=0
score=0
def check_answer(button):
    global current_question, score
    if button == questions[current_question][5]:
        score+=1
        score_label.configure(text=f" Your score: {score}/{len(questions)}")
        messagebox.showinfo("Correct", "You chose correct answer ")
    else: 
        messagebox.showinfo("Wrong", "You chose wrong answer ")
        root.destroy()
    current_question+=1
    if current_question<len(questions):
        display_question(current_question)
    else: 
        messagebox.showinfo("END", f"Game Over! Your score is {score}/{len(questions)}")
        root.destroy()
def display_question(index):
    question, a,b,c,d, ca=questions[index]
    question_label.config(text=question)
    button_a.config(text="A) "+a)
    button_b.config(text="B) "+b)
    button_c.config(text="C) "+c)
    button_d.config(text="D) "+d)   
root=tk.Tk()
root.title("Who Wants to Be Millionaire?")
root.config(bg="black")
score_label=tk.Label(root,text=f" Your score: {score}/{len(questions)}")
score_label.pack(padx=(500,10))
question_label=tk.Label(root, text="", width=50, height=3,bg="dark blue")
question_label.pack(pady=(20,10))

button_a=tk.Button(root, text="", command=lambda: check_answer("A"), width=50,bg="green")
button_a.pack()

button_b=tk.Button(root, text="", command=lambda: check_answer("B"), width=50,bg="green")
button_b.pack()

button_c=tk.Button(root, text="", command=lambda: check_answer("C"), width=50,bg="green")
button_c.pack()

button_d=tk.Button(root, text="", command=lambda: check_answer("D"), width=50,bg="green")
button_d.pack()

display_question(current_question)

root.mainloop()

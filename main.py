from tkinter import *
import random
import pyperclip

def generator():
    small="abcdefghijklmnopqrstuvwxyz"
    caps="ABCDEFGHIJKLMNOPQRTSUVWXYZ"
    nums="1234567890"
    specs="!@#$%^&*()_-+=><,.?|/\}{[]"
    strong = small+caps+nums+specs
    medium=small+caps+nums
    weak=small+caps
    pwlength=int(length_box.get())
    
    if choice.get()==1:
        passwordarea.delete(0, END)
        passwordarea.insert(0, ''.join(random.sample(weak,pwlength)))  
    elif choice.get()==2:
        passwordarea.delete(0, END)
        passwordarea.insert(0, ''.join(random.sample(medium,pwlength)))
    elif choice.get()==3:
        passwordarea.delete(0, END)
        passwordarea.insert(0, ''.join(random.sample(strong,pwlength)))
    
def copy():
    rand_password=passwordarea.get()
    pyperclip.copy(rand_password)

def reset():
    passwordarea.delete(0, END)
    length_box.delete(0, END)
    length_box.insert(0, "5")  
    choice.set(1)  

root=Tk()
root.config(bg="cadetblue2")
root.title("Password Generator")

choice=IntVar()
Font=('arial',13,"bold")
passlabel = Label(root,text="Password Generator", font=("Arial",20,"bold"),bg="cadetblue",fg="black")
passlabel.grid(pady=7)

passStrength = Label(root,text="Password Strength", font=("Arial",15,"bold"),bg="cadetblue",fg="black")
passStrength.grid(pady=5)

weak_rd_button = Radiobutton(root,text="Weak",value=1, variable=choice, font=Font)
weak_rd_button.grid(pady=5)
choice.set(1)

med_rd_button = Radiobutton(root,text="Medium",value=2, variable=choice, font=Font)
med_rd_button.grid(pady=5)

str_rd_button = Radiobutton(root,text="Strong",value=3, variable=choice, font=Font)
str_rd_button.grid(pady=5)

passlength = Label(root,text="Password Length", font=("Arial",15,"bold"),bg="cadetblue",fg="black")
passlength.grid(pady=5)

length_box = Spinbox(root,from_=5, to_=20, width=5, font=Font) 
length_box.grid(pady=5)


generatebutton=Button(root,text="Generate", font=Font, command=generator)
generatebutton.grid(pady=5)

passwordarea=Entry(root,width=25,bd=2,font=Font)
passwordarea.grid(pady=5)

copybutton=Button(root,text="Copy", font=Font, command=copy)
copybutton.grid(pady=5)

resetbutton=Button(root,text="Reset", font=Font, command=reset)
resetbutton.grid(pady=5)

root.mainloop()

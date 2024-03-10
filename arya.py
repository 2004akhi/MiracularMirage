# -- coding: utf-8 --
"""
Created on Sun Mar 10 09:18:14 2024

@author: Arya.V
"""

import tkinter as tk
from tkinter import *
root=tk.Tk()
root.title("to do list app")

root.configure(bg="lightpink")
label=tk.Label(root,text="MY TO DO LIST",font=('Algerian',18))
label.pack(padx=20,pady=20)
 
label=tk.Label(root,text="enter 1st category of task",font=('Monotype Corsiva',14))
label.pack(padx=20,pady=10)
myentry=tk.Entry(root)
myentry.pack()

label=tk.Label(root,text="enter task set 1",font=('Monotype Corsiva',14))
label.pack(padx=10,pady=20)
listbox=tk.Text(root,height=4,font=('Ariel',12))
listbox.pack(padx=10,pady=10)

root.geometry("400x600") 

Checkbutton1 = IntVar()   

Checkbutton2 = IntVar()   

Checkbutton3 = IntVar() 


Button1 = Checkbutton(root, text="TASK 1",

                      variable = Checkbutton1, 

                      onvalue = 1, 

                      offvalue = 0, 

                      height = 2,
                      
                      width=10,
                      
                      selectcolor="skyblue")


Button2 = Checkbutton(root, text="TASK 2",
                      
                      variable = Checkbutton2, 

                      onvalue = 1, 

                      offvalue = 0, 

                      height = 2,
                      
                      width=10,
                      
                      selectcolor="pink")

Button3 = Checkbutton(root, text = "TASK 3",  

                      variable = Checkbutton3, 

                      onvalue = 1, 

                      offvalue = 0, 

                      height = 2,
                      
                      width=10,
                      
                      selectcolor="lightgreen"
                      )
Button1.pack()   
Button2.pack()   
Button3.pack() 



#TASK SET 2
label=tk.Label(root,text="enter 2nd category of task",font=('Monotype Corsiva',14))
label.pack(padx=20,pady=10)
myentry=tk.Entry(root)
myentry.pack()

label=tk.Label(root,text="enter task set 2",font=('Monotype Corsiva',14))
label.pack(padx=10,pady=20)
listbox=tk.Text(root,height=4,font=('Arial',12))
listbox.pack(padx=10,pady=10)

root.geometry("400x600") 

Checkbutton4 = IntVar()   

Checkbutton5 = IntVar()   

Checkbutton6 = IntVar() 


Button4 = Checkbutton(root, text="TASK 1",

                      variable = Checkbutton4, 

                      onvalue = 1, 

                      offvalue = 0, 

                      height = 2,
                      
                      width=10,
                      
                      selectcolor="skyblue")


Button5 = Checkbutton(root, text="TASK 2",
                      
                      variable = Checkbutton5, 

                      onvalue = 1, 

                      offvalue = 0, 

                      height = 2,
                      
                      width=10,
                      
                      selectcolor="pink")

Button6 = Checkbutton(root, text = "TASK 3",  

                      variable = Checkbutton6, 

                      onvalue = 1, 

                      offvalue = 0, 

                      height = 2,
                      
                      width=10,
                      
                      selectcolor="lightgreen"
                      )
Button4.pack()   
Button5.pack()   
Button6.pack() 


#TASK SET 3
label=tk.Label(root,text="enter 3rd category of task",font=('Monotype Corsiva',14))
label.pack(padx=20,pady=10)
myentry=tk.Entry(root)
myentry.pack()

label=tk.Label(root,text="enter task set 3",font=('Monotype Corsiva',14))
label.pack(padx=10,pady=20)
listbox=tk.Text(root,height=4,font=('Ariel',10))
listbox.pack(padx=10,pady=10)

root.geometry("400x600") 

Checkbutton7 = IntVar()   

Checkbutton8 = IntVar()   

Checkbutton9 = IntVar() 


Button7 = Checkbutton(root, text="TASK 1",

                      variable = Checkbutton7, 

                      onvalue = 1, 

                      offvalue = 0, 

                      height = 2,
                      
                      width=10,
                      
                      selectcolor="skyblue")


Button8 = Checkbutton(root, text="TASK 2",
                      
                      variable = Checkbutton8, 

                      onvalue = 1, 

                      offvalue = 0, 

                      height = 2,
                      
                      width=10,
                      
                      selectcolor="pink")

Button9 = Checkbutton(root, text = "TASK 3",  

                      variable = Checkbutton9, 

                      onvalue = 1, 

                      offvalue = 0, 

                      height = 2,
                      
                      width=10,
                      
                      selectcolor="lightgreen"
                      )
Button7.pack()   
Button8.pack()   
Button9.pack() 

mainloop()


root.mainloop()
# Python Programme to create a replicate of CASIO fx-50 FH II

#import everything in tkinter module

from tkinter import *

root = Tk()
root.title("CASIO fx-50 FH II")

e = Entry(root, width=50, borderwidth=5)
e.grid (row=0, column =0, columnspan =5, padx=10, pady=10)
output = Text(root, height =2 ,width=65)
output.grid(row=1,column=0, columnspan =5, padx=10, pady=10)



def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_delete():
    e.delete(len(e.get())-1)

def button_clear():
    e.delete(0,END)

def button_exe():
    return


#Define the buttons

button_1 = Button(root, text="1", padx=40, pady=40, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=40, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=40, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=40, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=40, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=40, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=40, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=40, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=40, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=40, command=lambda: button_click(0))
button_dot = Button(root, text=".", padx=43, pady=40, command=lambda: button_click("."))
button_add = Button(root, text="+", padx=48, pady=40, command=lambda: button_click("+"))
button_deduct = Button(root, text="-", padx=44, pady=40, command=lambda: button_click("-"))
button_time = Button(root, text="×", padx=48, pady=40, command=lambda: button_click("×"))
button_divide = Button(root, text="÷", padx=44, pady=40, command=lambda: button_click("÷"))
button_del = Button(root, text="Del", padx=40, pady=40, command=lambda: button_delete())
button_ac = Button(root, text="AC", padx=40, pady=40, command=lambda:button_clear())
button_answer = Button(root, text="Ans", padx=90, pady=40, command=lambda: button_click("Ans"))
button_exe = Button(root,text="exe",padx=38, pady=40, command=lambda:button_click("exe"))

#displaying the button

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_del.grid(row=2, column=3)
button_ac.grid(row=2, column=4)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_time.grid(row=3,column=3)
button_divide.grid(row=3,column=4)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4,column=3)
button_deduct.grid(row=4,column=4)



button_0.grid(row=5, column=0)
button_dot.grid(row=5, column=1)
button_answer.grid(row=5, column=2, columnspan=2)
button_exe.grid(row=5, column=4)

root.mainloop()








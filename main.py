# Python Programme to create a replicate of CASIO fx-50 FH II

# import everything in tkinter module

from tkinter import *
from math import *

root = Tk()
root.title("CASIO fx-50 FH II")

# define and create the entry box and output box on top
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
output = Text(root, height=2, width=65)
output.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
output.configure(state="disabled")
e.configure(state="disabled")

stored_value = 0

# function for the buttons
# calculate the answer for the user input
def button_exe():
    global stored_value
    output.configure(state="normal")
    user_input = e.get()
    equation = str(user_input)
    try:
        answer = eval(equation.replace('Ans', str(stored_value)))
        stored_value = answer
        output.delete("1.0", "end")
        output.insert("1.0", str(answer))
        output.configure(state="disabled")
        e.configure(state="normal")
        e.delete(0, END)
        e.configure(state="disabled")
    except:
        output.delete("1.0", "end")
        output.insert("1.0", "Error")
        output.configure(state="disabled")
        e.configure(state="normal")
        e.delete(0, END)
        e.configure(state="disabled")


# adding the number to the entry box
def button_click(number):
    e.configure(state="normal")
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    e.configure(state="disabled")


# deleting the number in the entry box
def button_delete():
    e.configure(state="normal")
    e.delete(len(e.get()) - 1)
    e.configure(state="disabled")


# clearing everything in the entry box and output box
def button_clear():
    e.configure(state="normal")
    e.delete(0, END)
    e.configure(state="disabled")
    output.configure(state="normal")
    output.delete("1.0", "end")
    output.configure(state="disabled")


# Define the buttons
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
button_time = Button(root, text="*", padx=48, pady=40, command=lambda: button_click("*"))
button_divide = Button(root, text="/", padx=45, pady=40, command=lambda: button_click("/"))
button_del = Button(root, text="Del", padx=40, pady=40, command=lambda: button_delete())
button_ac = Button(root, text="AC", padx=40, pady=40, command=lambda: button_clear())
button_answer = Button(root, text="Ans", padx=90, pady=40, command=lambda: button_click("Ans"))
button_execute = Button(root, text="exe", padx=38, pady=40, command=lambda: button_exe())
button_sqrt = Button(root, text="√", padx=40, pady=10, command=lambda: button_click("sqrt("))
button_square = Button(root, text="x^2", padx=34, pady=10, command=lambda: button_click("**2"))
button_power = Button(root, text="^", padx=40, pady=10, command=lambda: button_click("**"))
button_log = Button(root, text="log", padx=39, pady=10, command=lambda: button_click("log("))
button_ln = Button(root, text="ln", padx=44, pady=10, command=lambda: button_click(0))
button_openBracket = Button(root, text="(", padx=40, pady=10, command=lambda: button_click("("))
button_closeBracket = Button(root, text=")", padx=40, pady=10, command=lambda: button_click(")"))
button_sin = Button(root, text="sin", padx=40, pady=10, command=lambda: button_click("sin("))
button_cos = Button(root, text="cos", padx=40, pady=10, command=lambda: button_click("cos("))
button_tan = Button(root, text="tan", padx=40, pady=10, command=lambda: button_click("tan("))


# displaying the button

button_sqrt.grid(row=2, column=0)
button_square.grid(row=2, column=1)
button_power.grid(row=2, column=2)
button_log.grid(row=2, column=3)
button_ln.grid(row=2, column=4)

button_openBracket.grid(row=3, column=0)
button_closeBracket.grid(row=3, column=1)
button_sin.grid(row=3, column=2)
button_cos.grid(row=3, column=3)
button_tan.grid(row=3, column=4)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_del.grid(row=4, column=3)
button_ac.grid(row=4, column=4)

button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_time.grid(row=5, column=3)
button_divide.grid(row=5, column=4)

button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_add.grid(row=6, column=3)
button_deduct.grid(row=6, column=4)

button_0.grid(row=7, column=0)
button_dot.grid(row=7, column=1)
button_answer.grid(row=7, column=2, columnspan=2)
button_execute.grid(row=7, column=4)

root.mainloop()

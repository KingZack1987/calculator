# Python Programme to create a scientific calculator

# import everything in tkinter module
from tkinter import *

# import method in math
from math import sqrt, sin, cos, tan, asin, acos, atan, exp
from math import log as ln
from math import factorial as fac
from math import log10 as log
from math import pi as π

root = Tk()
root.title("Scientific Calculator")
root.geometry("505x630")

# Define and create the entry box and output box on top
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
output = Text(root, height=2, width=65)
output.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
output.configure(state="disabled")
e.configure(state="disabled")

# Define valuables
stored_value = 0
m = 0
k = 0
shift = False


# Function for changing the buttons in shift mode
def button_change(button, updated_text, updated_command, width):
    button.config(text=updated_text, command=updated_command, padx=width)


# Implementing shift mode
def shift_mode():
    global shift
    if shift is False:
        button_change(button_sqrt, "√", lambda: button_click("sqrt("), 40)
        button_change(button_sin, "sin", lambda: button_click("sin("), 35)
        button_change(button_cos, "cos", lambda: button_click("cos("), 38)
        button_change(button_tan, "tan", lambda: button_click("tan("), 38)
        button_change(button_mvalue, "M+", lambda: button_madd(), 39)
        button_change(button_closeBracket, ")", lambda: button_click(")"), 47)
        button_change(button_openBracket, "(", lambda: button_click("("), 42)
        button_change(button_log, "log", lambda: button_click("log("), 33)
        button_change(button_ln, "ln", lambda: button_click("ln("), 38)
        button_change(button_inverse, "x^-1", lambda: button_click("**-1"), 29)
        button_change(button_percentage, "%", lambda: button_click("%"), 38)
        button_change(button_ac, "AC", lambda:  button_clear(), 40)
        shift = True
    else:
        button_change(button_mvalue, "M", lambda: button_click("M"), 43)
        button_change(button_sin, "sin^-1", lambda: button_click("asin("), 25)
        button_change(button_cos, "cos^-1", lambda: button_click("acos("), 28)
        button_change(button_tan, "tan^-1", lambda: button_click("atan("), 28)
        button_change(button_closeBracket, "MC", lambda: m_clear(), 39)
        button_change(button_openBracket, "M-", lambda: button_mdeduct(), 36)
        button_change(button_log, "10^x", lambda: button_click("10**("), 28)
        button_change(button_ln, "e^x", lambda: button_click("exp("), 34)
        button_change(button_inverse, "abs", lambda: button_click("abs("), 33)
        button_change(button_percentage, "π", lambda: button_click("π"), 38)
        button_change(button_ac, "OFF", lambda: root.destroy(), 36)
        shift = False


# Function for the buttons
# Function for M+
def button_madd():
    global m
    global k
    try:
        k = button_exe()
        m = int(m) + int(k)
        output.configure(state="normal")
        output.delete("1.0", "end")
        output.insert("1.0", "M+")
        e.configure(state="normal")
        e.delete(0, END)
        e.configure(state="disabled")
        output.configure(state="disabled")
    except:
        return

# function for M-
def button_mdeduct():
    global m
    global k
    try:
        k = button_exe()
        m = int(m) - int(k)
        output.configure(state="normal")
        output.delete("1.0", "end")
        output.insert("1.0", "M-")
        e.configure(state="normal")
        e.delete(0, END)
        e.configure(state="disabled")
        output.configure(state="disabled")
    except:
        return


# Function for calling M
def M():
    global m
    if m is not None:
        return m

# Function for clearing M
def m_clear():
    global m
    output.configure(state="normal")
    output.delete("1.0", "end")
    output.insert("1.0", "MC")
    e.configure(state="normal")
    e.delete(0, END)
    e.configure(state="disabled")
    output.configure(state="disabled")
    m = 0


# Calculating the answer for the user input
def button_exe():
    global stored_value
    output.configure(state="normal")
    user_input = e.get()
    equation = str(user_input)
    try:
        if equation != '':
            answer = eval(equation.replace('Ans', str(stored_value)).replace("M", str(m)).replace("%", str("/100")))
            stored_value = answer
            output.delete("1.0", "end")
            output.insert("1.0", str(answer))
            output.configure(state="disabled")
            e.configure(state="normal")
            e.delete(0, END)
            e.configure(state="disabled")
            return answer
        elif equation == "":
            return
    except:
        try:
            # Adding ) at the end of the equation to prevent error during the calculation
            answer = eval(equation.replace('Ans', str(stored_value)).replace("M", str(m)).replace("%", "/100") + ")")
            stored_value = answer
            output.delete("1.0", "end")
            output.insert("1.0", str(answer))
            output.configure(state="disabled")
            e.configure(state="normal")
            e.delete(0, END)
            e.configure(state="disabled")
            return answer
        except:
            # Printing error as the result
            output.delete("1.0", "end")
            output.insert("1.0", "Error")
            output.configure(state="disabled")
            e.configure(state="normal")
            e.delete(0, END)
            e.configure(state="disabled")


# adding the number and symbol to the entry box
def button_click(number):
    e.configure(state="normal")
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    e.configure(state="disabled")


# deleting the number and symbol in the entry box
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


# Define the basic buttons
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
button_answer = Button(root, text="Ans", padx=34, pady=40, command=lambda: button_click("Ans"))
button_execute = Button(root, text="exe", padx=93, pady=40, command=lambda: button_exe())

# Define more complicated symbol
button_sqrt = Button(root, text="√", padx=40, pady=10, command=lambda: button_click("sqrt("))
button_square = Button(root, text="x^2", padx=38, pady=10, command=lambda: button_click("**2"))
button_power = Button(root, text="^", padx=46, pady=10, command=lambda: button_click("**"))
button_log = Button(root, text="log", padx=33, pady=10, command=lambda: button_click("log("))
button_ln = Button(root, text="ln", padx=38, pady=10, command=lambda: button_click("ln("))
button_openBracket = Button(root, text="(", padx=42, pady=10, command=lambda: button_click("("))
button_closeBracket = Button(root, text=")", padx=47, pady=10, command=lambda: button_click(")"))
button_sin = Button(root, text="sin", padx=35, pady=10, command=lambda: button_click("sin("))
button_cos = Button(root, text="cos", padx=38, pady=10, command=lambda: button_click("cos("))
button_tan = Button(root, text="tan", padx=39, pady=10, command=lambda: button_click("tan("))
button_inverse = Button(root, text="x^-1", padx=29, pady=10, command=lambda: button_click("**-1"))
button_percentage = Button(root, text="%", padx=38, pady=10, command=lambda: button_click("%"))
button_mvalue = Button(root, text="M+", padx=39, pady=10, command=lambda: button_madd())
button_shift = Button(root, text="shift", padx=78, pady=10, command=lambda: shift_mode())

# Displaying the button
button_shift.grid(row=2, column=0, columnspan=2)
button_sqrt.grid(row=2, column=2)
button_power.grid(row=2, column=3)
button_square.grid(row=2, column=4)

button_inverse.grid(row=3, column=0)
button_percentage.grid(row=3, column=1)
button_sin.grid(row=3, column=2)
button_cos.grid(row=3, column=3)
button_tan.grid(row=3, column=4)

button_log.grid(row=4, column=0)
button_ln.grid(row=4, column=1)
button_openBracket.grid(row=4, column=2)
button_closeBracket.grid(row=4, column=3)
button_mvalue.grid(row=4, column=4)

button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)
button_del.grid(row=5, column=3)
button_ac.grid(row=5, column=4)

button_4.grid(row=6, column=0)
button_5.grid(row=6, column=1)
button_6.grid(row=6, column=2)
button_time.grid(row=6, column=3)
button_divide.grid(row=6, column=4)

button_1.grid(row=7, column=0)
button_2.grid(row=7, column=1)
button_3.grid(row=7, column=2)
button_add.grid(row=7, column=3)
button_deduct.grid(row=7, column=4)

button_0.grid(row=8, column=0)
button_dot.grid(row=8, column=1)
button_answer.grid(row=8, column=2)
button_execute.grid(row=8, column=3, columnspan=2)

root.mainloop()

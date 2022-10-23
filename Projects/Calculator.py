from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("500x500")
window.configure(background="light blue")

def clear_all():
    expression_field.delete(0, END)

def get_variables(num):
    expression = ""
    expression = expression + str(num)
    expression_field.insert(END, num)

def calculate():
    expression = ""
    expression = expression_field.get()
    try:
        result = eval(expression)
        expression_field.delete(0, END)
        expression_field.insert(0, result)
    except:
        expression_field.delete(0, END)
        expression_field.insert(0, "Error")


def undo():
    expression = ""
    expression = expression_field.get()
    if len(expression):
        new_expression = expression[:-1]
        expression_field.delete(0, END)
        expression_field.insert(0, new_expression)
    else:
        expression_field.delete(0, END)
        expression_field.insert(0, "Error")

expression = ""

expression_field = Entry(window)
expression_field.grid(row=0, column=0, columnspan=4, ipadx=70)

button1 = Button(window, text=' 1 ', fg='black', bg='red', command=lambda: get_variables(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(window, text=' 2 ', fg='black', bg='red', command=lambda: get_variables(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(window, text=' 3 ', fg='black', bg='red', command=lambda: get_variables(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(window, text=' 4 ', fg='black', bg='red', command=lambda: get_variables(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(window, text=' 5 ', fg='black', bg='red', command=lambda: get_variables(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(window, text=' 6 ', fg='black', bg='red', command=lambda: get_variables(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(window, text=' 7 ', fg='black', bg='red', command=lambda: get_variables(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(window, text=' 8 ', fg='black', bg='red', command=lambda: get_variables(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(window, text=' 9 ', fg='black', bg='red', command=lambda: get_variables(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(window, text=' 0 ', fg='black', bg='red', command=lambda: get_variables(0), height=1, width=7)
button0.grid(row=5, column=0)

plus = Button(window, text=' + ', fg='black', bg='red', command=lambda: get_variables("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(window, text=' - ', fg='black', bg='red', command=lambda: get_variables("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(window, text=' * ', fg='black', bg='red', command=lambda: get_variables("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(window, text=' / ', fg='black', bg='red', command=lambda: get_variables("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = Button(window, text=' = ', fg='black', bg='red', command=calculate, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(window, text='Clear', fg='black', bg='red', command=clear_all, height=1, width=7)
clear.grid(row=5, column='1')

Decimal = Button(window, text='.', fg='black', bg='red', command=lambda: get_variables('.'), height=1, width=7)
Decimal.grid(row=6, column=0)

undo = Button(window, text='Undo', fg='black', bg='red', command=undo, height=1, width=7)
undo.grid(row=6, column=1)

# start the GUI
window.mainloop()
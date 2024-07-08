from tkinter import *

root = Tk()
root.title("Calculator by Afia")

entry_field = Entry(root, width=35, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

calculation = []

def update_entry_field(number):
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(current) + str(number))

def clear_entry_field():
    entry_field.delete(0, END)

def perform_calculation(operator):
    current = entry_field.get()
    calculation.append(current)
    calculation.append(operator)
    entry_field.delete(0, END)

def equal_button():
    current = entry_field.get()
    calculation.append(current)
    result = eval(' '.join(calculation))
    entry_field.delete(0, END)
    entry_field.insert(0, result)
    calculation.clear()

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: update_entry_field(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: update_entry_field(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: update_entry_field(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: update_entry_field(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: update_entry_field(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: update_entry_field(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: update_entry_field(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: update_entry_field(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: update_entry_field(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: update_entry_field(0))

button_add = Button(root, text="+", padx=40, pady=20, command=lambda: perform_calculation("+"))
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: perform_calculation("-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: perform_calculation("*"))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: perform_calculation("/"))
button_equal = Button(root, text="=", padx=40, pady=20, command=equal_button)
button_clear = Button(root, text="Clear", padx=30, pady=20, command=clear_entry_field)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)

root.mainloop()
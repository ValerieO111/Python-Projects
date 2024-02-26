from tkinter import *

def click(key):
    try:
        if key == "=":
            result = str(eval(display.get()))[:10]  # Limit result to 10 characters
            display.delete(0, END)
            display.insert(END, "=" + result)
        elif key == "C":
            display.delete(0, END)
        else:
            display.insert(END, key)
    except:
        display.insert(END, "--> Error!")

# main:
window = Tk()
window.title("ValCalculator")

# Adjust window size
window.geometry("300x400")  # Medium size

# create top_row frame
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky="nsew")

# use Entry widget for an editable display
display = Entry(top_row, width=35, bg="coral", font=('Arial', 14))
display.grid(row=0, column=0, padx=10, pady=10)

# create num_pad_frame
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky="nsew")

# create operator_frame
operator = Frame(window)
operator.grid(row=1, column=1, sticky="nsew")

# provide a list of keys for the number pad:
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]

# create num_pad buttons with a loop
r = 0  # row counter
c = 0  # column counter
for btn_text in num_pad_list:
    Button(num_pad, text=btn_text, width=5, font=('Arial', 14),
           command=lambda key=btn_text: click(key)).grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c > 2:
        c = 0
        r += 1

# provide a list of keys for the operator pad:
operator_list = [
    '*', '/',
    '+', '-',
    '(' , ')',
    'C'
]

r = 0
c = 0
for btn_text in operator_list:
    Button(operator, text=btn_text, width=5, font=('Arial', 14),
           command=lambda key=btn_text: click(key)).grid(row=r, column=c, padx=5, pady=5)
    r += 1

# Run mainloop
window.mainloop()

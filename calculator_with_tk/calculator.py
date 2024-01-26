from tkinter import *

# Creating window and defining its name and size
window = Tk()
window.geometry("312x324")
window.resizable(0, 0)  # preventing from resizing the window
window.title("Calculator")


# function that constantly update after entering a number
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# function used for clearing all entered numbers
def button_clear():
    global expression
    expression = ""
    input_text.set("")


# function for calculation
def button_equal():
    global expression

    try:
        # eval() method parses the expression passed to this method and runs python expression (code) within the program
        result = str(eval(expression))
    except ZeroDivisionError:
        result = 'Error'
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()

# Creating a frame for input numbers
input_frame = Frame(window, width=312, height=50, bd=0, bg="white", highlightbackground="#908787",
                    highlightcolor="black", highlightthickness=2)

input_frame.pack(side=TOP)

# Creating input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50,
                    bg="white", fg='#5B5757', bd=0, justify=RIGHT)

input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Creating 'Frame' for the buttons below the 'input_frame'
buttons_frame = Frame(window, width=312, height=272.5, bg="#908787")
buttons_frame.pack()

# first row of buttons

Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#F5CBA7", cursor="hand2",
       command=lambda: button_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#F5CBA7", cursor="hand2",
       command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)


# second row of buttons
Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)

Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)

Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)

Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#F5CBA7", cursor="hand2",
       command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row of buttons
Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)

Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)

Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)

Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#F5CBA7", cursor="hand2",
       command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row of buttons

Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)

Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)

Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)

Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#F5CBA7", cursor="hand2",
       command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fifth row of buttons

Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#F5CBA7", cursor="hand2",
       command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)

Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#F5CBA7", cursor="hand2",
       command=lambda: button_equal()).grid(row=4, column=3, padx=1, pady=1)

window.mainloop()

from tkinter import *
from webbrowser import open_new
from tkinter import ttk
from tkinter import messagebox
from time import *
mainWin = Tk()
mainWin.geometry("559x529")
mainWin.resizable(True, True)
icon = PhotoImage(file="assistant.png")
mainWin.iconphoto(True, icon)
notebook = ttk.Notebook(mainWin)
tab1 = Frame(notebook)
# notebook
notebook.add(tab1, text="Notebook")
note = Text(tab1, font="Arial")
note.pack(expand=True, fill=BOTH)
# calculator
tab2 = Frame(notebook)
notebook.add(tab2, text="Calculator")
# clock
tab3 = Frame(notebook)
notebook.add(tab3, text="Clock")
# about
tab4 = Frame(notebook)
coder_label = Label(tab4, font=("Times New Roman", 50), fg="#FFFFFF", bg="Black", text="Coded by Sepehr")
coder_label.pack(fill=BOTH)
notebook.add(tab4, text="About")
notebook.pack(fill=BOTH)
equation_text = ""
equation_label = StringVar()


def github():
    open_new("https://github.com/gigasepehr")


def button_press(num=None, event=None):
    if notebook.select()[-1] != '2':
        return
    if event is not None:
        print(event.keysym)
    global equation_text
    symbols = ["*", "/", "-", "+"]
    equation_text = equation_label.get()
    if len(equation_text) >= 1:
        if (str(num) in symbols) and str(equation_text)[-1] in symbols:
            equation_text = equation_text[:-1]
        elif equation_text[-1].isdigit() and num.isdigit():
            pass
    else:
        pass
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals(event):
    if notebook.select()[-1] != '2':
        return
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = ""
    except ZeroDivisionError:
        messagebox.showerror(title="Error", message="You can't divide to zero!")
        # equation_text = ""
    except SyntaxError:
        messagebox.showerror(title="Error", message="Syntax error occurred.")


def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)


def delete(event):
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)


def plus(event):
    button_press("+")


def minus(event):
    button_press("-")


def multiple(event):
    button_press("*")


def divide(event):
    button_press("/")


def num_pad(event):
    button_press(event.keysym)



mainWin.bind("<BackSpace>", delete)
mainWin.bind("<Delete>", delete)
mainWin.bind("<plus>", plus)
mainWin.bind("<asterisk>", multiple)
mainWin.bind("<minus>", minus)
mainWin.bind("<slash>", divide)
mainWin.bind("<equal>", equals)
mainWin.bind("<Return>", equals)
mainWin.bind("1", num_pad)
mainWin.bind("2", num_pad)
mainWin.bind("3", num_pad)
mainWin.bind("4", num_pad)
mainWin.bind("5", num_pad)
mainWin.bind("6", num_pad)
mainWin.bind("7", num_pad)
mainWin.bind("8", num_pad)
mainWin.bind("9", num_pad)
mainWin.bind("0", num_pad)
coder_label.bind("<Button-1>", lambda o: github())
# region Buttons & Labels
label = Label(
    master=tab2,
    font=("Arial", 20),
    bg="White",
    width=500,
    height=2,
    textvariable=equation_label,
)
label.pack(fill=BOTH)
frame = Frame(master=tab2)
frame.pack(fill=BOTH)
button1 = Button(
    frame, text=1, command=lambda: button_press('1'), height=4, width=9, font=35,
)
button1.grid(row=0, column=0)
button2 = Button(
    frame, text=2, command=lambda: button_press('2'), height=4, width=9, font=35
)
button2.grid(row=0, column=1)
button3 = Button(
    frame, text=3, command=lambda: button_press('3'), height=4, width=9, font=35
)
button3.grid(row=0, column=2)
# button3.grid()
button4 = Button(
    frame, text=4, command=lambda: button_press('4'), height=4, width=9, font=35
)
button4.grid(row=1, column=0)
button5 = Button(
    frame, text=5, command=lambda: button_press('5'), height=4, width=9, font=35
)
button5.grid(row=1, column=1)
button6 = Button(
    frame, text=6, command=lambda: button_press('6'), height=4, width=9, font=35
)
button6.grid(row=1, column=2)
button7 = Button(
    frame, text=7, command=lambda: button_press('7'), height=4, width=9, font=35
)
button7.grid(row=2, column=0)
button8 = Button(
    frame, text=8, command=lambda: button_press('8'), height=4, width=9, font=35
)
button8.grid(row=2, column=1)
button9 = Button(
    frame, text=9, command=lambda: button_press('9'), height=4, width=9, font=35
)
button9.grid(row=2, column=2)
button0 = Button(
    frame, text=0, command=lambda: button_press('0'), height=4, width=20, font=35
)
# b = Button()
# button0.grid()
button0.grid(row=3, column=0, columnspan=2)
dotButton = Button(
    frame, text=".", command=lambda: button_press("."), height=4, width=9, font=35
)
dotButton.grid(row=3, column=2)
plusButton = Button(
    frame, text="+", command=lambda: button_press("+"), height=4, width=9, font=35
)
plusButton.grid(row=2, column=3)
minusButton = Button(
    frame, text="-", command=lambda: button_press("-"), height=4, width=9, font=35
)
minusButton.grid(row=2, column=4)
multipleButton = Button(
    frame, text="*", command=lambda: button_press("*"), height=4, width=9, font=35
)
multipleButton.grid(row=1, column=3)
divideButton = Button(
    frame, text="/", command=lambda: button_press("/"), height=4, width=9, font=35
)
divideButton.grid(row=1, column=4)
equalButton = Button(frame, text="=", command=equals, height=4, width=9, font=35)
equalButton.grid(row=3, column=3)
clearButton = Button(frame, text="C", command=clear, height=4, width=9, font=35)
clearButton.grid(row=0, column=3)


# endregion Buttons & Labels


# clockWin = Toplevel(tab3)

def last_digit(day_num):
    day_num_last_digit = str(day_num)[-1]
    if day_num_last_digit == '1':
        day_suffix = 'st'
    elif day_num_last_digit == '2':
        day_suffix = 'nd'
    elif day_num_last_digit == '3':
        day_suffix = 'rd'
    else:
        day_suffix = 'th'
    return day_suffix


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    # time_label.config(width=)
    day_string = strftime("%A")
    day_label.config(text=day_string)
    a = localtime()
    day_num = a[7]
    # day_num_last_digit = str(a[7])[-1]
    day_suffix = last_digit(day_num)
    day_full = "Today is : " + str(day_num) + day_suffix + " day of {}".format(a[0])  # nth day of year
    nth_label.config(text=day_full)
    month_day_num = a[2]
    month_day_suffix = last_digit(month_day_num)
    month_day_full = str(month_day_num) + month_day_suffix
    date_string = "Today is : {} {}, {}".format(month_day_full, strftime("%B"), a[0])
    date_label.config(text=date_string)
    tab3.after(1, update)


time_label = Label(tab3, font=("Gideon Roman", 50), fg="#00FF00", bg="Black")
time_label.pack(fill=BOTH)
day_label = Label(tab3, font=("MV Boli", 25), fg="#FF0000")
day_label.pack(fill=BOTH)
date_label = Label(tab3, font=("Alumni Sans", 25))
date_label.pack(fill=BOTH)
nth_label = Label(tab3, font=("Alumni Sans", 30))
nth_label.pack(fill=BOTH)
update()
# Button(clockWin, text="Quit", font=("Calibri", 25), fg="#000000", bg="White", command=lambda: clockWin.destroy()) \
#     .pack(expand=True)


# openCalcButton = Button(
#     mainWin, text="Open calculator", command=openCalculator, height=7, width=16, font=8
# )
# openTimeButton = Button(
#     mainWin, text="Open Clock", command=openClock, height=7, width=16, font=8
# )
# openCalcButton.pack()
# openTimeButton.pack()

# win.mainloop()
mainWin.mainloop()

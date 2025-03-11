# A program to convert AM to PM or PM to AM

import tkinter

# screen setup
window = tkinter.Tk()
window.title("Time Converter")
window.minsize(width=300, height=300)
window.config(padx=150)

# labels

label_title = tkinter.Label(text="Time Converter", font=30)
label_title.grid(column=1, row=0)

label_time = tkinter.Label(text="", font=20)
label_time.grid(column=2, row=4)

label_result = tkinter.Label(text="", font=20)
label_result.grid(column=1, row=6)


# am format to 24 hour format
def twelve_to_twentyfour_am():
    user_value_am = int(user_input.get())
    time_am = {am: 0 if am == 12 else am for am in range(1, 13)}

    label_result.config(text=f"{time_am[user_value_am]}")


# pm format to 24 hour format
def twelve_to_twentyfour_pm():
    user_value_pm = int(user_input.get())
    time_pm = {pm: pm if pm == 12 else pm + 12 for pm in range(1, 13)}

    label_result.config(text=f"{time_pm[user_value_pm]}")


# am text shown
def am_text():
    label_time.config(text="AM")


def pm_text():
    label_time.config(text="PM")


# buttons to choose am or pm
int_var = tkinter.IntVar()
am_converter = tkinter.Radiobutton(text="AM", value=1, variable=int_var, command=am_text)
pm_converter = tkinter.Radiobutton(text="PM", value=2, variable=int_var, command=pm_text)
am_converter.grid(column=0, row=3)
pm_converter.grid(column=2, row=3)


# button to convert
def convert_time():
    if int_var.get() == 1:
        twelve_to_twentyfour_am()
    else:
        twelve_to_twentyfour_pm()


am_pm_button = tkinter.Button(text="Convert", command=convert_time)
am_pm_button.grid(column=1, row=7)

# Input values for time
user_input = tkinter.Entry()
user_input.grid(column=1, row=4)

window.mainloop()

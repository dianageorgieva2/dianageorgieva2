from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)

label_miles = Label(text="Miles", font=("Ariel", 10,))
label_miles.grid(column=2, row=0)

label_isequalto = Label(text="is equal to", font=("Ariel", 10,))
label_isequalto.grid(column=0, row=1)

label_calc = Label(text="0", font=("Ariel", 10,))
label_calc.grid(column=1, row=1)

label_km = Label(text="Km", font=("Ariel", 10,))
label_km.grid(column=2, row=1)


def button_clicked():
    miles = float(input_miles.get())
    km = round(miles * 1.60934)
    label_calc.config(text=km)
    

calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)











window.mainloop()

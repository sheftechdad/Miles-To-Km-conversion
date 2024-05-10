import tkinter


def calculate():
    miles=float(mile_input.get())
    km= miles * 1.609
    kilo_result_label.config(text=f"{round(km)}")




window=tkinter.Tk()
window.title("Mile to KM converter")
window.config(padx=20,pady=20)

mile_input=tkinter.Entry(width=10)
mile_input.grid(column=1,row=0)

mile_label=tkinter.Label(text="mile")
mile_label.grid(column=2,row=0)

equal_label=tkinter.Label(text="is equal to")
equal_label.grid(column=0,row=1)


kilo_result_label=tkinter.Label(text="0")
kilo_result_label.grid(column=1,row=1)

kilometer_label=tkinter.Label(text="Km")
kilometer_label.grid(column=2,row=1)




my_button=tkinter.Button(text="Calculate",command=calculate)
my_button.grid(column=1,row=2)




window.mainloop()
import tkinter as tk

# fonction:
def addition():

    return

def multiplication():
    pass


def division():
    pass
    

def soustraction():
    pass


# interface:
racine =  tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0)
number1 = tk.Button(racine, text="1",font=("30"), command=add1)
number2 = tk.Button(racine, text="2",font=("30"), command=add2)
number3 = tk.Button(racine, text="3",font=("30"), command=add3)
number4 = tk.Button(racine, text="4",font=("30"), command=add4)
number5 = tk.Button(racine, text="5",font=("30"), command=add5)
number6 = tk.Button(racine, text="6",font=("30"), command=add6)
number7 = tk.Button(racine, text="7",font=("30"), command=add7)
number8 = tk.Button(racine, text="8",font=("30"), command=add8)
number9 = tk.Button(racine, text="9",font=("30"), command=add9)
plus = tk.Button(racine, text="+",font=("30"), command=addition)
moins = tk.Button(racine, text="-",font=("30"), command=multiplication)
diviser = tk.Button(racine, text="/",font=("30"), command=division)
multiplication = tk.Button(racine, text="*",font=("30"), command=soustraction)
# mainloop.
racine.mainloop()

import tkinter as tk

# Varioables:
HEIGHT, WIDTH = 4, 20

# fonction:
def addition():

    return

def multiplication():
    pass


def division():
    pass
    

def soustraction():
    pass


def add1():
    pass


def add2():
    pass


def add3():
    pass


def add4():
    pass


def add5():
    pass


def add6():
    pass


def add7():
    pass


def add8():
    pass


def add9():
    pass


# interface:
racine =  tk.Tk()
label = tk.Label(racine, bg="black", height=HEIGHT, width=WIDTH)
label.grid(column=0, row=0, columnspan=4)

#Pavé numérique:
number1 = tk.Button(racine, text="1",font=("30"), command=add1)
number1.grid(column=0, row=1)
number2 = tk.Button(racine, text="2",font=("30"), command=add2)
number2.grid(column=1, row=1)
number3 = tk.Button(racine, text="3",font=("30"), command=add3)
number3.grid(column=2, row=1)
number4 = tk.Button(racine, text="4",font=("30"), command=add4)
number4.grid(column=0, row=2)
number5 = tk.Button(racine, text="5",font=("30"), command=add5)
number5.grid(column=1, row=2)
number6 = tk.Button(racine, text="6",font=("30"), command=add6)
number6.grid(column=2, row=2)
number7 = tk.Button(racine, text="7",font=("30"), command=add7)
number7.grid(column=0, row=3)
number8 = tk.Button(racine, text="8",font=("30"), command=add8)
number8.grid(column=1, row=3)
number9 = tk.Button(racine, text="9",font=("30"), command=add9)
number9.grid(column=2, row=3)

# Opérations:
plus = tk.Button(racine, text="+",font=("30"), command=addition)
plus.grid(column=3, row=1)
moins = tk.Button(racine, text="-",font=("30"), command=multiplication)
moins.grid(column=3, row=2)
multiplication = tk.Button(racine, text="x",font=("30"), command=soustraction)
multiplication.grid(column=3, row=3)
diviser = tk.Button(racine, text="/",font=("30"), command=division)
diviser.grid(column=3, row=4)

# mainloop.
racine.mainloop()

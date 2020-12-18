import tkinter as tk

HEIGHT, WIDTH = 4, 20

# fonction:
def addition():
    label.config(text=" + ")

def multiplication():
    label.config(text=" * ")


def division():
    label.config(text=" / ")
    

def soustraction():
    label.config(text=" - ")


def nb0():
    global a
    a = 0
    label.config(text=a)
    liste.

def nb1():
    a = 1
    label.config(text=a)


def nb2():
    a = 2
    label.config(text=a)


def nb3():
    a = 3
    label.config(text=3)


def nb4():
    a = 4
    label.config(text=4)


def nb5():
    a = 5
    label.config(text=5)


def nb6():
    a = 6
    label.config(text=6)


def nb7():
    a = 7
    label.config(text=7)


def nb8():
    a = 8
    label.config(text=8)


def nb9():
    a = 9
    label.config(text=9)


# interface:
racine =  tk.Tk()
label = tk.Label(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0, columnspan=4)

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
moins = tk.Button(racine, text="-",font=("30"), command=multiplication)
moins.grid(column=3, row=2)
multiplication = tk.Button(racine, text="x",font=("30"), command=soustraction)
multiplication.grid(column=3, row=3)
diviser = tk.Button(racine, text="/",font=("30"), command=division)
diviser.grid(column=3, row=4)

# mainloop.
racine.mainloop()

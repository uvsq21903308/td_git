import tkinter as tk

HEIGHT, WIDTH = 4, 20

# fonction:
def addition():
    res = x + y
    label.config(text=res)

def multiplication():
    res = x * y
    label.config(text=res)


def division():
    res = x / y
    label.config(text=res)
    

def soustraction():
    res = x - y
    label.config(text=res)

def nb_x():



def nb1():
    
    label.config(text=1)


def nb2():
    label.config(text=2)


def nb3():
    label.config(text=3)


def nb4():
    label.config(text=4)


def nb5():
    label.config(text=1)


def nb6():
    label.config(text=1)


def nb7():
    pass


def nb8():
    pass


def nb9():
    pass


# interface:
racine =  tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
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

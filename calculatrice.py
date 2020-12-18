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


def calcul():
    pass


def nb0():
    global a
    a = 0
    label.config(text=a)
    liste

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
label = tk.Label(racine, text=" ", bg="black", height=HEIGHT, width=WIDTH)
label.grid(column=0, row=0, columnspan=4)

#Pavé numérique:
number0 = tk.Button(racine, text="0", font=("30"), command=nb0)
number0.grid(column=1, row=4)
number1 = tk.Button(racine, text="1",font=("30"), command=nb1)
number1.grid(column=0, row=1)
number2 = tk.Button(racine, text="2",font=("30"), command=nb2)
number2.grid(column=1, row=1)
number3 = tk.Button(racine, text="3",font=("30"), command=nb3)
number3.grid(column=2, row=1)
number4 = tk.Button(racine, text="4",font=("30"), command=nb4)
number4.grid(column=0, row=2)
number5 = tk.Button(racine, text="5",font=("30"), command=nb5)
number5.grid(column=1, row=2)
number6 = tk.Button(racine, text="6",font=("30"), command=nb6)
number6.grid(column=2, row=2)
number7 = tk.Button(racine, text="7",font=("30"), command=nb7)
number7.grid(column=0, row=3)
number8 = tk.Button(racine, text="8",font=("30"), command=nb8)
number8.grid(column=1, row=3)
number9 = tk.Button(racine, text="9",font=("30"), command=nb9)
number9.grid(column=2, row=3)

# Opérations:
egal = tk.Button(racine, text="=", font=("30"), command=calcul)
egal.grid(column=3, row=1)
plus = tk.Button(racine, text="+",font=("30"), command=addition)
plus.grid(column=3, row=2)
moins = tk.Button(racine, text="-",font=("30"), command=multiplication)
moins.grid(column=3, row=3)
multiplication = tk.Button(racine, text="x",font=("30"), command=soustraction)
multiplication.grid(column=3, row=4)
diviser = tk.Button(racine, text="/",font=("30"), command=division)
diviser.grid(column=2, row=4)

# mainloop.
racine.mainloop()

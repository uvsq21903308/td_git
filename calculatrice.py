import tkinter as tk

HEIGHT, WIDTH = 4, 20

#liste
liste = []

# fonction:
def addition():
    label.config(text="+")

def multiplication():
    label.config(text="*")


def division():
    label.config(text="/")
    

def soustraction():
    label.config(text="-")


def calcul():
    


def nb0():
    global a
    a = 0
    liste.append(a)

def nb1():
    global a
    a = 1
    liste.append(a)


def nb2():
    global a
    a = 2
    liste.append(a)


def nb3():
    global a
    a = 3
    liste.append(a)


def nb4():
    global a
    a = 4
    liste.append(a)


def nb5():
    global a
    a = 5
    liste.append(a)


def nb6():
    global a
    a = 6
    liste.append(a)


def nb7():
    global a
    a = 7
    liste.append(a)


def nb8():
    global a
    a = 8
    liste.append(a)


def nb9():
    global a
    a = 9
    liste.append(a)


# interface:
racine =  tk.Tk()
label = tk.Label(racine, bg="black", height=HEIGHT, width=WIDTH)
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

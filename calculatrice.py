import tkinter as tk

WIDTH = 20

#liste
liste = []
lst_calcul = []
operation= []

# fonction:
def addition():
    c = "0"
    for i in range(0,len(liste)):
        c += str(liste[i])
    lst_calcul.append(c)
    liste.clear()
    label.config(text="")
    operation.append(1)

def multiplication():
    c = "0"
    for i in range(0,len(liste)):
        c += str(liste[i])
    lst_calcul.append(c)
    liste.clear()
    label.config(text="")
    operation.append(2)

def division():
    c = "0"
    for i in range(0,len(liste)):
        c += str(liste[i])
    lst_calcul.append(c)
    liste.clear()
    label.config(text="")
    operation.append(3)

def soustraction():
    c = "0"
    for i in range(0,len(liste)):
        c += str(liste[i])
    lst_calcul.append(c)
    liste.clear()
    label.config(text="")
    operation.append(4)

def calcul():
    c = "0"
    for i in range(0,len(liste)):
        c += str(liste[i])
    lst_calcul.append(c)
    x = int(lst_calcul[0])
    if 1 in operation:
        x += int(lst_calcul[1])
    if 2 in operation:
        x *= int(lst_calcul[1])
    if 3 in operation:
        x /= int(lst_calcul[1])
    if 4 in operation:
        x -= int(lst_calcul[1])
    label.config(text=x)
    print(lst_calcul[0], lst_calcul[1])


def affichage():
    c = "0"
    for i in range(0,len(liste)):
        c += str(liste[i])
    label.config(text=int(c))

def nb0():
    liste.append(0)
    affichage()


def nb1():
    liste.append(1)
    affichage()


def nb2():
    liste.append(2)
    affichage()


def nb3():
    liste.append(3)
    affichage()


def nb4():
    liste.append(4)
    affichage()


def nb5():
    liste.append(5)
    affichage()


def nb6():
    liste.append(6)
    affichage()


def nb7():
    liste.append(7)
    affichage()


def nb8():
    liste.append(8)
    affichage()


def nb9():
    liste.append(9)
    affichage()


# interface:
racine =  tk.Tk()
label = tk.Label(racine, text="", fg="white", bg="black", width=WIDTH)
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
moins = tk.Button(racine, text="-",font=("30"), command=soustraction)
moins.grid(column=3, row=3)
multiplication = tk.Button(racine, text="x",font=("30"), command=multiplication)
multiplication.grid(column=3, row=4)
diviser = tk.Button(racine, text="/",font=("30"), command=division)
diviser.grid(column=2, row=4)


# mainloop.
racine.mainloop()

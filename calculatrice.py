import tkinter as tk

HEIGHT, WIDTH = 4, 40

# liste
liste = []
lst_calcul = []
operation = []

# fonction:


def addition():
    c = "0"
    for i in range(len(liste)):
        c += str(liste[i])
    c = int(c)
    lst_calcul.append(c)
    lst_calcul.append("+")
    liste.clear()
    label.config(text="")
    operation.append(1)


def multiplication():
    c = "0"
    for i in range(len(liste)):
        c += str(liste[i])
    c = int(c)
    lst_calcul.append(c)
    lst_calcul.append("*")
    liste.clear()
    label.config(text="")
    operation.append(2)


def division():
    c = "0"
    for i in range(len(liste)):
        c += str(liste[i])
    c = int(c)
    lst_calcul.append(c)
    lst_calcul.append("/")
    liste.clear()
    label.config(text="")
    operation.append(3)


def soustraction():
    c = "0"
    for i in range(len(liste)):
        c += str(liste[i])
    c = int(c)
    lst_calcul.append(c)
    lst_calcul.append("-")
    liste.clear()
    label.config(text="")
    operation.append(4)


def calcul():
    c = "0"
    for i in range(len(liste)):
        c += str(liste[i])
    c = int(c)
    lst_calcul.append(c)
    liste_cpt = []
    cpt = 0
    res = lst_calcul[0]
    if "*" or "/" in lst_calcul:
        condi = len(lst_calcul)
        i = 0
        while i < condi:
            val = lst_calcul[i]
            if "*" != val and "/" != val:
                cpt += 1
            else:
                if "*" == val:
                    x = lst_calcul[cpt - 1] * lst_calcul[cpt + 1]
                    lst_calcul.insert(cpt + 2, x)
                    liste_cpt.append(cpt)
                    cpt += 1
                    condi += 1
                else:
                    x = lst_calcul[cpt - 1] // lst_calcul[cpt + 1]
                    lst_calcul.insert(cpt + 2, x)
                    liste_cpt.append(cpt)
                    cpt += 1
                    condi += 1
            i += 1
    for j in range(len(liste_cpt)):
        nbr = len(liste_cpt) - 1 - j
        del lst_calcul[liste_cpt[nbr] - 1:liste_cpt[nbr] + 2]
    for k in range(len(lst_calcul)):
        val = lst_calcul[k]
        if "+" == val:
            res += lst_calcul[k + 1]
        elif "-" == val:
            res -= lst_calcul[k + 1]
    label.config(text=res)


def affichage():
    c = "0"
    for i in range(len(liste)):
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
racine = tk.Tk()
label = tk.Label(racine, text="", fg="white", bg="black", width=WIDTH, height=HEIGHT, anchor='e', font=("30"))
label.grid(column=0, row=0, columnspan=8)

# Pavé numérique:
number0 = tk.Button(racine, text="0", font=("50"), command=nb0, padx=70)
number0.grid(column=0, row=8, columnspan=4, rowspan=2)
number1 = tk.Button(racine, text="1", font=("30"), command=nb1, padx=23.5)
number1.grid(column=0, row=1, columnspan=2, rowspan=2)
number2 = tk.Button(racine, text="2", font=("50"), command=nb2, padx=23.5)
number2.grid(column=2, row=1, columnspan=2, rowspan=2)
number3 = tk.Button(racine, text="3", font=("30"), command=nb3, padx=23.5)
number3.grid(column=4, row=1, columnspan=2, rowspan=2)
number4 = tk.Button(racine, text="4", font=("30"), command=nb4, padx=23.5)
number4.grid(column=0, row=4, columnspan=2, rowspan=2)
number5 = tk.Button(racine, text="5", font=("30"), command=nb5, padx=23.5)
number5.grid(column=2, row=4, columnspan=2, rowspan=2)
number6 = tk.Button(racine, text="6", font=("30"), command=nb6, padx=23.5)
number6.grid(column=4, row=4, columnspan=2, rowspan=2)
number7 = tk.Button(racine, text="7", font=("30"), command=nb7, padx=23.5)
number7.grid(column=0, row=6, columnspan=2, rowspan=2)
number8 = tk.Button(racine, text="8", font=("30"), command=nb8, padx=23.5)
number8.grid(column=2, row=6, columnspan=2, rowspan=2)
number9 = tk.Button(racine, text="9", font=("30"), command=nb9, padx=23.5)
number9.grid(column=4, row=6, columnspan=2, rowspan=2)

# Opérations:
egal = tk.Button(racine, text="=", font=("30"), command=calcul, padx=23.5)
egal.grid(column=6, row=1, columnspan=4, rowspan=2)
plus = tk.Button(racine, text="+", font=("30"), command=addition, padx=23.5)
plus.grid(column=6, row=4, columnspan=2, rowspan=2)
moins = tk.Button(racine, text="-", font=("30"), command=soustraction, padx=23.5)
moins.grid(column=6, row=6, columnspan=2, rowspan=2)
multiplication = tk.Button(racine, text="x", font=("30"), command=multiplication, padx=23.5)
multiplication.grid(column=6, row=8, columnspan=2, rowspan=2)
diviser = tk.Button(racine, text="/", font=("30"), command=division, padx=25)
diviser.grid(column=4, row=8, columnspan=2, rowspan=2)


# mainloop.
racine.mainloop()

""" def calcul():
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
    print(lst_calcul[0], lst_calcul[1]) """

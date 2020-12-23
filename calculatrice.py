import tkinter as tk

HEIGHT, WIDTH = 4, 40

# liste
liste = []
lst_calcul = []
operation = []
test_flo = []

# fonction:


def addition(event):
    if 1 in test_flo:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = float(c)
        label.config(text=c)
    else:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = int(c)
        label.config(text=c)
    lst_calcul.append(c)
    lst_calcul.append("+")
    liste.clear()
    label.config(text="")
    operation.append(1)
    print("YES")


def multiplication(event):
    if 1 in test_flo:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = float(c)
        label.config(text=c)
    else:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = int(c)
        label.config(text=c)
    lst_calcul.append(c)
    lst_calcul.append("*")
    liste.clear()
    label.config(text="")
    operation.append(2)
    print("YES")


def division(event):
    if 1 in test_flo:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = float(c)
        label.config(text=c)
    else:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = int(c)
        label.config(text=c)
    lst_calcul.append(c)
    lst_calcul.append("/")
    liste.clear()
    label.config(text="")
    operation.append(3)


def soustraction(event):
    if 1 in test_flo:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = float(c)
        label.config(text=c)
    else:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = int(c)
        label.config(text=c)
    lst_calcul.append(c)
    lst_calcul.append("-")
    liste.clear()
    label.config(text="")
    operation.append(4)


def calcul(event):
    if 1 in test_flo:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = float(c)
        label.config(text=c)
    else:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = int(c)
        label.config(text=c)
    lst_calcul.append(c)
    liste_cpt = []
    cpt = 0
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
                    x = lst_calcul[cpt - 1] / lst_calcul[cpt + 1]
                    lst_calcul.insert(cpt + 2, x)
                    liste_cpt.append(cpt)
                    cpt += 1
                    condi += 1
            i += 1
    for j in range(len(liste_cpt)):
        nbr = len(liste_cpt) - 1 - j
        del lst_calcul[liste_cpt[nbr] - 1:liste_cpt[nbr] + 2]
    res = lst_calcul[0]
    for k in range(len(lst_calcul)):
        val = lst_calcul[k]
        if "+" == val:
            res += lst_calcul[k + 1]
        elif "-" == val:
            res -= lst_calcul[k + 1]
    label.config(text=res)


def nbrFlotant(event):
    test_flo.append(1)
    liste.append(".")


def cancel():
    label.config(text="")
    liste.clear()
    lst_calcul.clear()
    operation.clear()
    test_flo.clear()


def affichage():
    if 1 in test_flo:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = float(c)
        label.config(text=c)
    else:
        c = "0"
        for i in range(len(liste)):
            c += str(liste[i])
        c = int(c)
        label.config(text=c)


def nb0(event):
    liste.append(0)
    affichage()


def nb1(event):
    liste.append(1)
    affichage()


def nb2(event):
    liste.append(2)
    affichage()


def nb3(event):
    liste.append(3)
    affichage()


def nb4(event):
    liste.append(4)
    affichage()


def nb5(event):
    liste.append(5)
    affichage()


def nb6(event):
    liste.append(6)
    affichage()


def nb7(event):
    liste.append(7)
    affichage()


def nb8(event):
    liste.append(8)
    affichage()


def nb9(event):
    liste.append(9)
    affichage()


# interface:
racine = tk.Tk()
label = tk.Label(racine, text="", fg="white", bg="black",
                 width=WIDTH, height=HEIGHT, anchor='e', font=("30"))
label.grid(column=0, row=0, columnspan=8)

# Pavé numérique:
number0 = tk.Button(racine, text="0", font=(
    "50"), command=lambda: nb0(0), padx=23.5)
number0.grid(column=0, row=5, columnspan=2)
racine.bind('<KeyPress-0>', nb0)
number1 = tk.Button(racine, text="1", font=(
    "30"), command=lambda: nb1(1), padx=23.5)
number1.grid(column=0, row=2, columnspan=2)
racine.bind("<KeyPress-1>", nb1)
number2 = tk.Button(racine, text="2", font=(
    "50"), command=lambda: nb2(2), padx=23.5)
number2.grid(column=2, row=2, columnspan=2)
racine.bind("<KeyPress-2>", nb2)
number3 = tk.Button(racine, text="3", font=(
    "30"), command=lambda: nb3(3), padx=23.5)
number3.grid(column=4, row=2, columnspan=2)
racine.bind("<KeyPress-3>", nb3)
number4 = tk.Button(racine, text="4", font=(
    "30"), command=lambda: nb4(4), padx=23.5)
number4.grid(column=0, row=3, columnspan=2)
racine.bind("<KeyPress-4>", nb4)
number5 = tk.Button(racine, text="5", font=(
    "30"), command=lambda: nb5(5), padx=23.5)
number5.grid(column=2, row=3, columnspan=2)
racine.bind("<KeyPress-5>", nb5)
number6 = tk.Button(racine, text="6", font=(
    "30"), command=lambda: nb6(6), padx=23.5)
number6.grid(column=4, row=3, columnspan=2)
racine.bind("<KeyPress-6>", nb6)
number7 = tk.Button(racine, text="7", font=(
    "30"), command=lambda: nb7(7), padx=23.5)
number7.grid(column=0, row=4, columnspan=2)
racine.bind("<KeyPress-7>", nb7)
number8 = tk.Button(racine, text="8", font=(
    "30"), command=lambda: nb8(8), padx=23.5)
number8.grid(column=2, row=4, columnspan=2)
racine.bind("<KeyPress-8>", nb8)
number9 = tk.Button(racine, text="9", font=(
    "30"), command=lambda: nb9(9), padx=23.5)
number9.grid(column=4, row=4, columnspan=2)
racine.bind("<KeyPress-9>", nb9)

# Opérations:
egal = tk.Button(racine, text="=", font=(
    "30"), command=lambda: calcul("="), padx=23.5)
egal.grid(column=6, row=2, columnspan=4)
plus = tk.Button(racine, text="+", font=("30"),
                 command=lambda: addition("+"), padx=23.5)
plus.grid(column=6, row=3, columnspan=2)
moins = tk.Button(racine, text="-", font=("30"),
                  command=lambda: soustraction("-"), padx=23.5)
moins.grid(column=6, row=4, columnspan=2)
multiplications = tk.Button(racine, text="x", font=(
    "30"), command=lambda: multiplication("*"), padx=23.5)
multiplications.grid(column=6, row=5, columnspan=2)
diviser = tk.Button(racine, text="/", font=("30"),
                    command=lambda: division("/"), padx=25)
diviser.grid(column=4, row=5, columnspan=2)
flotant = tk.Button(racine, text=".", font=(
    "30"), command=lambda: nbrFlotant("."), padx=23.5)
flotant.grid(column=2, row=5, columnspan=2)
effacer = tk.Button(racine, text="Effacer", font=("30"),
                    command=cancel, padx=145)
effacer.grid(column=1, row=1, columnspan=8)

# mainloop.
racine.mainloop()

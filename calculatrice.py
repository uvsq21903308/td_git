import tkinter as tk

# fonction:
def addition():
    return


# interface:
racine =  tk.Tk()
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0)
number1 = tk.Button(racine, text="1",font=("30"), command=demCouleur)
number2 = tk.Button(racine, text="2",font=("30"), command=demCouleur)
number3 = tk.Button(racine, text="3",font=("30"), command=demCouleur)
number4 = tk.Button(racine, text="4",font=("30"), command=demCouleur)
number5 = tk.Button(racine, text="5",font=("30"), command=demCouleur)
number6 = tk.Button(racine, text="6",font=("30"), command=demCouleur)
number7 = tk.Button(racine, text="7",font=("30"), command=demCouleur)
number8 = tk.Button(racine, text="8",font=("30"), command=demCouleur)
number9 = tk.Button(racine, text="9",font=("30"), command=demCouleur)
plus = tk.Button(racine, text="+",font=("30"), command=demCouleur)
moins = tk.Button(racine, text="-",font=("30"), command=demCouleur)
diviser = tk.Button(racine, text="/",font=("30"), command=demCouleur)
multiplication = tk.Button(racine, text="*",font=("30"), command=demCouleur)
# mainloop.
racine.mainloop()

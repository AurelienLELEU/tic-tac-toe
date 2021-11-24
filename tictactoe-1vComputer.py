import tkinter as tk
import numpy as np
import Computer

global fin, grille, canvas, fenetre, score, j1, j2

dif = s = p = i = scorej1 = scorej2 = 0
taille = 100
start = tk.Tk()
joueur1 = tk.StringVar()
labeluti2 = tk.Label(start, text="Player Name ?")
entryuti2 = tk.Entry(start, textvariable=joueur1)


def btres():
    global i, grille, canvas, fenetre, p, joueur1, score, scorej1, scorej2, j1, j2, s
    if joueur1.get() != "":
        s = 0
        if p == 0:
            start.destroy()
            j2 = joueur1.get()
            j1 = "Computer"
        if p > 0:
            fenetre.destroy()
        fenetre = tk.Tk()
        i = 0
        grille = np.zeros((3, 3))
        canvas = tk.Canvas(fenetre, width=taille * 3, height=taille * 3, background="white")
        canvas.create_line(2 * taille, 0, 2 * taille, 3 * taille, width="7", fill="black")
        canvas.create_line(taille, 0, taille, 3 * taille, width="7", fill="black")
        canvas.create_line(0, taille, 3 * taille, taille, width="7", fill="black")
        canvas.create_line(0, 2 * taille, 3 * taille, 2 * taille, width="7", fill="black")
        canvas.bind("<Button-1>", clic)
        canvas.grid()
        if p > 0:
            fin.destroy()
        p += 1
    return


def ordistp():
    global dif
    dif = 0
    btres()


def ordirdm():
    global dif
    dif = 1
    btres()


difbot0 = tk.Button(start, text="Dumb Bot", command=ordistp)
difbot1 = tk.Button(start, text="Random Bot", command=ordirdm)

print(dif)
if dif == 0:
    ordi = Computer.IA_stp(1)
else:
    ordi = Computer.IA_rdm(2)


def croix(x, y):
    canvas.create_line(x + 20, y + 20, x + (taille - 20), y + (taille - 20), width="7", fill="blue")
    canvas.create_line(x + 20, y + (taille - 20), x + (taille - 20), y + 20, width="7", fill="blue")


def rond(x, y):
    canvas.create_oval(x + 20, y + 20, x + (taille - 20), y + (taille - 20), width="7", outline="red")


def case(x, y):
    if x < taille:
        colonne = 0
    elif x < 2 * taille:
        colonne = 1
    else:
        colonne = 2
    if y < taille:
        ligne = 0
    elif y < 2 * taille:
        ligne = 1
    else:
        ligne = 2
    return ligne, colonne


def coordonnees(ligne, colonne):
    if ligne == 0:
        y = 0
    elif ligne == 1:
        y = taille
    else:
        y = 2 * taille
    if colonne == 0:
        x = 0
    elif colonne == 1:
        x = taille
    else:
        x = 2 * taille
    return x, y


def fwin(x, y):
    global fin, scorej2, scorej1, score
    fin = tk.Tk()

    if i == 9:
        labelnul = tk.Label(fin, text="Draw!")
        labelnul.grid()
        restart()
    elif grille[x, y] == 1:
        labelwin = tk.Label(fin, text=j2 + " Won")
        labelwin.grid()
        restart()
        scorej2 += 1
    else:
        labelwin = tk.Label(fin, text=j1 + " Won")
        labelwin.grid()
        restart()
        scorej1 += 1
    score = j1, scorej1, "-", scorej2, j2
    labelscore = tk.Label(fin, text=score)
    labelscore.grid()


def restart():
    buttonrestart = tk.Button(fin, text="Restart ?", command=btres)
    buttonrestart.grid()


def align(ligne, colonne):
    global i, s
    if grille[ligne, 0] == grille[ligne, 1] == grille[ligne, 2] and grille[ligne, 0] != 0:
        fwin(ligne, colonne)
        canvas.create_line(0.5 * taille, (ligne + 0.5) * taille, 2.5 * taille, (ligne + 0.5) * taille,
                           width=taille / 10, fill="black")
        fwin(ligne, colonne)
        canvas.unbind("<Button-1>")
        s = "stop"
    elif grille[0, colonne] == grille[1, colonne] == grille[2, colonne] and grille[0, colonne] != 0:
        fwin(ligne, colonne)
        canvas.create_line((colonne + 0.5) * taille, 0.5 * taille, (colonne + 0.5) * taille, 2.5 * taille,
                           width=taille / 10, fill="black")
        canvas.unbind("<Button-1>")
        s = "stop"
    elif grille[0, 0] == grille[1, 1] == grille[2, 2] and grille[0, 0] != 0:
        fwin(ligne, colonne)
        canvas.create_line(0.5 * taille, 0.5 * taille, 2.5 * taille, 2.5 * taille,
                           width=taille / 10, fill="black")
        canvas.unbind("<Button-1>")
        s = "stop"
    elif grille[0, 2] == grille[1, 1] == grille[2, 0] and grille[0, 2] != 0:
        fwin(ligne, colonne)
        canvas.create_line(2.5 * taille, 0.5 * taille, 0.5 * taille, 2.5 * taille,
                           width=taille / 10, fill="black")
        canvas.unbind("<Button-1>")
        s = "stop"
    elif i == 9:
        fwin(ligne, colonne)
    return s


def alignement(ligne, colonne):
    global i
    align(ligne, colonne)
    i += 1


def clic(evenement):
    global i
    ligne, colonne = case(evenement.x, evenement.y)
    x, y = coordonnees(ligne, colonne)
    if grille[ligne, colonne] == 0:
        croix(x, y)
        grille[ligne, colonne] = 1
        alignement(ligne, colonne)
        tourbot()


def tourbot():
    if s != "stop":
        ligne, colonne = ordi.joue(grille.copy())
        x, y = coordonnees(ligne, colonne)
        rond(x, y)
        grille[ligne, colonne] = 2
        alignement(ligne, colonne)


labeluti2.grid()
entryuti2.grid()
entryuti2.grid()
difbot0.grid()
difbot1.grid()
tk.mainloop()

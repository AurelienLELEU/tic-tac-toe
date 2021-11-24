import tkinter as tk
import numpy as np
global fin, grille, canvas, fenetre, score, j1, j2


p = 0
taille = 100
i = 0
scorej1 = 0
scorej2 = 0
start = tk.Tk()
start.title("Tic Tac Toe")
joueur1 = tk.StringVar()
joueur2 = tk.StringVar()
labeluti2 = tk.Label(start, text="Player 1 ?")
entryuti2 = tk.Entry(start, textvariable=joueur1)
labelpass2 = tk.Label(start, text="Player 2 ?")
entrypass2 = tk.Entry(start, textvariable=joueur2)


def croix(x, y):
    canvas.create_line(x + 20, y + 20, x + (taille-20), y + (taille-20), width="7", fill="blue")
    canvas.create_line(x + 20, y + (taille-20), x + (taille-20), y + 20, width="7", fill="blue")


def rond(x, y):
    canvas.create_oval(x + 20, y + 20, x + (taille-20), y + (taille-20), width="7", outline="red")


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
        y = 2*taille
    if colonne == 0:
        x = 0
    elif colonne == 1:
        x = taille
    else:
        x = 2*taille
    return x, y


def clic(evenement):
    global i
    ligne, colonne = case(evenement.x, evenement.y)
    x, y = coordonnees(ligne, colonne)
    if grille[ligne, colonne] == 0:
        i += 1
        if i % 2 == 0:
            croix(x, y)
            grille[ligne, colonne] = 1
            alignement(ligne, colonne)
        else:
            rond(x, y)
            grille[ligne, colonne] = -1
            alignement(ligne, colonne)


def btres():
    global i, grille, canvas, fenetre, p, joueur1, joueur2, score, scorej1, scorej2, j1, j2
    if joueur1.get() != joueur2.get() != "":
        if p == 0:
            start.destroy()
            j1 = joueur1.get()
            j2 = joueur2.get()
        if p > 0:
            fenetre.destroy()
        fenetre = tk.Tk()
        fenetre.title("Tic Tac Toe")
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


def fwin(x, y):
    global fin, scorej2, scorej1, score
    fin = tk.Tk()
    fin.title("End !")

    if i == 9:
        labelnul = tk.Label(fin, text="Draw !")
        labelnul.grid()
        restart()
    elif grille[x, y] == 1:
        labelwin = tk.Label(fin, text=j2+" Won !")
        labelwin.grid()
        restart()
        scorej2 += 1
    else:
        labelwin = tk.Label(fin, text=j1+" Won !")
        labelwin.grid()
        restart()
        scorej1 += 1
    score = j1, scorej1, " - ", scorej2, j2
    print(score)
    labelscore = tk.Label(fin, text=score)
    labelscore.grid()


def restart():
    buttonrestart = tk.Button(fin, text="Restart ?", command=btres)
    buttonrestart.grid()


def alignement(ligne, colonne):
    global i
    if grille[ligne, 0] == grille[ligne, 1] == grille[ligne, 2] and grille[ligne, 0] != 0:
        fwin(ligne, colonne)
        canvas.create_line(0.5 * taille, (ligne + 0.5) * taille, 2.5 * taille, (ligne + 0.5) * taille,
                           width=taille / 10, fill="black")
        canvas.unbind("<Button-1>")
    elif grille[0, colonne] == grille[1, colonne] == grille[2, colonne] and grille[0, colonne] != 0:
        fwin(ligne, colonne)
        canvas.create_line((colonne + 0.5) * taille, 0.5 * taille, (colonne + 0.5) * taille, 2.5 * taille,
                           width=taille / 10, fill="black")
        canvas.unbind("<Button-1>")
    elif grille[0, 0] == grille[1, 1] == grille[2, 2] and grille[0, 0] != 0:
        fwin(ligne, colonne)
        canvas.create_line(0.5 * taille, 0.5 * taille, 2.5 * taille, 2.5 * taille,
                           width=taille / 10, fill="black")
        canvas.unbind("<Button-1>")
    elif grille[0, 2] == grille[1, 1] == grille[2, 0] and grille[0, 2] != 0:
        fwin(ligne, colonne)
        canvas.create_line(2.5 * taille, 0.5 * taille, 0.5 * taille, 2.5 * taille,
                           width=taille / 10, fill="black")
        canvas.unbind("<Button-1>")
    elif i == 9:
        fwin(ligne, colonne)


buttonregi = tk.Button(start, text="Register", command=btres)
labeluti2.grid()
entryuti2.grid()
labelpass2.grid()
entrypass2.grid()
buttonregi.grid()
tk.mainloop()

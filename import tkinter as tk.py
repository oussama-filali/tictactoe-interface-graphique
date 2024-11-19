import tkinter as tk
from tkinter import ttk


# Fonction pour réinitialiser la partie
def recommencer():
    global tour, grille, joueur_x, joueur_o
    # Réinitialisation de la grille
    grille = [["" for i in range(3)] for j in range(3)]
    tour = "X"  # Le premier tour commence avec le joueur X
    for i in range(3):
        for j in range(3):
            boutons[i][j].config(text="", state=tk.NORMAL, bg="SystemButtonFace", fg="black") # type: ignore
    label_tour.config(text="Tour de X") # type: ignore
    label_gagnant.config(text="") # type: ignore
    update_score()


# Fonction pour vérifier si quelqu'un a gagné
def verifier_victoire():
    global joueur_x, joueur_o
    # Vérification des lignes, colonnes et diagonales
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != "":
            colorier_gagnants([(i, 0), (i, 1), (i, 2)])
            return grille[i][0]
        if grille[0][i] == grille[1][i] == grille[2][i] != "":
            colorier_gagnants([(0, i), (1, i), (2, i)])
            return grille[0][i]

    if grille[0][0] == grille[1][1] == grille[2][2] != "":
        colorier_gagnants([(0, 0), (1, 1), (2, 2)])
        return grille[0][0]

    if grille[0][2] == grille[1][1] == grille[2][0] != "":
        colorier_gagnants([(0, 2), (1, 1), (2, 0)])
        return grille[0][2]

    return None


# Fonction pour colorier les boutons gagnants
def colorier_gagnants(cells):
    for i, j in cells:
        boutons[i][j].config(bg="lightgreen") # type: ignore


# Fonction pour vérifier si le jeu est en égalité
def verifier_egalite():
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "":
                return False
    return True


# Fonction pour mettre à jour le score et l'affichage du tour
def update_score():
    label_score_x.config(text=f"Joueur X\n  {joueur_x}") # type: ignore
    label_score_o.config(text=f"Joueur O\n  {joueur_o}") # type: ignore


# Fonction qui est appelée quand un bouton est cliqué
def jouer(i, j):
    global tour, joueur_x, joueur_o
    if grille[i][j] == "" and label_gagnant.cget("text") == "": # type: ignore
        # Mettre à jour la grille et le bouton
        grille[i][j] = tour
        # Définir la couleur en fonction du joueur
        couleur_texte = "red" if tour == "X" else "blue"

        # Mettre à jour le texte et la couleur du bouton sans le désactiver
        boutons[i][j].config(text=tour, fg=couleur_texte, font=("Arial", 40)) # type: ignore

        # Vérifier la victoire
        gagnant = verifier_victoire()
        if gagnant:
            if gagnant == "X":
                joueur_x += 1
                label_gagnant.config(text="Félicitations, X a gagné!", fg="green") # type: ignore
            else:
                joueur_o += 1
                label_gagnant.config(text="Félicitations, O a gagné!", fg="green") # type: ignore
        elif verifier_egalite():  # Si égalité
            for i in range(3):
                for j in range(3):
                    boutons[i][j].config(bg="yellow")  # type: ignore # Colorier tous les boutons en jaune
            label_gagnant.config(text="Égalité !") # type: ignore
        else:
            # Changer le tour
            tour = "O" if tour == "X" else "X"
            label_tour.config(text=f"Tour de {tour}") # type: ignore

        update_score()


# Initialisation de la fenêtre
fenetre = tk.Tk()
fenetre.title("Tic-Tac-Toe")

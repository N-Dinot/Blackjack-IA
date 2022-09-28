from tkinter import *
from random import *

fenetre = Tk()
# Création de la fenêtre de jeu
fenetre.title("Blackjack solo")
# Nom de la fenêtre
fenetre.config(bg="#1b1b1b")
# Couleur du fond de la fenêtre
fenetre.attributes('-fullscreen', True)
# Taille de la fenêtre

def creerjeu():
    """Crée la main de départ du joueur et de l'IA"""
    shuffle(paquet)
    # On mélange le paquet
    for i in range(2):
        # On fait piocher 2 cartes au joueur et à l'IA
        j.append(paquet.pop())
        ia.append(paquet.pop())


def pj():
    """Permet au joueur de piocher"""
    if paquet != []:
        j.append(paquet.pop())
        # Si le paquet n'est pas vide, alors on autorise à piocher
        mj.set('Votre main : ' + str(j))
        tj.set('Votre score est : ' + str(sum(j)))
        actj.set("Le joueur pioche !")
        p.set("Cartes restantes dans le paquet : " + str(len(paquet)))
    else:
        actj.set("Il n'y a plus de cartes dans le paquet !")
        # Sinon, on le previent
    pia()
    # On fait jouer l'IA après nous


def pia():
    """Permet à l'IA de piocher"""
    if sum(ia) < 16:
        # Si l'IA a moins de 16 points, elle pioche automatiquement (car trop loin de l'objectif) si le paquet n'est pas vide
        if paquet != []:
            ia.append(paquet.pop())
            actia.set("L'IA pioche !")
            p.set("Cartes restantes dans le paquet : " + str(len(paquet)))
    elif sum(ia) >= 16 and sum(ia) < 18:
        # Si l'IA a entre 16 points inclus et 18, alors elle a 3 chances sur 10 de prendre le risque de piocher une autre carte, si le paquet n'est pas vide
        if paquet != []:
            probap = randint(0, 10)
            if probap < 3:
                ia.append(paquet.pop())
                actia.set("L'IA pioche !")
                p.set("Cartes restantes dans le paquet : " + str(len(paquet)))
    else:
        actia.set("L'IA passe son tour")
        # Si l'IA ne remplie pas les conditons, alors elle passe son tour


def valider():
    """Décide, si le joueur passe son tour, de si l'IA doit le passer aussi ou non"""
    actj.set("Le joueur passe son tour")
    if sum(ia) >= 16:
        # Si l'IA a 16 points ou plus, alors elle a 7 chances sur 10 de passer sont tour aussi
        probaf = randint(0, 10)
        if probaf <= 7:
            actia.set("L'IA passe son tour")
            fin()
    elif paquet == []:
        # Même si elle n'a pas  assez de points, elle passe son tour si le paquet est vide
        actia.set("L'IA passe son tour")
        fin()
    elif sum(ia) < 16 and paquet != []:
        # Si le paquet n'est pas vide et qu'elle n'a pas assez de points, alors elle pioche
        pia()


def fin():
    """Détermine le gagnant ou une égalité une fois que le joueur et l'IA on passé leur tour"""
    if sum(j) < sum(ia) and sum(ia) <= 21:
        act.set("L'IA l'emporte ! Elle détient plus de points que vous, vous gagnerez une prochaine fois...")
        tia.set("Score de l'IA : " + str(sum(ia)))
        mia.set("Main de l'IA : " + str(ia))
    elif sum(j) > sum(ia) and sum(j) <= 21:
        act.set("Bravo ! Vous avez plus de points que l'IA, vous l'emportez !")
        tia.set("Score de l'IA : " + str(sum(ia)))
        mia.set("Main de l'IA : " + str(ia))
    elif sum(j) <= 21 and sum(ia) > 21:
        act.set("Bravo ! L'IA a dépassé 21, vous l'emportez !")
        tia.set("Score de l'IA : " + str(sum(ia)))
        mia.set("Main de l'IA : " + str(ia))
    elif sum(j) > 21 and sum(ia) <= 21:
        act.set("L'IA l'emporte ! Vous avez dépassé 21, vous gagnerez une prochaine fois...")
        tia.set("Score de l'IA : " + str(sum(ia)))
        mia.set("Main de l'IA : " + str(ia))
    elif sum(j) > 21 and sum(ia) > 21:
        act.set("Personne ne l'emporte ! Dommage, vous avez tout les deux dépassé 21...")
        tia.set("Score de l'IA : " + str(sum(ia)))
        mia.set("Main de l'IA : " + str(ia))
    elif sum(j) == sum(ia):
        act.set("Personne ne l'emporte ! Dommage, vous avez le même score...")
        tia.set("Score de l'IA : " + str(sum(ia)))
        mia.set("Main de l'IA : " + str(ia))


def quitter():
    """Ferme la fenêtre lorsqu'on clique sur le bouton correspondant"""
    fenetre.destroy()


def rejouer():
    """Permet de relancer une partie lorsqu'on clique sur le bouton correspondant"""
    a = 0
    while paquet != []:
        # On remet le paquet à 0
        paquet.pop()
    while j != []:
        # On remet la main du joueur à 0
        j.pop()
    while ia != []:
        # On remet la main de l'IA à 0
        ia.pop()
    for i in range(10):
        # On re-rempli le paquet
        a = a + 1
        paquet.append(a)
    creerjeu()
    # Et on re'mélange les cartes et donnont la main du joueur et de l'IA...
    p.set("Cartes restantes dans le paquet : " + str(len(paquet)))
    # Toute la fin permet de réinitialiser l'affichage
    actia.set("")
    actj.set("")
    act.set("")
    tia.set("Score de l'IA : " + str(ia[0] + ia[1]) + " + ? ")
    mia.set("Main de l'IA : " + str(ia[0]) + " + " + str(ia[1]) + " + ?")
    mj.set('Votre main : ' + str(j))
    tj.set('Votre score est : ' + str(sum(j)))


##PROGRAMME PRINCIPAL##

paquet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Valeurs des cartes dans le paquet (initialisation du paquet)
j = []
# Initialisation de la main du joueur
ia = []
# Initialisation de la main de l'IA
creerjeu()

h1 = Label(fenetre, text="", relief=FLAT, fg="white", bg="grey9", width=120, height=45, bd=0.5)
h1.place(x=335, y=125)
h3 = Label(fenetre, text="", relief=FLAT, fg="white", bg="grey15", width=32, height=31, bd=0.5)
h3.place(x=93, y=218)
h2 = Label(fenetre, text="", relief=FLAT, fg="white", bg="grey9", width=30, height=30, bd=0.5)
h2.place(x=100, y=225)
titreh2 = Label(fenetre, text="COMMANDES", relief=FLAT, fg="white", bg="grey8", width=17, height=3, font=("Courier"))
titreh2.place(x=102, y=240)
titre = Label(fenetre, text="BLACKJACK", relief=FLAT, fg="white", bg="grey7", width=22, height=1, font=("Courier", 30))
titre.place(x=500, y=30)
description = Label(fenetre,
                    text="Comment se joue le blackjack ?" + '\n' + '\n' + '\n' + '\n' + "Le Blackjack est un jeu de carte dans lequel" + '\n' + "les joueurs doivent se rapprocher le plus possible" + '\n' + " de 21, en piochant les cartes du paquet." + '\n' + '\n' + "Le paquet contient les cartes suivantes : " + '\n' + '\n' + "1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10" + '\n' + '\n' + '\n' + "Lors du commencement, chaque joueur pioche" + '\n' + "automatiquement 2 cartes que chacun peut voir." + '\n' + '\n' + "UNE FOIS qu'une carte a été PIOCHÉE, elle est" + '\n' + "retirée du paquet et ne peut pas être repiochée !" + '\n' + '\n' + "Toute carte piochée parla suite n'est visible que" + '\n' + "par son propriétaire ; le nombre présent sur la carte" + '\n' + "représente le nombre de point qu'elle vaut." + '\n' + '\n' + "Si le chiffre 21 est dépassé, alors c'est perdu" + '\n' + "(même si l'adversaire est bien en dessous de 21) !" + '\n' + '\n' + "Si vous avez peur de dépasser 21 lors de la" + '\n' + "prochaine pioche, alors vous pouvez passer" + '\n' + "votre tour ; tant qu'un autre joueur veut" + '\n' + "piocher, la partie continue." + '\n' + '\n' + "Ce n'est que lors de la fin de la partie que" + '\n' + "que les scores sont révélés et le gagnant désigné !",
                    relief=FLAT, fg="white", bg="grey7", width=40, height=40)
description.place(x=1200, y=125)

bouton_reinit = Button(fenetre, text="Quitter", width=5, bg="grey7", fg="red", command=quitter, relief=FLAT, activebackground='red')
# On crée le bouton pour quitter
bouton_reinit.place(x=10, y=10)
bouton_p = Button(fenetre, text="Pioche", width=15, height=2, bg="grey7", fg="orange", command=pj, relief=FLAT, activebackground='grey8')
# On crée le bouton pour piocher
bouton_p.place(x=150, y=405)
bouton_v = Button(fenetre, text="Valider la main", width=15, height=2, bg="grey7", fg="dodger blue", command=valider, relief=FLAT, activebackground='grey8')
# On crée le bouton pour passer son tour
bouton_v.place(x=150, y=455)
bouton_r = Button(fenetre, text="Rejouer", width=15, height=2, bg="grey7", fg="spring green", command=rejouer, relief=FLAT, activebackground='grey8')
# On crée le bouton pour relancer une partie
bouton_r.place(x=150, y=505)

p = StringVar()
# On crée l'affichage de :
prep = Label(fenetre, textvariable=p, fg='spring green', bg='grey7')
# Nombre de cartes restantes
prep.place(x=115, y=365)
p.set("Cartes restantes dans le paquet : " + str(len(paquet)))

actia = StringVar()
actiarep = Label(fenetre, textvariable=actia, fg='spring green', bg='grey9', font=("Fixedsys"))
actiarep.place(x=365, y=680)
actia.set("")
# Ce que choisie de faire l'IA

actj = StringVar()
actjrep = Label(fenetre, textvariable=actj, fg='spring green', bg='grey9', font=("Fixedsys"))
actjrep.place(x=365, y=230)
actj.set("")
# Ce que choisi de faire le joueur

act = StringVar()
actrep = Label(fenetre, textvariable=act, fg='spring green', bg='grey9', font=("Fixedsys"))
actrep.place(x=420, y=430)
act.set("")
# Les résultats d'une partie

tia = StringVar()
tiarep = Label(fenetre, textvariable=tia, fg='dodger blue', bg='grey7')
tiarep.place(x=365, y=720)
tia.set("Score de l'IA : " + str(ia[0] + ia[1]) + " + ? ")
# Le score que détient l'IA

mia = StringVar()
miarep = Label(fenetre, textvariable=mia, fg='dodger blue', bg='grey7')
miarep.place(x=365, y=760)
mia.set("Main de l'IA : " + str(ia[0]) + " + " + str(ia[1]) + " + ?")
# La main de l'IA

mj = StringVar()
mjr = Label(fenetre, textvariable=mj, fg='orange', bg='grey7')
mjr.place(x=365, y=150)
mj.set('Votre main : ' + str(j))
# La main du joueur

tj = StringVar()
tjrep = Label(fenetre, textvariable=tj, fg='orange', bg='grey7')
tjrep.place(x=365, y=190)
tj.set('Votre score est : ' + str(sum(j)))
# Le score que détient le joueur

fenetre.mainloop()
# Exécution de la fenêtre

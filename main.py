"""
Sandra Nitchi
Groupe 405
TP2

Ce programme est un jeu devinette
le joueur choisis un nombre minimale et maximale, et doivent ensuite essayer de deviner le nombre aleatoir choisi entre le max et min
le programme va indiquer si les essaies sont plus petits ou plus grands que la nombre choissi, jusqu'a que le joueur la devine
le joueur va ensuite avoir l'option de rejouer, ou quitter
"""


import random

def bornes():

    """
    Fonction qui sert a definir la borne minimale et maximale du jeu de devinette
    """

    global minimum, maximum
    minimum = int(input("Choissisez un nombre minimale:"))
    maximum = int(input("Choissisez un nombre maximale:"))
    print(f"jai choissi une nombre entre {minimum} et {maximum}! Essayez de la deviner")

def jeu_devinette():

    """
    Fonction du jeu de devinnette
    il compte le nombre d'essaies, indique au joueur si le nombre est plus grand ou plus petit que la reponse, et offre l'option de rejouer apres que le joueur a gagné
    """

    bornes()
    number = random.randint(minimum, maximum)
    guess_counter = 1

    guess = int(input(f"devinez la nombre de {minimum} a {maximum}"))

    while guess != number:
        if guess < number:
            print(f"le nombre est plus grand que {guess}")
            guess_counter = guess_counter + 1
            guess = int(input("devinez la nombre de"))

        else:
            print(f"le nombre est plus petit que {guess}")
            guess_counter = guess_counter + 1
            guess = int(input("devinez la nombre de 1 a 100"))

    print(f"bravo! {guess} etait en fait la numero")
    print(f"Ca vous a pris {guess_counter} essaies")
    answer = str(input("voulez vous rejouer? (y/n)"))
    if answer == "y" :
        jeu_devinette()
    else:
        print("au revoir")
jeu_devinette()


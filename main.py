#sandra nitchi
#TP2

import random

def bornes():
    global minimum, maximum
    minimum = int(input("Choissisez un nombre minimale:"))
    maximum = int(input("Choissisez un nombre maximale:"))
    print(f"jai choissi une nombre entre {minimum} et {maximum}! Essayez de la deviner")

def jeu_devinette():

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


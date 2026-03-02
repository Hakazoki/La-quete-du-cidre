from random import randint

class Dice:
    def lancer(nb, montant):
        score = 0
        for e in range(nb-1):
            lancer = randint(1,montant)
            score += lancer
            print(lancer)
        return score
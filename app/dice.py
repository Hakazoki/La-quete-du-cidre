from random import randint

class Dice:
    @staticmethod
    def lancer(nb, montant):
        """
        Lancer de dé
        Paramètres : nb (int) -> nombre de lancers / montant (int) -> nombre de faces du dé
        Sortie : Renvoie un tuple contenant le score total des lancers et une liste contenant le résultat de chaque lancer indépendament
        Initialisez une variable et assignez-lui Dice.lancer(nb,montant) pour lancer autant de dés que vous voulez
        Votre variable contiendra le score total
        """
        resultats = []
        score = 0
        for e in range(nb):
            lancer = randint(1,montant)
            score += lancer
            resultats.append(lancer)
            print(f"Lancé du dé : {lancer}")
        return (score, resultats)
from random import randint

class Dice:
    @staticmethod
    def lancer( nb = 1, nb_faces=20):
        """
        Lancer de dé
        Paramètres : nb (int) -> nombre de lancers / nb_faces (int) -> nombre de faces du dé
        Sortie : Renvoie une liste contenant le score total des lancers et une liste contenant le résultat de chaque lancer indépendament
        Initialisez une variable et assignez-lui Dice.lancer(nb,montant) pour lancer autant de dés que vous voulez
        """
        resultats = []
        score = 0
        for e in range(nb):
            lancer = randint(1,nb_faces)
            score += lancer
            resultats.append(lancer)
            print(f"Lancé du dé : {lancer}")
        return [score, resultats]
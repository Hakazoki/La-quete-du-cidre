from random import randint

class Dice:
    def __init__(self, nb_faces = 6, nb_dices  =1, additionnal_bonus = 0):
        """
        Exemple : Epée courte 2D4 + 1 sera appelé Dice(4, 2, 1)
        """
        self.nb_faces = nb_faces
        self.nb_dices = nb_dices
        self.additionnal_bonus = additionnal_bonus


    def jeter(self) -> int:
        """ Simple jet de dé. Retourne le total"""
        total = self.additionnal_bonus
        for _ in range(self.nb_dices):
            total += randint(1, self.nb_faces)
        return total
    
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
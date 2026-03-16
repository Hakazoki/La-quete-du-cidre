from objets import Consommable
from dice import *

class Potion(Consommable):
    def __init__(self,nom,description,soin,mana_regen):
        super().__init__(nom,description)
        self.soin = soin
        self.mana_regen = mana_regen
    
    def utiliser(self,entite):
        super().utiliser(entite)

class PotionDeGuerison(Potion):
    def __init__(self,nom = "Potion De Guérison",description = "Un flacon de verre contenant un liquide rougeoyant qui referme les plaies et redonne de la vigueur dès la première gorgée.", soin=0):
        super().__init__(nom,description,soin)
        self.soin = Dice.lancer(2,4)

    def utiliser(self,entite):

        super().utiliser(entite)

        if entite.race == "Mort_Vivant":
            entite.vie -= self.soin
        else:
            entite.vie += self.soin

class PotionDeGuerisonMajeur(Potion):
    def __init__(self,nom = "Potion de Guérison Majeur", description = "Une essence cramoisie bouillonnante dont l'éclat pur cicatrice instantanément les pires blessures et restaure la force vitale du héros."):
        super().__init__(nom,description)
        self.soin = Dice.lancer(4, 4)

    def utiliser(self,entite):
        super().utiliser(entite)

        if entite.race == "Mort_Vivant":
            entite.vie -= self.soin
        else:
            entite.vie += self.soin

class PotionDeMana(Potion):
    def __init__(self, nom, description, mana_regen):
        super().__init__(nom, description, mana_regen)
        mana_regen = 60
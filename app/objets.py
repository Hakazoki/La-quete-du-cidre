from dice import *

from abc import ABC, abstractmethod

class Objets(ABC):
    """
    Definition de la class abstract de l'objets
    """
    def __init__(self,nom,description):
        self.nom = nom
        self.description = description

    @abstractmethod
    def utiliser(self, entite):
        pass



class Consommable(Objets):
    """

    """
    def __init__(self,nom,description):
        super().__init__(nom,description)
        self.est_consomme = False

    @abstractmethod
    def utiliser(self, entite):
        if self.est_consomme == True:
            raise Exception('Je suis deja utilisé')
        super().utiliser(entite)
        self.est_consomme = True



class PotionDeGuerison(Consommable):
    def __init__(self,nom = "Potion De Guérison",description = "Un flacon de verre contenant un liquide rougeoyant qui referme les plaies et redonne de la vigueur dès la première gorgée."):
        super().__init__(nom,description)
        self.soin = Dice.lancer(2,4)

    def utiliser(self,entite):

        super().utiliser(entite)

        if entite.race == "Mort_Vivant":
            entite.vie -= self.soin
        else:
            entite.vie += self.soin

class PotionDeGuerisonMajeur(Consommable):
    def __init__(self,nom = "Potion de Guérison Majeur", description = "Une essence cramoisie bouillonnante dont l'éclat pur cicatrice instantanément les pires blessures et restaure la force vitale du héros."):
        super().__init__(nom,description)
        self.soin = Dice.lancer(4, 4)

    def utiliser(self,entite):
        super().utiliser(entite)

        if entite.race == "Mort_Vivant":
            entite.vie -= self.soin
        else:
            entite.vie += self.soin

class Fleche(Consommable):
    def __init__(self,nom = "Fléche en bois",description = "Un fût de bois poli, léger et nerveux, surmonté d'une pointe en métal noirci. Trois plumes grises assurent son équilibre, fixées par un fil de lin poissé."):
        super().__init__(nom,description)


class DagueDeLancer(Consommable):
    def __init__(self,nom = "Dague de Lancer",description = "Cette lame de 15 centimètres d'acier mat ne brille pas à la lumière, évitant ainsi de trahir votre position. Entre vos doigts, elle semble légère, presque vivante. Son équilibre parfait vous garantit que, là où votre regard se posera, la pointe trouvera son chemin."):
        super().__init__(nom,description)
        self.degat = Dice.lancer(1,4)

    def utiliser(self,entite):
        super().utiliser(entite)
        entite.vie -= self.degat




class Equipement(Objets):
    def __init__(self,nom, description):
        super().__init__(nom,description)
        self.est_equiper = False

    @abstractmethod
    def equiper(self,entite):
        if self.est_equiper == True:
            raise Exception('Déjà équiper')
        super().equiper(entite)
        self.est_equiper = True

class Arme(Equipement):
    def __init__(self,nom,description,attaque=0):
        super().__init__(nom,description)
        self.attaque = attaque

    def equiper(self,entite):
        super().equiper(entite)

class Armure(Equipement):
    def __init__(self,nom,description,defence_physique=0,defence_magique=0):
        super().__init__(nom,description)
        self.defence = defence_physique  
        self.defence_magique = defence_magique

    def equiper(self,entite):
        super().equiper(entite)
        self.defence += entite.defence_physique
        self.defence += entite.defence_magique

class ArmeADeuxMain(Arme):
    def __init__(self,nom,description,attaque=0):
        super().__init__(nom,description,attaque)
    
    def equiper(self,entite):
        super().equiper(entite)
        self.attaque += entite.attaque

class ArmeAUneMain(Arme):
    def __init__(self,nom,description,attaque=0):
        super().__init__(nom,description,attaque)
    
    def equiper(self,entite):
        super().equiper(entite)
        self.attaque += entite.attaque

class EpeeEnBois(ArmeAUneMain):
    def __init__(self,nom,description,attaque=0):
        super().__init__(nom,description,attaque)
        self.attaque = Dice.lancer(1,6)
    
    def equiper(self,entite):
        super().equiper(entite)
        self.attaque += entite.attaque





if __name__ == "__main__":
    popo = PotionDeGuerison()
    print(popo.description)







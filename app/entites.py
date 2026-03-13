from abc import ABC
from dice import Dice
from objets import *

class Entite(ABC):
    def __init__(self, race):
        self.race = race
        #Equipement
        self.arme = None
        self.casque = None
        self.plastron = None
        self.gants = None
        self.jambieres = None
        self.bottes = None
        #Stats
        self.vie = 20
        self.pv_max = 20
        self.lvl = 1
        self.exp = 0
        self.exp_next_lvl = 0
        self.force = 3
        self.dexterite = 3
        self.constitution = 3
        self.intelligence = 3
        self.sagesse = 3
        self.charisme = 3
        self.defense_physique = 0
        self.defense_magique = 0
        #valeurs combats
        self.attaque = self.bonus(self.force)
        self.defense = self.bonus(self.constitution) + self.defense_physique

    @property
    def est_vivant(self):
        return self.vie > 0
    
    def bonus(self, stat):
        bonus = 0
        if stat in [1,2,3,4]:
            bonus = -2
        elif stat in [5,6,7,8,9]:
            bonus = -1
        elif stat in [11,12,13,14,15]:
            bonus = 1
        elif stat in [16,17,18,19]:
            bonus = 2
        elif stat in [20,21,22]:
            bonus = 3
        return bonus

    def perte_pv(self, degat):
        if self.est_vivant():
            self.vie -= degat
    
    def gagner_pv(self, gain):
        self.vie += gain
        if self.vie > self.pv_max:
            self.vie = self.pv_max
        
    def attaquer(self, other):
        precision = Dice.lancer(1,20)
        if precision[0] >= 10 :
            attaque = Dice.lancer(1,20) + self.attaque
            defense = Dice.lancer(1,20) + self.defense
            degats = attaque - defense
            if degats < 0:
                degats = 0
            other.perdre_pv(degats)
        return



class Joueur(Entite):
    def __init__(self, race, classe, nom):
        super.__init__(race)
        self.classe = classe
        self.nom = nom
        #Inventaire consommables
        self.consommables = []
        #Stats
        self.force = Dice.lancer(1,20)[0] + 2 #bonus racial
        self.dexterite = Dice.lancer(1,20)[0]
        self.constitution = Dice.lancer(1,20)[0] + 2 #bonus racial
        self.intelligence = Dice.lancer(1,20)[0]
        self.sagesse = Dice.lancer(1,20)[0]
        self.charisme = Dice.lancer(1,20)[0]
        self.defense_physique = 0
        self.defense_magique = 0

    def stats(self):
        print(f"""force = {self.force}\n
            dextérité = {self.dexterite}\n
            constitution = {self.constitution}\n
            intelligence = {self.intelligence}\n
            sagesse = {self.sagesse}\n
            charisme = {self.charisme}\n """)

    def equiper(self, equipement):
        pass

    def desequiper(self, equipement):
        pass

    def consommer(self, objet):
        if isinstance(objet, Potion):
            self.gagner_pv(objet.soin)
            print(f"Vous gagnez {objet.soin} pv")
            self.consommables.remove(objet)
        return

    def lancer(self, objet, other):
        if isinstance(objet, ArmeDeLancer):
            precision = Dice.lancer(1,20)
            if precision[0] >= 10:
                other.perte_pv(objet.degat)
                print(f"L'ennemi perd {objet.degat} pv")
                self.consommables.remove(objet)
        return

class Monstre(Entite):
    def __init__(self, race):
        super().__init__(race)
        gain_exp = 0
        drop = []

    






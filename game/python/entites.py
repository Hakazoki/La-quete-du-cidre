from abc import ABC
from dice import Dice
from objets import *

#Classe abstraite entite ------------------------------------------------------------------------------
class Entite(ABC):
    def __init__(self, race):
        self.race = race
        #Equipement
        self.arme = []
        self.casque = None
        self.plastron = None
        self.gants = None
        self.jambieres = None
        self.bottes = None
        #Stats
        self.vie = 50
        self.pv_max = 50
        self.mana = 0
        self.mana_max = 0
        self.lvl = 1
        self.exp = 0
        self.exp_next_lvl = 0
        self.force = 3
        self.dexterite = 3
        self.constitution = 3
        self.intelligence = 3
        self.sagesse = 3
        self.charisme = 3
        #bonus lies aux armures
        self.defense_physique = 0
        self.defense_magique = 0

    @property
    def attaque(self)-> int:
        return self.bonus(self.force)

    @property
    def defense(self)-> int:
        return self.bonus(self.constitution) + self.defense_physique
    
    @property
    def est_vivant(self):
        return self.vie > 0
    
    def bonus(self, stat):
        bonus = 0
        match stat:
            case _ if stat < 5:
                bonus = -2
            case _ if stat < 10:
                bonus = -1
            case _ if stat == 10:
                bonus = 0
            case _ if stat < 16:
                bonus = 1
            case _ if stat < 20:
                bonus  = 2
            case _ :
                bonus = 3
        return bonus

    def perte_pv(self, degat):
        if self.est_vivant:
            self.vie -= degat
    
    def gagner_pv(self, gain):
        self.vie += gain
        if self.vie > self.pv_max:
            self.vie = self.pv_max
        
    def attaquer(self, other):
        """
        1/2 chances de toucher
        1 lancer pour l'attaque
        1 lancer pour la defense
        Difference entre l'attaque et la defense -> degats subis
        """
        precision = Dice.lancer()
        if precision[0] >= 10 :
            print("Vous touchez")
            attaque = Dice.lancer()[0] + self.attaque
            defense = Dice.lancer()[0] + other.defense
            if attaque - self.attaque == 20:
                attaque = attaque * 2
                print("Reussite critique !")
            elif attaque - self.attaque == 1:
                attaque = attaque/2
                print("Echec critique !")
            if defense - other.defense == 20:
                attaque = attaque / 2
                print("Reussite critique !")
            elif defense - other.defense == 1:
                attaque = attaque * 2
                print("Echec critique !")
            print(f"Attaque de {attaque} VS defense de {defense}")
            degats = attaque - defense
            if degats < 0:
                degats = 0
            other.perte_pv(degats)
        else:
            print("Vous ratez")
        return

    def __str__(self):
        return f"{self.__class__.__name__} avec PV de {self.vie}"

#Classe du joueur ----------------------------------------------------------------------------------
class Joueur(Entite):
    def __init__(self, race = "Nain", nom = "Gimli"):
        super().__init__(race)
        self.nom = nom
        #Inventaire consommables
        self.consommables = []
        #Stats
        self.force = Dice.lancer()[0]
        self.dexterite = Dice.lancer()[0]
        self.constitution = Dice.lancer()[0]
        self.intelligence = Dice.lancer()[0]
        self.sagesse = Dice.lancer()[0]
        self.charisme = Dice.lancer()[0]
        self.defense_physique = 0
        self.defense_magique = 0

    def stats(self):
        print(f"""\
            Statistiques :
            force = {self.force}
            dextérité = {self.dexterite}
            constitution = {self.constitution}
            intelligence = {self.intelligence}
            sagesse = {self.sagesse}
            charisme = {self.charisme}
            """)
        
    def info(self, other):
        print(f"""\
            Info ennemi :
            nom = {other.__class__.__name__}
            race = {other.race}
            vie = {other.pv_max}
            force = {other.force}
            dextérité = {other.dexterite}
            constitution = {other.constitution}
            intelligence = {other.intelligence}
            sagesse = {other.sagesse}
            charisme = {other.charisme}
            """)

    def equiper(self, equipement):
        if isinstance(equipement, ArmeAUneMain):
            if self.arme == [] or len(self.arme) < 2 and isinstance(self.arme[0], ArmeAUneMain) == True:
                self.arme = equipement
            else:
                raise Exception("Vous avez déjà une arme équippée")
        return
    
    def desequiper(self, equipement):
        if isinstance(equipement, ArmeAUneMain):
            if self.arme == []:
                raise Exception("Vous n'avez déjà aucune arme équippée")
            else:
                self.arme.remove(equipement)
        return

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

#Classes des differentes classes disponibles ------------------------------------------------------------------
class Voleur(Joueur):
    def __init__(self, race="Nain", nom="Gimli"):
        super().__init__(race, nom)
        self.dexterite += 3
        self.charisme += 2
        self.charisme -= 2
        self.defense_physique = 1

class Guerrier(Joueur):
    def __init__(self, race="Nain", nom="Gimli"):
        super().__init__(race, nom)
        self.force += 3
        self.constitution += 2
        self.intelligence -= 2
        self.defense_physique = 2

class EluDeMoradin(Joueur):
    def __init__(self, race="Nain", nom="Gimli"):
        super().__init__(race, nom)
        self.force += 3
        self.dexterite += 3
        self.constitution += 3
        self.intelligence += 3
        self.sagesse += 3
        self.charisme += 3
        self.defense_magique = 2
        self.defense_physique = 2

class Tavernier(Joueur):
    def __init__(self, race="Nain", nom="Gimli"):
        super().__init__(race, nom)
        self.force -= 1
        self.dexterite -= 1
        self.constitution -= 1
        self.intelligence -= 1
        self.sagesse -= 1
        self.charisme -= 1

class Mage(Joueur):
    def __init__(self, race="Nain", nom="Gimli"):
        super().__init__(race, nom)
        self.consommables = []
        self.mana = self.mana_max = 60
        self.force -= 2
        self.intelligence += 3
        self.sagesse += 2
        self.defense_magique = 2 
    
    def MissilesMagiques(self, other):
        print("Missiles magiques !")
        for element in Dice.lancer(3,10)[1]:
            if element > 2 :
                degats = Dice.lancer(1,8) + self.bonus(self.intelligence) - other.defense_magique
                other.perte_pv(degats)
        self.mana -= 10
        return
    
    def BouleDeFeu(self, other):
        print("Boule de feu !")
        if Dice.lancer() > 12:
            degats = Dice.lancer(1,30) + self.bonus(self.intelligence) - other.defense_magique
            other.perte_pv(degats)
            self.mana -= 20
        return

#Classes des monstres -------------------------------------------------------------------------------------
class Monstre(Entite):
    def __init__(self, race):
        super().__init__(race)
        gain_exp = 0
        drop = []

class Dummy(Monstre):
    def __init__(self, race = "Mannequin"):
        super().__init__(race)
        self.vie = self.pv_max = 9999
        self.constitution = 1

class UiiaCat(Monstre):
    def __init__(self, race = "Dieu"):
        super().__init__(race)
        self.vie = self.pv_max = 120
        self.force = 14
        self.dexterite = 11
        self.constitution = 12
        self.intelligence = 1
        self.sagesse = 18
        self.charisme = 18
        self.defense_magique = 5
        self.defense_physique = 5

class Skaven(Monstre):
    def __init__(self, race = "Skaven"):
        super().__init__(race)
        self.vie = self.pv_max = 40
        self.force = 12
        self.dexterite = 14
        self.constitution = 7
        self.intelligence = 5
        self.defense_physique = 2

class CrapeauMagicien(Monstre):
    def __init__(self, race = "Crapeau"):
        super().__init__(race)
        self.vie = self.pv_max = 60
        self.mana = self.mana_max = 60
        self.force = 6
        self.dexterite = 5
        self.constitution = 16
        self.intelligence = 16
        self.sagesse = 18
        self.charisme = 13
        self.defense_magique = 3

    def PluieDeGrenouille(self, other):
        print("Des grenouilles tombent sur vous !")
        for element in Dice.lancer(10,10)[1]:
            if element > 5:
                degats = Dice.lancer(1,2)[0] + self.bonus(self.intelligence) - other.defense_magique
                other.perte_pv(degats)
        self.mana -= 10

    

if __name__ == "__main__":
    m = Dummy()
    j = Joueur()
    j.stats()
    j.info(m)
    for i in range(10):
        j.attaquer(m)
        print(m)
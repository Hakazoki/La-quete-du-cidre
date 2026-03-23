from abc import ABC
from .dice import Dice
from .objets import *
from .Arme import *
from .Armure import *
from .Potion import *

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
        degats = self.bonus(self.force)
        if self.arme == []:
            return degats
        else:
            for element in self.arme:
                degats += element.attaque.jeter()
            return degats

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
        self.bourse = 1
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
                self.arme.append(equipement)
            else:
                raise Exception("Vous avez déjà une arme équippée")
        elif isinstance(equipement, ArmeADeuxMain) or isinstance(equipement, ArmeADistance):
            if self.arme == []:
                self.arme.append(equipement)
            else:
                raise Exception("Vous avez déjà une arme équippée")
        elif isinstance(equipement, Casque):
            if self.casque is None:
                self.casque = equipement
            else:
                raise Exception("Vous avez déjà un casque équippé")
        elif isinstance(equipement, Plastron):
            if self.plastron is None:
                self.plastron = equipement
            else:
                raise Exception("Vous avez déjà un plastron équippé")
        elif isinstance(equipement, Gants):
            if self.gants is None:
                self.gants = equipement
            else:
                raise Exception("Vous avez déjà des gants équippés")
        elif isinstance(equipement, Jambieres):
            if self.jambieres is None:
                self.jambieres = equipement
            else:
                raise Exception("Vous avez déjà des jambières équippées")
        elif isinstance(equipement, Bottes):
            if self.bottes is None:
                self.bottes = equipement
            else:
                raise Exception("Vous avez déjà des gants équippées")
        return
    
    def desequiper(self, equipement):
        if isinstance(equipement, ArmeAUneMain):
            if self.arme == []:
                raise Exception("Vous n'avez aucune arme équippée")
            else:
                self.arme.remove(equipement)
        elif isinstance(equipement, ArmeADeuxMain) or isinstance(equipement, ArmeADistance):
            if self.arme == []:
                raise Exception("Vous n'avez aucune arme équippée")
            else:
                self.arme.remove(equipement)   
        elif isinstance(equipement, Casque):
            if self.casque is not None:
                self.casque = None
            else:
                raise Exception("Vous n'avez aucun casque équippé")
        elif isinstance(equipement, Plastron):
            if self.plastron is not None:
                self.plastron = None
            else:
                raise Exception("Vous n'avez aucun plastron équippé")
        elif isinstance(equipement, Gants):
            if self.gants is not None:
                self.gants = None
            else:
                raise Exception("Vous n'avez aucun gant équippé")
        elif isinstance(equipement, Jambieres):
            if self.jambieres is not None:
                self.jambieres = None
            else:
                raise Exception("Vous n'avez aucune jambière équippée")
        elif isinstance(equipement, Bottes):
            if self.bottes is not None:
                self.bottes = None
            else:
                raise Exception("Vous n'avez aucun gant équippée")
        return

    def consommer(self, objet):
        if isinstance(objet, PotionDeMana):
            self.mana += objet.mana_regen
            if self.mana > self.mana_max:
                self.mana = self.mana_max
            print("Vous récupérez tout votre mana.")
        elif isinstance(objet, PotionDeGuerison) or isinstance(objet, PotionDeGuerisonMajeur):
            self.gagner_pv(objet.soin)
            print(f"Vous gagnez {objet.soin} points de vie !")
        objet.est_consomme = True
        self.consommables.remove(objet)

    def lancer(self, objet, other):
        precision = Dice.lancer(1,20)
        if precision[0] >= 10:
            other.perte_pv(objet.degat)
            print(f"L'ennemi perd {objet.degat} pv")
        else:
            print("Raté !")
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
        mana1 = PotionDeMana(60)
        mana2 = PotionDeMana(60)
        self.consommables = [mana1, mana2]
        self.mana = 0
        self.mana_max = 60
        self.force -= 2
        self.intelligence += 3
        self.sagesse += 2
        self.defense_magique = 2 
    
    def MissilesMagiques(self, other):
        print("Missiles magiques !")
        for element in Dice.lancer(3,10)[1]:
            if element > 2 :
                degats = Dice.lancer(1,8)[0] + self.bonus(self.intelligence) - other.defense_magique
                other.perte_pv(degats)
            else:
                print("Raté !")
        self.mana -= 10
        return
    
    def BouleDeFeu(self, other):
        print("Boule de feu !")
        if Dice.lancer()[0] > 12:
            degats = Dice.lancer(1,30)[0] + self.bonus(self.intelligence) - other.defense_magique
            other.perte_pv(degats)
            self.mana -= 20
        else:
            print("Raté !")
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
            else:
                print("Raté !")
        self.mana -= 10

    def CrachatAcide(self, other):
        print("Il vous crache dessus ! Attention : corrosif !")
        if Dice.lancer(1,10)[0] > 6:
            degats = Dice.lancer(1,20)[0] + self.bonus(self.intelligence) - other.defense_magique
            other.perte_pv(degats)
            self.mana -= 20
        else:
            print("Raté !")
        return

if __name__ == "__main__":
    m = Dummy()
    cat = UiiaCat()
    j = Mage()
    j.stats()
    j.consommer(j.consommables[0])
    print(j.mana)
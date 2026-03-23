"""
devrait plutôt être
__all__ = ["objets", "dice"]

J'ai commenté car inutile

from dice import Dice
from objets import Objets, Consommable, Equipement, Munition, Fleche
from Arme import (
    Arme, ArmeAUneMain, ArmeADistance, ArmeADeuxMain,
    EpeeEnBois, EpeeEnFer, Zweihander, Arc
)
from Armure import (
    Armure, Casque, Plastron, Gants, Jambieres, Bottes,
    CasqueEnCuire, ArmureEnCuire, GantsEnCuire, JambieresEnCuire, BottesEnCuire
)
from Potion import Potion, PotionDeGuerison, PotionVie, PotionDeMana, PotionDeGuerisonMajeur
from entites import (
    Entite, Joueur, Voleur, Guerrier, Mage,
    Monstre, Dummy, Skaven, CrapeauMagicien
)
"""

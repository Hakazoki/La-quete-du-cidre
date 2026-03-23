from .objets import Equipement

class Armure(Equipement):
    def __init__(self,nom,description,defence_physique,defence_magique):
        super().__init__(nom,description)
        self.defence_physique = defence_physique
        self.defence_magique = defence_magique
        

    def utiliser(self,entite):
        super().equiper(entite)
        entite.defence_physique += self.defence_physique
        entite.defence_magique += self.defence_magique

class Casque(Armure):
    def __init__(self,nom,description,defence_physique,defence_magique):
        super().__init__(nom,description,defence_physique,defence_magique)

class CasqueEnCuire(Casque):
    def __init__(self,nom,description,defence_physique):
        super().__init__(nom,description,defence_physique)
        defence_physique = 1

class CoiffeDerudi(Casque):
    def __init__(self,nom,description,defence_magique):
        super().__init__(nom,description,defence_magique)
        defence_magique = 1
        

class Plastron(Armure):
    def __init__(self,nom,description,defence_physique,defence_magique):
        super().__init__(nom,description,defence_physique,defence_magique)

class ArmureEnCuire(Plastron):
    def __init__(self,nom,description,defence_physique):
        super().__init__(nom,description,defence_physique)
        defence_physique = 2

class RobeDeMagicien(Plastron):
    def __init__(self,nom,description,defence_magique):
        super().__init__(nom,description,defence_magique)
        defence_magique = 2
class Gants(Armure):
    def __init__(self,nom,description,defence_physique,defence_magique):
        super().__init__(nom,description,defence_physique,defence_magique)

class GantsEnCuire(Gants):
    def __init__(self,nom,description,defence_physique):
        super().__init__(nom,description,defence_physique)
        defence_physique = 1
class Jambieres(Armure):
    def __init__(self,nom,description,defence_physique,defence_magique):
        super().__init__(nom,description,defence_physique,defence_magique)

class JambieresEnCuire(Jambieres):
    def __init__(self,nom,description,defence_physique):
        super().__init__(nom,description,defence_physique)
        defence_physique = 2
class Bottes(Armure):
    def __init__(self ,nom ,description ,defence_physique ,defence_magique):
        super().__init__(nom ,description ,defence_physique ,defence_magique)

class BottesEnCuire(Bottes):
    def __init__(self, nom, description, defence_physique):
        super().__init__(nom, description, defence_physique)
        defence_physique = 1
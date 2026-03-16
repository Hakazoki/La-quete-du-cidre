from objets import Equipement

class Armure(Equipement):
    def __init__(self,nom,description,defence_physique=0,defence_magique=0):
        super().__init__(nom,description)
        self.defence_physique = defence_physique  
        self.defence_magique = defence_magique

    def utiliser(self,entite):
        super().equiper(entite)
        entite.defence_physique += self.defence_physique
        entite.defence_magique += self.defence_magique
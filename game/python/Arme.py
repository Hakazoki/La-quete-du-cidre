from objets import Equipement,Munition,Fleche
from dice import Dice



class Arme(Equipement):
    def __init__(self,nom,description,attaque : Dice):
        super().__init__(nom,description)
        self.bonus_attaque = attaque

    def utiliser(self,entite : "Entite"):
        entite.equiper(self)

class ArmeADeuxMain(Arme):
    def __init__(self,nom,description,attaque):
        super().__init__(nom,description,attaque)

class ArmeAUneMain(Arme):
    def __init__(self,nom,description,attaque):
        super().__init__(nom,description,attaque)

class EpeeEnBois(ArmeAUneMain):
    def __init__(self,nom = "Epée en Bois",description= "Simple Epée en bois"):
        super().__init__(nom,description,Dice(4,1))
        
        

class EpeeEnFer(ArmeAUneMain):
    def __init__(self,nom = "Epée en Fer",description = "Une lame de fer sombre de 60 cm, brute et fonctionnelle. Sa garde en croix et sa poignée gainée de cuir privilégient l'efficacité au style. C’est une arme équilibrée, forgée pour l'estocade et le combat rapproché.",attaque = 0):
        super().__init__(nom,description,Dice(6,1))

class Zweihander(ArmeADeuxMain):
    def __init__(self, nom = "Zweihander", description = "Une grand epee a deux mains"):
        super().__init__(nom, description, Dice(10,1))

class ArmeADistance(Arme):
    def __init__(self,nom,description,attaque,ammo_type :type[Munition]):
        super().__init__(nom,description,attaque)
        self.ammo_type = ammo_type
        self.max_ammo = ammo_type.max_ammo
        self.ammo = self.max_ammo
    
    def tirer(self,entite) -> int | None:
        """
        Utiliser l'arme.
        Retourne les dégats de l'arme.
        None si l'attaque n'est pas possible
        """
        if  self.ammo > 0:
            self.ammo -= 1
            return self.bonus_attaque.jeter()
        return None 

class Arc (ArmeADistance):
    def __init__(self,nom = "Arc en bois", description ="Arc taillé en bois", ammo_type = Fleche):
        super().__init__(nom,description, Dice(4, 2), ammo_type)
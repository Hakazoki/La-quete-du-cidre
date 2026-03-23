from objets import Equipement, Munition, Fleche
from dice import Dice
from entites import Entite, Joueur

class Arme(Equipement):
    def __init__(self,nom,description,attaque : Dice):
        super().__init__(nom,description)
        self.attaque = attaque

    def utiliser(self,entite : Entite):
        entite.equiper(self)

class ArmeADeuxMain(Arme):
    def __init__(self,nom,description,attaque=0):
        super().__init__(nom,description,attaque)

class ArmeAUneMain(Arme):
    def __init__(self,nom,description,attaque=0):
        super().__init__(nom,description,attaque)

class EpeeEnBois(ArmeAUneMain):
    def __init__(self,nom = "Epée en Bois",description= "Simple Epée en bois",attaque=0):
        super().__init__(nom,description,Dice(4,1))
        print(self.attaque)
        

class EpeeEnFer(ArmeAUneMain):
    def __init__(self,nom = "Epée en Fer",description = "Une lame de fer sombre de 60 cm, brute et fonctionnelle. Sa garde en croix et sa poignée gainée de cuir privilégient l'efficacité au style. C’est une arme équilibrée, forgée pour l'estocade et le combat rapproché.",attaque = 0):
        super().__init__(nom,description,Dice(6,1))

class Zweihander(ArmeADeuxMain):
    def __init__(self, nom = "Zweihander", description = "Une grand epee a deux mains", attaque=0):
        super().__init__(nom, description, Dice(6,1))

class ArmeADistance(Arme):
    def __init__(self,nom,description,attaque,ammo_type :type[Munition],max_ammo=30):
        super().__init__(nom,description,attaque)
        self.ammo_type = ammo_type
        self.max_ammo = ammo_type.max_ammo
        self.ammo = max_ammo
    
    def tirer(self,entite) -> int | None:
        """
        Utiliser l'arme.
        Retourne les dégats de l'arme.
        None si l'attaque n'est pas possible
        """
        if  self.ammo >= 0:
            self.ammo -= 1
            return self.attaque.jeter()
        return None 

class Arc (ArmeADistance):
    def __init__(self,nom = "Arc en bois", description ="Arc taillé en bois", ammo_type = Fleche):
        super().__init__(nom,description, Dice(4, 2), ammo_type)



if __name__ == "__main__":
    # popo = PotionDeGuerison()
    arme = Arc()
    toto = Joueur("Elfe", "Barbare")
    toto.equiper(arme)
    # print(popo.description)
    print(arme.tirer(toto))
    print(arme.tirer(toto))
    print(arme.tirer(toto))
    print(arme.tirer(toto))
    print(f"Il me reste {arme.ammo}")
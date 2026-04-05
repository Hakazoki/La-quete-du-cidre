init -8 python:

    class Arme(Equipement):
        def __init__(self, nom, description, attaque: Dice, icone="images/items/default_icone.png"):
            super().__init__(nom, description, icone) 
            self.attaque = attaque

        def get_stats_affichage(self):
            stats = super().get_stats_affichage()
            if hasattr(self, 'attaque'):
                stats.append(f"{{color=#ff0000}}Dégâts : {self.attaque.nb_dices}D{self.attaque.nb_faces}{{/color}}")
            return stats

    class ArmeAUneMain(Arme):
        def __init__(self, nom, description, attaque, icone="images/items/default_icone.png"):
            super().__init__(nom, description, attaque, icone)

    class ArmeADeuxMain(Arme):
        def __init__(self, nom, description, attaque, icone="images/items/default_icone.png"):
            super().__init__(nom, description, attaque, icone)

    class EpeeEnBois(ArmeAUneMain):
        def __init__(self,nom = "Epée en Bois",description= "Simple Epée en bois",attaque=0,icone="images/items/fc1521.png"):
            super().__init__(nom,description,Dice(4,1))
            
    class EpeeEnFer(ArmeAUneMain):
        def __init__(self,nom = "Epée en Fer",description = "Une lame de fer sombre de 60 cm, brute et fonctionnelle. Sa garde en croix et sa poignée gainée de cuir privilégient l'efficacité au style. C’est une arme équilibrée, forgée pour l'estocade et le combat rapproché.",attaque = 0,icone="images/items/fc1449.png"):
            super().__init__(nom,description,Dice(6,1))
    
    class DagueEnFer(ArmeAUneMain):
        def __init__(self,nom = "Dague en Fer",description = "Une lame courte et robuste, forgée dans un fer sombre et légèrement piqué par le temps. Sa garde est dépouillée, faite d'une simple barre de métal brut, et son manche est enveloppé de cuir tanné, un peu râpé par l'usage. Elle n'a rien d'élégant, mais elle est parfaitement équilibrée pour une prise en main rapide et tranchante.",attaque = 0,icone="images/items/fc1521.png"):
            super().__init__(nom,description,Dice(4,1))

    class Hache(ArmeAUneMain):
        def __init__(self, nom = "Hache en Fer", description = "Une hache en fer forgé à la main par un maître forgeron. Son élégance disparait au profit de sa sauvagerie", attaque = 0,icone = "images/items/fc1465.png"):
            super().__init__(nom, description, Dice(4,1))

    class Zweihander(ArmeADeuxMain):
        def __init__(self, nom = "Zweihander", description = "Une grand epee a deux mains",attaque=0,icone="images/items/fc1616.png"):
            super().__init__(nom, description, Dice(10,1))

    class MarteauDeMoradin(ArmeADeuxMain):
        def __init__(self, nom = "Marteau de Moradin", description = "Un grand marteau qui aurait été forgé par le dieu Moradin lui-même. Personne ne peut l'utiliser s'il n'est pas l'élu.", attaque = 0,icone="images/items/fc1801.png"):
            super().__init__(nom, description, Dice(18,1))

    class BatonDeSorcier(ArmeADeuxMain):
        def __init__(self, nom = "Bâton de Sorcier", description = "Un bâton contenant une plume de Phénix conçu pour et par les plus grands mages de notre histoire. Un nain paraît tout petit à côté", attaque=0,icone="images/items/fc1492.png"):
            super().__init__(nom, description, Dice(6,1))

    class ArmeADistance(Arme):
        def __init__(self,nom,description,attaque,ammo_type :type[Munition],icone="images/items/default_icone.png"):
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
        def __init__(self,nom = "Arc en bois", description ="Arc taillé en bois", ammo_type = Fleche,icone="images/items/fc1484.png"):
            super().__init__(nom,description, Dice(4, 2), ammo_type)
init -9 python :

    from abc import ABC, abstractmethod

    class Objets(ABC):
        """
        Definition de la class abstract de l'objets
        """
        def __init__(self,nom,description,icone):
            self.nom = nom
            self.description = description
            
            self.icone = icone
            self.effet = "Aucun"

        @abstractmethod
        def utiliser(self, entite):
            pass

    class Consommable(Objets):
        """

        """
        def __init__(self,nom,description,icone="../images/items/default_icone.png"):
            super().utiliser(Entite)
            self.est_consomme = True

    class Munition(Consommable):
        max_ammo = 30
        def __init__(self,nom,description,icone):
            super().__init__(nom,description)

    class Cle(Consommable):
        def __init__(self,nom = "Clé du chat",description = "Une clé ornée d'une tête de félin. Elle semble ouvrir une serrure",icone="images/items/default_icone.png"):
            super().__init__(nom,description,icone)
            self.effet = "Ouvre une porte"

        def utiliser(self,entite):
            renpy.say(None, "Cette clé s'utilisera automatiquement devant la bonne porte.")

    class HerbeCap(Consommable):
        def __init__(self,nom = "Herbe du Cap",description = "Une plante séchée à l'odeur irrésistible pour les créatures de type félin.",icone="images/items/default_icone.png"):
            super().__init__(nom,description,icone)
            self.effet = "Calme même le plus grand des félins"
        
        def utiliser(self,entite):
            renpy.say(None, "Ça sent bon, mais ce n'est pas le moment de jardiner. Gardez-la pour plus tard !")

    class Fleche(Munition):
        max_ammo = 10
        def __init__(self,nom = "Fléche en bois",description = "Un fût de bois poli, léger et nerveux, surmonté d'une pointe en métal noirci. Trois plumes grises assurent son équilibre, fixées par un fil de lin poissé.",icone="images/items/fc2154.png"):
            super().__init__(nom,description,icone)

    class ArmeDeLancer(Consommable):
        def __init__(self,nom,description,degat,icone):
            super().__init__(nom,description,icone)
            self.degat = degat
        
        def lancer(self,entite):
            self.degat -= entite.pv
            
    class DagueALancer(ArmeDeLancer):
        def __init__(self,nom = "Dague de Lancer",description = "Cette lame de 15 centimètres d'acier mat ne brille pas à la lumière, évitant ainsi de trahir votre position. Entre vos doigts, elle semble légère, presque vivante. Son équilibre parfait vous garantit que, là où votre regard se posera, la pointe trouvera son chemin.",icone="images/items/default_icone.png"):
            super().__init__(nom,description,icone)
            self.degat = Dice.lancer(4,1)

        def lancer(self,entite):
            entite.vie -= self.degat

    class Equipement(Objets):
        def __init__(self,nom, description,icone="images/items/default_icone.png"):
            super().__init__(nom,description,icone)
            self.est_equiper = False

        def utiliser(self,entite):
            if self.est_equiper == True:
                raise Exception('Déjà équiper')
            super().utiliser(entite)
            self.est_equiper = True
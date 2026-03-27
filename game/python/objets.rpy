init python :

    from abc import ABC, abstractmethod
    from dice import Dice

    class Objets(ABC):
        """
        Definition de la class abstract de l'objets
        """
        def __init__(self,nom,description):
            self.nom = nom
            self.description = description

        @abstractmethod
        def utiliser(self, entite):
            pass

    class Consommable(Objets):
        """

        """
        def __init__(self,nom,description):
            super().__init__(nom,description)
            self.est_consomme = False

        @abstractmethod
        def utiliser(self, entite):
            if self.est_consomme == True:
                raise Exception('Je suis deja utilisé')
            super().utiliser(entite)
            self.est_consomme = True

    class Munition(Consommable):
        max_ammo = 30
        def __init__(self,nom,description):
            super().__init__(nom,description)

    class Fleche(Munition):
        max_ammo = 10
        def __init__(self,nom = "Fléche en bois",description = "Un fût de bois poli, léger et nerveux, surmonté d'une pointe en métal noirci. Trois plumes grises assurent son équilibre, fixées par un fil de lin poissé."):
            super().__init__(nom,description)

    class ArmeDeLancer(Consommable):
        def __init__(self,nom,description,degat):
            super().__init__(nom,description)
            self.degat = degat
        
        def lancer(self,entite):
            self.degat -= entite.pv
            
    class DagueALancer(ArmeDeLancer):
        def __init__(self,nom = "Dague de Lancer",description = "Cette lame de 15 centimètres d'acier mat ne brille pas à la lumière, évitant ainsi de trahir votre position. Entre vos doigts, elle semble légère, presque vivante. Son équilibre parfait vous garantit que, là où votre regard se posera, la pointe trouvera son chemin."):
            super().__init__(nom,description)
            self.degat = Dice.lancer(4,1)

        def lancer(self,entite):
            entite.vie -= self.degat

    class Equipement(Objets):
        def __init__(self,nom, description):
            super().__init__(nom,description)
            self.est_equiper = False

        @abstractmethod
        def utiliser(self,entite):
            if self.est_equiper == True:
                raise Exception('Déjà équiper')
            super().utiliser(entite)
            self.est_equiper = True
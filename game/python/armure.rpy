init -8 python :


    class Armure(Equipement):
        def __init__(self,nom,description,defence_physique,defence_magique,icone="images/items/default_icone.png"):
            super().__init__(nom,description,icone)
            self.defence_physique = defence_physique
            self.defence_magique = defence_magique
            

        def utiliser(self,entite):
            entite.equiper(self)
            entite.defense_physique += self.defence_physique
            entite.defense_magique += self.defence_magique

        def get_stats_affichage(self):
            stats = super().get_stats_affichage() 
            stats.append(f"{{color=#ff8000}}Déf. Phys : +{self.defence_physique}{{/color}}")
            stats.append(f"{{color=#cc00ff}}Déf. Mag : +{self.defence_magique}{{/color}}")
            return stats

    class Casque(Armure):
        def __init__(self,nom,description,defence_physique,defence_magique,icone="images/items/default_icone.png"):
            super().__init__(nom,description,defence_physique,defence_magique,icone)

    class CasqueEnCuire(Casque):
        def __init__(self,nom="Casque en cuir",description="Un casque en cuir basique, un indispensable pour les aventuriers en herbe soucieux de leur petit crâne délicat.",defence_physique=1, defence_magique=0,icone="images/items/armor_004.png"):
            super().__init__(nom,description,defence_physique,defence_magique,icone)
            defence_physique = 1

    class CoiffeDerudi(Casque):
        def __init__(self,nom="Coiffe d'érudit",description="Coiffe de mage décerné uniquement aux magiciens s'étant illustré dans une bataille épique.",defence_physique=0,defence_magique=1,icone="images/items/fc1964.png"):
            super().__init__(nom,description,defence_physique,defence_magique,icone)
            defence_magique = 1
            
    class Plastron(Armure):
        def __init__(self,nom,description,defence_physique,defence_magique,icone="images/items/default_icone.png"):
            super().__init__(nom,description,defence_physique,defence_magique,icone)

    class ArmureEnCuire(Plastron):
        def __init__(self,nom="Plastron en cuir",description="Un bon plastron qui vous protégera à coup sûr de certaines attaques (faites attention quand même)",defence_physique=2, defence_magique=0,icone="images/items/armor_012.png"):
            super().__init__(nom,description,defence_physique, defence_magique,icone)
            defence_physique = 2

    class RobeDeMagicien(Plastron):
        def __init__(self,nom="Robe de magicien",description="Un habit de haute couture que seul les mages les plus agguerris peuvent espérer se voir offrir en guise de récompense",defence_physique=0,defence_magique=2,icone="images/items/fc2030.png"):
            super().__init__(nom,description,defence_physique,defence_magique,icone)
            defence_magique = 2

    class Gants(Armure):
        def __init__(self,nom,description,defence_physique,defence_magique,icone="images/items/default_icone.png"):
            super().__init__(nom,description,defence_physique,defence_magique,icone)

    class GantsEnCuire(Gants):
        def __init__(self,nom="Gants de protection en cuir",description="Gants de protection pouvant servir aux aventuriers préoccupés par leurs doigts fragiles comme aux gros forgerons bien virils",defence_physique=1, defence_magique=0,icone="images/items/armor_020.png"):
            super().__init__(nom,description,defence_physique, defence_magique,icone)
            defence_physique = 1

    class Jambieres(Armure):
        def __init__(self,nom,description,defence_physique,defence_magique,icone="images/items/default_icone.png"):
            super().__init__(nom,description,defence_physique,defence_magique,icone)

    class JambieresEnCuire(Jambieres):
        def __init__(self,nom="Jambières en cuir",description="Jambières en cuir tanné qui vous assureront un charisme et une présence impressionnante lors de vos aventures et autres voyages vers des cultures étrangères.",defence_physique=2, defence_magique=0,icone="images/items/armor_028.png"):
            super().__init__(nom,description,defence_physique, defence_magique,icone)
            defence_physique = 2

    class Bottes(Armure):
        def __init__(self ,nom ,description ,defence_physique ,defence_magique,icone="images/items/default_icone.png"):
            super().__init__(nom ,description ,defence_physique ,defence_magique,icone)

    class BottesEnCuire(Bottes):
        def __init__(self, nom="Bottes en cuir", description="Bottes en cuir pour les aventuriers soucieux de leurs orteils ou pour les fashionistas qui se balladent dans la ville uniquement quand il y a un marché. Non mais sérieusement, vous les trouvez pas complétement débiles avec leurs paires de bottes de toutes les couleurs juste pour attirer les regards ? Faut vraiment ne rien avoir à faire de sa vie pour sortir de chez soi uniquement pour frimer au marché de la ville. Surtout qu'en général ils achètent que des fruits et des légumes ces bouffeurs d'herbe. Si on voulait voir des truc débiles avec du cuir sur eux qui mangent de l'herbe, je serai allé dans le pré de mon pote à la sortie du village pour voir ses vaches", defence_physique=2, defence_magique=0,icone="images/items/armor_036.png"):
            super().__init__(nom, description, defence_physique, defence_magique,icone)
            defence_physique = 1
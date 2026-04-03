init -8 python :


    class Potion(Consommable):
        def __init__(self,nom,description,icone):
            super().__init__(nom,description,icone)
        
        def utiliser(self,entite):
            super().utiliser(entite)

    class PotionVie(Potion):
        def __init__(self, nom, description,soin,icone):
            super().__init__(nom, description,soin,icone)
            self.soin = soin

        def utiliser(self, entite):
            super().utiliser(entite)
            if entite.race == "Mort_Vivant":
                entite.vie -= self.soin
            else:
                entite.vie += self.soin

    class PotionMana(Potion):
        def __init__(self,nom,description,mana_regen,icone):
            super().__init__(nom,description,icone)
            self.mana_regen = mana_regen

    class PotionDeGuerison(PotionVie):
        def __init__(self,nom = "Potion De Guérison",description = "Un flacon de verre contenant un liquide rougeoyant qui referme les plaies et redonne de la vigueur dès la première gorgée.", soin=0,icone="images/items/fc267.png"):
            super().__init__(nom,description,soin,icone)
            self.soin = Dice.lancer(2,4)

    class PotionDeGuerisonMajeur(PotionVie):
        def __init__(self,nom = "Potion de Guérison Majeur", description = "Une essence cramoisie bouillonnante dont l'éclat pur cicatrise instantanément les pires blessures et restaure la force vitale du héros.",soin=0,icone="images/items/fc272.png"):
            super().__init__(nom,description,soin,icone)
            self.soin = Dice.lancer(4, 4)

    class PotionDeMana(PotionMana):
        def __init__(self, nom = "Potion de Mana", description = "Une fiole remplie d'un liquide bleu profond créée par les plus grands mages du monde, vous serez revigorés en une gorgée et vous pourrez repartir au combat.",mana_regen = 60,icone="images/items/mana_potion.png"):
            super().__init__(nom,description,mana_regen,icone)

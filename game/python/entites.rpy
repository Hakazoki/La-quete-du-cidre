init -7 python :

    from abc import ABC
    from random import randint
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classe abstraite entite -------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    class Entite(ABC):
        def __init__(self, race):
            self.race = race
            self.couleur_log = "#e74c3c"
            #Equipement
            self.arme = [None, None]
            self.casque = None
            self.plastron = None
            self.gants = None
            self.jambieres = None
            self.bottes = None
            #Stats
            self.vie = 100
            self.pv_max = 100
            self.mana = 0
            self.mana_max = 0
            self.lvl = 1
            self.exp = 0
            self.exp_next_lvl = 0
            self.force = 3
            self.dexterite = 3
            self.constitution = 3
            self.intelligence = 3
            self.sagesse = 3
            self.charisme = 3
            #bonus lies aux armures
            self.defense_physique = 0
            self.defense_magique = 0

        @property
        def attaque(self)-> int:
            degats = self.bonus(self.force)
            if self.arme == [None, None]:
                return degats
            elif isinstance(self.arme[0], ArmeADistance):
                degats = self.bonus(self.dexterite) + self.arme[0].attaque.jeter()
                return degats
            else:
                for element in self.arme:
                    degats += element.attaque.jeter()
                return degats

        @property
        def defense(self)-> int:
            return self.bonus(self.constitution) + self.defense_physique
        
        @property
        def est_vivant(self):
            return self.vie > 0
        
        def bonus(self, stat):
            bonus = 0
            match stat:
                case _ if stat < 5:
                    bonus = -2
                case _ if stat < 10:
                    bonus = -1
                case _ if stat == 10:
                    bonus = 0
                case _ if stat < 16:
                    bonus = 1
                case _ if stat < 20:
                    bonus  = 2
                case _ :
                    bonus = 3
            return bonus

        def perte_pv(self, degat):
            if self.est_vivant:
                self.vie -= degat
        
        def gagner_pv(self, gain):
            self.vie += gain
            if self.vie > self.pv_max:
                self.vie = self.pv_max
            
        def attaquer(self, other):
            """
            1/2 chances de toucher
            1 lancer pour l'attaque
            1 lancer pour la defense
            Difference entre l'attaque et la defense -> degats subis
            """
            degats_totaux = 0

            if self.type_degat == "physique":
                precision = Dice.lancer()
                if precision[0] >= 10 :
                    store.log_msg(f"{getattr(self, 'nom', self.race)} touche sa cible !", self.couleur_log)
                    attaque = Dice.lancer()[0] + self.attaque
                    defense = Dice.lancer()[0] + other.defense

                    if attaque - self.attaque == 20:
                        attaque = attaque * 2
                        store.log_msg("Réussite critique !", self.couleur_log)
                    elif attaque - self.attaque == 1:
                        attaque = attaque / 2
                        store.log_msg("Échec critique de l'attaque !", self.couleur_log)
                        
                    if defense - other.defense == 20:
                        attaque = attaque / 2
                        store.log_msg("Défense parfaite en face !", other.couleur_log)
                    elif defense - other.defense == 1:
                        attaque = attaque * 2
                        store.log_msg("Échec de la défense adverse !", other.couleur_log)

                    degats_totaux = max(0, attaque - defense)
                    other.perte_pv(degats_totaux)
                else:
                    store.log_msg(f"{getattr(self, 'nom', self.race)} rate son attaque !", self.couleur_log)
            else :
                aleatoire = randint(1,2)
                match aleatoire:
                    case 1:
                        degats_totaux = self.sort1(other)
                    case 2:
                        degats_totaux = self.sort2(other)
                other.perte_pv(degats_totaux)
                
            return degats_totaux

        def __str__(self):
            return f"{self.__class__.__name__} avec PV de {self.vie}"
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classe du joueur --------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    class Joueur(Entite):
        def __init__(self, race = "Nain", nom = "Gimli"):
            super().__init__(race)
            self.type_degat = "physique"
            self.nom = nom
            self.couleur_log = "#3498db"
            self.bourse = 1
            #Inventaires
            popo1 = PotionDeGuerison()
            popo2 = PotionDeGuerison()
            self.consommables = [popo1, popo2]
            self.equipements = []
            #Armes
            self.arme = [None, None]
            #Armures
            self.tete = CasqueEnCuire()
            self.torse = ArmureEnCuire()
            self.mains = GantsEnCuire()
            self.jambes = JambieresEnCuire()
            self.pieds = BottesEnCuire()
            self.tete.utiliser(self)
            self.torse.utiliser(self)
            self.mains.utiliser(self)
            self.jambes.utiliser(self)
            self.pieds.utiliser(self)
            #Stats
            self.force = Dice.lancer()[0]
            self.dexterite = Dice.lancer()[0]
            self.constitution = Dice.lancer()[0]
            self.intelligence = Dice.lancer()[0]
            self.sagesse = Dice.lancer()[0]
            self.charisme = Dice.lancer()[0]
            self.defense_physique = 0
            self.defense_magique = 0

        def stats(self):
            return f"""\
                Statistiques :
                force = {self.force}
                dextérité = {self.dexterite}
                constitution = {self.constitution}
                intelligence = {self.intelligence}
                sagesse = {self.sagesse}
                charisme = {self.charisme}

                Equipement :
                armes => {self.arme[0].nom}
                casque => {self.casque.nom}
                plastron => {self.plastron.nom}
                gants => {self.gants.nom}
                jambières => {self.jambieres.nom}
                bottes => {self.bottes.nom}
                """

        def info(self, other):
            return f"""\
                Info ennemi :
                nom = {other.__class__.__name__}
                race = {other.race}
                vie = {other.pv_max}
                armes = {other.armes}
                force = {other.force}
                dextérité = {other.dexterite}
                constitution = {other.constitution}
                intelligence = {other.intelligence}
                sagesse = {other.sagesse}
                charisme = {other.charisme}
                """

        def equiper(self, equipement):
            if isinstance(equipement, ArmeAUneMain):
                if self.arme[0] is None:
                    self.arme[0] = equipement
                    if equipement in self.equipements:
                        self.equipements.remove(equipement)
                elif self.arme[1] is None and isinstance(self.arme[0],ArmeADeuxMain) == False or isinstance(self.arme[0],ArmeADistance) == False:
                    self.arme[1] = equipement
                    if equipement in self.equipements:
                        self.equipements.remove(equipement)
            elif isinstance(equipement, ArmeADeuxMain) or isinstance(equipement, ArmeADistance):
                if self.arme[0] is None:
                    self.arme[0] = equipement
                    if equipement in self.equipements:
                        self.equipements.remove(equipement)
            elif isinstance(equipement, Casque):
                if self.casque is None:
                    self.casque = equipement
                    if equipement in self.equipements:
                        self.equipements.remove(equipement)
            elif isinstance(equipement, Plastron):
                if self.plastron is None:
                    self.plastron = equipement
                    if equipement in self.equipements:
                        self.equipements.remove(equipement)
            elif isinstance(equipement, Gants):
                if self.gants is None:
                    self.gants = equipement
                    if equipement in self.equipements:
                        self.equipements.remove(equipement)
            elif isinstance(equipement, Jambieres):
                if self.jambieres is None:
                    self.jambieres = equipement
                    if equipement in self.equipements:
                        self.equipements.remove(equipement)
            elif isinstance(equipement, Bottes):
                if self.bottes is None:
                    self.bottes = equipement
                    if equipement in self.equipements:
                        self.equipements.remove(equipement)
            return

        def desequiper(self, equipement):
            if isinstance(equipement, ArmeAUneMain) or isinstance(equipement, ArmeADeuxMain) or isinstance(equipement, ArmeADistance) :
                if self.arme != [None, None]:
                    self.equipements.append(equipement)
                    self.arme.remove(equipement)
                    self.arme.append(None)
            elif isinstance(equipement, Casque):
                if self.casque is not None:
                    self.equipements.append(equipement)
                    self.casque = None
            elif isinstance(equipement, Plastron):
                if self.plastron is not None:
                    self.equipements.append(equipement)
                    self.plastron = None
            elif isinstance(equipement, Gants):
                if self.gants is not None:
                    self.equipements.append(equipement)
                    self.gants = None
            elif isinstance(equipement, Jambieres):
                if self.jambieres is not None:
                    self.equipements.append(equipement)
                    self.jambieres = None
            elif isinstance(equipement, Bottes):
                if self.bottes is not None:
                    self.equipements.append(equipement)
                    self.bottes = None
            return

        def consommer(self, objet):
            # Après, ici la logique devrait plutot être dans l'objet lui-même.
            # Genre objet.consommer(self)
            # Et dans les objets une méthode consommer(cible)
            if isinstance(objet, PotionDeMana):
                self.mana += objet.mana_regen
                if self.mana > self.mana_max:
                    self.mana = self.mana_max
                print("Vous récupérez tout votre mana.")
            elif isinstance(objet, PotionDeGuerison) or isinstance(objet, PotionDeGuerisonMajeur):
                gain = objet.soin.jeter()
                self.gagner_pv(gain)
                print(f"Vous gagnez {gain} points de vie !")
            objet.est_consomme = True
            self.consommables.remove(objet)

        def lancer(self, objet, other):
            precision = Dice.lancer(1,20)
            if precision[0] >= 10:
                other.perte_pv(objet.degat)
                print(f"L'ennemi perd {objet.degat} pv")
            else:
                print("Raté !")
            self.consommables.remove(objet)
            return

        def stat_cap(self, stat, bonus):
            stat += bonus
            if stat > 20:
                stat = 20
            elif stat < 1:
                stat = 1
            return
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classes des differentes classes disponibles -----------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    class Voleur(Joueur):
        def __init__(self, race="Nain", nom="Gimli"):
            super().__init__(race, nom)
            arc = Arc()
            self.equiper(arc)
            self.stat_cap(self.dexterite,5)
            self.stat_cap(self.intelligence,1)
            self.stat_cap(self.charisme,-2)
            self.defense_physique = 1

    class Barbare(Joueur):
        def __init__(self, race="Nain", nom="Gimli"):
            super().__init__(race, nom)
            h1 = Hache()
            h2 = Hache()
            self.equiper(h1)
            self.equiper(h2)
            self.stat_cap(self.force, 5)
            self.stat_cap(self.constitution, 4)
            self.stat_cap(self.intelligence, -2)
            self.defense_physique = 2

    class EluDeMoradin(Joueur):
        def __init__(self, race="Nain", nom="Gimli"):
            super().__init__(race, nom)
            marto = MarteauDeMoradin()
            self.equiper(marto)
            self.stat_cap(self.force,5)
            self.stat_cap(self.constitution,5)
            self.stat_cap(self.dexterite,5)
            self.stat_cap(self.intelligence,5)
            self.stat_cap(self.sagesse,5)
            self.stat_cap(self.charisme,5)
            self.defense_magique = 5
            self.defense_physique = 5

    class Tavernier(Joueur):
        def __init__(self, race="Nain", nom="Gimli"):
            super().__init__(race, nom)
            ptitepee = EpeeEnBois()
            self.arme = [ptitepee]
            self.stat_cap(self.force, -1)
            self.stat_cap(self.constitution, -1)
            self.stat_cap(self.dexterite, -1)
            self.stat_cap(self.intelligence, -1)
            self.stat_cap(self.sagesse, -1)
            self.stat_cap(self.charisme, -1)

    class Mage(Joueur):
        def __init__(self, race="Nain", nom="Gimli"):
            super().__init__(race, nom)
            self.type_degat = "magique"
            baton = BatonDeSorcier()
            self.arme = [baton, None]
            self.tete = CoiffeDerudi()
            self.torse = RobeDeMagicien()
            self.desequiper(self.casque)
            self.desequiper(self.plastron)
            self.tete.utiliser(self)
            self.torse.utiliser(self)
            mana1 = PotionDeMana()
            mana2 = PotionDeMana()
            self.consommables.append(mana1)
            self.consommables.append(mana2)
            self.mana = 100
            self.mana_max = 100
            self.stat_cap(self.force, -2)
            self.stat_cap(self.intelligence, 5)
            self.stat_cap(self.sagesse, 5)
            self.defense_magique = 2

        def sort1(self, other):
            store.log_msg("Missiles magiques !", self.couleur_log)
            degats_totaux = 0
            for element in Dice.lancer(3,10)[1]:
                if element > 2 :
                    degats = Dice.lancer(1,12)[0] + self.bonus(self.intelligence) + self.arme[0].attaque.jeter() - other.defense_magique
                    degats_totaux += max(0, degats) 
                else:
                    store.log_msg("Un missile rate sa cible !", self.couleur_log)
            self.mana -= 10
            return degats_totaux

        def sort2(self, other):
            store.log_msg("Boule de feu !", self.couleur_log)
            degats_totaux = 0
            if Dice.lancer()[0] > 11:
                degats_totaux = max(0, Dice.lancer(1,35)[0] + self.bonus(self.intelligence) + self.arme[0].attaque.jeter() - other.defense_magique)
                self.mana -= 20
            else:
                store.log_msg("La boule de feu rate lamentablement !", self.couleur_log)
            return degats_totaux

    #Classes des monstres -------------------------------------------------------------------------------------
    class Monstre(Entite):
        def __init__(self, race):
            super().__init__(race)
            self.type_degat = "physique"
            gain_exp = 0
            drop = []

    class Dummy(Monstre):
        def __init__(self, race = "Mannequin"):
            super().__init__(race)
            self.vie = self.pv_max = 9999
            self.constitution = 1

    class UiiaCat(Monstre):
        def __init__(self, race = "Dieu"):
            super().__init__(race)
            self.vie = self.pv_max = 120
            self.force = 12
            self.dexterite = 11
            self.constitution = 12
            self.intelligence = 1
            self.sagesse = 18
            self.charisme = 18
            self.defense_magique = 5
            self.defense_physique = 5

    class Skaven(Monstre):
        def __init__(self, race = "Skaven"):
            super().__init__(race)
            self.vie = self.pv_max = 40
            self.force = 12
            self.dexterite = 14
            self.constitution = 7
            self.intelligence = 5
            self.defense_physique = 2

    class CrapeauMagicien(Monstre):
        def __init__(self, race = "Crapeau"):
            super().__init__(race)
            self.type_degat = "magique"
            self.vie = self.pv_max = 60
            self.mana = self.mana_max = 60
            self.force = 6
            self.dexterite = 5
            self.constitution = 10
            self.intelligence = 12
            self.sagesse = 18
            self.charisme = 13
            self.defense_magique = 3

        def sort1(self, other):
            store.log_msg("Le crapaud invoque une pluie de grenouilles !", self.couleur_log)
            degats_totaux = 0
            for element in Dice.lancer(4,10)[1]:
                if element > 5:
                    degats = Dice.lancer(1,2)[0] + self.bonus(self.intelligence) - other.defense_magique
                    degats_totaux += max(0, degats)
                else:
                    pass 
            self.mana -= 10
            return degats_totaux

        def sort2(self, other):
            store.log_msg("Le crapaud vous crache dessus ! Attention : corrosif !", self.couleur_log)
            degats_totaux = 0
            if Dice.lancer(1,10)[0] > 6:
                degats_totaux = max(0, Dice.lancer(1,20)[0] + self.bonus(self.intelligence) - other.defense_magique)
                self.mana -= 20
            else:
                store.log_msg("Le crachat rate !", self.couleur_log)
            return degats_totaux
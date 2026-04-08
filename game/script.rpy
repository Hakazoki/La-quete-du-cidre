define config.developer = True
# Vous pouvez placer le script de votre jeu dans ce fichier.
init python:
    blorp=0
    
# Debug Menu ('CTRL + D' Pour ouvrire le menu)

init python:
    def toggle_debug():
        if config.developer:
            if renpy.get_screen("debug_class_menu"):
                renpy.hide_screen("debug_class_menu")
            else:
                renpy.show_screen("debug_class_menu")

init 1 python:
    config.underlay.append(
        renpy.Keymap(
            ctrl_K_d = toggle_debug,  
        )
    )

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image chat = im.Scale("chat01.png", 900, 1000)
image Oiia = im.Scale("Oiia_cat.png", 900, 1000)
image poster_chat = im.Scale("wanted-poster.png", 900, 1000)
image bg taverne = im.Scale("taverne01.jpg", 1920, 1080)
image fin_nice_boat = im.Scale("fin_nice_boat.png", 1920, 1080)
image bg_open_space = Solid("#cccccc")
image bg_office_night = Solid("#1a1a1a")
image frame_01 = im.Scale("bloggif_frames_gif/frame-01.jpg", 750, 750)
image frame_02 = im.Scale("bloggif_frames_gif/frame-02.jpg", 750, 750)
image frame_03 = im.Scale("bloggif_frames_gif/frame-03.jpg", 750, 750)
image frame_04 = im.Scale("bloggif_frames_gif/frame-04.jpg", 750, 750)
image frame_05 = im.Scale("bloggif_frames_gif/frame-05.jpg", 750, 750)
image frame_06 = im.Scale("bloggif_frames_gif/frame-06.jpg", 750, 750)
image frame_07 = im.Scale("bloggif_frames_gif/frame-07.jpg", 750, 750)
image frame_08 = im.Scale("bloggif_frames_gif/frame-08.jpg", 750, 750)
image frame_09 = im.Scale("bloggif_frames_gif/frame-09.jpg", 750, 750)
image frame_10 = im.Scale("bloggif_frames_gif/frame-10.jpg", 750, 750)
image frame_11 = im.Scale("bloggif_frames_gif/frame-11.jpg", 750, 750)
image frame_12 = im.Scale("bloggif_frames_gif/frame-12.jpg", 750, 750)
image frame_13 = im.Scale("bloggif_frames_gif/frame-13.jpg", 750, 750)
image frame_14 = im.Scale("bloggif_frames_gif/frame-14.jpg", 750, 750)
image frame_15 = im.Scale("bloggif_frames_gif/frame-15.jpg", 750, 750)
image frame_16 = im.Scale("bloggif_frames_gif/frame-16.jpg", 750, 750)
image frame_17 = im.Scale("bloggif_frames_gif/frame-17.jpg", 750, 750)
image frame_18 = im.Scale("bloggif_frames_gif/frame-18.jpg", 750, 750)
image plaine = im.Scale("Plaine.jpg", 1920, 1080)
image end_cave = im.Scale("end_cave.jpg", 1920, 1080)
image dungeon_entrance = im.Scale("dungeon_entrance.jpeg", 1920, 1080)
image labyrinthe_porte = im.Scale("porte_labyrinthe.png", 1920, 1080)
image salle_labyrinthe_porte_droite = im.Scale("Salle_Labyrinthe_Porte_Droite.png", 1920, 1080)
image salle_labyrinthe_porte_gauche = im.Scale("Salle_Labyrinthe_Porte_Gauche.png", 1920, 1080)
image salle_labyrinthe_trois_porte = im.Scale("Salle_Labyrinthe_Trois_Porte.jpg", 1920, 1080)
image salle_labyrinthe_porte_droite_centre = im.Scale("Salle_Labyrinthe_Porte_Droite_Centre.png", 1920, 1080)
image salle_labyrinthe_porte_gauche_centre = im.Scale("Salle_Labyrinthe_Porte_Gauche_Centre.png", 1920, 1080)
image salle_labyrinthe_porte_centre = im.Scale("salle_labyrinthe_porte_centre.png", 1920, 1080)
image salle_labyrinthe_coffre = im.Scale("salle_labyrinthe_coffre.png", 1920, 1080)
image mc_base = im.Scale("Minecraft-levier.png", 1920, 1080)
image mc_gauche = im.Scale("Minecraft-levier-1.png", 1920, 1080)
image mc_centre = im.Scale("Minecraft-levier-2.png", 1920, 1080)
image mc_droite = im.Scale("Minecraft-levier-3.png", 1920, 1080)
image truck_kun = im.Scale("truck_kun.png", 1920, 1080)
image handshake:
            "frame_01"
            0.1
            "frame_02"
            0.1
            "frame_03"
            0.1
            "frame_04"
            0.1
            "frame_05"
            0.1
            "frame_06"
            0.1
            "frame_07"
            0.1
            "frame_08"
            0.1
            "frame_09"
            0.1
            "frame_10"
            0.1
            "frame_11"
            0.1
            "frame_12"
            0.1
            "frame_13"
            0.1
            "frame_14"
            0.1
            "frame_15"
            0.1
            "frame_16"
            0.1
            "frame_17"
            0.1
            "frame_18"
            0.1
            repeat


# Progression Quizz

screen prog_questionnaire(etape, totale=10):
    zorder 80

    frame:
        xalign 0.5 yalign 0.05
        padding(7, 7)
        background Solid("#222222")
        
        hbox:
            spacing 5
            bar value AnimatedValue(etape, totale) xysize (300, 20) left_bar "#3498db" right_bar "#766050"

# Fin Progression Quizz

# Ecran des statistiques

screen bouton_stats():
    if pc is not None:
        textbutton "Statistiques":
            xalign 0.98 yalign 0.02 # Position Bouton
            action ToggleScreen("ecran_stats")

screen ecran_stats():
    modal True
    zorder 100

    frame:
        xalign 0.5 yalign 0.5
        padding (20,20)

        vbox:
            spacing 15

            if pc is not None:
                text "Statistiques de [pc.nom]" size 28 bold True xalign 0.5
                
                grid 2 13:
                    spacing 20

                    null height 10
                    null height 10
                    
                    text "Niveau :" bold True
                    text "[pc.lvl]"

                    text "PV :" bold True
                    text "[pc.vie]"

                    text "Mana :" bold True
                    text "[pc.mana]"

                    text "Exp :" bold True
                    text "[pc.exp]"

                    # Une cassure dans la grille
                    null height 10
                    null height 10

                    text "Classe : [pc.__class__.__name__]" bold True
                    null height 10

                    text "Constitution :" bold True
                    text "[pc.constitution]"

                    text "Force :" bold True
                    text "[pc.force]"

                    text "Dexterité :" bold True
                    text "[pc.dexterite]"

                    text "Intelligence :" bold True
                    text "[pc.intelligence]"

                    text "Sagesse :" bold True
                    text "[pc.sagesse]"

                    text "Charisme :" bold True
                    text "[pc.charisme]"
            
            else:
                text "Personnage pas encore initialisé." color "#ff0000" xalign 0.5
            
            null height 10

            textbutton "Fermer":
                xalign 0.5
                action Hide("ecran_stats")

# Fin ecran stats

# Inventaire

screen bouton_inventaire():
    if pc is not None:
        textbutton "Inventaire":
            xalign 0.98 yalign 0.06 # Position bouton
            action ToggleScreen("Inventaire")

screen Inventaire():
    modal True
    zorder 100
    
    default tooltip_objet = None

    frame:
        xalign 0.5 yalign 0.5
        padding (20, 20)
        xysize (650, 450) 

        vbox:
            spacing 15

            if pc is not None:
                text "Inventaire" size 28 bold True xalign 0.5
                
                hbox:
                    spacing 20
                    
                    

                    
                    frame:
                        xysize (250, 300)
                        padding (15, 15)
                        background Solid("#222222")
                        
                        if tooltip_objet is not None:
                            vbox:
                                spacing 10
                                text "[tooltip_objet.nom]" bold True size 22
                                text "[tooltip_objet.description]" size 14

                                if hasattr(tooltip_objet, 'effet') and tooltip_objet.effet != "Aucun":
                                    text "Effet : [tooltip_objet.effet]" size 16 color "#42f554"
                                    
                                if hasattr(tooltip_objet, 'mana_regen') and tooltip_objet.mana_regen > 0:
                                    text "Regen Mana : [tooltip_objet.mana_regen]" size 16 color "#42a4f5"
                                    
                                if hasattr(tooltip_objet, 'soin') and tooltip_objet.soin is not None:
                                    text "Soin : [tooltip_objet.soin.nb_dices]D[tooltip_objet.soin.nb_faces]" size 16 color "#f54242"
                                    
                        else:
                            text "Survolez un objet pour afficher ses propriétés." size 14 align (0.5, 0.5) text_align 0.5

                    vpgrid:
                        cols 4
                        spacing 5 
                        mousewheel True
                        scrollbars "vertical"
                        allow_underfull True
                        xysize (340, 300) 
                        
                        if pc.consommables:
                            for item in pc.consommables:
                                frame:
                                    xysize (80, 80)
                                    padding (5, 5)
                                    background Solid("#333333")
                                    
                                    imagebutton:
                                        idle item.icone 
                                        hover item.icone

                                        # Utilisation des consommables
                                        action Function(pc.consommer, item) 
                                        hovered SetScreenVariable("tooltip_objet", item)
                                        unhovered SetScreenVariable("tooltip_objet", None)
                                        align (0.5, 0.5)
            else:
                text "Pas encore d'inventaire." color "#ff0000" xalign 0.5
    
            null height 10

            textbutton "Fermer":
                xalign 0.5
                action Hide("Inventaire")

# Fin inventaire

# Equipements

screen bouton_equipement():
    if pc is not None:
        textbutton "Équipement":
            xalign 0.98 yalign 0.1 # Position bouton
            action ToggleScreen("Menu_Equipement")

screen slot_equipement(item, pos_x, pos_y, nom_slot):
    frame:
        xpos pos_x ypos pos_y
        xysize (80, 80)
        padding (5, 5)
        background Solid("#333333")

        if item is not None:
            imagebutton:
                idle Transform(item.icone, size=(64, 64))
                hover Transform(item.icone, size=(64, 64))

                # Déséquiper Items
                action Function(pc.desequiper, item) 
                hovered SetScreenVariable("tooltip_objet", item)
                align (0.5, 0.5)
        else:
            text nom_slot size 14 align (0.5, 0.5) color "#777777"

screen Menu_Equipement():
    modal True
    zorder 100
    default tooltip_objet = None

    frame:
        xalign 0.5 yalign 0.5
        padding (20, 20)
        xysize (1050, 500)

        hbox:
            spacing 20

            # --- Trucs Equiper ---
            frame:
                xysize (300, 460)
                background Solid("#222222")
                text "Équipement" xalign 0.5 ypos 10 bold True size 22

                use slot_equipement(pc.casque, 110, 50, "Tête")
                use slot_equipement(pc.arme[0] if pc.arme else None, 20, 140, "Arme")
                use slot_equipement(pc.arme[1] if pc.arme else None, 20, 230, "Arme")
                use slot_equipement(pc.plastron, 110, 140, "Torse")
                use slot_equipement(pc.gants, 200, 140, "Mains")
                use slot_equipement(pc.jambieres, 110, 230, "Jambes")
                use slot_equipement(pc.bottes, 110, 320, "Pieds")

            # --- Inventaire ---
            frame:
                xysize (340, 460)
                background Solid("#222222")
                
                vpgrid:
                    cols 4
                    spacing 5 
                    mousewheel True
                    scrollbars "vertical"
                    allow_underfull True
                    
                    if hasattr(pc, 'equipements') and pc.equipements:
                        for item in pc.equipements:
                            if item is not None:
                                frame:
                                    xysize (80, 80)
                                    padding (5, 5)
                                    background Solid("#333333")
                                    
                                    imagebutton:
                                        idle Transform(item.icone, size=(64, 64)) 
                                        hover Transform(item.icone, size=(64, 64))
                                        action Function(pc.equiper, item) 
                                        hovered SetScreenVariable("tooltip_objet", item)
                                        unhovered SetScreenVariable("tooltip_objet", None)
                                        align (0.5, 0.5)
                    else:
                        text "Sac vide." size 16 align (0.5, 0.5) color "#777777"

            # --- Tooltip ---
            frame:
                xysize (330, 400)
                yalign 1.0
                padding (15, 15)
                background Solid("#222222")
                
                if tooltip_objet is not None:
                    textbutton "x":
                        xalign 1.0 yalign 0.0
                        action SetScreenVariable("tooltip_objet", None)
                    vbox:
                        spacing 10
                        text "[tooltip_objet.nom]" bold True size 20
                        null height 5
                        viewport:
                            mousewheel True
                            scrollbars "vertical"
                            yfill False 
                            
                            vbox:
                                spacing 10
                                text "[tooltip_objet.description]" size 14
                                
                                if hasattr(tooltip_objet, 'get_stats_affichage'):
                                    for stat in tooltip_objet.get_stats_affichage():
                                        text stat size 16
                else:
                    text "Survolez un objet." size 14 align (0.5, 0.5)
                    
        textbutton "Fermer":
            xalign 1.0 yalign 0.0
            action Hide("Menu_Equipement")

# Fin Equipements

# Ecran séductrion

screen barre_seduction():
    zorder 999

    fixed:
        xalign 0.5 
        ypos 50
        xsize 400 ysize 80 

        
        add Solid("#330000aa") xsize 400 ysize 80 xalign 0.5

        
        $ bar_val = max(0, min(100, (seduction + 50) / 2))
        bar:
            value bar_val
            range 100
            xsize 380
            ysize 30 
            xalign 0.5
            ypos 25  
            unscrollable "unscrollable"

        
        if seduction > 100:
            $ extension_droite = (seduction - 100) * 4
            add Solid("#ffaa44"):
                xsize extension_droite ysize 30
                ypos 25   
                xpos 400   
                xanchor 0.0

        
        if seduction < -50:
            $ extension_gauche = (abs(seduction) - 50) * 4
            add Solid("#ff4444"):
                xsize extension_gauche ysize 30
                ypos 25
                xpos 0     
                xanchor 1.0

        
        text "Niveau de Séduction : [seduction]%" size 18 xalign 0.5 ypos 5
        
        
        if seduction <= -50:
            text "{b}{color=#ff0000}ERREUR : PURETÉ CRITIQUE{/color}{/b}" size 14 xalign 0.5 ypos 60
        elif seduction >= 150:
            text "{b}{color=#ff00ff}ALERTE : OBSESSION{/color}{/b}" size 14 xalign 0.5 ypos 60

# Fin écreant séduction

# Variables de log

default combat_log = []
init python:
    def log_msg(texte, couleur="#dddddd"):
        combat_log.append(f"{{color={couleur}}}{texte}{{/color}}")
        if len(combat_log) > 6:
            combat_log.pop(0)

# Fin log

# Stats Combat Crapo

screen Combat_Crapo():
    zorder 80 

    
    frame:
        xalign 0.02 yalign 0.2
        padding (15, 15)
        xysize (350, 150)
        
        vbox:
            spacing 5
            text "[pc.nom]" size 24 bold True

            hbox:
                text "PV:" min_width 50
                bar value AnimatedValue(pc.vie, pc.pv_max) xysize (200, 20) left_bar "#2ecc71"
                text " [pc.vie]/[pc.pv_max]" size 14
                
            if pc.mana_max > 0:
                hbox:
                    text "PM:" min_width 50
                    bar value AnimatedValue(pc.mana, pc.mana_max) xysize (200, 20) left_bar "#3498db"
                    text " [pc.mana]/[pc.mana_max]" size 14

    frame:
        xalign 0.98 yalign 0.2
        padding (15, 15)
        xysize (350, 120)
        
        vbox:
            spacing 5
            text "Albert le [crapomagicien.race]" size 24 bold True color "#e74c3c"
            
            hbox:
                text "PV:" min_width 50
                bar value AnimatedValue(crapomagicien.vie, crapomagicien.pv_max) xysize (200, 20) left_bar "#e74c3c"
                text " [crapomagicien.vie]/[crapomagicien.pv_max]" size 14

    frame:
        xalign 0.5 yalign 0.85
        padding (15, 15)
        xysize (650, 200)
        background Solid("#111111d9")
        
        vbox:
            spacing 5
            for msg in combat_log:
                text msg size 16 color "#dddddd"

    # Fin Stats Combat Crapo

# Stats Combat Oiia

screen Combat_Oiia():
    zorder 80 

    
    frame:
        xalign 0.02 yalign 0.2
        padding (15, 15)
        xysize (350, 150)
        
        vbox:
            spacing 5
            text "[pc.nom]" size 24 bold True

            hbox:
                text "PV:" min_width 50
                bar value AnimatedValue(pc.vie, pc.pv_max) xysize (200, 20) left_bar "#2ecc71"
                text " [pc.vie]/[pc.pv_max]" size 14
                
            if pc.mana_max > 0:
                hbox:
                    text "PM:" min_width 50
                    bar value AnimatedValue(pc.mana, pc.mana_max) xysize (200, 20) left_bar "#3498db"
                    text " [pc.mana]/[pc.mana_max]" size 14

    frame:
        xalign 0.98 yalign 0.2
        padding (15, 15)
        xysize (350, 120)
        
        vbox:
            spacing 5
            text "[oiiacat_combat.race]" size 24 bold True color "#e74c3c"
            
            hbox:
                text "PV:" min_width 50
                bar value AnimatedValue(oiiacat_combat.vie, oiiacat_combat.pv_max) xysize (200, 20) left_bar "#e74c3c"
                text " [oiiacat_combat.vie]/[oiiacat_combat.pv_max]" size 14

    frame:
        xalign 0.5 yalign 0.85
        padding (15, 15)
        xysize (650, 200)
        background Solid("#111111d9")
        
        vbox:
            spacing 5
            for msg in combat_log:
                text msg size 16 color "#dddddd"

    # Fin Stats Combat Oiia

# définition de variables

default p = None
default drunk = 0
default pts_voleur = 0
default pts_barbare = 0
default pts_mage = 0
default pc = None
default fouille_salle4 = False
default skaven_yandere_fin = False

# Déclarez les personnages utilisés dans le jeu.
define g = Character('Gromli Fût-Perdu', color="#ff3434")
define s = Character('La Serrure qui parle', color="#ff3434")
define h = Character('Héro', color="#c8ffc8")
define t = Character('Tavernier', color="#c8ffc8")
define v = Character('Voyante louche', color="#c8ffc8")
define b = Character('Barbare costaud', color="#c8ffc8")
define p = Character("[pc_name]", color="#ffabf1")
define se = Character("Oracle de Maintenance blazé")
define boss = Character('M. Grondin (Manager)', color="#ff0000")
define coll = Character('Kévin du Marketing', color="#00fbff")
define truck = Character('Truck-kun', color="#f098ca")
define crapo = Character('Albert Le Crapo Magicien De Lécole De La Bave', color="#77f242")
define voix = Character('Voix Mystérieuse', color="#8e44ad", what_italic=True)
define pnj_skaven = Character("Skaven", color="#5c4033")
define inconnu = Character("???", color="#585858", what_italic=True)
define oiiacat = Character("Chat", color="#9df2e1", what_italic=True)

# Déclarez des transitions et effets visuels
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define flash_rouge = Fade(0.1, 0.0, 0.5, color="#ff0000")
define flash_blanc = Fade(0.1, 0.0, 0.5, color="#ffffff")

#Déclarez des sfx
define sfx_get_class = "audio/get_class.mp3"
define sfx_item_get = "audio/item_get.mp3"

# Le jeu commence ici
label start:
    show screen bouton_stats
    show screen bouton_inventaire
    show screen bouton_equipement
    achieve started


# Switch pour les différents états du scénario
$ boire_alcool = False
$ tavernier_taverne = True
$ voyante_taverne = True
$ barbare_taverne = True
$ glorp = True
# Fin Switch

# Création du personnage
label intro:

    play music "quiz_theme.mp3"
    
    voix "Qui es-tu jeune nain?"
    jump q1
label q1:
    show screen prog_questionnaire(1)
    with dissolve
    menu:
        voix "Un voyou embête une fille dans une rue marchande animée ! Que faîtes-vous ?"
        "a)Je sauve la demoiselle en détresse !!!.":
            $ pts_barbare += 1
            voix "L'héroïsme... ou l'inconscience."
            jump q2
        "b)Je lui baisse discrètement son slip.":
            $ pts_voleur += 1
            voix "Hehe... La fourberie naine dans toute sa splendeur."
            jump q2
        "c)J'appelle la milice.":
            $ pts_mage += 1
            voix "Pragmatique. Très bien."
            jump q2
        "d)Je me fais dessus.":
            voix "..."
            voix "Pathétique. Passons."
            jump q2

label q2:
    show screen prog_questionnaire(2)
    with dissolve
    menu:
        voix "Un pouilleux commence une conversation avec vous. Vous ne comprenez absolument rien à ce qu'il dit. Que lui dîtes-vous?"
        "a)Hum... Vous pouvez répéter ?":
            $ pts_mage += 1
            voix "Vous avez l'intention de lui faire répétez combien de fois ?"
            jump q3
        "b)Bien... Hum, il faut que j'y aille.":
            $ pts_voleur += 1
            voix "Belle esquive !"
            jump q3
        "c)Ques tu mveu, tu veu une pièce c'est ça ?.":  
            $ pts_barbare += 1
            voix "Vous ne savez pas parler ?"
            jump q3
label q3:
    show screen prog_questionnaire(3)
    with dissolve
    menu:
        voix "Un collègue de picole vous ramène quelque chose que vous aviez oublié. Comment le remerciez-vous ?"
        "a)Merci, je te revaudrai ça.":  
            $ pts_voleur += 1
            voix "Un service pour un service, bel esprit !"
            jump q4
        "b)Merci, mon brave !":
            $ pts_mage += 1
            voix "Simple, mais efficace"
            jump q4
        "c)Une grosse baffe dans la tronche, c'est MES affaires.":
            $ pts_barbare += 1
            voix "Parfait, apprenez lui à ne pas toucher à vos affaires !"
            jump q4
        
label q4:
    show screen prog_questionnaire(4)
    with dissolve
    menu:
        voix "Une main sort des toilettes ! Que faîtes-vous?"
        "a)Je m'enfuis en hurlant.":
            $ pts_voleur += 1
            voix "Mimi Geignarde est une folle, fuyez !"
            jump q5
        "b)Je referme le couvercle.":  
            $ pts_mage += 1
            voix "Et vous laissez cette pauvre main dans les sanitaires ? La pauvre."
            jump q5
        "c)Je la serre.":
            $pts_barbare += 1
            voix "Quelle politesse, un nain digne de ce nom."
            jump q5

label q5:
    show screen prog_questionnaire(5)
    with dissolve
    menu:
        voix "Racontez-nous une blague"
        "a)Alors c'est un nain, un elfe et un orc qui rentrent dans un bar...":
            $ pts_voleur += 1
            voix "Oui, oui, oui, on va s'arreter là, merci."
            jump q6
        "b)Tire sur mon doigt !":
            $ pts_barbare += 1
            voix "... Vous avez quel âge serieusement ?"
            jump q6
        "c)T'imagine si Kornifex avait écrit le 3ème grimmoire de lucidité avec de l'encre de pieuvre calcinée!":
            $ pts_mage += 1
            voix "Euh, j'imagine que c'est amusant."
            jump q6

label q6:
    show screen prog_questionnaire(6)
    with dissolve
    menu:
        voix "Attrapez n'importe quel doigt de la main gauche avec la main droite. Quel doigt avez-vous choisi ?"
        "a)Le pouce.":
            voix "Choix intéressant."
            $ pts_barbare += 1
            jump q7
        "b)L'index.":
            voix "Choix intéressant."
            $ pts_barbare += 1
            $ pts_voleur += 1
            $ pts_mage += 1
            jump q7
        "c)Le majeur.":
            voix "Choix intéressant."
            $ pts_voleur += 1
            jump q7
        "d)L'annulaire.":
            voix "Choix intéressant."
            $ pts_mage += 1
            jump q7
        "e)L'auriculaire.":
            voix "Choix intéressant."
            $ pts_mage += 1
            jump q7

label q7:
    show screen prog_questionnaire(7)
    with dissolve
    menu:
        voix "Quelqu'un dit que vous êtes bizarre mais marrant. Vous vous sentez comment ?"
        "a)Super!":
            voix "Quel optimisme, vous n'écoutez que le positif !"
            $ pts_voleur += 1
            jump q8
        "b)Triste.":
            voix "Quel esprit faible, vous n'écoutez que le négatif."
            $ pts_mage += 1
            jump q8
        "c)Nain.":
            voix "Euh... Oui."
            $ pts_barbare += 1
            $ pts_mage += 1
            $ pts_voleur += 1
            jump q8
        "d)Ca me laisse naindifférent.":
            voix "Très drôle..."
            $ pts_mage += 1
            $ pts_voleur += 1
            jump q8
        
label q8:
    show screen prog_questionnaire(8)
    with dissolve
    menu:
        voix "Voici un seau. Si vous mettez de l'eau dedans, vous le remplissez..."
        "a)A ras.":
            voix "Vous allez en faire tomber partout."
            $ pts_barbare += 1
            jump q9
        "b)A demi.":
            voix "Un choix raisonnable."
            $ pts_mage += 1
            jump q9
        "c)Un peu.":
            voix "C'est tout ?"
            $ pts_voleur += 1
            jump q9
        "d)Jeter le seau.":
            voix "Euh, vous êtes sensé remplir le seau pas le jeter."
            $ pts_barbare += 1
            jump q9

label q9:
    show screen prog_questionnaire(9)
    with dissolve
    menu:
        voix "Vous entendez un cri venant de derrière la porte ! Comment réagissez-vous ?"
        "a)Je l'ouvre d'un coup.":
            voix " Quel réactivité !"
            $  pts_voleur += 1
            jump q10
        "b)Je crie aussi.":
            voix "Pourquoi ?"
            $ pts_barbare += 1
            jump q10
        "c)Je toque à la porte.":
            voix "Woah, vous êtes d'un calme et d'une politesse à toute épreuve."
            $ pts_mage += 1
            jump q10

label q10:
    show screen prog_questionnaire(10)
    with dissolve
    menu:
        voix "Vous gagnez le jackpot au WiNainMax ! Que faîtes-vous de l'argent ?"
        "a)J'économise.":
            voix "Le choix de la prudence, un choix judicieux"
            $ pts_voleur += 1
        "b)Je le donne.":
            voix "Quel âme charitable, si seulement le monde était rempli d'homme comme vous !"
            $pts_mage += 1
        "c)Tournée générale de 3 semaines au bar !":
            voix "HAHAHAHA, un vrai nain !"
            $ pts_barbare += 1


stop music fadeout 2.5
hide screen prog_questionnaire

# Fin Création

# Instanciation Joueur

python:
    scores_classes = {"Barbare": pts_barbare, "Voleur": pts_voleur, "Mage": pts_mage}
    score_max = max(scores_classes.values())
    vainqueurs = [classe for classe, score in scores_classes.items() if score == score_max]
    
    if len(vainqueurs) > 1:
        classe_joueur = renpy.random.choice(vainqueurs)
    else:
        classe_joueur = vainqueurs[0]
    
    match classe_joueur:
        case "Barbare":
            pc = Barbare()
        case "Voleur":
            pc = Voleur()
        case "Mage":
            pc = Mage()

    
    
# Fin Instanciation Joueur

label personnage:
    
    if classe_joueur == "Barbare":
        "Votre audace sans limites fait de vous un guerrier intrépide, dont le cri de guerre fait trembler les murs des donjons les plus sombres !"
        play sound sfx_get_class
        "Vous êtes barbare"
    if classe_joueur == "Voleur":
        "Votre sens de l'observation aiguisé fait de vous un expert de la discrétion, capable de déjouer tous les pièges pour s'emparer des trésors les mieux gardés."
        play sound sfx_get_class
        "Vous êtes voleur"
    if classe_joueur == "Mage":
        "Votre curiosité insatiable pour les mystères du monde fait de vous un érudit des arcanes, maniant les éléments pour transformer le destin à votre guise."
        play sound sfx_get_class
        "Vous êtes mage"


scene bg taverne

"Tout commença un soir ordinaire, dans une taverne qui ne payait pas de mine, quand un drôle de nain bien connu du village grimpa sur une table pour attirer l'attention."

show chat at right with moveinbottom

g "Mon trésor ? Je vous le laisse si vous le voulez. Trouvez-le ! Je l'ai laissé quelque part dans ce monde !"

hide chat

"Dit-il en s'évanouissant"

play music "elevator-music.mp3"

$ pc_name = renpy.input("Brave aventurier, fils de glorp et héritier au trône de glorptopia, quel est ton valeureux nom ?", length=20).strip() or "Aventurier"

stop music


$ pc.nom = Character(pc_name)
$ p = Character(pc_name)


menu:

    "Je suis mineur":
        jump mineur

    "je suis majeur":
        jump majeur
    "Es-tu mineur ou majeur ?"

label mineur:
    "Dorian... c'est une taverne ici, sort d'ici !"
    jump fin

label majeur:
    "Salutation [pc_name], que veux-tu ?"
    jump choix_boire

label majeur_boit:
    "Ce sera tout ?"
    jump choix_boire

menu choix_boire:

    "Je veux me rendre dans le donjon !":
        jump aventure
    "J'ai soif":
        $ boire_alcool = True
        jump alcool
label alcool:
    "*Gulp* *Gulp* *Gulp*"
    $ drunk += 1
    if drunk >= 5:
        jump finalcool
    else:
        jump majeur_boit

label aventure:
    "Pourquoi veux-tu te rendre dans le donjon ?"

menu:

    "Pour la gloire":
        jump taverne
    
    "Pour l'argent":
        jump taverne

    "Pour l'alcool" if boire_alcool:
        jump dialogue_tavernier

label taverne:
    t "Laisse tomber, le donjon est un endroit trop dangeureux pour un nain comme toi"
    p "J'ai pas peur ! Dis moi comment aller à la taverne"
    jump dialogue_tavernier

label dialogue_tavernier:
    t "HAHAHA, t'es un marrant toi !"
    t "Tiens, voici une carte pour aller dans le donjon."
    p "Merci chef !"
    jump choix_taverne
    "Que voulez-vous faire maintenant ?"

menu choix_taverne: 
    "Parler au tavernier" if tavernier_taverne:
        $ tavernier_taverne = False
        jump choix_tavernier
    "Parler à une voyante" if voyante_taverne:
        $ voyante_taverne = False
        jump choix_voyante
    "Parler à un barbare" if barbare_taverne:
        $ barbare_taverne = False
        jump choix_barbare
    "Jouer aux runes avec le nain du coin" if glorp:
        $ glorp = False
        p "Hé l'ami, on se fait une partie de runes ?"
        "Le nain sort une grille de 10x10. C'est un puzzle 'Tête de Monstre'."
        call screen picross(PUZZLE_CRANE)
        p "Haha ! J'ai résolu ton énigme !"
        "Le nain grogne et te donne quelques pièces d'or."
        jump choix_taverne
    "Sortir de la taverne":
        jump sortie_taverne
    "Que voulez-vous faire maintenant ?"


menu choix_tavernier:
    "Sers moi ton meilleur alcool pour me donner du courage !":
        jump alcool_tavernier
    "T'as des informations sur le donjon ?":
        jump information_tavernier
    t "Encore toi ? Tu veux quoi ?"
label alcool_tavernier:
    t "Tiens, une bière."
    jump choix_taverne
label information_tavernier:
    t "J'en sais rien, bon courage."
    jump choix_taverne

menu choix_voyante:
    "J'SUIS PAS PETIT !":
        jump enerve_voyante
    "D'accord !":
        jump avenir_voyante
    "Je ne crois pas en la voyance.":
        jump choix_taverne
    v "Bonjour, petit nain, veux-tu lire ton avenir ?"
label enerve_voyante:
    v "Non bien sur, tu es un nain de taille de nain."
    p "QUOI ? T'ES MECHANTE, JE ME CASSE !"
    jump choix_taverne
label avenir_voyante:
    v "Bien, quelle est ta date de naissance ?"
    p "J'sais pas."
    v "Mmh, je vois ..."
    p "Tu vois quoi ?"
    v "Ton avenir est curieux, ta destiné sera rempli d'embuche, mais si tu restes courageux, tu atteindra ton but."
    p "Ok."
    jump choix_taverne
    
menu choix_barbare:
    "Vous le prennez par le col":
        jump finbarbare
    "Vous vous excusez et continuez votre chemin":
        jump choix_taverne
    
    "Vous vous faites une poignée de main" if isinstance(pc, Barbare):
        show handshake:
            align (.50, .10)
        "MY MAN"
        hide handshake
        jump choix_taverne 
    "Un barbare passe à côté de vous et vous bouscule, comment réagissez vous ?"


label sortie_taverne:
    "Après de longues heures à vous amuser à la taverne, vous décidez d'enfin sortir de la taverne et vous approchez de la porte."
    
menu choix_sortie_taverne:
    "Changer d'avis et retourner dans la taverne":
        jump fintaverne
    "Ouvrir la porte et débuter votre aventure":
        $ dice_isekai = Dice.lancer(1, 100)[0]
        if dice_isekai >= 99:
            jump truck_kun
        else:
            jump exterieur_taverne

label exterieur_taverne:
    scene plaine

menu:        
    "Vous décidez de la parcourir jusqu'à ce que vous trouviez le donjon.":
        jump entree_donjon
    "Vous criez très fort pour débuter votre aventure":
        jump crier_fort   
    "Vous vous retrouvez devant une plaine magnifique. Vous éprouvez une légère nostalgie en la regardant."

label crier_fort:
    "Les passants vous regardent, ils vous prennent juste pour un guignol"
    jump entree_donjon
    
label entree_donjon:
    scene dungeon_entrance

menu:
    "Vous entrez dans le donjon":
        jump debut_donjon

    "Vous admirez l'entrée":
        jump admire_entree
    "Vous voila devant le donjon, que faites-vous ?"

label admire_entree:
    "C'est un beau donjon"
    jump entree_donjon

label debut_donjon:

#------------------------------------- COMBAT CRAPAUD MAGICIEN -------------------------------------

    scene labyrinthe_porte
    "Alors que vous approchez la porte, vous entendez un étrange croakement, il vous donne froid dans le dos"
    play sound "croak.mp3" volume 0.5
    inconnu "*croak* *croak*"
    with flash
    show crapo at right with moveinright
    "C'est alors que la terrible créature surgit !"
    p "Un crapaud magicien, je hais ces saloperies de tout mon être ! Leurs yeux sont pleins de malice ..."

    $ crapomagicien = CrapeauMagicien()
    $ combat_log = []
    $ log_msg("Un Crapaud Magicien vous barre la route !")

    show screen Combat_Crapo

    label boucle_combat_crapo:
        if pc.vie <= 0:
            jump defaite_crapo
        if crapomagicien.vie <= 0:
            jump victoire_crapo

        menu:
            
            "Attaquer avec [pc.arme[0].nom]" if not isinstance(pc, Mage) and pc.arme:
                $ degats = pc.attaquer(crapomagicien)
                $ log_msg(f"Vous attaquez ! Le crapaud subit {degats} dégâts.")
                with hpunch

            "Attaquer à mains nues" if not isinstance(pc, Mage) and not pc.arme:
                $ degats = pc.attaquer(crapomagicien)
                $ log_msg(f"Vous collez un boure-pif ! Le crapaud subit {degats} dégâts.")
                with hpunch

            "Canaliser un sort" if isinstance(pc, Mage) and pc.mana >= 20:
                $ degats = pc.attaquer(crapomagicien)
                $ log_msg(f"Vous déchainez un sort ! Le crapaud subit {degats} dégâts.")
                with flash_blanc

            "Canaliser un faible sort" if isinstance(pc, Mage) and pc.mana <= 20 and pc.mana >= 10:
                $degats = pc.sort1(crapomagicien)
                $ log_msg(f"Vous lancez un faible missile magique, il ne vous reste plus de mana ! Le crapaud subit {degats} dégâts.")
                with flash_blanc

            "Vous n'avez plus de mana !!" if isinstance(pc, Mage) and pc.mana <=10:
                $ log_msg(f"Vous tentez de canaliser le peu de mana qu'il vous reste mais vous êtes à sec ! Prenez une potion !")

            

        $ degats_subis = crapomagicien.attaquer(pc)
        $ log_msg(f"Le crapaud riposte ! Vous subissez {degats_subis} dégâts.")
        if degats_subis > 0:
            with vpunch
            with flash_rouge

        jump boucle_combat_crapo

label defaite_crapo:
    hide screen Combat_Crapo
    "Le terrifiant crapaud magicien viens à bout de votre piètre vie de nain, vous n'étiez tout simplement pas à la hauteur d'une telle créature."
    jump fin

label victoire_crapo:
    hide screen Combat_Crapo
    "Vous avez vaincu le terrible crapaud magicien !"
    jump entre_labyrinthe

#------------------------------------- FIN COMBAT CRAPAUD MAGICIEN -------------------------------------


label entre_labyrinthe:
    scene labyrinthe_porte

    menu:
        "Une grande porte ce dresse devant vous, que faites-vous"

        "Vous évaluez la solidité de la porte avec vos pectoraux saillants." if isinstance(pc,Barbare):
            $ d20 = Dice.lancer(1,20)[0]
            jump voie_du_barbare

        "Vous sortez vos outils en espérant que vos mains tremblent dans le bon sens." if isinstance(pc,Voleur):
            $ d20 = Dice.lancer(1,20)[0]
            jump voie_du_voleur

        "Vous utilisez votre élocution pour convaincre la porte que sa fonction de fermeture est obsolète." if isinstance(pc,Mage):
            $ d20 = Dice.lancer(1,20)[0]
            jump voie_du_mage

        "Vous décidez de rebrousser chemin parce-qu'à quoi bon ? De toute façon, cette aventure devait bien se terminer quelque part":
            jump autre_chemin

label autre_chemin:
    scene plaine

    menu:
        "Abandonner votre quête et repartir affronter les rires de la taverne":
            jump fin_depression

        "Reprendre votre courage en main et repartir affronter votre destin":
            $ d20 = Dice.lancer(1,20)[0]
            if isinstance(pc,Barbare):
                jump voie_du_barbare
            if isinstance(pc,Voleur):
                jump voie_du_voleur
            if isinstance(pc,Mage):
                jump voie_du_mage

        "Vous rebroussez chemin et, à la vue de la taverne, votre point de départ, vous ressentez une déception profonde envers vous même. Que souhaitez-vous faire ?"
       
label fin_depression:
    scene bg taverne

    "Vous revoilà à la taverne, vous vous étiez juré de changer mais le patron de la taverne et les habitués vous voient passer les portes pour une énième fois."
    "Vous entendez des rires éclater en vous revoyant, vous qui étiez si sûr de vous avant de partir. Vous les entendez remettre en question votre courage et votre sens de l'héroïsme."
    "Personne n'attendait rien de vous mais vous avez quand même réussi à décevoir le peu de personne qui aurait pu croire en vous."
    "La couardise n'est pas une vertue mais savoir reconnaître ses faiblesses, oui."
    "Vous n'êtes pas le héros de cette histoire et vous le savez. A présent, vous allez juste essayer de vivre avec cette humiliation sur la conscience."
    jump fin

label voie_du_barbare:      
        if d20 == 20:
            "Vous fixez la porte avec un mépris souverain et la traversez sans l'ouvrir : le concept de 'porte' est purement subjectif pour vous"
            jump labyrinthe_salle01   
        elif d20 >= 10:
            "Vous donnez un grand coup d'épaule. Dans un craquement sinistre, le bois cède. Vous passez."
            jump labyrinthe_salle01
        elif d20 > 1:
            "Vous chargez la porte, mais vous rebondissez dessus lamentablement. Votre épaule vous fait mal."
            jump entre_labyrinthe
        else:
            "Vous tentez de défoncer la porte avec votre tête. la porte n'a rien, mais vous vous assommez tout seul pour les dix prochaine minute."
            jump entre_labyrinthe

label voie_du_voleur:
        if d20 == 20:
            "Vous trébuchez sur vos propres lacets, puis tombez la tête la première contre la porte qui s'ouvre par miracle. Quel talent."
            jump labyrinthe_salle01
        elif d20 >= 10:
            "Quelques secondes de manipulation avec vos outils et le verrou finit par céder dans un clic satisfaisant."
            jump labyrinthe_salle01
        elif d20 > 1:
            "La serrure est plus complexe que prévu. Vous n'arrivez qu'à coincer un bout de métal à l'intérieur."
            jump entre_labyrinthe  
        else:
            "Votre outil de crochetage casse net dans la serrure. En prime, vous vous pincez les doigts si fort que vous poussez un cri de souris."
            jump entré_labyrinthe

label voie_du_mage:
        if d20 == 20:
            "Vous convainquez la serrure que, d'un point de vue métaphysique, son état naturel devrait être 'déverrouillé'. Elle s'exécute par pur respect intellectuel."
            jump labyrinthe_salle01
        elif d20 >= 10:
            "Votre argumentation est implacable. Le verrou, intimidé par votre logique, finit par lâcher prise dans un soupir métallique."
            jump labyrinthe_salle01
        elif d20 > 1:
            "La porte est têtue. Elle refuse d'écouter vos arguments et semble même se verrouiller un peu plus fort par pur esprit de contradiction."
            jump entre_labyrinthe_salle01
        else:
            "À force de vouloir paraître trop savant, vous vous emmêlez dans vos syllabes et lancez accidentellement un sort de 'Mutisme' sur vous-même. Vous ne pouvez plus dire un mot, et la porte semble se moquer de vous en silence."
            jump entre_labyrinthe_salle01

label labyrinthe_salle01:
    scene salle_labyrinthe_trois_porte

    if isinstance(pc, Barbare):
        $ description_salle = "L'odeur de poussière vous donne envie de frapper les murs pour vérifier l'écho. Quelle porte choisir ?"
    elif isinstance(pc, Voleur):
        $ description_salle = "Le sol est trop propre pour être honnête... Quelque chose cloche. Par où passer ?"
    else:
        $ description_salle = "L'air vibre d'une magie instable qui pourrait transformer vos bottes en canards. Quelle direction prendre ?"
    
    menu:
        
        "[description_salle]"

    
        "Vous décidez de prendre la porte à droite":
            jump labyrinthe_salle03

        "Vous décidez de prendre la porte à gauche":
            if isinstance(pc, Barbare):
                jump salle02_enigme_barbare
            elif isinstance(pc, Voleur):
                jump salle02_enigme_voleur
            else:
                jump salle02_enigme_mage

        "Vous décidez de prendre la porte au centre":
            "Vous vous dirigez vers la porte située au centre de la pièce. En tentant de l'ouvrir, vous réalisez qu'elle est verrouillée de l'intérieur. Vous décidez alors de frapper poliment."
            "Une voix agacée s'élève derrière le bois :"
            "C'est occupé ! Revenez plus tard, quand j'aurai fini !"
            "Alors que la voix se tait, une odeur particulièrement âcre et indéfinissable s'échappe de l'interstice de la porte. Vous reculez instinctivement d'un pas, comprenant soudainement pourquoi cette pièce était fermée."
            jump labyrinthe_salle01

    
label salle02_enigme_barbare:
    scene salle_labyrinthe_porte_droite_centre
   
    menu:
        "Insérer votre hache dans l'encoche du premier guerrier.":
            "Rien ne se passe, à part un bruit de métal contre la pierre"
            jump salle02_enigme_barbare

        "Fapper un coup de poing démesuré sur le centre de la fresque.":
            "Bing ! Le mécanisme reconnaît la force pure. La port tremble et s'efface."
            jump labyrinthe_salle04

        "Chercher un bouton caché derrière le bouclier du roi.":
            show poster_chat
            "Vous trouvez un étrange poster qui vous semble familier"
            hide poster_chat
            jump salle02_enigme_barbare
   
    "La fresque représente quatre guerriers. Le dernier n'a pas d'arme, son poing est levé vers le ciel."

label salle02_enigme_voleur:
    scene salle_labyrinthe_porte_droite_centre
    "La serrure de la porte centrale vous regarde avec mépris. Elle semble attendre quelque chose."

menu enigme_voleur:
    s "Écoutez mon petit pote, je m'ennuie à mourir dans ce couloir. Si tu veux que je tourne, il me faut une info croustillante ou un truc qui brille. Alors ?"

    "Lui raconter une blague sur les barbare.":
        p "Alors, c'est l'histoire d'un barbare, mais pas un petit barbare de foire, non..."
        p "Un type qui s'apppele Grog. Le genre de gars qui utilise des troncs comme cure-dents et qui ne s'est pas laver depuis le couronnement du rois précédent."
        p "Bref..., Grog arrive devant la Grande Bibliothèque de l'Ordre des Sages. Il pousse les portes double - qui pèsent trois tonne chacune - comme si c'était des rideaux de perles."
        p "Il entre en faisant un boucan d'enfer avec ses bottes en cuir de mammouth. Un silence de mort règne, on entendrait une mouche péter."
        p "Grog marche sur le parquet qui gince, s'approche du bibliothécaire, un petit vieux tout sec qui ressemble à un parchemin oublié..."
        p "Il pose son énorme hache pleine de sang de gobelin sur le bureau en acjou vernis. Le bureau craque, le vieux sursaute, ses lunettes tombent."
        p "Grog le regarde droit dans les yeux, avec une haleine qui sent le vieux fromage de chèvre, et il hurle : {i}'HÉ, LE VIEUX ! DONNE-MOI LE PLUS GROS GRIMOIRE DE MAGIE QUE T'AS EN STOCK !'{/i}"
        p "Le vieux s'exécute en tremblant, il va chercher un livre monstrueux, au moins huit cents pages de parchemin sacré, relié en peau de dragon rouge avec des fermoins en argent pur."
        p "Grog ouvre le bouquin. Il regarde la première page. Ses yeux s'écarquillent, il commence à transpirer en voyant toutes ces petites lettres noires, bien alignées..."
        p "Et là, d'un coup, il se met à hurler à la mort : {i}'AU SECOURS ! DES ARAIGNÉES NOIRES SUR DU PAPIER BLANC ! ELLES VEULENT ME BOUFFER LE CERVEAU !'{/i}"
        p "Et là, il lève son énorme poing, il prend de l'élan pour éclater le livre et-"

        window hide
        pause 0.2

        "{b}{size=+20}STOP !{/size}{/b}" with hpunch

        p "Mais... J'arrive a la meilleure pa- "
        s "Oh par tous les engrenages du monde... Arrête. Pitié. J'ai eu envie de me dévisser toute seule dès la deuxième phrase."
        s "C'est long, c'est pénible, et la chute est plus plate que le ventre d'un squelette donjon."
        s "Je suis une serrure de précision, mon gars, j'ai des standards."
        s "Ne refaites plus jamais ça. Si j'avais des oreilles, je serais en train de saigner du cuivre fondu."
        s "Rangez votre humour au fond de votre sac, à côté de vos rossignols rouillés, et ne le ressortez que si vous voulez torturer quelqu'un."

        jump enigme_voleur

    "Lui glissez un pot-de-vin":
        p "Tien j'ai dix balle, tu veux ?"
        s "Dix balles ? Seulement ? Vous savez les temps sont durs en ce moment j'ai une femme, deux enfants..."
        p "Douze balles. C'est mon dernier mot, je n'ai plus que des jetons de lave-linge après ça, j'ai même plus de quoi payer la bonne Josianne"
        s "Josianne ? La Josianne qui fait les poussières dans l'aile Est ? Oh, ne m'en parlez pas, elle a un plumeau qui gratte, c'est un enfer pour mes finitions en cuivre."
        p "Oh, croyez-moi, entre son plumeau qui gratte et sa façon de polir le manche... elle sait comment faire briller les bijoux de famille, même les plus rouillés."
        s "(Un petit silence métallique gêné, puis un cliquetis de gorge)"
        s "Ah... Je vois le genre. Elle fait dans la 'rénovation complète' de l'équipement, c'est ça ? Je comprends mieux pourquoi le levier de la herse a l'air si... vigoureux ces temps-ci."
        p "Exactement. Alors, ces douze balles ? C'est ça ou je vous laisse avec la poussière et les acariens magiques."
        s "Bon... D'accord. Mais vous rajoutez un jeton de lave-linge. Le petit dernier a avalé un bouton de manchette et il fait un bruit de grelot quand il court, faut que je le passe à l'essorage."
        p "Vendu. Douze balles et un jeton de lavage. On est bons ?"
        s "On est bons. Allez, glissez ça dans la fente, et doucement hein ! Je suis pas une de ces serrures de taverne que tout le monde peut forcer avec un bout de fil de fer."
        "CLING. CLANG. SCHLIP."
        "La serrure gobe le tout avec un petit frisson de métal."
        s "Ah... Ça glisse tout seul. Allez, passez vite avant que la femme du verrou de gauche ne me surprenne à faire des affaires avec vous !"
        jump labyrinthe_salle04

    "Tenter de la crocheter en douce pendant qu'elle parle.":
        s "'AÏE ! MAIS ÇA VA PAS ? C'EST  DU HARCÈLEMENT, ÇA !' Elle se verrouille deux fois plus fort. 'Réfléchis un peu au lieu de tripoter mon mécanisme !'"
        jump enigme_voleur


label salle02_enigme_mage:
    scene salle_labyrinthe_porte_droite_centre

    "Vous entrez dans la salle. Pas de monstre, pas de pièges à piques, juste une petite table en bois avec un cristal de communication qui clignote frénétiquement en rose fluo."
    
    "Une voix nasillarde et fatiguée s'en échappe :"
    
    se "{i}'Bienvenue au Support Technique de l'Archimage Xylothar. Si vous appelez pour un familier coincé dans une dimension de poche, tapez 1.'{/i}"
    
    se "{i}'Si vous avez accidentellement transformé votre apprenti en table de chevet, tapez 2. Pour déverrouiller la porte, répondez à la question de sécurité suivante.'{/i}"
    
    se "{i}'L'énergie magique est comme un chat de gouttière... que se passe-t-il si vous lui mettez un petit chapeau pointu en plein milieu d'une tempête de mana ?'{/i}"

    
label .choix_enigme: 

    "Le cristal de communication attend votre réponse."

    menu:
        "Option 1 : La tempête s'arrête par respect pour votre style vestimentaire.":
            "Une petite voix ricane : {i}'Hahaha ! Non. La mode n'a aucun pouvoir ici.'{/i}"
            "Une étincelle rose vous pique le nez. Vous perdez 2 PV de dignité."
            $ pc.pv -= 2
            jump .choix_enigme 

        "Option 2 : Vous provoquez une explosion de paillettes et un paradoxe temporel.":
            "La voix change de ton : {i}'Ah ! Un connaisseur. C'est la base de la loi de Murphy Arcanique.'{/i}"
            "{b}CLIC.{/b} La porte se déverrouille."
            $ enigme_mage_resolue = True
            jump labyrinthe_salle04

        "Option 3 : Le chat devient un Archimage et vous demande un loyer.":
            "{i}'Théorie intéressante, mais nous sommes au SAV ici, pas dans un club d'écriture.'{/i}"
            "Le cristal s'éteint un instant... puis se rallume."
            jump .choix_enigme

label labyrinthe_salle04:
    scene salle_labyrinthe_coffre

    if not fouille_salle4:
        if isinstance(pc,Barbare):
            "Une salle étrangement calme. Pas de monstres, juste un coffre qui vous attend au milieu comme une provocation."
        elif isinstance(pc, Voleur):
            "Vos yeux s'écarquillent. Un poster de recherche ? Sur un mur de donjon ? Et ce coffre n'est même pas piégé..."
        elif isinstance(pc, Mage):
            "L'aura de cette salle est... bizarre. Ça sent moins le souffre et plus la litière propre. Très perturbant."
    
    label menu_salle04:
    menu:
        "Observer le poster sur le mur":
            "Il s'agit d'un avis de recherche pour un certain 'Gromli'. La prime est astronomique."
            "Le chat sur la photo a un regard qui semble lire dans votre âme... ou qui veut juste des croquettes."
            jump menu_salle04

        "Ouvrir le coffre" if not fouille_salle4:
            $ fouille_salle4 = True
            $ item1 = Cle()
            $ item2 = HerbeCap()
            
            if isinstance(pc, Barbare):
                "Vous soulevez le couvercle d'un coup sec. À l'intérieur, pas d'or, mais des objets curieux."
            elif isinstance(pc, Voleur):
                "Vous crochetez la serrure en un temps record. Le contenu est... inattendu."
            elif isinstance(pc, Mage):
                "D'un geste de la main, vous déverrouillez le coffre. Une odeur de plantes séchées s'en échappe."


            play sound sfx_item_get
            $ pc.consommables.append(item1)
            $ pc.consommables.append(item2)
            
            "{i}Vous avez obtenu la {b}[item1.nom]{/b} (ornée d'une tête de chat) !{/i}"
            "{i}Vous avez obtenu un sachet d'{b}[item2.nom]{/b}. Ça sent bizarrement bon.{/i}"
            "Ces objets ont été ajoutés à votre inventaire."
            jump menu_salle04

        "Repartir sur vos pas":
            "Vous laissez cette pièce étrange derrière vous et retournez vers la salle précédante."
            jump labyrinthe_salle02

label labyrinthe_salle02:
    scene salle_labyrinthe_porte_droite_centre
menu:
    "Vous n'avez plus de raisons de rester ici. Vous sentez que vous approchez du but."

    "Vous décidez de revenir sur vos pas":
        jump labyrinthe_salle01

    "Vous décidez de prendre la porte au centre":
        jump labyrinthe_salle04

label labyrinthe_salle03:
    scene salle_labyrinthe_porte_gauche_centre
menu:
    "Vous entendez un grondement sourd venant du fond de ce donjon. Qui sait ce qui vous attend à la fin de votre périple ?"

    "Vous décidez de prendre la porte au centre":
        jump salle_05_speed_dating

    "Vous décidez de revenir sur vos pas":
        jump labyrinthe_salle01



label salle_05_speed_dating:
    scene salle_labyrinthe_porte_centre
    $ seduction = 0
    show screen barre_seduction
    
    pnj_skaven "Skritch ! Approche-approche, humaine-chose. On va voir si ton cœur est assez noir-sombre pour moi !"

    
    pnj_skaven "D'abord... Qu'est-ce que tu penses de mon odeur ?"
    menu:
        "On pourrait peut-être aérer la salle ?":
            $ seduction -= 30
        "Tu sens le rat sauvage, c'est très musqué.":
            $ seduction += 20
        "Je n'ai jamais rien senti d'aussi nauséabond.":
            $ seduction -= 50
        "C'est une odeur... très marquée.":
            $ seduction += 10
    $ renpy.restart_interaction()

    
    pnj_skaven "Si on trouve une réserve de nourriture, comment on fait ?"
    menu:
        "On divise tout équitablement à 50/50.":
            $ seduction -= 20
        "Je mange tout et je te laisse les restes si tu es sage.":
            $ seduction += 40
        "Je te laisse manger en premier, c'est la politesse.":
            $ seduction -= 40
        "On se bat à mort pour savoir qui mange tout.":
            $ seduction += 30
    $ renpy.restart_interaction()

    
    pnj_skaven "Comment tu comptes protéger notre futur nid-maison contre les intrus ?"
    menu:
        "Je ferme la porte à clé et je demande qui est là.":
            $ seduction -= 30
        "Je piège le sol avec des lames empoisonnées." if isinstance(pc, Voleur):
            $ seduction += 50
        "Je reste devant la porte et j'écrase tout ce qui bouge." if isinstance(pc, Barbare):
            $ seduction += 40
        "Je dresse un mur de flammes vertes magiques !" if isinstance(pc, Mage):
            $ seduction += 50
    $ renpy.restart_interaction()

    
    pnj_skaven "Si je te vole ton goûter pendant que tu dors, tu fais quoi ?"
    menu:
        "Je te mords l'oreille pour te donner une leçon.":
            $ seduction += 20
        "Je boude dans mon coin en pleurant.":
            $ seduction -= 40
        "Je te félicite pour ton agilité-vol !":
            $ seduction += 40
    $ renpy.restart_interaction()

    
    pnj_skaven "C'est quoi ton rêve le plus fou-dingue ?"
    menu:
        "Invoquer une pluie de rats géants sur la ville !" if isinstance(pc, Mage):
            $ seduction += 50
        "Faire la paix entre les humains et les rats.":
            $ seduction -= 60
        "Devenir le cerveau de l'ombre et trahir tout le monde !" if isinstance(pc, Voleur):
            $ seduction += 50
        "Trouver une montagne de fromage infinie.":
            $ seduction += 30
    $ renpy.restart_interaction()

    
    pnj_skaven "Si tu devais m'offrir un bijou, ce serait quoi ?"
    menu:
        "Un diamant pur de la mine des nains.":
            $ seduction -= 30
        "Un collier fait de dents de répurgateurs.":
            $ seduction += 40
        "Un vieux bouton que j'ai trouvé par terre.":
            $ seduction += 20
        "Une bague en malepierre qui donne des mutations.":
            $ seduction += 30
    $ renpy.restart_interaction()

    
    pnj_skaven "Si on se fait coincer par des gardes, tu fais quoi ?"
    menu:
        "Je m'enfuis et je reviens te chercher plus tard.":
            $ seduction += 30
        "Je me rends pour te sauver la vie.":
            $ seduction -= 70
        "Je te pousse dans les bras des gardes pour m'enfuir.":
            $ seduction += 60
        "Je saute pour te sauver, au péril de ma vie !":
            $ seduction -= 50
    $ renpy.restart_interaction()

    
    pnj_skaven "Mon bras-pattes est cassé après ce combat... Tu fais quoi ?"
    menu:
        "Je t'emmène chez le guérisseur du village.":
            $ seduction -= 60
        "Je te greffe un membre de rat pris sur un cadavre." if isinstance(pc, Voleur):
            $ seduction += 50
        "Je te soigne avec une potion de régénération." if isinstance(pc, Mage):
            $ seduction -= 40
        "Je t'attache un bout de bois avec une corde et on continue." if isinstance(pc, Barbare):
            $ seduction += 30
    $ renpy.restart_interaction()

    
    pnj_skaven "Dis-moi, quelle est la chose la plus magnifique que tu aies jamais vue ?"
    menu:
        "Un coffre rempli de pièces d'or volées.":
            $ seduction += 20
        "Un coucher de soleil sur les montagnes.":
            $ seduction -= 60
        "Une pile de cadavres de nains parfaitement alignés.":
            $ seduction += 40
        "Le visage d'un ami fidèle.":
            $ seduction -= 40
    $ renpy.restart_interaction()

    
    pnj_skaven "Si on devait composer une chanson pour le Grand Rat Cornu, quel instrument utiliser ?"
    menu:
        "Le son de mes poings frappant un bouclier." if isinstance(pc, Barbare):
            $ seduction += 30
        "Une harpe, c'est doux et mélodieux.":
            $ seduction -= 50
        "Ma flûte à rats, pour les hypnotiser." if isinstance(pc, Mage):
            $ seduction += 40
        "Le bruit de mes lames que j'aiguise." if isinstance(pc, Voleur):
            $ seduction += 40
    $ renpy.restart_interaction()

    
    pnj_skaven "Dernière réflexion : qu'est-ce qui est le plus important au monde ?"
    menu:
        "Le pouvoir de posséder ce qu'on veut.":
            $ seduction += 30
        "L'honneur et la loyauté.":
            $ seduction -= 80
        "La capacité à trahir au bon moment.":
            $ seduction += 60
        "La connaissance absolue.":
            $ seduction -= 30
    $ renpy.restart_interaction()

    hide screen barre_seduction
    jump verdict_skaven


label verdict_skaven:
    hide screen barre_seduction

# --- ÉVÉNEMENT SPÉCIAL ----
    if seduction <= -50:
        pnj_skaven "NON ! Trop de... bonté... de lumière... de politesse..."
        pnj_skaven "MON CŒUR DE RAT NE SUPPORTE PAS TANT DE PURETÉ !!!"
        
        play sound "audio/sfx_explosion.mp3"
        with vpunch
        
        "Le Skaven explose littéralement dans une gerbe de sang, de tripes et... de paillettes magiques."
        "La porte derrière les restes fumants de la créature s'ouvre toute seule, comme terrifiée par votre gentillesse."
        
        $ passage_salle05_debloque = True    
        jump labyrinthe_salle08

# --- FIN CACHÉE -------
    if seduction >= 150:
        $ skaven_yandere_fin = True
        pnj_skaven "Skritch... Je ne peux plus te laisser partir..."
        pnj_skaven "Tu es à moi. Pour toujours. Je te suivrai... partout. Dans l'ombre. Derrière toi."
        "Le Skaven rejoint votre groupe. Son regard est fixe, dilaté, et ne cligne plus des yeux."
        $ passage_salle05_debloque = True
        jump labyrinthe_salle08

    # --- RÉUSSITE NORMALE ---
    elif seduction >= 50:
        pnj_skaven "Skritch ! Tu me plais, humaine-chose. Passe vite avant que je ne reprenne mes esprits !"
        $ passage_salle05_debloque = True
        jump labyrinthe_salle08

    # --- ÉCHEC NORMAL ---
    else:
        pnj_skaven "Toi être ennuyeuse-chose. Moi avoir faim maintenant !"
        jump fin

label labyrinthe_salle08:
    scene salle_labyrinthe_porte_gauche

menu:
    "Plus vous avancez, plus vous sentez une forte pression sur vos épaules."

    "Partir vers la porte de gauche":
        jump labyrinthe_salle07
    



label labyrinthe_salle07:
    scene salle_labyrinthe_trois_porte

menu:
    "Ici, le silence est un mensonge. La porte colossale dégage une aura électrique, imprégnée d'une odeur entêtante de malt et de... poils ? Une chose est certaine : le maître des lieux vous a déjà senti arriver."

    "Vous décidez de prendre la porte au centre":
        jump enigme_minecraft

    "Vous décidez de prendre la porte a gauche":
        jump labyrinthe_salle06

    "Vous décidez de revenir sur vos pas":
        jump labyrinthe_salle08

    "Salle Secrète(WIP)":
        jump salle_secrete

label enigme_minecraft:
    scene mc_base 
    
    "Une faille dimensionnelle s'ouvre. Trois leviers de pierre se dressent devant vous."

label choix_levier:
    menu:
        "Actionner le levier de gauche":
            scene mc_gauche 
            "Un clic sourd retentit... La porte du boss tremble et s'ouvre enfin !"
            jump salle_du_boss

        "Actionner le levier du centre":
            scene mc_centre 
            "Le levier résiste. Une décharge électrique parcourt vos doigts. Ce n'est pas celui-là."
            jump choix_levier 

        "Actionner le levier de droite":
            scene mc_droite 
            "Une lumière s'allume, mais la porte est toujours fermée. Vous devriez essayer un autre levier."
            jump choix_levier 

label labyrinthe_salle06:
    scene salle_labyrinthe_porte_droite
    "Il n'y a rien de spécial ici"
menu:
    "(WIP)"

    "Vous décidez de prendre la porte a droite":
        jump labyrinthe_salle07

#--------------------------Combat Boss--------------------------

label salle_du_boss:
    scene end_cave
    play music "audio/boss_theme.mp3"
    
    show Oiia at center with moveinbottom
    "Le terrible Oiiacat se dresse contre vous !"
    "Il tourne sur lui-même avec une vitesse défiant les lois de la physique. Ses miaulements forment une mélodie hypnotique..."

    $ oiiacat_combat = UiiaCat()
    $ combat_log = []
    $ log_msg("Le combat final contre l'Oiiacat commence !")

    show screen Combat_Oiia

label boucle_combat_oiiacat:
    if pc.vie <= 0:
        jump defaite_oiiacat
    if oiiacat_combat.vie <= 0:
        jump victoire_oiiacat

    menu:
        "Utiliser l'[item2.nom]" if any(isinstance(i, HerbeCap) for i in pc.consommables):
            $ log_msg("Vous jetez une poignée d'herbe à chat au sol !", "#2ecc71")
            "L'Oiiacat s'arrête net de tourner. Il se roule dedans avec frénésie, oubliant totalement de se défendre !"
            
            $ degats_herbe = oiiacat_combat.vie / 2
            $ oiiacat_combat.perte_pv(degats_herbe)
            
            $ log_msg(f"L'Oiiacat est déconcentré ! Il perd {int(degats_herbe)} PV.")
            
            python:
                for i in pc.consommables:
                    if isinstance(i, HerbeCap):
                        pc.consommables.remove(i)
                        break
            with hpunch

        "Attaquer avec [pc.arme[0].nom]" if not isinstance(pc, Mage) and pc.arme:
            $ degats = pc.attaquer(oiiacat_combat)
            $ log_msg(f"Vous frappez le chat en plein tournoiement ! Il subit {degats} dégâts.")
            with hpunch
            

        "Tenter de l'attraper par la queue" if not isinstance(pc, Mage) and not pc.arme:
            $ degats = pc.attaquer(oiiacat_combat)
            $ log_msg(f"Vous essayez de stopper sa rotation ! L'Oiiacat subit {degats} dégâts.")
            with vpunch

        "Lancer une explosion de mana" if isinstance(pc, Mage) and pc.mana >= 20:
            $ degats = pc.attaquer(oiiacat_combat)
            $ log_msg(f"Votre magie perturbe son rythme ! L'Oiiacat subit {degats} dégâts.")

        "Canaliser un faible sort" if isinstance(pc, Mage) and pc.mana <= 20 and pc.mana >= 10:
            $degats = pc.sort1(crapomagicien)
            $ log_msg(f"Vous lancez un faible missile magique pour ralentir sa rotation, il ne vous reste plus de mana ! L'Oiiacat subit {degats} dégâts.")
            with flash_blanc

        "Vous n'avez plus de mana !!" if isinstance(pc, Mage) and pc.mana <=10:
            $ log_msg(f"Vous tentez de canaliser le peu de mana qu'il vous reste mais vous êtes à sec ! Prenez une potion !")



    $ degats_subis = oiiacat_combat.attaquer(pc)
    $ log_msg(f"L'Oiiacat miaule de façon stridente ! Vous subissez {degats_subis} dégâts.")
    
    if degats_subis > 0:
        with vpunch
        with flash_rouge 

    jump boucle_combat_oiiacat

label defaite_oiiacat:
    hide screen Combat_Oiia
    stop music fadeout 1.0
    with vpunch
    "Le tournoiement incessant du chat finit par vous faire perdre l'équilibre. Vous sombrez dans l'oubli, bercé par son miaulement éternel..."
    jump fin

label victoire_oiiacat:
    hide screen Combat_Oiia
    stop music fadeout 1.0
    with vpunch
    "Dans une ultime rotation, l'Oiiacat explose en mille paillettes de pixel !"
    "Le labyrinthe redevient silencieux. Vous avez vaincu la menace tournante."
    if skaven_yandere_fin:
        jump fin_nice_boat
    else:
        jump fin

#--------------------------Fin Combat Boss--------------------------

label salle_secrete:
    
menu:
    "(WIP)":
        jump fin



label fin_nice_boat:
    scene fin_nice_boat
    play music "sea_wave_sfx.mp3"
    with fade

    "Le calme de l'océan est apaisant."
    "Le Skaven est assis sur le pont, bercé par les vagues, loin du labyrinthe et de ses horreurs."
 
    
    "Dans ses bras-pattes, iel serre tendrement votre tête décapitée."
    "Votre regard est fixe, figé pour l'éternité dans une expression de surprise glacée."
    
    pnj_skaven "Tu souris enfin. (Des larmes de bonheur perlant dans ses yeux de rat)"
    
    
    pnj_skaven "Skritch... Enfin. Tu ne me trahiras plus jamais. Tu ne regarderas plus personne."
    pnj_skaven "Tu es à moi. Pour l'éternité. Nous sommes... enfin... UN."
    
    "Le Skaven frotte doucement son museau contre votre joue froide."
    
    achieve yandere_end

    "{b}FIN SECRÈTE : Nice Boat.{/b}"
    jump fin

label finalcool:
    "Après plusieurs verres de trop, vous vacillez… puis vous vous affaissez lamentablement dans votre chope, sous les rires étouffés de la taverne."
    jump fin
label finbarbare:
    "Vous essayez d'attrapper le col de barbare qui est torse nu, vous échouez"
    "Le barbare soulève une table et vous fracasse le crâne, vous mourez sur le coup"
    jump fin
label fintaverne:
    "Vous avez décidé de rester vivre dans la taverne, et depuis ce jour, entre les chopes débordantes, les chants graves des mineurs et la chaleur du grand foyer de pierre, vous vous sentez plus nain que jamais, trouvant enfin un foyer aussi solide qu'un roc et aussi chaleureux qu’un banquet nain."
    jump fin
label fin:
    "Merci d'avoir joué."
return

label truck_kun:

    play sound "Truck_klaxon.mp3" volume 0.5

    scene truck_kun with flash

    truck "POUÊÊÊÊÊÊÊÊÊÊÊT !!!"

    pause 0.2
    stop sound
    play sound "Truck_accident.mp3" volume 0.5
    with hpunch

    pause 0.2
    scene black with dissolve
    "..."
    stop sound
    "Tout devient noir..."
    "Puis..."
    
    play music "Office_ambiance.mp3" volume 1
    
    "Bip... Bip... Bip..."
    
    scene bg_open_space with fade
    
    show coll at right
    coll "Hé, [pc_name] ! Ohé, tu m'écoutes ?"
    
    p "Hein ? Quoi ? Par les barbes d'Ulfar, où est ma hache ?! Et c'est quoi cette armure en tissu gris qui me gratte les jambes ?"
    
    coll "Ta hache ? Tu veux dire ton coupe-papier ? Arrête de déconner, on a la réunion sur les KPI du troisième trimestre dans cinq minutes."
    
    p "KPI ? Est-ce une nouvelle forme de magie noire ? Et d'où vient cette lumière blafarde qui tombe du plafond ?"
    
    coll "C'est des néons, mec. T'as encore trop forcé sur l'hydromel artisanal hier soir, c'est ça ?"
    
    show boss at left with moveinleft
    boss "[pc_name] ! Pourquoi vous n'êtes pas devant votre tableur Excel ? Le donjon des dossiers clients ne va pas se vider tout seul !"
    
    p "Un... un tableur ? Est-ce un artefact ancien ?"
    
    boss "C'est un artefact qui s'appelle 'Productivité'. Et si vous ne remplissez pas les cellules avant midi, votre prime de fin d'année va s'évaporer comme un sort de niveau 1."
    
    menu:
        "Tenter de lancer un sort de boule de feu sur la photocopieuse":
            p "KRAK-KA-BOUM ! Brûle, machine infernale !"
            "Vous jetez votre café brûlant sur la machine. Elle fait quelques étincelles avant d'afficher 'Erreur 404'."
            boss "C'est ça... On va déduire les réparations de votre salaire. Allez en salle de pause."
            jump fin_bureau
            
        "Chercher une taverne dans les couloirs":
            p "Tavernier ! Apporte-moi une pinte de la meilleure bière, et vite !"
            coll "La machine à café est en panne, il reste juste du thé à la camomille dégueulasse."
            p "Quelle malédiction est-ce donc ?"
            jump fin_bureau
            
        "Accepter son destin de salarié":
            p "Très bien... Montrez-moi ce 'Excel'. S'il faut combattre des chiffres pour l'honneur de ma lignée, soit !"
            boss "C'est l'esprit. Et mettez une cravate, on dirait que vous sortez d'une grotte."
            jump fin_bureau

label fin_bureau:
    scene bg_office_night with fade
    "Huit heures plus tard..."
    
    "Vous n'avez terrassé aucun dragon, mais vous avez survécu à trois réunions Zoom."
    "Le seul trésor que vous avez trouvé est un ticket restaurant de 9 euros."
    
    p "C'est donc ça... l'enfer des humains ? Pas de gloire, pas de chants... juste le bruit de la clim."
    stop music
    
    achieve isekai_office
    
    "Peut-être qu'en traversant la route demain matin, vous aurez plus de chance ?"
    
    jump fin
# Vous pouvez placer le script de votre jeu dans ce fichier.
init python:
    blorp=0
    


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image chat = im.Scale("chat01.png", 900, 1000)
image poster_chat = im.Scale("wanted-poster", 900, 1000)
image bg taverne = im.Scale("taverne01.jpg", 1920, 1080)
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
image dungeon_entrance = im.Scale("dungeon_entrance.jpeg", 1920, 1080)
image labyrinthe_porte = im.Scale("porte_labyrinthe.png", 1920, 1080)
image salle_labyrinthe_porte_droite = im.Scale("Salle_Labyrinthe_Porte_Droite.png", 1920, 1080)
image salle_labyrinthe_porte_gauche = im.Scale("Salle_Labyrinthe_Porte_Gauche.png", 1920, 1080)
image salle_labyrinthe_trois_porte = im.Scale("Salle_Labyrinthe_Trois_Porte.jpg", 1920, 1080)
image salle_labyrinthe_porte_droite_centre = im.Scale("Salle_Labyrinthe_Porte_Droite_Centre.png", 1920, 1080)
image salle_labyrinthe_porte_gauche_centre = im.Scale("Salle_Labyrinthe_Porte_Gauche_Centre.png", 1920, 1080)
image salle_labyrinthe_porte_centre = im.Scale("salle_labyrinthe_porte_centre.png", 1920, 1080)
image salle_labyrinthe_coffre = im.Scale("salle_labyrinthe_coffre.png", 1920, 1080)
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
                                    
                                if hasattr(tooltip_objet, 'soin') and tooltip_objet.soin > 0:
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
                                        action NullAction() 
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


#

default p = None
default drunk = 0
default pts_voleur = 0
default pts_barbare = 0
default pts_mage = 0
default pc = None
default fouille_salle4 = False

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

# Déclarez des transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

#Déclarez des sfx
define sfx_get_class = "game/audio/get_class.mp3"
define sfx_item_get = "game/audio/item_get.mp3"

# Le jeu commence ici
label start:
    show screen bouton_stats
    show screen bouton_inventaire

    


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
    
    "Qui es tu jeune nain?"
    jump q1

menu q1:
    "Un voyou embête une fille dans une rue animée de la place marchande!Que faîtes-vous?"
    "a)Je sauve la demoiselle en détresse !!!.":
        $ pts_barbare += 1
        jump q2
    "b)Je lui baisse discrètement son slip.":
        $ pts_voleur += 1
        jump q2
    "c)J'appelle la milice.":
        $ pts_mage += 1
        jump q2
    "d)Je me fais dessus.":
        jump q2

menu q2:
    "Un pouilleu commence une conversation avec vous.Vous ne comprenez absolument rien à ce qu'il dit.Que lui dîtes-vous?"
    "a)Hum...Vous pouvez répéter?":
        $ pts_mage += 1
        jump q3
    "b)Bien...Hum,il faut que j'y aille.":
        $ pts_voleur += 1
        jump q3
    "c)Ques tu mveu, tu veu une pièce c'est ça ?.":  
        $ pts_barbare += 1
        jump q3

menu q3:
    "Un collègue de picole vous ramène quelque chose que vous aviez oublié. Comment le remerciez-vous?"
    "a)Merci, je te revaudrais ça.":  
        $ pts_voleur += 1
        jump q4
    "c)Merci,mon brave!":
        $ pts_mage += 1
        jump q4
    "d)Une grosse baffe dans la tronche, c'est MES affaires.":
        $ pts_barbare += 1
        jump q4
        
menu q4:
    "Une main sort des toilettes!Que faîtes-vous?"
    "a)Je m'enfuis en hurlant.":
        $ pts_voleur += 1
        jump q5
    "b)Je referme le couvercle.":  
        $ pts_mage += 1
        jump q5
    "c)Je la serre.":
        $pts_barbare += 1
        jump q5

menu q5:
    "Arrivez-vous souvent en retard à l'église?"
    "a)Oui.":
        $ pts_barbare += 1
        jump q6
    "b)Non.":
        $ pts_mage += 1
        jump q6
    "c)C'est la faute des goblins":
        $ pts_voleur += 1
        jump q6
        
menu q6:
    "Osez-vous entrer dans une maison hantée?"
    "a)Oui avec quelqu'un.":
        $ pts_mage +=1
        jump q7
    "b)Euh...non...":
        $ pts_voleur += 1
        jump q7
    "c)Elle est même pas en forme de T ta maison!":
        $ pts_barbare += 1
        jump q7

menu q7:
    "Racontez-nous une blague"
    "a)Alors c'est un nain un elfe et un orc qui rentrent dans un bar...":
        $ pts_voleur += 1
        jump q8
    "b)Tire sur mon doigt !":
        $ pts_barbare += 1
        jump q8
    "c)T'imagine si Kornifex avait écrit le 3ème grimmoire de lucidité avec de l'encre de pieuvre calcinée!":
        $ pts_mage += 1
        jump q8

menu q8:
    "Attrapez n'importe quel doigt de la main gauche avec la main droite.Quel doigt avez-vous choisi?"
    "a)Le pouce.":
        $ pts_barbare += 1
        jump q9
    "b)L'index.":
        $ pts_barbare += 1
        $ pts_voleur += 1
        $ pts_mage += 1
        jump q9
    "c)Le majeur.":
        $ pts_voleur += 1
        jump q9
    "d)L'annulaire.":
        $ pts_mage += 1
        jump q9
    "e)L'auriculaire.":
        $ pts_mage += 1
        jump q9

menu q9:
    "Avez-vous déjà construit un piège?"
    "a)....":
        $ pts_voleur += 1
        jump q10
    "b)Non, j'ai pas besoin de ce genre de subterfuge de bas étage.":
        $pts_mage += 1
        jump q10
    "c)J'en ai déjà casser un, ça compte ?":
        $ pts_barbare += 1
        jump q10

menu q10:
    "A quelle vitesse répondez-vous à un pigeon voyageur?"
    "a)J'y réponds immédiatement, il en va de mon honneur!":
        $ pts_mage += 1
        jump q11
    "b)Jsuis pas un naintellectuel moi, je sais pas écrire.":
        $ pts_barbare += 1
        jump q11
    "c)Trop fatigant.":
        $ pts_voleur += 1
        jump q11

menu q11:
    "Vous êtes à la plage et le temps est superbe.Comme vous sentez-vous?"
    "a)Super bien! J'ai creusé un super trou!":
        $ pts_barbare += 1
        jump q12
    "b)Super! Je viens de terminer une reproduction en sable de la tour d'ivoire d'Udum-Arak!":
        $ pts_mage += 1
        jump q12
    "c)J'ai envie de rentrer...":
        $pts_voleur += 1
        jump q12
        
menu q12:
    "C'est les vacances d'été! Où aimeriez-vous aller?"
    "a)Jsuis déjà en vacance toute l'année à la taverne":
        $ pts_barbare += 1
        jump q13
    "b)En thalasso.":
        $ pts_voleur += 1
        jump q13
    "c)Je pars pas en vacances, je n'ai pas le temps":
        $ pts_mage += 1
        jump q13
    "d)Je dois bien avouer que j'ai toujours rêver de visiter le colysée d'idylthir.":
        $ pts_voleur += 1
        $ pts_barbare += 1
        jump q13

menu q13:
    "Quelqu'un dit que vous êtes bizarre mais marrant.Vous vous sentez comment?"
    "a)Super!":
        $ pts_voleur += 1
        jump q14
    "b)Triste.":
        $ pts_mage += 1
        jump q14
    "c)Nain.":
        $ pts_barbare += 1
        $ pts_mage += 1
        $ pts_voleur += 1
        jump q14
    "d)Ca me laisse naindifférent.":
        $ pts_mage += 1
        $ pts_voleur += 1
        jump q14
        
menu q14:
    "La route se divise:elle part à droite et à gauche.On vous dit qu'il y a un trésor sur celle de droite.De quel côté allez-vous?"
    "a)A droite! Les lingots m'appellent!":
        $ pts_barbare += 1
        jump q15
    "b)Un piège!A gauche.":
        $ pts_mage += 1
        jump q15
    "c)Peu importe.":
        $ pts_voleur += 1
        jump q15
    "d)Tout droit.":
        $ pts_barbare +=1
        jump q15

menu q15:
    "Voici un seau.Si vous mettez de l'eau dedans,vous le remplissez..."
    "a)A ras.":
        $ pts_barbare += 1
        jump q16
    "b)A demi.":
        $ pts_mage += 1
        jump q16
    "c)Un peu.":
        $ pts_voleur += 1
        jump q16
    "d)Jeter le seau.":
        $ pts_barbare += 1
        jump q16

menu q16:
    "Vous aimez bien une personne...Mais aucun moyen de s'en rapprocher que faîtes-vous?"
    "a)Je lui déclare ma flamme.":
        $ pts_voleur += 1
        jump q17
    "b)Je lui créer un poème.":
        $ pts_barbare += 1
        jump q17
    "c)Je l'admire de loin.":
        $ pts_mage += 1
        jump q17

menu q17:
    "Vous entendez un cri venant de derrière la porte!Comment réagissez-vous?"
    "a)Je l'ouvre d'un coup.":
        $  pts_voleur += 1
        jump q18
    "b)Je crie aussi.":
        $ pts_barbare += 1
        jump q18
    "c)Je toque à la porte.":
        $ pts_mage += 1
        jump q18

menu q18:
    "Vous trouvez la besace d'un aventurier dans un donjon que faites vous ?"
    "a)Je l'apporte à la guilde des aventuriers.":
        $ pts_mage += 1
        jump q19
    "b)CEST A MOI!":
        $ pts_voleur += 1
        jump q19  
    "c)Pas lus?":
        $ pts_barbare += 1
        jump q19

menu q19:
    "Les extraterrestres nous envahissent!Que faîtes-vous?"
    "a)Je lutte!":
        $ pts_barbare += 1
        jump q20
    "b)Je fuis.":
        $ pts_mage += 1
        jump q21
    "c)Rien.":
        $ pts_voleur += 1
        jump q21

menu q20:
    "Vous avez bien combattu...mais les extraterrestres gagnent...Il y en a un qui vous dit <<Tu nous as impressionés,c'était un plaisir à voir.Joins-toi à nous,et ensemble,dirigeons le Monde.>>Que faîtes-vous?"
    "a)J'accepte.":
        $ pts_voleur += 1
        jump q21  
    "b)Je refuse.":
        $ pts_barbare += 1
        $ pts_mage += 1
        jump q21

menu q21:
    "On vous donne le choix entre deux cadeaux.Le quel allez-vous choisir?"
    "a)Le gros.":
        $ pts_barbare += 1
        jump q22  
    "b)Le petit.":
        $ pts_mage += 1
        jump q22
    "c)Les deux.":
        $ pts_voleur += 1
        jump q22

menu q22:
    "On vous enferme par erreur dans une pièce noire comme de l'encre!Que faîtes-vous?"
    "a)Je pleure.":
        $ pts_mage += 1
        jump q25  
    "b)J'enfonce la porte.":
        $ pts_barbare += 1
        jump q25
    "c)Je fais une sieste.":
        $ pts_voleur += 1
        jump q25

menu q25:
    "Vous gagnez le jackpot au WiNainMax!Que faîtes-vous de l'argent?"
    "a)J'économise.":
        $ pts_voleur += 1
        jump q26
    "b)Je le donne.":
        $pts_mage += 1
        jump q26
    "c)Tournée générale de 3 semaines au bar!":
        $ pts_barbare += 1
        jump q26

menu q26:
    "L'empereur des Nains Grobiff XIVII est face à vous, comment lui parlez-vous?"
    "a)Calmement. ":
        $ pts_voleur += 1
    "b)ON S'EN FICHE!!!":
        $ pts_barbare += 1
    "c)Nerveusement.":
        $ pts_mage += 1


stop music fadeout 2.5
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
        play music sfx_get_class
        "Vous êtes barbare"
    if classe_joueur == "Voleur":
        "Votre sens de l'observation aiguisé fait de vous un expert de la discrétion, capable de déjouer tous les pièges pour s'emparer des trésors les mieux gardés."
        play sfx sfx_get_class
        "Vous êtes voleur"
    if classe_joueur == "Mage":
        "Votre curiosité insatiable pour les mystères du monde fait de vous un érudit des arcanes, maniant les éléments pour transformer le destin à votre guise."
        play sfx sfx_get_class
        "Vous êtes mage"


scene bg taverne

"Tout commença un soir ordinaire, dans une taverne qui ne payait pas de mine, quand un drôle de nain, bien connu du village grimpa sur une table pour attirer l'attention."

show chat at right

g "Mon trésor ? Je vous le laisse si vous voulez. Trouvez-le ! Je l'ai laissé quelque part dans ce monde !"

hide chat

"Dit-il en s'évanouissant"

play music "elevator-music.mp3"

$ pc_name = renpy.input("Brave aventurier fils de glorp héritier au throne de glorptopia, Quel est ton valeureux nom ?", length=20).strip() or "Aventurier"

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
    "Boire"
    $ drunk += 1
    "[drunk]"
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
    v "mmh, je vois ..."
    p "tu vois quoi ?"
    v "Ton avenir est curieux, ta destiné sera rempli d'embuche, mais si tu restes courageux, tu atteindra ton but."
    p "ok."
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
    "Après de longues heures à vous amuser à la taverne vous décidez d'enfin sortir de la taverne et vous approchez de la porte."
    
menu choix_sortie_taverne:
    "Changer d'avis et retourner dans la taverne":
        jump fin_taverne
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
        jump devant_donjon
    "Vous criez très fort pour débuter votre aventure":
        jump crier_fort   
    "Vous vous retrouvez devant une plaine magnifique. Vous éprouvez une légère nostalgie en la regardant."

label crier_fort:
    "Les passants vous regardent, ils vous prennent juste pour un guignol"
    jump devant_donjon

label devant_donjon:    
    "glorp"
    
label entree_donjon:
    scene dungeon_entrance

menu:
    "Vous entrez dans le donjon":
        jump debut_donjon

    "Vous admirez l'entrée":
        jump admire_entree
    "Vous voila devant le donjon, que faites-vous ?"

label debut_donjon:
    scene labyrinthe_porte
    "Un crapaud, je les hais de tout mon être"
    $ crapomagicien = CrapeauMagicien()
    while pc.vie > 0 or crapomagicien.vie > 0:
        menu:
            #Combat contre le crapaud magicien
            # "Vous utilisez votre {pc.arme} pour attaquer le crapaud magicien!" if isinstance(pc, Barbare, Voleur):

            "Vous canalisez votre magie pour attaquer le crapaud magicien!" if isinstance(pc, Mage):
                $ pc.attaquer(crapomagicien)
                "Le crapaud magicien subit  points de dommage. Il lui reste  points de vie. [crapomagicien.vie]"
                "Le crapaud magicien attaque en retour!"
                $ crapomagicien.attaquer(pc)
                "Vous subissez  points de dommage. Il vous reste  points de vie."

    jump entre_labyrinthe

label admire_entree:
    "C'est un beau donjon"
    jump entree_donjon

label entre_labyrinthe:
    scene labyrinthe_porte

    menu:
        "Une grande porte ce dresse contre vous que faite vous"

        "Vous évaluez la solidité de la porte avec vos pectoraux saillants." if isinstance(pc,Barbare):
            $ d20 = Dice.lancer(1,20)[0]
            jump voie_du_barbare

        "Vous sortiz vos outils en espérant que vos mains tremblent dans le bon sens." if isinstance(pc,Voleur):
            $ d20 = Dice.lancer(1,20)[0]
            jump voie_du_voleur

        "Vous utilisez votre élocution pour convaincre la porte que sa fonction de fermeture est obsolète." if isinstance(pc,Mage):
            $ d20 = Dice.lancer(1,20)[0]
            jump voie_du_mage

        "Vous décider de rebrousser chemin parce que a quoi bon de toute façon cette aventure devais bien ce terminer quelque part":
            jump autre_chemin
       
label voie_du_barbare:      
        if d20 == 20:
            "Vous fixer la porte avec un mépris souverain et la traversez sans l'ouvrir : le concept de 'porte' est purement subjectif pour vous"
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
            "Vous trouvé un étrange poster qui vous semble famillier"
            hide poster_chat
            jump salle02_enigme_barbare
   
    "La fresque reprèsente quatre guerriers. Le dernier n'a pas d'arme, son poing est levé vers le ciel."

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
        s "Dix balles ? Seulement ? Vous savez les temps son dure en ce moment j'ai une femme, deux enfant..."
        p "Douze balles. C'est mon dernier mot, je n'ai plus que des jetons de lave-linge après ça, j'ai même plus de quoi payez la bonne Josianne"
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
        s "'AÏE ! MAIS ÇA VA PAS ? C'EST HARCÈLEMENT, ÇA !' Elle se verrouille deux fois plus fort. 'Réfléchis un peu au lieu de tripoter mon mécanisme !'"
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

            play sfx "sfx_item_get"
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
    "(WIP)"

    "Vous décidez de prendre la porte a droite":
        jump labyrinthe_salle01

    "Vous décidez de prendre la porte au centre":
        jump labyrinthe_salle04

label labyrinthe_salle03:
    scene salle_labyrinthe_port_gauche_centre
menu:
    "(WIP)"

    "Vous décidez de prendre la porte au centre":
        jump labyrinthe_salle05

    "Vous décidez de prendre la porte de gauche":
        jump labyrinthe_salle01

label labyrinthe_salle05:
    scene salle_labyrinthe_porte_centre
menu:
    "(WIP)"

    "Vous décidez de prendre la porte au centre":
        jump labyrinthe_salle08

label labyrinthe_salle08:
    scene salle_labyrinthe_porte_gauche
menu:
    "(WIP)"

    "Vous décidez de prendre la porte de gauche":
        jump labyrinthe_salle07

label labyrinthe_salle07:
    scene salle_labyrinthe_trois_porte

menu:
    "Ici, le silence est un mensonge. La porte colossale dégage une aura électrique, imprégnée d'une odeur entêtante de malt et de... poils ? Une chose est certaine : le maître des lieux vous a déjà senti arriver."

    "Vous décidez de prendre la porte au centre":
        jump salle_du_boss

    "Vous décidez de prendre la porte a gauche":
        jump labyrinthe_salle06

    "Vous décidez de prendre la porte a droite":
        jump labyrinthe_salle08
    "Salle Secrète(WIP)":
        jump salle_secrete

label labyrinthe_salle06:
    scene salle_labyrinthe_porte_droite
    "test"
menu:
    "(WIP)"

    "Vous décidez de prendre la porte a droite":
        jump labyrinthe_salle07

label salle_du_boss:

menu:
    "Boss a vaincre(WIP)":
        jump fin

label salle_secrete:
    
menu:
    "(WIP)":
        jump fin
    "test":
        jump fin



   

label finalcool:
    "Après plusieurs verres de trop, vous vacillez… puis vous vous affaissez lamentablement dans votre chope, sous les rires étouffés de la taverne."
    jump fin
label finbarbare:
    "Vous essayez d'attrapper le col de barbare qui est torse nu, vous échouez"
    "Le barbare soulève une table et vous fracasse le crâne, vous mourrez sur le coup"
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
    
    "FÉLICITATIONS : Vous avez débloqué la fin secrète 'Burn-out Isekai'."
    
    "Peut-être qu'en traversant la route demain matin, vous aurez plus de chance ?"
    
    jump fin
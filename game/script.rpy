# Vous pouvez placer le script de votre jeu dans ce fichier.
init python:
    blorp = 0


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image chat = im.Scale("chat01.png", 900, 1000)
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

default p = None
default drunk = 0
default pts_voleur = 0
default pts_barbare = 0
default pts_mage = 0

# Déclarez les personnages utilisés dans le jeu.
define g = Character('Gromli Fût-Perdu', color="#ff3434")
define h = Character('Héro', color="#c8ffc8")
define t = Character('Tavernier', color="#c8ffc8")
define v = Character('Voyante louche', color="#c8ffc8")
define b = Character('Barbare costaud', color="#c8ffc8")
define p = Character("[pc_name]", color="#ffabf1")
define boss = Character('M. Grondin (Manager)', color="#ff0000")
define coll = Character('Kévin du Marketing', color="#00fbff")
define truck = Character('Truck-kun', color="#f098ca")

# Déclarez des transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# Le jeu commence ici
label start:
    


# Switch pour les différents états du scénario
$ boire_alcool = False
$ tavernier_taverne = True
$ voyante_taverne = True
$ barbare_taverne = True
$ glorp = True
# Fin Switch

# Création du personnage
label intro:
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

# Fin Création

# Instanciation Joueur

python:
    pc = Voleur()

# Fin Instanciation Joueur


scene bg taverne

"Tout commença un soir ordinaire, dans une taverne qui ne payait pas de mine, quand un drôle de nain, bien connu du village grimpa sur une table pour attirer l'attention."

show chat at right

g "Mon trésor ? Je vous le laisse si vous voulez. Trouvez-le ! Je l'ai laissé quelque part dans ce monde !"

hide chat

"Dit-il en s'évanouissant"

play music "elevator-music.mp3"

$ pc_name = renpy.input("Brave aventurier fils de glorp héritier au throne de glorptopia, Quel est ton valeureux nom ?", length=20).strip() or "Aventurier"

stop music
#     pc.nom = pc_name

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
        $ tavernier = False
        jump choix_tavernier
    "Parler à une voyante" if voyante_taverne:
        $ voyante = False
        jump choix_voyante
    "Parler à un barbare" if barbare_taverne:
        $ barbare = False
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
    "Vous vous escusez et continuez votre chemin":
        jump choix_taverne
    "Vous vous faites une poignée de main": #todo rajouter un if barbare
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
        if dice_isekai >= 50:
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
    

    

# menu entree_donjon:
# scene dungeon_entrance.jpeg
#     "Vous entrez dans le donjon"
#         jump debut_donjon
#     "Vous admirez l'entrée"
#         jump admire_entree
#     "Vous voila devant le donjon, que faites-vous ?"

# label debut_donjon:
#     scene je_sais_pas
#         "Un crapaud, je les hais de tout mon être"
#             jump combat_crapaud_magicien

# label admire_entree:
#     "C'est un beau donjon"
#     jump entree_donjon











label finalcool:
    "Après plusieurs verres de trop, vous vacillez… puis vous vous affaissez lamentablement dans votre chope, sous les rires étouffés de la taverne."
    jump fin
label finbarbare:
    "Vous essayez d'attrapper le col de barbare qui est torse nue, vous échouez"
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
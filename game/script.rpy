# Vous pouvez placer le script de votre jeu dans ce fichier.
# init python:
#     from python.dice import *
#     from python.objets import *
#     from python.entites import *


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image chat = im.Scale("chat01.png", 900, 1000)
image bg taverne = im.Scale("taverne01.jpg", 1920, 1080)

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

# Le jeu commence ici
label start:
    


# Switch pour les différents états du scénario
$ boire_alcool = False
$ tavernier_taverne = True
$ voyante_taverne = True
$ barbare_taverne = True
$ picross_taverne = True
$ picrossfini_taverne = False
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

scene bg taverne

"Tout commença un soir ordinaire, dans une taverne qui ne payait pas de mine, quand un drôle de nain, bien connu du village grimpa sur une table pour attirer l'attention."

show chat at right

g "Mon trésor ? Je vous le laisse si vous voulez. Trouvez-le ! Je l'ai laissé quelque part dans ce monde !"

hide chat

"Dit-il en s'évanouissant"

play music "elevator-music.mp3"

$ pc_name = renpy.input("Brave aventurier fils de glorp héritier au throne de glorptopia, Quel est ton valeureux nom ?", length=20).strip() or "Aventurier"

stop music

# python:
#     pc = Joueur(race="Nain", classe="Barbare")
#     pc.nom = pc_name

$ p = Character(pc_name)

p "J'ai envis d'un bon bolet de cidre"

"Es-tu mineur ou majeur ?"

menu:

    "Je suis mineur":
        jump mineur

    "je suis majeur":
        jump majeur

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
        jump sortietaverne

label taverne:
    t "Laisse tomber, le donjon est un endroit trop dangeureux pour un nain comme toi"
    p "J'ai pas peur ! Dis moi comment aller à la taverne"
    jump sortietaverne

label sortietaverne:
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
    "Jouer aux runes avec le nain du coin" if picross_taverne:
        $ picross_taverne = False
        $ picrossfini_taverne = True
        p "Hé l'ami, on se fait une partie de runes ?"
        "Le nain sort une grille de 10x10. C'est un puzzle 'Tête de Monstre'."
        call screen picross(EXAMPLE_5X5_PICROSS_PUZZLE)
        p "Haha ! J'ai résolu ton énigme !"
        "Le nain grogne et te donne quelques pièces d'or." #TODO:Rajouter les pièces d'or
        jump choix_taverne
    "Jouer aux runes avec le nain du coin" if picrossfini_taverne:
        "casse toi !"
        jump choix_taverne
    "Sortir de la taverne":
        jump fin
    "Que voulez-vous faire maintenant ?"


menu choix_tavernier:
    "Sers moi ton meilleur alcool pour me donner du courage !":
        jump alcool_tavernier
    "T'as des informations sur le donjon ?":
        jump information_tavernier
    t "Encore toi ? Tu veux quoi ?"
label alcool_tavernier:
    t "Tiens, une bière"
    jump choix_taverne
label information_tavernier:
    t "J'en sais rien, bon courage"
    jump choix_taverne

menu choix_voyante:
    "J'SUIS PAS PETIT !":
        jump enerve_voyante
    "D'accord !":
        jump avenir_voyante
    "Je ne crois pas en la voyance":
        jump choix_taverne
    v "Bonjour, petit nain, veux-tu lire ton avenir ?"
label enerve_voyante:
    v "Non bien sur, tu es un nain de taille de nain"
    p "QUOI ? T'ES MECHANTE, JE ME CASSE"
    jump choix_taverne
label avenir_voyante:
    v "Bien, quelle est ta date de naissance"
    p "J'sais pas"
    v "mmh, je vois ..."
    p "tu vois quoi ?"
    v "Ton avenir est curieux, ta destiné sera rempli d'embuche, mais si tu restes courageux, tu atteindra ton but."
    p "ok"
    jump choix_taverne
    
# menu choix_barbare:
#     "test"


label finalcool:
    "Après plusieurs verres de trop, vous vacillez… puis vous vous affaissez lamentablement dans votre chope, sous les rires étouffés de la taverne."
    jump fin
label fin2:
    "test"
label fin:
    "Merci d'avoir joué."
return
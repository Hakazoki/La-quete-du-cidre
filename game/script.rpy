# Vous pouvez placer le script de votre jeu dans ce fichier.
init python:
    from python.entites import *
    from python.dice import *


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image chat = im.Scale("chat01.png", 900, 1000)
image bg taverne = im.Scale("taverne01.jpg", 1920, 1080)

default p = None
default drunk = 0

# Déclarez les personnages utilisés dans le jeu.
define g = Character('Gromli Fût-Perdu', color="#ff3434")
define h = Character('Héro', color="#c8ffc8")
define t = Character('Tavernier', color="#c8ffc8")
define v = Character('Voyante louche', color="#c8ffc8")
define b = Character('Barbare costaud', color="#c8ffc8")
define p = Character("[pc_name]", color="#ffabf1")

# Le jeu commence ici
label start:

$ boire_alcool = False

scene bg taverne

"Tout commença un soir ordinaire, dans une taverne qui ne payait pas de mine, quand un drôle de nain, bien connu du village grimpa sur une table pour attirer l'attention."

show chat at right

g "Mon trésor ? Je vous le laisse si vous voulez. Trouvez-le ! Je l'ai laissé quelque part dans ce monde !"

hide chat

"Dit-il en s'évanouissant"

$ pc_name = renpy.input("Brave aventurier fils de glorp héritier au throne de glorptopia, Quel est ton valeureux nom ?", length=20).strip() or "Aventurier"

# python:
#     pc = Joueur(race="Nain", classe="Barbare")
#     pc.nom = pc_name

$ p = Character(pc_name)

p "J'ai envis d'un bon bolet de cidre"

"Est-tu mineur ou majeur ?"

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
    # "Merci, pour la bière, je veux me rendre dans le donjon !" if boire_alcool:
    #         jump fin
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
        jump fin
    
    "Pour l'argent":
        jump fin

    "Pour l'alcool" if boire_alcool:
        jump fin2


label finalcool:
    "Après plusieurs verres de trop, vous vacillez… puis vous vous affaissez lamentablement dans votre chope, sous les rires étouffés de la taverne."
    jump fin
label fin2:
    "test"
label fin:
    "Merci d'avoir joué."
return
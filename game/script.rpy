# Vous pouvez placer le script de votre jeu dans ce fichier.


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image chat01 = im.Scale("chat01.jpg", 900, 1000)
image taverne01 = im.Scale("taverne01.jpg", 1920, 1080)

# Déclarez les personnages utilisés dans le jeu.
define n = Character('Narrateur', color="#c8ffc8")
define g = Character('Gromli Fût-Perdu', color="#c8ffc8")
define h = Character('Héro', color="#c8ffc8")
define t = Character('Tavernier', color="#c8ffc8")
define v = Character('Voyante louche', color="#c8ffc8")
define b = Character('Barbare costaud', color="#c8ffc8")


# Le jeu commence ici
label start:

scene taverne01

n "Tout commença un soir ordinaire, dans une taverne qui ne payait pas de mine, quand un drôle de nain, bien connu du village grimpa sur une table pour attirer l'attention."

show chat01 at right

g "Mon trésor ? Je vous le laisse si vous voulez. Trouvez-le ! Je l'ai laissé quelque part dans ce monde !"

return
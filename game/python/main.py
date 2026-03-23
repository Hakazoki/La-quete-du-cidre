from entites import Joueur,Dummy
from Arme import EpeeEnBois

m= Dummy()
j = Joueur()
arme = EpeeEnBois()

j.equiper(arme)
print(j.arme)
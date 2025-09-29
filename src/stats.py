import numpy as np
from data import quantité, prix_unitaire

print(prix_unitaire)
# Utilisation de numpy pour effectuer des calculs : somme 

valeur_totale = np.sum(quantité *prix_unitaire)
print(" La valeur de stock : ", valeur_totale,"DH")


# ● Valeur totale du stock (somme(prix * quantité)).
# ● Prix moyen des produits.
# ● Prix minimum et maximum.
# ● Produit le plus cher et le moins cher.


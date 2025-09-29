import numpy as np
from data import stock
print(stock)


quantites = np.array([item[1] for item in stock])
print(quantites)
prix = np.array([item[2] for item in stock])

# Calculs
valeurs_par_article = quantites * prix
valeur_totale = np.sum(valeurs_par_article)
print("Valeur du stock par article :", valeurs_par_article)
print(f" La valeur totale est : {valeur_totale} DH " )

#  Prix moyen des produits
x=len(stock)
print(x)
prix_moyen = sum(item [2] for item in stock) / x
print( "La valeur moyenne des prix : ", prix_moyen)

# Prix minimum :

min_prix= min(prix)
print("Le minimum de prix : ", min_prix)

# Prix maximum : 
max_prix= max(prix)
print("Le maximum de prix : ", max_prix)

# Produit le plus cher :
produit_le_plus_cher= max(stock, key = lambda produit : produit[2])
print("Le produit le plus cher est :", produit_le_plus_cher)
# Produit le moins cher :

produit_le_moins_cher= min(stock, key = lambda produit : produit[2])
print("Le produit le moins cher est :", produit_le_moins_cher)







import numpy as np
from data import stock

# print(stock)

quantites = np.array([item[1] for item in stock])
print(quantites)
prix = np.array([item[2] for item in stock])

# valeur_tot = np.sum(quantites*prix)
# print(f"La valeur totale est : {valeur_tot} DH")


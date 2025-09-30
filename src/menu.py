import numpy as np
from data import stock
from stock import ajouter,modifier,supprimer,afficher
from visualize import barres,pie
from stats import afficher_stats

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Ajouter un produit")
        print("2. Supprimer un produit")
        print("3. Modifier la quantité d’un produit")
        print("4. Afficher le stock")
        print("5. Afficher les statistiques")
        print("6. Afficher un graphique de barres")
        print("7. Afficher un graphique de pie")
        print("8. Quitter")
 
        choix = input("Choisissez une option (1-8) : ")

        if choix == '1':
            ajouter(stock)
        elif choix == '2':
            supprimer(stock)
        elif choix == '3':
            modifier(stock)
        elif choix == '4':
            afficher(stock)
        elif choix == '5':
            afficher_stats()
        elif choix == '6':
            barres(stock) 
        elif choix == '7':
            pie(stock)   
        elif choix == '8':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 8.")

if __name__ == "__main__":
    menu()
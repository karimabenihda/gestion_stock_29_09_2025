import numpy as np
import  matplotlib as plt
from data import stock

def trouver_produit(nom):
    """Retourne l'index du produit dans stock, ou -1 s'il n'existe pas"""
    for i, produit in enumerate(stock):
        if produit[0].lower() == nom.lower():
            return i
    return -1

def ajouter_produit():
    nom = input("Nom du produit à ajouter : ")
    if trouver_produit(nom) != -1:
        print("Produit déjà existant.")
        return
    try:
        quantite = int(input("Quantité : "))
        prix = float(input("Prix unitaire : "))
        stock.append([nom, quantite, prix])
        print(f"Produit '{nom}' ajouté.")
    except ValueError:
        print("Quantité ou prix invalide.")

def supprimer_produit():
    nom = input("Nom du produit à supprimer : ")
    idx = trouver_produit(nom)
    if idx == -1:
        print("Produit non trouvé.")
    else:
        del stock[idx]
        print(f"Produit '{nom}' supprimé.")

def modifier_quantite():
    nom = input("Nom du produit à modifier : ")
    idx = trouver_produit(nom)
    if idx == -1:
        print("Produit non trouvé.")
        return
    try:
        nouvelle_quantite = int(input("Nouvelle quantité : "))
        stock[idx][1] = nouvelle_quantite
        print(f"Quantité du produit '{nom}' modifiée.")
    except ValueError:
        print("Quantité invalide.")

def afficher_stock():
    if not stock:
        print("Stock vide.")
    else:
        print("\nStock actuel :")
        print(f"{'Produit':<15} {'Quantité':<10} {'Prix Unitaire':<15}")
        print("-" * 40)
        for produit in stock:
            print(f"{produit[0]:<15} {produit[1]:<10} {produit[2]:<15}")

def afficher_stats():
    if not stock:
        print("Stock vide.")
        return
    total_articles = sum(p[1] for p in stock)
    valeur_totale = sum(p[1] * p[2] for p in stock)
    produit_max = max(stock, key=lambda p: p[1])
    produit_min = min(stock, key=lambda p: p[1])
    
    print(f"Nombre total d'articles en stock : {total_articles}")
    print(f"Valeur totale du stock : {valeur_totale} unités monétaires")
    print(f"Produit le plus en stock : {produit_max[0]} ({produit_max[1]} unités)")
    print(f"Produit le moins en stock : {produit_min[0]} ({produit_min[1]} unités)")

def afficher_graphique():
    if not stock:
        print("Stock vide.")
        return
    print("Type de graphique :")
    print("1. Bar chart")
    print("2. Pie chart")
    choix = input("Votre choix : ")
    produits = [p[0] for p in stock]
    quantites = [p[1] for p in stock]

    if choix == '1':
        plt.bar(produits, quantites)
        plt.title("Quantité des produits en stock")
        plt.ylabel("Quantité")
        plt.xlabel("Produit")
    elif choix == '2':
        plt.pie(quantites, labels=produits, autopct='%1.1f%%')
        plt.title("Répartition du stock (quantités)")
    else:
        print("Choix invalide.")
        return
    plt.show()

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Ajouter un produit")
        print("2. Supprimer un produit")
        print("3. Modifier la quantité d’un produit")
        print("4. Afficher le stock")
        print("5. Afficher les statistiques")
        print("6. Afficher un graphique")
        print("7. Quitter")

        choix = input("Choisissez une option (1-7) : ")

        if choix == '1':
            ajouter_produit()
        elif choix == '2':
            supprimer_produit()
        elif choix == '3':
            modifier_quantite()
        elif choix == '4':
            afficher_stock()
        elif choix == '5':
            afficher_stats()
        elif choix == '6':
            afficher_graphique()
        elif choix == '7':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 7.")

if __name__ == "__main__":
    menu()
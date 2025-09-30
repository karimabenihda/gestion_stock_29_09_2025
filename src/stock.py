#ajouter un produits
def ajouter(l):
    added_product=input('entre product name: ')
    added_qte=int(input('entre product quantity: '))
    added_price=float(input('entre product price: '))
    l.append([added_product,added_qte,added_price])
    print(l)

#supprimer un produits
def supprimer(l):
    to_delete=input("entrer le nom produit que voulez supprimer: ")
    for i,element in enumerate (l):
        if element[0]==to_delete:
            index=i
            print(index)

    if l.pop(index):
        print(f"{element[0]} deleted seccessfully")
    print(l)

  
#modify un produits
def modifier(l):
    to_delete=input("entrer le nom produit que voulez modifier: ")
    to_edit_name=input("entrer le nom produit: ")
    to_edit_qte=int(input("entrer la quantite produit: "))
    to_edit_price=float(input("entrer le prix produit: "))

    for i,element in enumerate (l):
        if element[0]==to_delete:
            index=i
            print(index)

    l[index]=[to_edit_name,to_edit_qte,to_edit_price]
    print(l)

#afficher un produits
def afficher(l):
    print(l)
from data import arr1,arr2,arr3
import numpy as np

added_product=input('entre product name: ')
added_qte=int(input('entre product quantity: '))
added_price=input('entre product price: ')

arr1=np.append(arr1,added_product)
arr2=np.append(arr2,added_qte)
arr3=np.append(arr3,added_price)


#supprimer un produits
to_delete=input("entrer le nom produit que voulez supprimer: ")
index = np.where(arr1 == to_delete)[0][0]

np.delete(arr1,index)
print(arr1)


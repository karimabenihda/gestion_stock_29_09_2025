import matplotlib.pyplot as plt

def barres(stock):
    qte=[item[1] for item in stock]
    names=[item[0] for item in stock]
    plt.bar(names,qte,color='r')

    plt.title("Graphique en barres : quantité par produit")
    plt.xlabel("Produits")
    plt.ylabel("Quantité")
    plt.show()

def pie(stock):
    qte=[item[1] for item in stock]
    names=[item[0] for item in stock]
    prices=[item[2] for item in stock]
    one_list=list(zip(qte,prices))
    for i in one_list:
        total=[i[0]*i[1] for i in one_list]

    plt.pie(
        total,
        labels=names,
        autopct='%1.1f%%', 
        startangle=140
    )

    plt.title(" répartition de la valeur totale du stock par produit. ")
    plt.show()
 

 

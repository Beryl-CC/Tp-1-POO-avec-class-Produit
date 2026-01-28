from models.categorie import Categorie
from models.produit import Produit

try:
    cat = Categorie("Ordinateur", "Claviers, souris, etc.")


    p1 = Produit("KB-001", "Clavier", 100, 15)
    p2 = Produit("MS-002", "Souris", 100, 0)  # Rupture de stock
    p3 = Produit("SC-003", "Écran", 100, 5)
    p1.afficher()
    cat.ajouter_produit(p1)
    cat.ajouter_produit(p2)
    cat.ajouter_produit(p3)
    print(cat.nb_produits)
    print(cat.valeur_totale)
    for produit in cat.produits_disponibles:
        produit.afficher()
    print(cat.nb_produits)           # 3
    print(cat.valeur_totale)         # 2000
    print(len(cat.produits_disponibles))  # 2 (souris en rupture)
except ValueError as e:
    print(e)



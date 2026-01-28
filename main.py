from models.categorie import *
from models.produit import *
from datetime import date

""""
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
"""

clavier = ProduitElectronique("KB-001", "Clavier RGB", 79.99, 15, 24, 0.5)
fromage = ProduitAlimentaire("ALI-001", "Comté", 12.99, 50, "2025-06-15")

print(clavier.calculer_frais_livraison)  # 11.0 (10 + 0.5*2)
print(fromage.calculer_frais_livraison())  # 15.0

clavier.afficher_details()  # Garantie: 24 mois, Poids: 0.5kg
fromage.afficher_details()  # Péremption: 2025-06-15

print(fromage.est_perime())  # False (ou True selon la date)
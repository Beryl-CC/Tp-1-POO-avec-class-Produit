from models.categorie import *
from models.produit import *
from models.inventaire import *
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
"""
clavier = ProduitElectronique("KB-001", "Clavier RGB", 79.99, 15, 24, 0.5)
fromage = ProduitAlimentaire("ALI-001", "Comté", 12.99, 50, "2025-06-15")

print(clavier.calculer_frais_livraison)  # 11.0 (10 + 0.5*2)
print(fromage.calculer_frais_livraison())  # 15.0

clavier.afficher_details()  # Garantie: 24 mois, Poids: 0.5kg
fromage.afficher_details()  # Péremption: 2025-06-15

print(fromage.est_perime())  # False (ou True selon la date)
"""
"""
inv = Inventaire()

inv.ajouter(ProduitElectronique("KB-001", "Clavier", 79.99, 15, 24, 0.5))
inv.ajouter(ProduitElectronique("SC-001", "Écran", 299.99, 5, 36, 5.0))
inv.ajouter(ProduitAlimentaire("ALI-001", "Comté", 12.99, 50, "2025-06-15"))
inv.ajouter(ProduitAlimentaire("ALI-002", "Lait", 1.50, 100, "2024-01-01"))  # Périmé

print(inv.total_frais_livraison())  # 61.0 (11 + 20 + 15 + 15)
print(len(inv.lister_par_type(ProduitElectronique)))  # 2
print(len(inv.produits_perimes()))  # 2
"""


p1 = ProduitElectronique("KB-001", "Clavier", 79.99, 8)
p2 = ProduitAlimentaire("RA-909", "Tomates", 6.99, 10)
p3 = ProductFactory.create(ProduitElectronique, {"ref": "MS-001", "nom": "Souris", "prix": 49.99, "stock": 5})
p4 = ProductFactory.create(ProduitAlimentaire, {"ref": "FR-001", "nom": "Comté", "prix": 21.99, "stock": 10})
print(p1)                   # Clavier (KB-001) - 79.99€ HT
print(repr(p2))             # Produit('KB-001', 'Clavier', 79.99)

print(p1 < p2)              # False
print(p1 == p2)             # False

print(Produit.valider_prix(-30))    # False
print(Produit.valider_prix(49.99))  # True             
print(repr(p3))
print(repr(p4))
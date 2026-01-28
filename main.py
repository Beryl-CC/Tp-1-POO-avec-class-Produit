from models.categorie import Categorie
from models.produit import Produit


cat = Categorie("Périphériques", "Claviers, souris, etc.")

p1 = Produit("KB-001", "Clavier", 79.99, 15)
p2 = Produit("MS-002", "Souris", 49.99, 0)  # Rupture de stock
p3 = Produit("SC-003", "Écran", 199.99, 5)

cat.ajouter_produit(p1)
cat.ajouter_produit(p2)
cat.ajouter_produit(p3)

print(cat.nb_produits)           # 3
print(cat.valeur_totale)         # 2199.80
print(len(cat.produits_disponibles))  # 2 (souris en rupture)


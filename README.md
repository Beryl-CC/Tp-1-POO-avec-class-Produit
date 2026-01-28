# TP4 : Categorie avec gestion des produits

## Objectif

Améliorer la classe Categorie avec encapsulation et propriétés calculées.

## Propriétés à implémenter

- `nom` : chaîne de 2+ caractères
- `nb_produits` : propriété calculée (len des produits)
- `valeur_totale` : somme des valeurs de stock de tous les produits
- `produits_disponibles` : liste des produits avec stock > 0

## Exemple d'utilisation

```python
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
```

## Indices

- `produits_disponibles` : `[p for p in self._produits if p.stock > 0]`
- `valeur_totale` : `sum(p.valeur_stock for p in self._produits)`
# TP1 : Classe Produit pour PyInventory

## Objectif

Créer la classe Produit de base pour le projet PyInventory.

## Attributs d'instance

- `reference` : code unique du produit (ex: "KB-001")
- `nom` : nom du produit
- `prix_ht` : prix hors taxes
- `stock` : quantité en stock

## Attributs de classe

- `tva` : taux de TVA (20% par défaut)
- `nb_produits` : compteur de produits créés

## Méthodes

- `prix_ttc()` : retourne le prix TTC
- `afficher()` : affiche les informations du produit
- `est_disponible()` : retourne True si stock > 0
- `ajouter_stock(quantite)` : ajoute au stock
- `retirer_stock(quantite)` : retire du stock (si possible)
- `valeur_stock()` : retourne prix_ht * stock

## Exemple d'utilisation

```python
p1 = Produit("KB-001", "Clavier mécanique RGB", 79.99, 15)
p2 = Produit("MS-002", "Souris gaming 16000 DPI", 49.99, 25)

p1.afficher()
# Réf: KB-001 | Clavier mécanique RGB | 79.99€ HT (95.99€ TTC) | Stock: 15

print(f"Valeur du stock: {p1.valeur_stock()}€")  # 1199.85€
p1.retirer_stock(3)   # Stock retiré: 3. Nouveau stock: 12
p1.retirer_stock(20)  # Stock insuffisant

print(f"Total produits: {Produit.nb_produits}")  # 2
```

## Indices

- Prix TTC : `self.prix_ht * (1 + Produit.tva / 100)`
- Utilisez les f-strings pour l'affichage
- Vérifiez que la quantité à retirer ne dépasse pas le stock


# TP2 : Classe Categorie pour PyInventory

## Objectif

Créer la classe Categorie pour organiser les produits.

## Attributs

- `nom` : nom de la catégorie (ex: "Périphériques")
- `description` : description de la catégorie
- `produits` : liste des produits de cette catégorie (liste vide par défaut)

## Méthodes

- `ajouter_produit(produit)` : ajoute un produit à la catégorie
- `retirer_produit(reference)` : retire un produit par sa référence
- `lister_produits()` : affiche tous les produits de la catégorie
- `nb_produits()` : retourne le nombre de produits
- `valeur_totale()` : retourne la somme des valeurs de stock

## Exemple d'utilisation

```python
peripheriques = Categorie("Périphériques", "Claviers, souris, etc.")

p1 = Produit("KB-001", "Clavier RGB", 79.99, 15)
p2 = Produit("MS-002", "Souris gaming", 49.99, 25)

peripheriques.ajouter_produit(p1)
peripheriques.ajouter_produit(p2)

peripheriques.lister_produits()
# Catégorie: Périphériques (2 produits)
# - KB-001: Clavier RGB - 79.99€ - Stock: 15
# - MS-002: Souris gaming - 49.99€ - Stock: 25

print(f"Valeur totale: {peripheriques.valeur_totale()}€")  # 2449.60€
```

## Indices

- Stockez les produits dans une liste : `self.produits = []`
- Pour retirer : parcourez la liste et comparez les références
- Valeur totale : somme de `produit.valeur_stock()` pour chaque produit

# TP3 : Produit encapsulé pour PyInventory

## Objectif

Appliquer l'encapsulation complète à la classe Produit de PyInventory.

## Instructions

- Reprenez la classe Produit du Jour 1
- Transformez tous les attributs en attributs protégés (`_`)
- Créez des propriétés avec validation pour :
  - `reference` : chaîne de 3+ caractères, convertie en majuscules
  - `nom` : chaîne de 2+ caractères
  - `prix_ht` : nombre positif, arrondi à 2 décimales
  - `stock` : entier positif ou nul
- Ajoutez les propriétés calculées : `prix_ttc`, `valeur_stock`
- Ajoutez les méthodes : `ajouter_stock()`, `retirer_stock()`

## Tests à exécuter

```python
p = Produit("kb-001", "Clavier RGB", 79.99, 15)
print(p.reference)    # KB-001 (converti en majuscules)
print(p.prix_ttc)     # 95.99

p.prix_ht = 69.99     # OK
p.ajouter_stock(10)   # Stock: 25
p.retirer_stock(5)    # Stock: 20

# Ces lignes doivent lever des exceptions
# p.prix_ht = -10     # ValueError
# p.stock = 5.5       # TypeError
# p.reference = "ab"  # ValueError (trop court)
```

## Indices

- Dans le constructeur, utilisez `self.attribut = valeur` (pas `self._attribut`) pour déclencher les setters
- Utilisez `isinstance(valeur, (int, float))` pour vérifier les nombres
- N'oubliez pas `round(valeur, 2)` pour les prix


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


# TP5 : Hiérarchie de produits pour PyInventory

## Objectif

Créer une hiérarchie de classes pour les produits de PyInventory.

## Instructions

- Transformez Produit en classe abstraite avec :
  - Méthode abstraite `calculer_frais_livraison()`
  - Méthode abstraite `afficher_details()`
- Créez `ProduitElectronique(Produit)` avec :
  - Attribut supplémentaire : `garantie_mois`
  - Frais de livraison : 10€ + 2€ par kg
  - Attribut : `poids_kg`
- Créez `ProduitAlimentaire(Produit)` avec :
  - Attribut supplémentaire : `date_peremption`
  - Frais de livraison : 15€ (réfrigéré)
  - Méthode : `est_perime()` qui retourne True si daté

## Tests à exécuter

```python
clavier = ProduitElectronique("KB-001", "Clavier RGB", 79.99, 15, 24, 0.5)
fromage = ProduitAlimentaire("ALI-001", "Comté", 12.99, 50, "2025-06-15")

print(clavier.calculer_frais_livraison())  # 11.0 (10 + 0.5*2)
print(fromage.calculer_frais_livraison())  # 15.0

clavier.afficher_details()  # Garantie: 24 mois, Poids: 0.5kg
fromage.afficher_details()  # Péremption: 2025-06-15

print(fromage.est_perime())  # False (ou True selon la date)
```

## Indices

- Utilisez `from datetime import date` pour les dates
- `date.fromisoformat("2025-06-15")` pour convertir une chaîne
- `est_perime(): return self._date_peremption < date.today()`
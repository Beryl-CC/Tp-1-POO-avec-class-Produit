from models.produit import *

class Inventaire:
    def __init__(self):
        self.liste_produits = []
    
    def ajouter(self, produit):
        if not isinstance(produit, Produit):
            return False
        self.liste_produits.append(produit)
    
    def total_frais_livraison(self):
        prix_total = 0
        for produit in self.liste_produits:
            prix_total += produit.calculer_frais_livraison
        return prix_total

    def lister_par_type(self, type_classe):
        return [p for p in self.liste_produits if isinstance(p, type_classe)]
    
    def produits_perimes(self):
        return [p for p in self.liste_produits if isinstance(p, ProduitAlimentaire) and p.est_perime()]



        





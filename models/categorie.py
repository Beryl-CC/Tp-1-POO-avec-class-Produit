class Categorie:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)
    
    def retirer_produit(self, reference):
        for i in self.produits:
            if i.reference == reference:
                self.produits.remove(i)
    
    def lister_produits(self):
        for i in self.produits:
            i.afficher()
    
    def nb_produits(self):
        return len(self.produits)
    
    def valeur_totale(self):
        somme = 0
        for produit in self.produits:
            somme += produit.valeur_stock()
        return somme
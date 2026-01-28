class Produit:
    """
    Classe représentant un produit avec référence, nom, prix et stock.
    Attributs de classe :
        tva : taux de TVA pour tous les produits
        nb_produits : nombre total de produits (exemple ici fixé à 2)
    """

    tva = 20
    nb_produits = 0
    
    def __init__(self, reference, nom, prix_ht, stock):
        """
        Initialise un produit avec sa référence, son nom, son prix HT et son stock.
        """
        self.reference = reference
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock

        Produit.nb_produits += 1

    def prix_ttc(self):
        """
        Retourne le prix TTC du produit.
        """
        return self.prix_ht * (1 + Produit.tva / 100)
    
    def afficher(self):
        """
        Affiche les infos du produit : référence, nom, prix HT et TTC, stock.
        """
        print(f"Réf: {self.reference} | {self.nom} | {self.prix_ht}€ HT ({self.prix_ttc():.2f}€ TTC) | Stock: {self.stock}")
    
    def est_disponible(self):
        """
        Retourne True si le produit est en stock, False sinon.
        """
        if self.stock >= 1:
            return True
        else:
            return False
               
    def ajouter_stock(self, quantite):
        """
        Ajoute une quantité donnée au stock du produit.
        """
        self.stock += quantite
    
    def retirer_stock(self, quantite):
        """
        Retire une quantité donnée du stock si possible, sinon affiche un message d'erreur.
        """
        if self.stock >= quantite:
            self.stock -= quantite
        else:
            print("Il n'y a plus ce produit en stock ou nous n'en avons pas assez pour votre requête")
    
    def valeur_stock(self):
        """
        Retourne la valeur totale du stock du produit (prix HT * quantité).
        """
        return self.prix_ht * self.stock
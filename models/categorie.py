class Categorie:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
        self.produits = []

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, chaine):
        if not isinstance(chaine, str) or len(chaine) < 3:
            raise ValueError("La chaine doit être d'au moins 3 lettres")
        self._nom = chaine
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, chaine):
        if not isinstance(chaine, str):
            raise ValueError("Cela doit être une chaine de caractère")
        self._description = chaine
    
    @property
    def produits(self):
        return self._produits
    
    @produits.setter
    def produits(self, liste):
        self._produits = liste
    
    @property
    def nb_produits(self):
        return len(self._produits)
    
    @property
    def valeur_totale(self):
        somme = 0
        for produit in self.produits:
            somme += produit.valeur_stock
        return somme
    
    @property
    def produits_disponibles(self):
        liste = []
        for produit in self.produits:
            if produit.est_disponible():
                liste.append(produit)
        return liste

    def ajouter_produit(self, produit):
        self.produits.append(produit)
    
    def retirer_produit(self, reference):
        for i in self.produits:
            if i.reference == reference:
                self.produits.remove(i)
    
    def lister_produits(self):
        for i in self.produits:
            i.afficher()
    
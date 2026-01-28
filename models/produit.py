from abc import ABC, abstractmethod
from datetime import date

class Produit(ABC):
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

    @property
    def valeur_stock(self):
        """
        Retourne la valeur totale du stock du produit (prix HT * quantité).
        """
        return round(self._prix_ht * self.stock, 2)
    
    @property
    def reference(self):
        return self._reference

    @property
    def nom(self):
        return self._nom
    
    @property
    def prix_ht(self):
        return self._prix_ht
    
    @property
    def stock(self):
        return self._stock

    @reference.setter
    def reference(self, chaine):
        if len(chaine) < 4:
            raise ValueError("Chaine de caractère pas assez grande")
        self._reference = chaine.upper()
    
    @nom.setter
    def nom(self, chaine):
        if len(chaine) < 3:
            raise ValueError("Chaine de caractère pas assez grande")
        self._nom = chaine
    
    @prix_ht.setter
    def prix_ht(self, nombre):
        if not isinstance(nombre, (int, float)) or nombre <= 0:
            raise ValueError("Il faut un nombre positif")
        round(nombre, 2)
        self._prix_ht = round(nombre, 2)
    
    @stock.setter
    def stock(self, nombre):
        if not isinstance(nombre, int) or nombre < 0:
            raise ValueError("Stock invalide")
        self._stock = nombre
    
    @property
    def prix_ttc(self):
        """
        Retourne le prix TTC du produit.
        """
        return round(self._prix_ht * (1 + Produit.tva / 100), 2)
    
    @abstractmethod
    def calculer_frais_livraison(self):
        pass

    @abstractmethod
    def afficher_details(self):
        pass
    
    def afficher(self):
        """
        Affiche les infos du produit : référence, nom, prix HT et TTC, stock.
        """
        print(f"Réf: {self._reference} | {self._nom} | {self._prix_ht:.2f}€ HT ({self.prix_ttc:.2f}€ TTC) | Stock: {self._stock}")
    
    def est_disponible(self):
        """
        Retourne True si le produit est en stock, False sinon.
        """
        if self._stock >= 1:
            return True
        else:
            return False
               
    def ajouter_stock(self, quantite):
        """
        Ajoute une quantité donnée au stock du produit.
        """
        self._stock += quantite
    
    def retirer_stock(self, quantite):
        """
        Retire une quantité donnée du stock si possible, sinon affiche un message d'erreur.
        """
        if self._stock >= quantite:
            self._stock -= quantite
        else:
            print("Il n'y a plus ce produit en stock ou nous n'en avons pas assez pour votre requête")
    

class ProduitElectronique(Produit):
    def __init__(self, reference, nom, prix_ht, stock, garantie_mois, poids_kg):
        super().__init__(reference, nom, prix_ht, stock)
        self.garantie_mois = garantie_mois
        self.poids_kg = poids_kg

    @property
    def garantie_mois(self):
        return self._garantie_mois

    @garantie_mois.setter
    def garantie_mois(self, value):
        if not isinstance(value, (int, float)):
            ValueError("Il faut mettre des chiffres entier")
        self._garantie_mois = value
    
    @property
    def poids_kg(self):
        return self._poids_kg

    @poids_kg.setter
    def poids_kg(self, value):
        if not isinstance(value, int):
            ValueError("Il faut mettre des chiffres")
        self._poids_kg = value

    @property
    def calculer_frais_livraison(self):
        prix_frais_livraison = 10 + self.poids_kg * 2
        return prix_frais_livraison
    
    def afficher_details(self):
        print(f"Garanti: {self._garantie_mois} mois, Poids: {self._poids_kg}kg")
    
class ProduitAlimentaire(Produit):

    frais_livraison = 15

    def __init__(self, reference, nom, prix_ht, stock, date_peremption):
        super().__init__(reference, nom, prix_ht, stock)
        self.date_peremption = date_peremption
    
    @property
    def date_peremption(self):
        return self._date_peremption
    
    @date_peremption.setter
    def date_peremption(self, value):
        if not isinstance(value, str):
            ValueError("Il faut mettre la date sous forme de chaine de caractère valide")
        self._date_peremption = value
    
    def calculer_frais_livraison(self):
        return ProduitAlimentaire.frais_livraison
    
    def afficher_details(self):
        print(f"Péremption: {self._date_peremption}")
    
    def est_perime(self):
        date_en_obj = date.fromisoformat(self._date_peremption)
        date_peremption = date_en_obj < date.today()
        if date_peremption == True:
            print("La date de péremption n'a pas encore été atteinte")
        else:
            print("La date de péremption a déjà été atteinte")
        


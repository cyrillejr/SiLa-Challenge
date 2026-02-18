import json
import datetime

class SoldeInsuffisantError(Exception): pass
class PlafondDepasserError(Exception): pass

class Compte:
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial
        self.historique = []

    def ajouter_historique(self, type_op, montant):
        entree = {
            "temps": str(datetime.datetime.now()),
            "type": type_op,
            "montant": montant,
            "solde_apres": self.solde
        }
        self.historique.append(entree)

    def deposer(self, montant):
        self.solde += montant
        self.ajouter_historique("Depot", montant)

    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantError(f"Echec: Solde insuffisant ({self.solde})")
        self.solde -= montant
        self.ajouter_historique("Retrait", montant)

def sauvegarder_donnees(comptes, fichier="jour1/banque.json"):
    data = {c.titulaire: {"solde": c.solde, "historique": c.historique} for c in comptes}
    with open(fichier, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    mon_compte = Compte("Cyrille", 1000)
    mon_compte.deposer(500)
    sauvegarder_donnees([mon_compte])
    print("✅ Données sauvegardées dans jour1/banque.json")

"""Define the main controller."""
# A faire : importation des models.
from views.view import View

class Controller:
    """Main controller."""

    def __init__(self):
        pass
   
    def generate_pairs(self):
        # générer paires de players (Systeme Suisse)
        return True

    def get_players(self):
        pass


    def start_tournament(self):
        view = View()
        # Créer les players
        view.create_player()
    # générer paires
    # générer matchs
    # générer Tournament

    
    def run(self):
        pass
    
t = start_tournament()

"""1. Créer un nouveau tournoi.
    2. Ajouter huit joueurs.
    3. L'ordinateur génère des paires de joueurs pour le premier tour.
    4. Lorsque le tour est terminé, entrez les résultats.
    5. Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.
"""


"""
A faire
génération des paires (système suisse)
    1. Au début du premier tour, triez tous les joueurs en fonction de leur 
    classement.
    2. Divisez les joueurs en deux moitiés, une supérieure et une inférieure. 
    Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur 
    joueur de la moitié inférieure, et ainsi de suite. 
    Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé 
    avec le joueur 5, le joueur 2 est jumelé avec le joueur 6, etc.
    3. Au prochain tour, triez tous les joueurs en fonction de leur nombre 
    total de points. Si plusieurs joueurs ont le même nombre de points, 
    triez-les en fonction de leur rang.
"""
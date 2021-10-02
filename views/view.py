
class View:
    def prompt_for_tounament(self):
        """Prompt to create new tournament """
        name = input("Donnez un nom au tournoi : ")
        location = input("Saisissez le lieu où se déroule le tournoi : ")
        date = input("Indiquez sur combien de jours se déroulera le tournoi ? : ")
        description = input("Ajouter une description du Tournois : ")
        if description == "":
             description = None

        """Choose for 1 item of bullet, blitz or coup rapide"""
        time = ""
        while not time.isdigit():
            time = input("Time : Choisissez entre \n 1 : Bullet, \n 2 : Blitz, \n 3 : Coup Rapide \n")
            if not time.isdigit():
                print("Saisissez uniquement 1, 2 ou 3")

        num_of_rounds = 4

        return [name, location, date, time, num_of_rounds, time, description]

    def create_player(self):
        """create new players"""
        players_list = []
        add_player = "O"
        while add_player == "O":
            first_name = input("Tapez le prénom du joueur : ").capitalize()
            last_name = input("Tapez le nom de famille du joueur : ").capitalize()
            date_of_birth = input("Saisissez la date de naissance au format 01/12/2000 :\n")
            gender = input("Le joueur est 1 : Homme 2 : femme :")
            rank = input("Saisissez le rang du joueur si connu :")
            add_player = input("Créer un nouveau joueur ? O : Oui  N : Non\n").capitalize()
            players_list.append([first_name, last_name, date_of_birth, gender, rank])
            print(players_list)
    # Sortie : 
    # ['T01', 'Moorea', '3', '1', 4, [['Simon', 'Dupont'], ['Christophe', 'Poisson']], '1', 'un simple tournoi de test']



    def show_players(self):
        # par ordre alpha
        # par classement
        pass
    
    def show_players_from_tournament(self):
        """Affiche les joueurs d'un tournoi"""
        # par ordre alpha
        # par classement
        pass

    def show_tournaments(self):
        """Affiche la liste des Tounois."""
        pass

    def rounds_of_tournament(show_tournament):
        """Affiche tous des Rounds d'un tournoi."""
        pass

    def matches_of_tournament(show_tournament):
        """Affiche tous les matchs d'un tournois"""
        pass

"""
Générer des rapports :
Nous aimerions pouvoir afficher les rapports suivants dans le programme :

    • Liste de tous les acteurs :
        ◦ par ordre alphabétique ;
        ◦ par classement.
    • Liste de tous les joueurs d'un tournoi :
        ◦ par ordre alphabétique ;
        ◦ par classement.
    • Liste de tous les tournois.
    • Liste de tous les tours d'un tournoi.
    • Liste de tous les matchs d'un tournoi.


Classement des joueurs 
    Afficher le classement
    modifier le classement. 
"""
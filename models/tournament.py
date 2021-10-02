
import datetime

class Tournament:
    def __init__(self, name, location, date, num_of_rounds=4, players_list, time, description, rounds):
        self.name = name
        self.location = location
        self.num_of_rounds = num_of_rounds
        self.players_list = players_list
        self.time = time
        self.description = description
        self.rounds = rounds
        self.date = date
        """Calcul de la date de fin si le tournoi est sur plusieurs jours"""
        if self_date != 1:
            curr_date = datetime.date.today()
            end_date = curr_date + datetime.timedelta(days=input_date)
            self_date.append(str(curr_date))
            self_date.append(str(end_date))
        else:
            date.append(str(datetime.date.today())
  

"""stocker les instances de rounds (listes)
    implementer stockage dans TinyDB
"""

class Player:
    """Player."""

    def __init__(self, name):
        """Has a name and a hand."""
        self.name = name
        return self.name

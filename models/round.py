import datetime

class Round:
    """ Round """

    def __init__(self, name, starting_time, ending_time, list_of_matches=[]):
        self.name = name
        self.starting_time = starting_time
        self.ending_time = ending_time

        self.starting_time = str(datetime.datetime.now()).split(".")[0]
        self.list_of_matches = list_of_matches


    def create_match(self, name, player_01, player_02):
        self.name = name
        self.player_01 = player_01
        self.player_02 = player_02
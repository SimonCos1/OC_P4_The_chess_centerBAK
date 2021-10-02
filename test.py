"""
class Lapin:
    def __init__(self, name = "Lapinou"):
       self.name = name
       self.location = "tahiti"

y = Lapin()

print(y.name)
print(y.location)

#------------------------------
from views.view import View

t = View()
tt = t.prompt_for_time()
print(tt)
print(f"{tt}")
"""
 
"""
players_list = []
first_name = "Simon"
last_name = "Caussin"
players_list.append([first_name, last_name])
first_name = "Eliasbeth"
last_name = "Hubert"
players_list.append([first_name, last_name])

print(players_list)"""
from views.view import View

class Controller:
    def __init__(self):
        pass
   
    def start_tournament(self):
        view = View()
        # Créer les players
        view.create_player()

        
y = Controller()
yy = y.start_tournament()

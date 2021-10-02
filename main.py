"""Entry point."""

from models.tounament import Tournament
from controllers.base import Controller
from views.base import View


def main():
    """Instancie """
    tounament = Tournament()
    view = View()
    game = Controller(tounament, view)
    game.run()


if __name__ == "__main__":
    main()
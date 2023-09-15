import arcade

from game.config import config
from game.game import Game


def run():
    game = Game(config())
    game.setup()
    
    arcade.run()

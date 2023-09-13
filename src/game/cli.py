import arcade

from game.config import config
from game.game import Game


def run():
    game = Game(config())
    
    arcade.run()

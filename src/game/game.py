import arcade


class Game(arcade.Window):
    def __init__(self, conf):
        super().__init__(
            conf["screen"]["width"],
            conf["screen"]["height"],
            conf["screen"]["title"])
        
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        self.clear()

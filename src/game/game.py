from random import randint
import arcade


class Game(arcade.Window):
    def __init__(self, conf):
        self.pixel_size = conf["screen"]["pixel_size"]

        super().__init__(
            conf["screen"]["width"]*conf["screen"]["pixel_size"],
            conf["screen"]["height"]*conf["screen"]["pixel_size"],
            conf["screen"]["title"],
            antialiasing=False)
        
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

        self.player = None
        self.scene = None
        self.camera = None

    def setup(self):
        self.player = arcade.Sprite(
            "assets/player.png",
            scale=self.pixel_size,
            image_width=16, image_height=16)

        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite("Player", self.player)
        
        self.scene.add_sprite_list("Walls")
        for i in range(self.height//(16*self.pixel_size)):
            for j in range(self.width//(16*self.pixel_size)):
                if randint(0, 3) == 0:
                    wall = arcade.Sprite(
                        "assets/wall.png",
                        scale=self.pixel_size, image_width=16, image_height=16)
                    
                    wall.center_x = j*16*self.pixel_size
                    wall.center_y = i*16*self.pixel_size

                    self.scene.add_sprite("Walls", wall)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player, self.scene.get_sprite_list("Walls"))
        
        self.camera = arcade.Camera(self.width, self.height)

    def center_camera_to_player(self):
        screen_center_x = self.player.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player.center_y - (
            self.camera.viewport_height / 2
        )

        self.camera.move_to((screen_center_x, screen_center_y))

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y = 5
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = -5
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 5
    
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0
    
    def on_update(self, delta_time):
        """Movement and game logic"""

        self.physics_engine.update()
        self.center_camera_to_player()

    def on_draw(self):
        self.camera.use()
        self.clear()
        self.scene.draw(filter=arcade.gl.NEAREST)

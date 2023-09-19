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
        
        self.map = None
        self.scene = None
        self.player = None
        self.camera = None

    def setup(self):
        self.map = arcade.load_tilemap("maps/test3.json", self.pixel_size, {
            "Walls": {
                "use_spatial_hash": True,
            },
        })

        self.scene = arcade.Scene.from_tilemap(self.map)

        self.player = arcade.Sprite(
            "assets/player.png",
            scale=self.pixel_size,
            image_width=16, image_height=16)
        self.scene.add_sprite("Player", self.player)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player, self.scene.get_sprite_list("Boundaries"))
        
        self.camera = arcade.Camera(self.width, self.height)

    def adjust_camera(self):
        player_left_bound = self.player.center_x - 64*self.pixel_size
        player_right_bound = self.player.center_x + 64*self.pixel_size
        player_bottom_bound = self.player.center_y - 64*self.pixel_size
        player_top_bound = self.player.center_y + 64*self.pixel_size
        
        camera_left_bound = self.camera.position.x
        camera_right_bound = self.camera.position.x + self.camera.viewport_width
        camera_bottom_bound = self.camera.position.y
        camera_top_bound = self.camera.position.y + self.camera.viewport_height

        new_x = self.camera.position.x
        new_y = self.camera.position.y

        if player_left_bound < camera_left_bound:
            new_x = player_left_bound

        if player_right_bound > camera_right_bound:
            new_x = player_right_bound - self.camera.viewport_width

        if player_bottom_bound < camera_bottom_bound:
            new_y = player_bottom_bound

        if player_top_bound > camera_top_bound:
            new_y = player_top_bound - self.camera.viewport_height

        self.camera.move((new_x, new_y))

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
        self.adjust_camera()

    def on_draw(self):
        self.camera.use()
        self.clear()
        self.scene.draw(filter=arcade.gl.NEAREST)

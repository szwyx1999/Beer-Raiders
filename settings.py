class Settings:
    """Save all the settings of the game"""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background = 'brewery-background.png'

        # Define Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)

        # Player settings
        self.beer_limit = 3
        self.animate_speed = 0.2
        self.health_image = 'images/beer-box.png'

        # Bullet settings
        self.bulletImg = 'images/bullet.png'
        self.bullets_allowed = 4

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.player_speed = 7.3
        self.bullet_speed = 8.3
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50


    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.player_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
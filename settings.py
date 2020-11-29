class Settings:
    """Save all the settings of the game"""

    def __init__(self):
        """Initialize the game's settings"""
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
        self.player_speed = 8.3
        self.animate_speed = 0.2

        # Bullet settings
        self.bullet_speed = 4.0
        self.bulletImg = 'bullet.png'
        self.bullets_allowed = 4
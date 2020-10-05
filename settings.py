class Settings():
    '''Save all the settings of the game'''

    def __init__(self):

        # Define Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)

        # Player

        # Bullet
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = YELLOW



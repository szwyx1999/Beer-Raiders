class GameStats:
    """Track statistics for Beer Raiders."""
    def __init__(self, br_game):
        """Initialize statistics."""
        self.settings = br_game.settings
        self.reset_stats()
        # Start the game in an inactive state
        self.game_active = False
        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.beers_left = self.settings.beer_limit
        self.score = 0
        self.level = 1
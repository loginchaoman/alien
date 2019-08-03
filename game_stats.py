class GameStats():
    def __init__(self,a_settings):
        self.a_settings =a_settings
        self.reset_stats()
        self.game_active = False
    def reset_stats(self):
        self.ships_left = self.a_settings.ship_limit
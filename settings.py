class Settings():
    def __init__(self):
        #初始化游戏内的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 3#子弹设置
        self.bullet_speed_factor=4
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=80,80,80
        self.bullets_allow = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction= 1
        self.ship_limit = 3

from game_framework import *

class Background:
    def __init__(self):
        self.image = load_image('Resource\\background.png')
        self.bgm = load_music('Resource\\BGM.mp3')
        self.bgm.set_volume(14)
        self.bgm.repeat_play()
    def draw(self):
        self.image.draw(400, 300)
        
class Face:
    def __init__(self):
        self.image = load_image('Resource\\kim.PNG')
    def draw(self):
        self.image.draw(630, 500)
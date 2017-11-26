from game_framework import *
import game_framework
image=None

class Attack_Effect:
    ILDE = 0
    image=None
    def __init__(self):
        self.x=0
        self.y=0
        self.frame = 0
        self.frames = 0
        if Attack_Effect.image==None:
            Attack_Effect.image=load_image('attack_effect.png')

    def update(self):
                    self.frame = (self.frame + 1) % 6

    def draw(self,x,y):
        self.image.clip_draw(self.frame * 70, 370, 800, 80, x, y)




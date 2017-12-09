from game_framework import *
import game_framework
image=None

class Attack_Effect:
    image=None
    def __init__(self):
        self.x=0
        self.y=0
        self.frame = 0
        self.frames = 0
        if Attack_Effect.image==None:
            Attack_Effect.image=load_image('Resource\\attack_effect.png')

    def update(self):
                    self.frame = (self.frames + 1) % 6

    def draw(self,x,y):
        self.image.clip_draw(40, 370, 40, 70, 30, 40)




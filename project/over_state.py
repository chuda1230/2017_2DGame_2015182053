import game_framework
from main_state import *
from Player import GetScore
from pico2d import *


name = "OverState"
player = None
score = None


class Death_Player:
    image = None
    font = None

    def __init__(self):
        self.x, self.y = 400,300
        self.frame = 0
        self.frames  = 0
        if Death_Player.image == None:
            Death_Player.image = load_image('Resource\\Player.png')
        if Death_Player.font == None:
            Death_Player.font = load_font('Resource\\ENCR10B.TTF', 30)

    def update(self,frame_time):
        self.frame = (self.frames + 1) % 9

    def draw(self):
        global score
        Death_Player.font.draw(300, 270, ' Score: %d' % score, (255, 255, 255))
        self.image.clip_draw(self.frame+590, 450, 70, 55, self.x, self.y)

def enter():
    global image,player,score
    import os
    player=Death_Player()
    score = GetScore()
    image=load_image('Resource\\black.png')


def exit():
    global image,player,score
    del(image)
    del(player)
    score = 0
import title_state

def handle_events(frame_time):
    global score
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.push_state(title_state)




def draw():
    clear_canvas()
    image.draw(400,300)
    player.draw()
    update_canvas()







def update(frame_time):
    player.update(frame_time)
    pass


def pause():
    pass


def resume():
    pass







import game_framework
from main_state import *
from pico2d import *


name = "OverState"
image = None
player = None
class Player:
    image = None
    font = None

    def __init__(self):
        self.x, self.y = 400,300
        self.frame = 0
        self.frames  = 0
        if Player.image == None:
            Player.image = load_image('Player.png')
        if Player.font == None:
            Player.font = load_font('ENCR10B.TTF', 30)

    def update(self,frame_time):
        self.frame = (self.frames + 1) % 9

    def draw(self):
        global score
        Player.font.draw(300, 270, ' Score: %d' % main_state.getScore(), (255, 255, 255))
        self.image.clip_draw(self.frame+590, 450, 70, 55, self.x, self.y)

def enter():
    global image,player
    import os
    player=Player()
    os.chdir("D:\\2DGame\\2017_2DGame_2015182053\\Resource")
    image=load_image('black.png')


def exit():
    global image,player
    del(image)
    del(player)

import main_state

def handle_events(frame_time):
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(title_state)



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







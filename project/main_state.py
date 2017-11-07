import random
import json
import os
from pico2d import *
import game_framework
import title_state



name = "MainState"

player = None
grass = None
font = None

os.chdir('D:\\2DGame\\2017_2DGame_2015182053\\Resource')

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Player:
    def __init__(self):
        self.x, self.y = 20, 80
        self.frame = 0
        self.image = load_image('Player.gif')
        self.dir = 1

    def update(self):
        self.frame = 0
        #self.x += self.dir
        #if self.x >= 800:
        #    self.dir = -1
        #elif self.x <= 0:
        #    self.dir = 1



    def draw(self):
        self.image.clip_draw(self.frame * 100, 735, 40, 50, self.x, self.y)


def enter():
    global player,grass
    player=Player()
    grass=Grass()


def exit():
    global player,grass
    del(player)
    del(grass)

def pause():
    pass


def resume():
    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)
            #game_framework.quit()
        #if p key goto pause_state
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            #game_framework.push_state(pause_state)


def update():
    player.update()
    pass


def draw_main_scene():
    grass.draw()
    player.draw()

def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()
    pass






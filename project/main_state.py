import random
import json
import os
from pico2d import *
import game_framework
import title_state

high=False
middle=False
low=False


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

class Shield_Enemy:
    PIXEL_PER_METER = (10.0 / 0.3)
    WALK_SPEED_KMPH = 20.0
    WALK_SPEED_MPM = (WALK_SPEED_KMPH * 1000.0 / 60.0)
    WALK_SPEED_MPS = (WALK_SPEED_MPM / 60.0)
    WALK_SPEED_PPS = (WALK_SPEED_MPS * PIXEL_PER_METER)

    image = None
    WALK = 0
    def __init__(self):
        self.frame = 0
        self.state = self.WALK
        if Shield_Enemy.image == None:
            Shield_Enemy.image = load_image('EggPawnShield.gif')

    def walk(self):
        self.frame+=1

    def update(self):
        distance = Shield_Enemy.WALK_SPEED_PPS * frame_time
        self.frame = (self.frames + 1) % 7
        delay(0.1)
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0 , 60, 80, self.x, self.y)


class Player:
    image=None
    IDLE, LOW_ATTACK, MIDDLE_ATTACK, HIGH_ATTACK=0,1,2,3

    def __init__(self):
        self.x, self.y = 70, 80
        self.frame = 0
        self.attack_frames=0
        self.state=self.IDLE
        if Player.image==None:
            Player.image = load_image('Player.png')


    def idle(self):
        global high,middle,low
        self.frame=0
        self.attack_frames=0
        if low==True:
            self.state=self.LOW_ATTACK
        elif middle==True:
            self.state=self.MIDDLE_ATTACK
        elif high==True:
            self.state=self.HIGH_ATTACK


    def low_kick(self):
        global low
        self.attack_frames += 1
        if self.attack_frames == 2:
            low=False
            self.state=self.IDLE
            self.attack_frames=0

    def middle_kick(self):
        global middle
        self.attack_frames+=1
        if self.attack_frames ==3:
            middle=False
            self.state=self.IDLE
            self.attack_frames=0

    def high_kick(self):
        global high
        self.attack_frames += 1
        if self.attack_frames == 2:
            high = False
            self.state = self.IDLE
            self.attack_frames = 0


    handle_state = {
        IDLE: idle,
        LOW_ATTACK: low_kick,
        MIDDLE_ATTACK: middle_kick,
        HIGH_ATTACK: high_kick
    }


    def update(self):
        global low,middle,high
        if low==True or middle==True or high==True:
            self.frame = (self.attack_frames + 1) % 3
            delay(0.1)
        else:
            self.frame=0
        print(self.state)
        self.handle_state[self.state](self)
        #self.x += self.dir
        #if self.x >= 800:
        #    self.dir = -1
        #elif self.x <= 0:
        #    self.dir = 1



    def draw(self):
        global low,middle,high
        if low==True:
            self.image.clip_draw(self.frame * 100, 665, 43, 60, self.x, self.y)
        elif middle==True:
            self.image.clip_draw(self.frame * 100, 720, 54, 55, self.x, self.y)
        elif high==True:
            self.image.clip_draw(self.frame * 100, 620, 54, 55, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 510, 54, 55, self.x, self.y)


def enter():
    global player,grass
    player=Player()
    grass=Grass()


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time



def exit():
    global player,grass
    del(player)
    del(grass)

def pause():
    pass


def resume():
    pass


def handle_events():
    global middle,low,high
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
        elif event.type==SDL_KEYDOWN and event.key==SDLK_a:
            middle=True
        elif event.type==SDL_KEYDOWN and event.key==SDLK_z:
            low=True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            high = True


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






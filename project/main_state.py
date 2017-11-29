import json
import os
from pico2d import *
from game_framework import *
import game_framework
import title_state
from attack_effect import Attack_Effect
import copy
import over_state
import pause_state

enemy_list=[]
heart_list=[]

score=0
timePass=0
hittime=0
total_hit=0

name = "MainState"
attack_effect=None
player = None
background = None
font = None
s_enemy = None
dog_enemy = None
blue_enemy = None
heart=None
face=None

high=False
middle=False
low=False
hit=False


os.chdir('D:\\2DGame\\2017_2DGame_2015182053\\Resource')

class Face:
    def __init__(self):
        self.image = load_image('kim.PNG')
    def draw(self):
        self.image.draw(630, 500)


class Background:
    def __init__(self):
        self.image = load_image('background.png')
    def draw(self):
        self.image.draw(400, 300)

class Heart:
    image=None
    def __init__(self,x,y):
        self.x=x
        self.y=y
        if Heart.image == None:
            Heart.image = load_image('heart_1.png')
    def draw(self):
        self.image.draw(self.x,self.y)
    def erase(self):
        heart_list.remove(self)

def heartspawn():
    global heart_list
    for i in range(670,800,20):
        newHeart=Heart(i,500)
        heart_list.append(newHeart)

class Blue_Enemy:
    PIXEL_PER_METER = (10.0 / 0.3)
    WALK_SPEED_KMPH = 20.0
    WALK_SPEED_MPM = (WALK_SPEED_KMPH * 1000.0 / 60.0)
    WALK_SPEED_MPS = (WALK_SPEED_MPM / 60.0)
    WALK_SPEED_PPS = (WALK_SPEED_MPS * PIXEL_PER_METER)
    image = None
    WALK = 0

    def __init__(self, x, y):
        global enemy_list
        self.x, self.y = x, y
        self.frame = 0
        self.dir = -1
        self.state = self.WALK
        if Blue_Enemy.image == None:
            Blue_Enemy.image = load_image('enemy2-1.png')

    def update(self, frame_time):
        distance = Blue_Enemy.WALK_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 5
        self.x += (self.dir * distance)

    def draw(self):
        self.image.clip_draw(self.frame * 122, 2020, 55, 120, self.x, self.y)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x, self.y + 30

    def getEffectX(self):
        return self.x-30
    def getEffectY(self):
        return self.y

    def getType(self):
        type = 2
        return type

    def death(self):
        global enemy_list
        enemy_list.remove(self)

class Dog_Enemy:
    PIXEL_PER_METER = (10.0 / 0.3)
    WALK_SPEED_KMPH = 30.0
    WALK_SPEED_MPM = (WALK_SPEED_KMPH * 1000.0 / 60.0)
    WALK_SPEED_MPS = (WALK_SPEED_MPM / 60.0)
    WALK_SPEED_PPS = (WALK_SPEED_MPS * PIXEL_PER_METER)
    image = None
    WALK = 0

    def __init__(self, x, y):
        global enemy_list
        self.x, self.y = x, y
        self.frame = 0
        self.dir = -1
        self.state = self.WALK
        if Dog_Enemy.image == None:
            Dog_Enemy.image = load_image('enemy4.png')

    def update(self, frame_time):
        distance = Dog_Enemy.WALK_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 6
        self.x += (self.dir * distance)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x, self.y + 30

    def draw(self):
        self.image.clip_draw(self.frame * 95, 20, 80, 50, self.x, self.y)

    def getType(self):
        type = 1
        return type

    def getEffectX(self):
        return self.x-30
    def getEffectY(self):
        return self.y-30

    def death(self):
        global enemy_list
        enemy_list.remove(self)




class Shield_Enemy:
    PIXEL_PER_METER = (10.0 / 0.3)
    WALK_SPEED_KMPH = 15.0
    WALK_SPEED_MPM = (WALK_SPEED_KMPH * 1000.0 / 60.0)
    WALK_SPEED_MPS = (WALK_SPEED_MPM / 60.0)
    WALK_SPEED_PPS = (WALK_SPEED_MPS * PIXEL_PER_METER)

    image = None
    WALK = 0
    def __init__(self,x,y):
        global enemy_list
        self.x, self.y = x,y
        self.frame = 0
        self.dir=-1
        self.state = self.WALK
        if Shield_Enemy.image == None:
            Shield_Enemy.image = load_image('enemy1-1.png')


    def update(self , frame_time):
        distance = Shield_Enemy.WALK_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 7
        self.x+=(self.dir*distance)

    def draw(self):
        self.image.clip_draw(self.frame*132 , 1100 , 70, 120, self.x, self.y)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def getType(self):
        type=0
        return type

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x, self.y + 30

    def getEffectX(self):
        return self.x

    def getEffectY(self):
        return self.y-30

    def death(self):
        global enemy_list
        enemy_list.remove(self)


def SpawnEnemy():
    global enemy_list
    num = random.randint(0, 2)
    if (num == 0):
        newDog = Dog_Enemy(850, 55)
        enemy_list.append(newDog)
    elif(num==1):
        newObject = Shield_Enemy(850, 80)
        enemy_list.append(newObject)
    elif(num==2):
        newBlue = Blue_Enemy(850, 80)
        enemy_list.append(newBlue)


class Player:
    image=None
    font=None
    IDLE, LOW_ATTACK, MIDDLE_ATTACK, HIGH_ATTACK,HIT=0,1,2,3,4

    def __init__(self):
        self.x, self.y = 70, 70
        self.frame = 0
        self.attack_frames=0
        self.hit_frames=0
        self.state=self.IDLE
        if Player.image==None:
            Player.image = load_image('player.png')
        if Player.font == None:
            Player.font=load_font('ENCR10B.TTF', 20)


    def idle(self):
        global high,middle,low
        self.frame=0
        self.attack_frames=0
        self.hit_frames=0
        if low==True:
            self.state=self.LOW_ATTACK
        elif middle==True:
            self.state=self.MIDDLE_ATTACK
        elif high==True:
            self.state=self.HIGH_ATTACK
        elif hit==True:
            self.state=self.HIT


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

    def hit_motion(self):
        global hit
        self.hit_frames +=1
        if self.hit_frames == 3:
            hit = False
            self.state=self.IDLE
            self.hit_frames=0


    handle_state = {
        IDLE: idle,
        LOW_ATTACK: low_kick,
        MIDDLE_ATTACK: middle_kick,
        HIGH_ATTACK: high_kick,
        HIT: hit_motion
    }


    def update(self,frame_time):
        global low,middle,high,hit
        if low == True or middle == True or high == True:
            self.frame = (self.attack_frames + 1) % 3
        elif hit == True:
            self.frame = (self.hit_frames+1)%3
        else:
            self.frame=0
        self.handle_state[self.state](self)
        #self.x += self.dir
        #if self.x >= 800:
        #    self.dir = -1
        #elif self.x <= 0:
        #    self.dir = 1



    def draw(self):
        global low,middle,high,score
        Player.font.draw(0, 540, ' Score: %d' % score, (255, 255,255))
        if low==True:
            self.image.clip_draw(self.frame+70, 680, 65, 50, self.x, self.y)
        elif middle==True:
            self.image.clip_draw(self.frame+70, 720, 65, 50, self.x, self.y)
        elif high==True:
            self.image.clip_draw(self.frame+106, 620, 55, 60, self.x, self.y)
        elif hit==True:
            self.image.clip_draw(self.frame, 450, 45, 55,self.x,self.y)
        else:
            self.image.clip_draw(self.frame * 60, 510, 54, 55, self.x, self.y)
        delay(0.05)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def attack_bb(self):
        return self.x, self.y - 30, self.x + 50, self.y + 30
    def get_bb(self):
        return self.x, self.y - 30, self.x + 30, self.y + 30
    def draw_attack_bb(self):
        draw_rectangle(*self.attack_bb())

def getScore():
    global score
    return score

def enter():
    global player,background,s_enemy,dog_enemy,blue_enemy,heart,face,attack_effect
    background = Background()
    player=Player()
    face=Face()
    heartspawn()
    attack_effect=Attack_Effect()



def exit():
    global player,background,s_enemy,dog_enemy,blue_enemy,heart,face
    del(player)
    del(background)
    del(s_enemy)
    del(dog_enemy)
    del(blue_enemy)
    del(heart)
    del(face)
    del(attack_effect)

def pause():
    pass


def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a>right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b:  return False
    if bottom_a > top_b: return False
    return True

def attack_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.attack_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a>right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b:  return False
    if bottom_a > top_b: return False
    return True


def handle_events(frame_time):
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)

def update(frame_time):
    global timePass,hit,hittime,total_hit,score
    for heart in heart_list:
        if(hit == True):
            heart.erase()
            hit=False
    player.update(frame_time)

    for enemy in enemy_list:
        enemy.update(frame_time)
    timePass += frame_time
    hittime += frame_time
    if(timePass>3):
        SpawnEnemy()
        timePass = 0

    for enemy in enemy_list:
        if collide(player,enemy) and hittime>1.6:
            hit=True
            total_hit+=1
            hittime=0
            if (total_hit == 7.0):
                game_framework.push_state(over_state)
        if attack_collide(player,enemy) and enemy.getType() == 0 and high==True:
            attack_effect.update()
            enemy.death()
            score+=10
        elif attack_collide(player,enemy) and enemy.getType() == 1 and low==True:
            attack_effect.update()
            enemy.death()
            score+=10
        elif attack_collide(player,enemy) and enemy.getType() == 2 and middle==True:
            attack_effect.update()
            enemy.death()
            score+=10



def draw_main_scene():
    background.draw()
    face.draw()
    player.draw()
    for enemy in enemy_list:
        if(attack_collide(player,enemy) and enemy.getType() == 0):
            attack_effect.draw(enemy.getEffectX(),enemy.getEffectY())

    for heart in heart_list:
        heart.draw()
    if(low==True or middle==True or high==True):
        player.draw_attack_bb()
    else:
        player.draw_bb()
    for enemy in enemy_list:
        enemy.draw()
        enemy.draw_bb()


def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()
    pass






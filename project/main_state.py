import json
import os
from Heart import *
import game_framework
import title_state
from Player import *
from Enemy import getEnemy_list,SpawnEnemy,delEnemy_list
from Background import *
from Collide import *
import over_state
import pause_state

total_time=0
timePass=0
hittime=0
total_hit=0

name = "MainState"
score = None
player = None
background = None
font = None
heart=None
face=None

def enter():
    global player,background,heart,face
    background = Background()
    player=Player()
    face=Face()
    heartspawn()
    SetScore(0)

def exit():
    global player,background,heart,face
    del(background)
    delEnemy_list()
    if heart != None:
        del(heart)
    del(face)

def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    global middle,low,high
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_a:
            player.middle=True
        elif event.type==SDL_KEYDOWN and event.key==SDLK_z:
            player.low=True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            player.high = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            player.air = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)

def update(frame_time):
    global timePass,hittime,total_hit,combo,total_time
    for heart in heart_list:
        if(player.hit == True):
            heart.erase()
            player.hit=False
    player.update(frame_time)

    for enemy in getEnemy_list():
        enemy.update(frame_time)
    total_time+=(frame_time*0.0001)
    timePass += frame_time
    hittime += frame_time
    if(timePass>1.5-total_time):
        SpawnEnemy()
        timePass = 0

    for enemy in getEnemy_list():
        if collide(player,enemy) and hittime>1.0:
            if (len(heart_list)-1 == 0):
                game_framework.change_state(over_state)
            else:
                player.hit=True
                Player.ComboZero(0)
                hittime=0

        elif attack_collide(player,enemy) and enemy.getType() == 0 and player.high==True:
            Player.high_attack_sound.play()
            enemy.death()
            Player.PlusCombo(1)
            Player.PlusScore(10, GetCombo())
        elif attack_collide(player,enemy) and enemy.getType() == 1 and player.low==True:
            Player.low_attack_sound.play()
            enemy.death()
            Player.PlusCombo(1)
            Player.PlusScore(10,GetCombo())
        elif attack_collide(player,enemy) and enemy.getType() == 2 and player.middle==True:
            Player.middle_attack_sound.play()
            enemy.death()
            Player.PlusCombo(1)
            Player.PlusScore(10, GetCombo())
        elif attack_collide(player,enemy) and enemy.getType() == 3 and player.air==True:
            Player.high_attack_sound.play()
            enemy.death()
            Player.PlusCombo(1)
            Player.PlusScore(10, GetCombo())

def draw_main_scene():
    background.draw()
    face.draw()
    player.draw()
    for heart in heart_list:
        heart.draw()

    for enemy in getEnemy_list():
        enemy.draw()
        #enemy.draw_bb()

def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()
    pass






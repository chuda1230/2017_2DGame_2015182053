import json
import os
from Heart import *
import game_framework
import title_state
from attack_effect import Attack_Effect
from Player import *
from Enemy import getEnemy_list,SpawnEnemy
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
attack_effect=None
player = None
background = None
font = None
heart=None
face=None

def enter():
    global player,background,heart,face,attack_effect,score
    background = Background()
    player=Player()
    face=Face()
    heartspawn()
    attack_effect=Attack_Effect()

def exit():
    dellist=getEnemy_list()
    global player,background,heart,face,score
    del(player)
    del(background)
    del(dellist)
    del(heart)
    del(face)
    del(score)
    del(attack_effect)

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
            #game_framework.quit()
        #if p key goto pause_state
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            #game_framework.push_state(pause_state)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_a:
            player.middle=True
        elif event.type==SDL_KEYDOWN and event.key==SDLK_z:
            player.low=True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            player.high = True
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
    total_time+=(frame_time*0.01)
    timePass += frame_time
    hittime += frame_time
    if(timePass>1.5-total_time):
        SpawnEnemy()
        timePass = 0

    for enemy in getEnemy_list():
        if collide(player,enemy) and hittime>1.6:
            player.hit=True
            Player.ComboZero(0)
            hittime=0
            if (len(heart_list)-1 == 0):
                game_framework.push_state(over_state)
        if attack_collide(player,enemy) and enemy.getType() == 0 and player.high==True:
            attack_effect.update()
            enemy.death()
            Player.PlusCombo(1)
            Player.PlusScore(10, GetCombo())
        elif attack_collide(player,enemy) and enemy.getType() == 1 and player.low==True:
            attack_effect.update()
            enemy.death()
            Player.PlusCombo(1)
            Player.PlusScore(10,GetCombo())
        elif attack_collide(player,enemy) and enemy.getType() == 2 and player.middle==True:
            attack_effect.update()
            enemy.death()
            Player.PlusCombo(1)
            Player.PlusScore(10, GetCombo())

def draw_main_scene():
    background.draw()
    face.draw()
    player.draw()
    for enemy in getEnemy_list():
        if(attack_collide(player,enemy) and enemy.getType() == 0):
            attack_effect.draw(enemy.getEffectX(),enemy.getEffectY())

    for heart in heart_list:
        heart.draw()
    if(player.low==True or player.middle==True or player.high==True):
        player.draw_attack_bb()
    else:
        player.draw_bb()
    for enemy in getEnemy_list():
        enemy.draw()
        enemy.draw_bb()

def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()
    pass






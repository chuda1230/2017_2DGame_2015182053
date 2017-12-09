import game_framework
from pico2d import *
import title_state
import main_state

name = "PauseState"
image = None
logo_time = 0.0
counter = 0

def enter():
    global image
    image=load_image('Resource\\pause.png')

def exit():
    global image
    del(image)




def update(frame_time):
    global counter
    counter = (counter + 1)%500
    pass


def draw():
    global image
    clear_canvas()
    main_state.draw_main_scene()
    if counter < 300:
        image.draw(400,300)
    update_canvas()
    pass




def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            #game_framework.change_state(title_state)
            #if key is p return to previos state
                game_framework.pop_state()






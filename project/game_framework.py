import random
from pico2d import *
from os import *
import main_state
import over_state
class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw


class TestGameState:

    def __init__(self, name):
        self.name = name

    def enter(self):
        print("State [%s] Entered" % self.name)

    def exit(self):
        print("State [%s] Exited" % self.name)

    def pause(self):
        print("State [%s] Paused" % self.name)

    def resume(self):
        print("State [%s] Resumed" % self.name)

    def handle_events(self,frame_time):
        print("State [%s] handle_events" % self.name)

    def update(self,frame_time):
        print("State [%s] update" % self.name)

    def draw(self):
        print("State [%s] draw" % self.name)



running = None
stack = None


def change_state(state):
    global stack
    pop_state()
    stack.append(state)
    state.enter()



def push_state(state):
    global stack
    if (len(stack) > 0):    #스택에 뭔가가 있으면
        stack[-1].pause()   #이놈의 포즈를 호출한뒤
    stack.append(state)     #가고자하는 스테이트를 스택에 추가
    state.enter()           #해당 스테이트 입장
#change와 push의차이
#change=현재상태에서 다른상태로 갈때 현재상태를 exit하고 감
#push=현재상태에 미련이 있어서 잠깐 갔다가 다시돌아옴


def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].resume()



def quit():
    global running
    running = False

current_time = 0.0
def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


game_time=0
def run(start_state):
    global running, stack,current_time,game_time
    running = True
    stack = [start_state]
    start_state.enter()
    current_time = get_time()
    while (running):
        frame_time = get_frame_time()
        game_time+=frame_time
        stack[-1].handle_events(frame_time)
        stack[-1].update(frame_time)
        stack[-1].draw()
    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()


def test_game_framework():
    start_state = TestGameState('StartState')
    run(start_state)



if __name__ == '__main__':
    test_game_framework()
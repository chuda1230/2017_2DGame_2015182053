from pico2d import *
import os
import game_framework

import start_state
import main_state
import over_state
open_canvas(sync=True)
game_framework.run(start_state)
close_canvas()
# fill here

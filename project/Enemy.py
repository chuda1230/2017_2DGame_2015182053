from game_framework import *
enemy_list=[]
total_time=0
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
            Blue_Enemy.image = load_image('Resource\\Blue_enemy.png')

    def update(self, frame_time):
        global total_time
        total_time=total_time+frame_time
        addspeed = total_time*0.0001
        distance = Blue_Enemy.WALK_SPEED_PPS * (frame_time+addspeed)
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
    JUMP = 1

    def __init__(self, x, y):
        global enemy_list
        self.x, self.y = x, y
        self.frame = 0
        self.dir = -1
        self.state = self.WALK
        if Dog_Enemy.image == None:
            Dog_Enemy.image = load_image('Resource\\Dog_enemy.png')

    def update(self, frame_time):
        global total_time
        total_time = total_time + frame_time
        addspeed = total_time * 0.0001
        distance = Dog_Enemy.WALK_SPEED_PPS * (frame_time+addspeed)
        self.frame = (self.frame + 1) % 6
        self.x += (self.dir * distance)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x, self.y + 30

    def draw(self):
        self.image.clip_draw(self.frame * 95, 20, 80, 50, self.x, self.y)
        #self.image.clip_draw(self.frame + 635, 20, 40, 70, self.x, self.y)

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


class Muscle_Enemy:
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
        if Muscle_Enemy.image == None:
            Muscle_Enemy.image = load_image('Resource\\Muscle_enemy.png')


    def update(self , frame_time):
        global total_time
        total_time = total_time + frame_time
        addspeed = total_time * 0.0001
        distance = Muscle_Enemy.WALK_SPEED_PPS * (frame_time+addspeed)
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
    num = random.randint(0,2)
    if (num == 0):
        newDog = Dog_Enemy(850, 55)
        enemy_list.append(newDog)
    elif(num==1):
        newObject = Muscle_Enemy(850, 80)
        enemy_list.append(newObject)
    elif(num==2):
        newBlue = Blue_Enemy(850, 80)
        enemy_list.append(newBlue)

def getEnemy_list():
    global enemy_list
    return enemy_list




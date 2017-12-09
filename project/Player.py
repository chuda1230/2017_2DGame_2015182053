from game_framework import *

score=0
combo=0

class Player:
    high = False
    middle = False
    low = False
    hit = False
    image=None
    font=None
    high_attack_sound = None
    middle_attack_sound = None
    low_attack_sound = None
    IDLE, LOW_ATTACK, MIDDLE_ATTACK, HIGH_ATTACK,HIT=0,1,2,3,4

    def __init__(self):
        self.x, self.y = 70, 70
        self.frame = 0
        self.attack_frames=0
        self.hit_frames=0
        self.state=self.IDLE
        if Player.image==None:
            Player.image = load_image('Resource\\player.png')
        if Player.font == None:
            Player.font=load_font('Resource\\ENCR10B.TTF', 20)
        if Player.high_attack_sound == None:
            Player.high_attack_sound = load_wav('Resource\\high_attack.ogg')
            Player.high_attack_sound.set_volume(32)
        if Player.middle_attack_sound == None:
            Player.middle_attack_sound = load_wav('Resource\\middle_attack.ogg')
            Player.middle_attack_sound.set_volume(32)
        if Player.low_attack_sound == None:
            Player.low_attack_sound = load_wav('Resource\\low_attack.ogg')
            Player.low_attack_sound.set_volume(32)

    def idle(self):
        global high,middle,low
        self.frame=0
        self.attack_frames=0
        self.hit_frames=0
        if self.low==True:
            self.state=self.LOW_ATTACK
        elif self.middle==True:
            self.state=self.MIDDLE_ATTACK
        elif self.high==True:
            self.state=self.HIGH_ATTACK
        elif self.hit==True:
            self.state=self.HIT


    def low_kick(self):
        self.attack_frames += 1
        if self.attack_frames == 2:
            self.low=False
            self.state=self.IDLE
            self.attack_frames=0

    def middle_kick(self):
        self.attack_frames+=1
        if self.attack_frames ==3:
            self.middle=False
            self.state=self.IDLE
            self.attack_frames=0

    def high_kick(self):
        self.attack_frames += 1
        if self.attack_frames == 2:
            self.high = False
            self.state = self.IDLE
            self.attack_frames = 0

    def hit_motion(self):
        self.hit_frames +=1
        if self.hit_frames == 3:
            self.hit = False
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
        if self.low == True or self.middle == True or self.high == True:
            self.frame = (self.attack_frames + 1) % 3
        elif self.hit == True:
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
        if combo<5:
            Player.font.draw(12, 520,'Combo: %d' % combo,(255, 255, 255))
        elif combo<10 and combo>=5:
            Player.font.draw(12, 520, 'Combo: %d' % combo, (255, 255, 0))
        elif combo >= 10:
            Player.font.draw(12, 520, 'Combo: %d' % combo, (255, 0, 0))

        Player.font.draw(0, 540, ' Score: %d' % score, (255, 255, 255))
        if self.low==True:
            self.image.clip_draw(self.frame+70, 680, 65, 50, self.x, self.y)
        elif self.middle==True:
            self.image.clip_draw(self.frame+70, 720, 65, 50, self.x, self.y)
        elif self.high==True:
            self.image.clip_draw(self.frame+106, 620, 55, 60, self.x, self.y)
        elif self.hit==True:
            self.image.clip_draw(self.frame, 450, 45, 55,self.x,self.y)
        else:
            self.image.clip_draw(self.frame * 60, 510, 54, 55, self.x, self.y)
        delay(0.05)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def attack_bb(self):
        return self.x, self.y - 30, self.x + 50, self.y + 30
    def get_bb(self):
        return self.x, self.y - 30, self.x + 10, self.y + 30
    def draw_attack_bb(self):
        draw_rectangle(*self.attack_bb())

    def PlusScore(num,combo):
        global score
        score+=num+combo
        return score
    def PlusCombo(num):
        global combo
        combo+=num
        return combo
    def ComboZero(num):
        global combo
        combo=combo*num
        return combo

def GetScore():
    global score
    return score
def GetCombo():
    global combo
    return combo

from game_framework import *
heart_list=[]

class Heart:
    image=None
    font = None
    def __init__(self,x,y):
        self.x=x
        self.y=y
        if Heart.image == None:
            Heart.image = load_image('Resource\\heart_1.png')
    def draw(self):
        self.image.draw(self.x,self.y)
    def erase(self):
        heart_list.remove(self)

def heartspawn():
    global heart_list
    for i in range(670,800,20):
        newHeart=Heart(i,500)
        heart_list.append(newHeart)
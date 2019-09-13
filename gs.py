'''
  - Future implementation: 
User inputs all the parameters or the planet (mass, radius, velocity) and it will make an accurate model 
of it with an appropriate color for the mass of the object (e.g. objects of roughly one solar mass 
will be yellow) and objects that are super dense will be turned into blackholes 
'''
from tkinter import *
import time
from random import random
import math

gui = Tk()
var = IntVar()
gui.geometry("1538x792+-10+0")
c = Canvas(gui ,width=1920 ,height=1080)
c.pack()
gui.title("G R A V I T Y    S I M U L A T O R")
c.configure(background='black')

go = False
balls = []

#--------------------------------------------------------

class Ball():
    def __init__(self,x,y,vx,vy,color = 'white',m = 10):
        self.x = x
        self.y = y
        self.m = m
        if m**(1/3)*3 < 50: self.w = m**(1/3)*3
        else: self.w = 50
        self.h = self.w
        self.vx = vx
        self.vy = vy
        self.color = color
    def move(self):
        self.x += self.vx
        self.y += self.vy
    def display(self):
        c.create_oval(self.x-self.w/2,self.y-self.h/2,self.x+self.w/2,self.y+self.h/2,fill = self.color,outline = '',tag = 'animate')
        for i in range(0,len(balls)):
            x_dist = balls[i].x-self.x
            y_dist = self.y-balls[i].y
            dist = ((x_dist)**2+(y_dist)**2)**0.5
            accel = 0
            if dist != 0:
                accel = 0.5*balls[i].m/(dist**2)
            if x_dist < 0:
                self.vx -= abs(accel*math.cos(math.atan(y_dist/x_dist)))
#                if self.color == 'yellow': print('ACCEL_X:', accel*math.cos(math.atan(y_dist/x_dist)))
            elif x_dist > 0:
                self.vx += abs(accel*math.cos(math.atan(y_dist/x_dist)))
#                if self.color == 'yellow': print('ACCEL_X:', accel*math.cos(math.atan(y_dist/x_dist)))
            if y_dist < 0:
                if x_dist == 0:
                    self.vy += accel
#                    if self.color == 'yellow': print('ACCEL_Y:', accel)
                else:
                    self.vy += abs(accel*math.sin(math.atan(y_dist/x_dist)))
#                    if self.color == 'yellow': print('ACCEL_Y:', accel*math.sin(math.atan(y_dist/x_dist)))
            elif y_dist > 0:
                if x_dist == 0:
                    self.vy -= accel
#                    if self.color == 'yellow': print('ACCEL_Y:', accel)
                else:
                    self.vy -= abs(accel*math.sin(math.atan(y_dist/x_dist)))
#                    if self.color == 'yellow': print('ACCEL_Y:', accel*math.sin(math.atan(y_dist/x_dist)))
            
#            line_dist = 15-0.05*dist
#            if line_dist > 0:
#                c.create_line(self.x,self.y,(balls[i].x),(balls[i].y), fill = self.color,width = min(self.w,balls[i].w)/2,tag = 'animate')
    def getXY(self):
        return (self.x,self.y)


def pause():
    go = False
    print('test')
def play():
    go = True
def reset():
    balls = []

def display_all():
    for o in c.find_withtag('animate'):
        c.delete(o)
        
    for b in balls:
        b.move()
        b.display()
        

#-----------------------------------------------------

gui.update()

# Generate random balls
for _ in range(10):
    balls.append(Ball(random()*c.winfo_width(),random()*c.winfo_height(), random()*4-2, random()*4-2, 'white', 10))

#m/m' --> s/sqrt(m')
#d*d' --> s/s'

# Testing
'''balls.append(Ball(c.winfo_width()/2, c.winfo_height()/2+36000000, 41,     0,'red',    6.39*10^23      ))
balls.append(Ball(c.winfo_width()/2, c.winfo_height()/2 + 150000000, 31.022, 0,'white',  7.34767309*10^22))
balls.append(Ball(c.winfo_width()/2, c.winfo_height()/2 + 149600000, 31,     0,'blue',   5.972*10^24     ))
balls.append(Ball(c.winfo_width()/2, c.winfo_height()/2,             0,      0,'yellow', 1.989*10^30     ))
'''

balls.append(Ball(c.winfo_width()/2, c.winfo_height()/2 + 200,       5,     0,'blue',   100     ))
balls.append(Ball(c.winfo_width()/2, c.winfo_height()/2,             0,      0,'yellow', 10000     ))

'''l1 = Label(c, text = 'MASS')
e1 = Entry(gui)
b1 = Button(c, text = 'PAUSE', command = pause())
b2 = Button(c, text = 'PLAY', command = play())
b3 = Button(c, text = 'RESET', command = reset())

c.create_window(100, 20, window = e1)
c.create_window(100, 40, window = l1)
c.create_window(200, 40, window = b1)
c.create_window(300, 120, window = b2)
c.create_window(400, 120, window = b3)
'''

try:
    while True:
        addb = 0
        for b in balls:
            if b.x > c.winfo_width()+30 or b.x + b.w < -30 or b.y > c.winfo_height()+30 or b.y + b.h < -30:
                balls.remove(b)
                addb += 1
        for _ in range(addb):
            side = random()*4
            if 0 <= side < 1:
                balls.append(Ball(-30,random()*c.winfo_height(),random(),random()*2-1))
            elif 1 <= side < 2:
                balls.append(Ball(c.winfo_width(),random()*c.winfo_height(),-random(),random()*2-1))
            elif 2 <= side < 3:
                balls.append(Ball(random()*c.winfo_width(),-30,random()*2-1,random()))
            else:
                balls.append(Ball(random()*c.winfo_width(),c.winfo_height(),random()*2-1,-random()))
        
        
        display_all()
        gui.update()
        time.sleep(0.01)
except TclError:
    exit()
gui.mainloop()


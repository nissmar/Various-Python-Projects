import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rd
from math import cos,sin

#Right click to start the animation

fig = plt.figure()
ax = plt.axes(xlim=(-10,10), ylim=(-15,5))
line1,=plt.plot([],[],'-o',color='k',lw=5)
line2,=plt.plot([],[])
posx=[]
posy=[]
l0=2

global pos,vitesse,accel,pas,raideur
pas=0.05
pos=complex(0,-1.5*l0)
raideur=2.5

vitesse=complex(0,0)
accel=complex(0,0)




def anim(i):
    global pos,vitesse,accel,pas,posx,posy
    accel=complex(0,-9.81)-raideur*(abs(pos)-l0)*pos/abs(pos)
    vitesse+=pas*accel
    pos+=pas*vitesse
    line1.set_data([0,pos.real],[0,pos.imag])
    posx.append(pos.real)
    posy.append(pos.imag)
    line2.set_data([posx],[posy])
    return line1,line2,
 
def clic(event):
    global pos,vitesse,accel,posx,posy
    if event.button==3:
        x=(event.xdata)
        y=(event.ydata)
        pos=complex(x,y)
        print(x,y)
        vitesse=complex(0,0)
        accel=complex(0,0)
        posx=[]
        posy=[]
        line2.set_data([],[])
        line1.set_data([],[])
            
   
        
    

cid = fig.canvas.mpl_connect('button_press_event',clic)
anim = animation.FuncAnimation(fig, anim,interval=1, blit=True)
plt.show()
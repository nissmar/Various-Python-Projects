import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rd
fig,ax=plt.subplots()

global dim,tab
dim=20
tab=np.zeros((dim,dim))

print('''HOW TO PLAY: Left click to add, right click to remove''')

class Grain():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def bouge(self):
        if tab[max(self.x-1,0),self.y]==0:
            tab[self.x,self.y]=0
            self.x-=1
            tab[self.x,self.y]=1
        elif self.x>2:
            if self.y<dim-1:
                if tab[self.x-2,self.y+1]==0:
                    tab[self.x,self.y]=0
                    self.y+=1
                    tab[self.x,self.y]=1
            if self.y>0:
                if tab[self.x-2,self.y-1]==0:
                    tab[self.x,self.y]=0
                    self.y-=1
                    tab[self.x,self.y]=1
        
        
     

im=plt.imshow(tab,vmin=0, vmax=1, origin='lower',animated=True)

# L=[]
L=[Grain(rd.randint(dim//2,dim-1),rd.randint(0,dim-1)) for i in range(10)]

def anim(i):

    for elem in L:
        elem.bouge()
    # print(tab)
    im.set_data(tab)
    return im,
 


def clic(event):
    if event.button==1:
        x=int(event.xdata)
        y=int(event.ydata)
        if 0<=x<dim and 0<=y<dim:
            L.append(Grain(y,x))
            
    if event.button==2:
        print("TILT")
        for elem in L:
            elem.x=dim-1-elem.x
        for i in range(dim):
            for j in range(dim):
                tab[i,j]=0
    if event.button==3:
        x=int(event.xdata)
        y=int(event.ydata)
        for elem in L:
            if elem.x==y and elem.y==x:
                tab[y,x]=0
                # plt.pause(0.1)
                L.remove(elem)
    

cid = fig.canvas.mpl_connect('button_press_event',clic)
anim = animation.FuncAnimation(fig, anim,interval=10, blit=True)
plt.show()
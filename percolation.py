import matplotlib.pyplot as plt
import random as rd
import numpy as np
import matplotlib.animation as animation

fig=plt.figure()

DIM=100
tab=np.zeros((DIM,DIM))
tab[DIM//2,DIM//2]=1
im=plt.imshow(tab)

def conforme(x):
    return 0<=x[0]<DIM and 0<=x[1]<DIM
    
def percol(tab,p):
    avoir=[]
    vus=[]
    for i in range(DIM):
        for j in range(DIM):
            if tab[i,j]!=0:
                avoir.append((i,j))
    while avoir!=[]:
        x,y=avoir.pop()
        for couple in [(x,(y+1)),(x,(y-1)),((x+1),y),((x-1),y)]:
            if not(couple in vus) and rd.random()<p and conforme(couple):
                tab[couple]=1
                vus.append(couple)
                avoir.append(couple)
    im.set_data(tab)
    plt.pause(0.001)

def percolanim(i,p,avoir,vus):
    for i in range(100):
        if avoir!=[]:
            x,y=avoir.pop(0)
            for couple in [(x,(y+1)),(x,(y-1)),((x+1),y),((x-1),y)]:
                if not(couple in vus) and rd.random()<p and conforme(couple):
                    tab[couple]=1
                    vus.append(couple)
                    avoir.append(couple)
    im.set_data(tab)
    return p,avoir,vus
    

anim = animation.FuncAnimation(fig, percolanim, fargs=([0.59,[(DIM//2,DIM//2)],[]]), interval=10, blit=False)
plt.show()

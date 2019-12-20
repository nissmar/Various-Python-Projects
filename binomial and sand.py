import matplotlib.pyplot as plt
import numpy as np
import random as rd
plt.interactive(True)

fig,ax=plt.subplots()

global dim
dim=200
nb=400

#

    
def affiche(L,t):
    for elem in L:
        a,b=elem
        t[a,b]=1-t[a,b]


def bouge(L,t):
    l=[]
    for elem in L:
        a,b=elem
        if a<dim-1:
            if a%2==0 and a<3*dim//4:
                t[a,b]=0
                if rd.randint(0,1)==0:
                    b=min(dim//2-1,b+1)
                else:
                    b=max(b-1,0)
            if t[a+1,b]==0:
                t[a+1,b]=1
                t[a,b]=0
                elem=(a+1,b)
                
            else:
                t[a,b]=1
        l.append(elem)
    return l
                
plt.close()
L=[(0,dim//4)]
tab=np.zeros((dim,dim//2))
L=bouge(L,tab)
im=plt.imshow(tab)

for i in range(nb+dim+1):
    if i<nb:
        L.append((0,dim//4))
    L=bouge(L,tab)
    if i%10==0:
        im.set_data(tab)
        im.axes.figure.canvas.draw()
        plt.pause(0.000001)
plt.show()
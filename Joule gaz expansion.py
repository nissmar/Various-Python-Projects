import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as rd
from math import cos, sin, radians


#Joule expansion Simulation

dim=20
nbpart=400
haut=[]
bas=[]

fac=0.13
bordureh1=dim/4.0-2*fac         
bordureh2=dim/4.0+2*fac
bordurev1=dim/2.0-1                 #ouverture
bordurev2=dim/2.0+1
vlim1=1
vlim2=dim-1
hlim1=1
hlim2=dim-1
fig = plt.figure()
ax = plt.axes(xlim=(1, dim-1), ylim=(1, dim-1))
texte = ax.text(17, 17,'',fontsize=15)
texte2 = ax.text(17, 16,'',fontsize=15)
line, = ax.plot([], [],'o', lw=2)

plt.plot([1,bordurev1],[bordureh2,bordureh2],'k',linewidth=4)
plt.plot([bordurev2,dim-1],[bordureh2,bordureh2],'k',linewidth=4)
plt.plot([1,dim-1],[1-2*fac,1-2*fac],'k',linewidth=4)
plt.plot([1,dim-1],[dim-1+2*fac,dim-1+2*fac],'k',linewidth=4)
plt.plot([dim-1+2*fac,dim-1+2*fac],[1,dim-1],'k',linewidth=4)
plt.plot([1-2*fac,1-2*fac],[1,dim-1],'k',linewidth=4)



Particule=[]
for i in range(nbpart):
    Particule.append([rd.random()*(dim-2)+1,rd.random()*(bordureh2-2)+1,rd.randint(-180,180)])
x=[e[0] for e in Particule]
y=[e[1] for e in Particule]
line.set_data([x],[y])

    
def bouge(i,lst,nb,nb2):
    
    for elem in lst:
        
        dir=elem[2]
        x=elem[0]
        y=elem[1]
        if  (y>vlim1 and y>vlim2) or (y<vlim1 and y<vlim2) or (y<bordureh2 and y>bordureh1 and not(x>bordurev1 and x<bordurev2)):
            elem[2]=(180-dir)
            elem[0]-=sin(radians(180-dir))*fac
            elem[1]+=cos(radians(180-dir))*fac
        elif (x>hlim1 and x>hlim2) or (x<hlim1 and x<hlim2):
            elem[2]=-dir
            elem[0]-=sin(radians(-dir))*fac
            elem[1]+=cos(radians(-dir))*fac
        else:
            elem[0]-=sin(radians(dir))*fac
            elem[1]+=cos(radians(dir))*fac
        
    x=[]
    y=[]
    for e in lst:
        x.append(e[0])
        y.append(e[1])
        if e[1]>bordureh2:
            nb+=1
        else:
            nb2+=1
    haut.append(nb)
    bas.append(nb2)
    
    texte.set_text(nb/float(nbpart)*100)
    texte2.set_text(nb2/float(nbpart)*100)
    line.set_data([x],[y])





anim = animation.FuncAnimation(fig, bouge, fargs=([Particule,0,0]),
                                interval=1, blit=False)
plt.show()
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import acos, asin,cos,sin, pi
from matplotlib.widgets import Slider, Button, RadioButtons

#michelson interferometer simulator
a=0.00

def lum(a,I,lamb,D,x):
    return 2*I*(1+cos(2*pi/(lamb)*a*D/(D**2+x**2)**0.5))

def tablum(tab,dim,a,I,lamb,D,scale):

    for i in range(dim):
        for j in range(dim):
            x=((-dim//2+i)**2+(-dim/2+j)**2)**0.5*scale
            tab[i,j]=[lum(a,I,lamb,D,x)/4/I,0,0]
    return tab

    
    
I=0.25
lamb=600*10**(-9)
D=2
dim=60
scale=1/10/dim
faca=1/1000
fig, ax = plt.subplots(ncols=2)
plt.subplots_adjust(bottom=0.25)
k=np.linspace(-1.4*(dim/2)*scale,1.4*(dim/2)*scale,1000)
ligne=ax[0].plot(k,[lum(a*faca,I,lamb,D,x) for x in k])
ax[0].set_xlim([-1.4*(dim/2)*scale,1.4*(dim/2)*scale])
ax[0].set_ylim([-0.2, 4*I+0.2])
axcolor = 'lightgoldenrodyellow'
axa = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
sa = Slider(axa, 'a (mm)', -3, 3, valinit=0.00)
tab=np.zeros((dim,dim,3))
tablum(tab,dim,a*faca,I,lamb,D,scale)

im=ax[1].imshow(tab)


def update(val):
    a=sa.val
    ligne[0].set_data(k,[lum(a*faca,I,lamb,D,x) for x in k])
    im.set_data(tablum(tab,dim,a*faca,I,lamb,D,scale))
sa.on_changed(update)

plt.show()


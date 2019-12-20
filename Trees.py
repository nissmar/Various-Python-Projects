import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import acos, asin,cos,sin
from matplotlib.widgets import Slider, Button, RadioButtons

alpha=0.9
r=0.7

class Arbre:
    def __init__(self,x0,y0,x1,y1):
        self.segment=[[x0,y0],[x1,y1]]
        self.abs=[x0,x1]
        self.ord=[y0,y1]
        self.longueur=((x1-x0)**2+(y1-y0)**2)**0.5
        def signe(a):
            if a>=0:
                return 1
            return -1
        self.angle=acos((x1-x0)/(self.longueur))*signe(y1-y0)
    def suivant(self,alpha,r):
        x0,y0=self.segment[1]
        x3=x0+r*(self.longueur)*cos(self.angle-alpha)
        y3=y0+r*(self.longueur)*sin(self.angle-alpha)
        x2=x0+r*(self.longueur)*cos(self.angle+alpha)
        y2=y0+r*(self.longueur)*sin(self.angle+alpha)
        return Arbre(x0,y0,x2,y2), Arbre(x0,y0,x3,y3)
    
    
def develop(n,A,alpha,r):
    if n>=1:
        c,d=Arbre.suivant(A,alpha,r)
        return develop(n-1,c,alpha,r)+develop(n-1,d,alpha,r)+[A]
    return []

def affiche(n,alpha,r):
    L=develop(n,Arbre(0,0,0,1),alpha,r)
    for l in L:
        plt.plot(l.abs,l.ord,'b')
    plt.show()

def affiche(n):

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    arbres=develop(n,Arbre(0,0,0,1),alpha,r)
    lignes=[ax.plot(A.abs,A.ord,'b') for A in arbres]
    
    plt.axis([-3, 3, 0, 3.5])
    
    axcolor = 'lightgoldenrodyellow'
    axr = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    axalpha = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
    salpha = Slider(axalpha, 'alpha', 0, 1.57, valinit=0.9)
    sr = Slider(axr, 'r', 0.1,0.9, valinit=0.7)
    
    
    def update(val):
        r = sr.val
        alpha = salpha.val
        # print(r,alpha)
        for l,A in zip(lignes,develop(n,Arbre(0,0,0,1),alpha,r)):
            l[0].set_data(A.abs,A.ord)
            fig.canvas.draw_idle()
    sr.on_changed(update)
    salpha.on_changed(update)
    
    plt.show()

affiche(8)
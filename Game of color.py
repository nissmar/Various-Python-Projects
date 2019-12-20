import matplotlib.pyplot as plt
import numpy as np
import random as rd
import matplotlib.widgets as mw
import time

global dim, nbcouleurs
dim=10
nbcouleurs = 3


class Tab():
    def __init__(self,n,nbcoul,AX,Cmap):
        self.cmap=plt.get_cmap(Cmap)
        self.ax=AX
        Lcoul=[k for k in range(nbcoul)]
        self.tab=np.random.choice(Lcoul,(n,n))
        self.zone=[[0,0]]
        self.front=[[0,0]]
        self.nbcoul=nbcoul
        self.dim=n
        self.im=ax.imshow(self.tab,cmap=Cmap)
        self.boutons=[mw.Button(plt.axes([0.25+0.5*k/(nbcoul-1),0.15,0.05,0.05]),"",color=self.cmap(k/(nbcoul-1))[0:3],hovercolor=self.cmap(k/(nbcoul-1))[0:3]) for k in range(nbcoul)]
        self.adjacent(self.tab[0,0])
        self.update()
        
    def reset(self,event):
        Lcoul=[k for k in range(self.nbcoul)]
        self.tab=np.random.choice(Lcoul,(self.dim,self.dim))
        self.zone=[[0,0]]
        self.front=[[0,0]]
        self.update()
        
        
    def adjacent(self,coul): #etend la zone à la nouvelle couleur
        print(coul)
        avoir=self.front[:]
        avoir2=[]
        for elem in self.zone:
            x,y=elem
            self.tab[x,y]=coul
        while avoir!=[]:
            avoir2[:]=[]
            for elem1 in avoir:

                x,y=elem1
                for elem in [[x-1,y],[x,y+1],[x,y-1],[x+1,y]]:
                    i,j=elem
                    if 0<=i<self.dim and 0<=j<self.dim and not([i,j] in self.zone) and not([i,j] in avoir2) and self.tab[i,j]==coul:
                        avoir2.append([i,j])
            avoir[:]=avoir2
            self.zone+=avoir
            self.front+=avoir
        newfront=[]
        for elem in self.front:
            i,j=elem
            if not([i+1,j] in self.zone) or not([i,j+1] in self.zone) or not([i-1,j] in self.zone) or not([i,j-1] in self.zone):
                newfront.append([i,j])
        self.front[:]=newfront
        self.update()
                
    def solveseul(self):
        k=0
        while len(self.zone)!=self.dim*self.dim:
            k+=1
            k=k%self.nbcoul
            self.adjacent(k)
            
    def update(self):
        self.im.set_data(self.tab)
        self.im.axes.figure.canvas.draw()


fig,ax=plt.subplots()
plt.subplots_adjust(bottom=0.25)

     

t=Tab(dim,4,ax,'terrain')  #'viridis','terrain','plasma','inferno','magma'
reset=mw.Button(plt.axes([0.49,0.07,0.07,0.04]),"reset")
reset.on_clicked(t.reset)
for k in range(len(t.boutons)):
    t.boutons[k].on_clicked(lambda event, k=k : t.adjacent(k))
plt.show()

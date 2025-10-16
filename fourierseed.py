import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import random as rnd
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

class Fourierpicture:
    def __init__(self,sym=5,len=10,dec=np.sqrt,n=10000,color="k"):
        self.s=sym
        self.l=len
        self.dec=dec
        self.seed=None
        self.n=n
        self.arr=[1]*self.l
        self.f= lambda t:1
        self.x=[0]
        self.y=[0]
        self.color=color
        self.fig = plt.figure(figsize=(10,10),dpi=100)
        self.plot = self.fig.add_subplot()
        self.plot.axis("off")

    def makearray(self):
        if self.seed!=None:
            rnd.seed(self.seed)
        arr=[]
        for i in range(self.l):
            re = rnd.random()-self.dec(i)
            im = rnd.random()*np.pi*2
            arr.append(re+1j*im)
        self.arr= arr

    def fourier(self):
        #creates a fourier sum with coefficients exp(a) for a in arr
        #s is symmetry order, ie only consider exp(1+i*s)
        self.f =  lambda t: sum([np.exp(self.arr[i])*np.exp((1+i*self.s)*1j*t) for i in range(self.l)])

    def makeplot(self):
        res=np.array([self.f(2*np.pi*t/self.n) for t in range(self.n+1)])
        self.x=res.real
        self.y=res.imag
        self.plot.cla()
        self.plot.axis("off")
        self.plot.plot(self.x,self.y,self.color)

    def addCanvas(self,frame):
        self.canvas= FigureCanvasTkAgg(self.fig,master=frame)
        self.canvas.get_tk_widget().pack()

    def showplot(self):
        self.canvas.draw()

    def doall(self):
        self.makearray()
        self.fourier()
        self.makeplot()
        self.showplot()


fourier = Fourierpicture()
window = Tk()
f1 = Frame(window)
f2 = Frame(window)
f1.grid(row=0,column=0,sticky="nsew")
f2.grid(row=0,column=1,sticky="nsew")
window.title("Fourier Pictures")
window.geometry("1000x1000")
fourier.addCanvas(f2)


doall_button = Button(f1,command=fourier.doall,text="Plot")
doall_button.pack()

enter_sym = Entry(f1,width=5)
enter_sym.pack()
def setsym():
    fourier.s=int(enter_sym.get())
setsym_button = Button(f1,command=setsym,text="Set Symmetry")
setsym_button.pack()

enter_len = Entry(f1,width=5)
enter_len.pack()
def setlen():
    fourier.l=int(enter_len.get())
setlen_button = Button(f1,command=setlen,text="Set Detail")
setlen_button.pack()

enter_seed = Entry(f1,width=15)
enter_seed.pack()
def setseed():
    ent=enter_seed.get()
    if ent=="":
        fourier.seed=None
    else:
        fourier.seed=ent
    print(fourier.seed)
setseed_button = Button(f1,command=setseed,text="Set Seed")
setseed_button.pack()



window.mainloop()

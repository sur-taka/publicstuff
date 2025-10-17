import numpy as np
from matplotlib import pyplot as plt
import random as rnd
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        self.file="pic.png"
        self.enter_seed=None

    def makearray(self):
        seed=None
        if self.seed!=None:
            seed=self.seed
        else:
            seed=str(rnd.random())
        rnd.seed(seed)
        self.enter_seed.delete(0)
        self.enter_seed.insert(0,seed)
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

    def save(self):
        self.fig.savefig(self.file, transparent=True)


fourier = Fourierpicture()
fourier.plot.set_facecolor((1,1,1))
window = Tk()
f1 = Frame(window)
f2 = Frame(window)
f1.grid(row=0,column=0,sticky="nsew")
f2.grid(row=0,column=1,sticky="nsew")
window.title("Fourier Pictures")
window.geometry("1000x1000")
fourier.addCanvas(f2)

def _quit():
    window.quit()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", _quit)


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
fourier.enter_seed=enter_seed
def setseed():
    ent=enter_seed.get()
    if ent=="":
        fourier.seed=None
    else:
        fourier.seed=ent
setseed_button = Button(f1,command=setseed,text="Set Seed")
setseed_button.pack()

choose_color = ttk.Combobox(f1)
choose_color['values'] = ("Black","White","Red","Blue","Green","Yellow","Cyan","Magenta")
choose_color.current(0)
choose_color.pack()
colors=["k","w","r","b","g","y","c","m"]
def setcolor(e):
    cur=choose_color.current()
    fourier.color=colors[cur]
choose_color.bind("<<ComboboxSelected>>",setcolor)

enter_file = Entry(f1,width=15)
enter_file.pack()
def setfile():
    fourier.file=enter_file.get()+".png"
setfile_button = Button(f1,command=setfile,text="Set File")
setfile_button.pack()

save_button = Button(f1,command=fourier.save,text="Save")
save_button.pack()



window.mainloop()

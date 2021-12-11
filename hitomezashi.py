from tkinter import *
import random as ran


class Patternrc:
    def __init__(self,length):
        self.length = length
        self.lst =[True]*length
    def set(self,start,onl,offl):
        pl = onl+offl
        if start:
            for i in range(self.length):
                if (i%pl<onl):
                    self.lst[i] = True
                else:
                    self.lst[i] = False
        else:
            for i in range(self.length):
                if (i%pl<offl):
                    self.lst[i] = False
                else:
                    self.lst[i] = True

class Pattern:
    def __init__(self,w=20,h=20,onl=1,offl=1,s=0,dl=10,pon=0.5):
        self.w=w
        self.h=h
        self.onl=onl
        self.offl=offl
        self.pl= onl+offl
        self.cs = [True]*self.w
        self.rs = [True]*self.h
        self.s= s
        self.dl = dl
        self.pon = pon
        self.rows=[]
        for i in range(self.h-1):
            self.rows.append(Patternrc(self.w))
        self.cols=[]
        for i in range(self.w-1):
            self.cols.append(Patternrc(self.h))

    def sethw(self,h,w):
        self.h=h
        self.w = w
        self.rows=[]
        for i in range(self.h-1):
            self.rows.append(Patternrc(self.w))
        self.cols=[]
        for i in range(self.w-1):
            self.cols.append(Patternrc(self.h))
        self.cs = [True]*self.w
        self.rs = [True]*self.h


    def setprob(self,pon):
        self.pon=pon

    def randomstarts(self):
        ran.seed(self.s)
        for i in range(self.h-1):
            r = ran.random()
            self.rs[i] = (r<self.pon)
        for i in range(self.w-1):
            r = ran.random()
            self.cs[i] = (r<self.pon)

    def setpattern(self):
        for i in range(self.h-1):
            self.rows[i].set(self.rs[i],self.onl,self.offl)
        for i in range(self.w-1):
            self.cols[i].set(self.cs[i],self.onl,self.offl)

    def printpattern(self):
        for i in range(self.h-1):
            print(self.rows[i].lst)
        for i in range(self.w-1):
            print(self.cols[i].lst)

    def drawpat(self,canv):
        canv.delete("all")
        d = self.dl
        for i in range(self.h-1):
            for j in range(self.w):
                b = self.rows[i].lst[j]
                if b:
                    canv.create_line(d*j,d*(i+1),d*(j+1),d*(i+1))
        for i in range(self.w-1):
            for j in range(self.h):
                if self.cols[i].lst[j]:
                    canv.create_line(d*(i+1),d*j,d*(i+1),d*(j+1))


p = Pattern()
root = Tk()
Label(root, text="Height").grid(row=1)
Label(root, text="Width").grid(row=0)
Label(root, text="On Length").grid(row=2)
Label(root, text="Off Length").grid(row=3)
Label(root, text="Seed").grid(row=4)
Label(root, text="Probability on").grid(row=5)

enw = Entry(root)
enw.insert(10,"20")
enh = Entry(root)
enh.insert(10,"20")
enon = Entry(root)
enon.insert(10,"1")
enoff = Entry(root)
enoff.insert(10,"1")
enseed = Entry(root)
enseed.insert(10, "0")
enprob = Entry(root)
enprob.insert(10,"0.5")
enw.grid(row=0,column=1)
enh.grid(row=1,column=1)
enon.grid(row=2,column=1)
enoff.grid(row=3,column=1)
enseed.grid(row=4,column=1)
enprob.grid(row=5,column=1)


cw = 200
ch = 200

c = Canvas(root,width = cw, height = ch)
c.grid(row=7)

def sethw():
    p.sethw(int(enh.get()),int(enw.get()))
    c.config(width=p.w*p.dl,height=p.h*p.dl)
def setonoff():
    p.onl = int(enon.get())
    p.offl = int(enoff.get())
def setseed():
    p.s = int(enseed.get())
def rand():
    p.randomstarts()
    p.setpattern()
    #p.printpattern()
def drawcanv():
    p.drawpat(c)
def setprob2():
    p.setprob(float(enprob.get()))



buthw = Button(root,text="Set Height/Width", command=sethw)
butonoff = Button(root, text= "Set On/Off Length", command=setonoff)
butseed = Button(root, text = "Set Seed", command=setseed)
butrand = Button(root, text= "Randomize Starts", command = rand)
butdraw = Button(root, text= "Draw", command=drawcanv)
butprob = Button(root, text= "Set Probability", command=setprob2)
buthw.grid(row=0,column=2)
butonoff.grid(row=2,column=2)
butseed.grid(row=4,column=2)
butprob.grid(row=5,column=2)
butrand.grid(row=6)
butdraw.grid(row=6,column=1)



root.mainloop()

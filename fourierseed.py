import numpy as np
from matplotlib import pyplot as plt
import random as rnd


def fourier(arr,s):
#creates a fourier sum with coefficients exp(a) for a in arr
#s is symmetry, ie only consider exp(1+i*s)
    l=len(arr)
    return lambda t: sum([np.exp(arr[i])*np.exp((1+i*s)*1j*t) for i in range(l)])

def makeplot(f,n,fname=None):
#plots a 2pi periodic function f with n steps
    res=np.array([f(2*np.pi*t/n) for t in range(n+1)])
    x=res.real
    y=res.imag
    plt.figure(figsize=(10,10),dpi=100)
    plt.plot(x,y,"k")
    plt.axis("off")
    if fname==None:
        plt.savefig("pic.png")
    else:
        plt.savefig(fname)
    plt.close()

def makerandomarr(seed=None,dec=np.sqrt,l=None):
#creates a random array of complex numbers from a seed
#real part is random(0,1)-dec(i) , imaginary part is random(0,2pi)
    rnd.seed(seed)
    if l==None:
        l = rnd.choice(range(10,20))
    arr=[]
    for i in range(l):
        re = rnd.random()-dec(i)
        im = rnd.random()*np.pi*2
        arr.append(re+1j*im)
    return arr

n=10000

for s in range(5,10):
    for l in range(10,20):
        for i in range(5):
            fname="picture_"+str(s)+"_"+str(l)+"_"+str(i)
            arr=makerandomarr(l=l)
            f=fourier(arr,s=s)
            makeplot(f,n,fname=fname)

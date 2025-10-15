import numpy as np
from matplotlib import pyplot as plt
import random as rnd

def fourier(arr,s):
#creates a fourier sum with coefficients exp(a) for a in arr
#s is symmetry, ie only consider exp(1+i*s)
    l=len(arr)
    return lambda t: sum([np.exp(arr[i])*np.exp((1+i*s)*1j*t) for i in range(l)])

def makeplot(f,n):
#plots a 2pi periodic function f with n steps
    res=np.array([f(2*np.pi*t/n) for t in range(n+1)])
    x=res.real
    y=res.imag
    plt.plot(x,y)
    plt.show()

def makerandomarr(seed=None,dec=np.sqrt):
#creates a random array of complex numbers from a seed
#real part is random(0,1)-dec(i) , imaginary part is random(0,2pi)
    rnd.seed(seed)
    l = rnd.choice([5,6,7,8,9])
    arr=[]
    for i in range(l):
        re = rnd.random()-dec(i)
        im = rnd.random()*np.pi*2
        arr.append(re+1j*im)
    return arr

n=10000
l=20
s=7
arr=makerandomarr("dagmar")
f= fourier(arr,s)
makeplot(f,n)

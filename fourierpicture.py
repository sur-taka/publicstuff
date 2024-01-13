import numpy as np
from matplotlib import pyplot  as plt

def strtonum(w,m):
    r=[]
    for c in w:
        n=ord(c)-96
        a=n//m-n//2
        b=n%m-m//2
        r.append(a+b*1j)
    return r

def fourier(arr,k):
    l=len(arr)
    return lambda t: sum([arr[i]/(i+1)**k*np.exp((1+l*i)*1j*t) for i in range(l)])



def makeplot(s,k,m):
    for w in s:
        arr=strtonum(w,m)
        f=fourier(arr,k)
        res=np.array([f(2*np.pi*t/n) for t in range(n+1)])
        x=res.real
        y=res.imag
        plt.plot(x,y)
    plt.show()

k=1
m=5
n=1000

running=True
while running:
    s= input().split(" ")
    match s[0]:
        case "quit":
            running=False
            continue
        case "setk":
            k= int(s[1])
            continue
        case "setm":
            m= int(s[1])
            continue
        case "setn":
            n= int(s[1])
            continue
    makeplot(s,k,m)

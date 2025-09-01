from matplotlib import pyplot as plt
import numpy as np

pi=np.pi
phi=(1+5**.5)/2
NN=3000

def ctoi(c):
	return ord(c)-96
	
def scaletoi(x1,r,l):
	return x1/r*l

def mod(x1,m):
	while x1<0:
		x1+=m
	while x1>=m:
		x1-=m
	return x1
	
def makecoeff(xx,r,m,f,n):
	c=scaletoi(xx,r,m)
	res=[]
	while len(res)<n:
		c=mod((c+m)*f,m)
		res.append(c)
	return res
	
def makecoeffcomplex(ch,r1,r2,m1,m2,f1,f2,n):
	x1=ctoi(ch)
	a=makecoeff(x1,r1,m1,f1,n)
	b=makecoeff(x1,r2,m2,f2,n)
	res=[np.exp(-m1*(k+2)-a[k]+1.j*b[k]) for k in range(n)]
	return [1]+res
	
def wordtocoeff(w,m,f,sc):
	n=len(w)
	res=[]
	for i in range(n):
		c=w[i]
		n=ctoi(c)
		a=n%m
		b=n//m
		res.append(1/(sc)**(i)*(a+b*1j))
	return res
		
	

def fourier(coeff,period):
	l=len(coeff)
	return lambda t : sum([coeff[i]*np.exp(2*pi*1.j*(1+i*period)*t) for i in range(l)])
	
def fourierpoints(coeff,period, N):
	f= fourier(coeff,period)
	points = [f(i/N) for i in range(N+1)]
	return points

cc='d'

def makeplot2(w,N,period,sc,width,col,m):
	coef=wordtocoeff(w,m,phi+1,sc)
	pointse=fourierpoints(coef,period,NN)
	x=[p.real for p in pointse]
	y=[p.imag for p in pointse]
	plt.plot(x,y,linewidth=width,color=col)
	plt.show()

def makeplot(w,n,N,period,sc):
	count=0
	for cc in w:
		coef= makecoeffcomplex(cc,26,26,.5,2*pi,phi,phi,n)
		coef=[sc**count*z for z in coef]
		pointse=fourierpoints(coef,period,NN)
		x=[p.real for p in pointse]
		y=[p.imag for p in pointse]
		plt.plot(x,y)
		count-=1
	plt.show()
	plt.savefig(w)
	
w='saire'
w1='artur'

per=7
scale=1.5
sc=1.5
nn=4
wid=3
co='red'
#makeplot(w,nn,NN,per,scale)
makeplot2(w1,NN,per,sc,wid,co,5)
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Run 'python ode.py 0 0.8 100 0.001' to reproduce my work

# Parts 1 and 2 Variables

x0=float(sys.argv[1]) #initial position 
v0=float(sys.argv[2]) #initial velocity 
t0=0 
T=float(sys.argv[3]) # maximum time in seconds
h0=float(sys.argv[4]) # length of time steps in seconds
N=int(T/h0) # number of time steps

numHVal=5
xErrorMax=np.zeros(numHVal)
xErrorMaxIm=np.zeros(numHVal)

# Assignment Part 1

def xExVal(xi,vi,h):
    return xi+h*vi
def vExVal(xi,vi,h):
    return vi-h*xi   
def xImVal(xi,vi,h):
    return (xi+h*vi)/(1+h**2)
def vImVal(xi,vi,h):
    return (vi-h*xi)/(1+h**2) 
     
def iterate(h):
    t=np.zeros(N)    
    t[0]=t0
    xEx=np.zeros(N)
    xEx[0]=x0
    vEx=np.zeros(N)
    vEx[0]=v0
    xIm=np.zeros(N)
    xIm[0]=x0
    vIm=np.zeros(N)
    vIm[0]=v0
    for i in range(1,N):
        xEx[i]=xExVal(xEx[i-1],vEx[i-1],h)
        vEx[i]=vExVal(xEx[i-1],vEx[i-1],h)
        t[i]=t0+i*h
        xIm[i]=xImVal(xIm[i-1],vIm[i-1],h)
        vIm[i]=vImVal(xIm[i-1],vIm[i-1],h)
    return (t, xEx, vEx, xIm, vIm)
    
def vstimePlots(t,xEx,vEx):
    plt.figure(figsize=(7,5))
    plt.title('Explicit Euler Method')
    plt.subplot(221)
    plt.plot(t,xEx,'r-')
    plt.xlabel('time (t)')
    plt.ylabel('x(t)')
    plt.subplot(222)
    plt.plot(t,vEx,'r-')
    plt.xlabel('time (t)')
    plt.ylabel('v(t)')
    plt.subplot(223)
    xError=x0*np.cos(t)+v0*np.sin(t)-xEx
    plt.plot(t,xError,'m-')
    plt.xlabel('time (t)')
    plt.ylabel(r'$x_{analytic}(t)-x(t)$')
    plt.subplot(224)
    yError=-x0*np.sin(t)+v0*np.cos(t)-vEx
    plt.plot(t,yError,'m-')
    plt.xlabel('time (t)')
    plt.ylabel(r'$v_{analytic}(t)-v(t)$')

def energyPlot(t,xEx,vEx):
    plt.figure(figsize=(7,5))
    plt.title('Explicit Euler Method')
    plt.subplot(311)
    eEx=np.power(xEx,2)+np.power(vEx,2)
    plt.plot(t,eEx,'r-')
    plt.xlabel('time (t)')
    plt.ylabel('total energy (E(t))')    
    plt.subplot(312)
    eAn = np.power(x0*np.cos(t) + v0*np.sin(t),2) + np.power(-x0*np.sin(t) + v0*np.cos(t),2)
    plt.plot(t,eAn,'b-')
    plt.xlabel('time (t)')
    plt.ylabel(r'$E_{analytic}(t)$')
    plt.subplot(313)
    plt.plot(t,eAn-eEx,'m-')
    plt.xlabel('time (t)')
    plt.ylabel(r'$E_{analytic}(t)-E(t)$')

def errorPlot():
    plt.figure(figsize=(7,5))
    plt.title('Explicit Euler Method')
    for i in range(numHVal):
        itFuncs=iterate(h0/(2**i))
        xErrorMax[i]=np.amax(x0*np.cos(itFuncs[0])+v0*np.sin(itFuncs[0]) - itFuncs[1])
    plt.plot(h0/2**np.arange(0,numHVal),xErrorMax,'mo-')
    plt.xlabel('h')
    plt.ylabel(r'$max(x_{analytic}(t)-x(t))$')

def implicitPlot(t,xIm,vIm):
    plt.figure(figsize=(7,5))
    plt.title('Implicit Euler Method')
    plt.subplot(221)
    plt.plot(t,xIm,'r-')
    plt.xlabel('time (t)')
    plt.ylabel('x(t)')
    plt.subplot(222)
    plt.plot(t,vIm,'r-')
    plt.xlabel('time (t)')
    plt.ylabel('v(t)')
    plt.subplot(223)
    xError=x0*np.cos(t)+v0*np.sin(t)-xIm
    plt.plot(t,xError,'m-')
    plt.xlabel('time (t)')
    plt.ylabel(r'$x_{analytic}(t)-x(t)$')
    plt.subplot(224)
    yError=-x0*np.sin(t)+v0*np.cos(t)-vIm
    plt.plot(t,yError,'m-')
    plt.xlabel('time (t)')
    plt.ylabel(r'$y_{analytic}(t)-y(t)$')   
  
def energyImplicitPlot(t,xIm,vIm):
    plt.figure(figsize=(7,5))
    plt.title('Implicit Euler Method')
    plt.subplot(311)
    eIm=np.power(xIm,2)+np.power(vIm,2)
    plt.plot(t,eIm,'r-')
    plt.xlabel('time (t)')
    plt.ylabel('total energy (E(t))')    
    plt.subplot(312)
    eAn = np.power(x0*np.cos(t) + v0*np.sin(t),2) + np.power(-x0*np.sin(t) + v0*np.cos(t),2)
    plt.plot(t,eAn,'b-')
    plt.xlabel('time (t)')
    plt.ylabel(r'$E_{analytic}(t)$')
    plt.subplot(313)
    plt.plot(t,eAn-eIm,'m-')
    plt.xlabel('time (t)')
    plt.ylabel(r'$E_{analytic}(t)-E(t)$') 
     
def errorImplicitPlot():
    plt.figure(figsize=(7,5))
    plt.title('Implicit Euler Method')
    for i in range(numHVal):
        itFuncs=iterate(h0/(2**i))
        xErrorMaxIm[i] = np.amax(x0*np.cos(itFuncs[0]) + v0*np.sin(itFuncs[0]) - itFuncs[3])
    plt.plot(h0/2**np.arange(0,numHVal),xErrorMaxIm,'mo-')
    plt.xlabel('h')
    plt.ylabel(r'$max(x_{analytic}(t)-x(t))$')

# Assignment Part 2
def iterateSym(h):
    xSym=np.zeros(N)
    xSym[0]=x0
    vSym=np.zeros(N)
    vSym[0]=v0
    for i in range(1,N):
        xSym[i]=xExVal(xSym[i-1],vSym[i-1],h)
        vSym[i]=vExVal(xSym[i],vSym[i-1],h)
    return (xSym, vSym)
    
def phaseSpace(xEx,vEx,xIm,vIm,xSym,vSym):
    gs=GridSpec(14,14)
    plt.figure(figsize=(7,5))
    plt.subplot(gs[0:4,0:4])
    plt.plot(xEx,vEx,'r-',linewidth=0.2)
    plt.xlabel(r'$x_{explicit}(t)$')
    plt.ylabel(r'$v_{explicit}(t)$')
    plt.subplot(gs[0:4,5:9])
    plt.plot(xSym,vSym,'b-',linewidth=0.2)
    plt.xlabel(r'$x_{symplectic}(t)$')
    plt.ylabel(r'$v_{symplectic}(t)$')
    plt.subplot(gs[0:4,10:14])
    plt.plot(xIm,vIm,'r-',linewidth=0.2)
    plt.xlabel(r'$x_{implicit}(t)$')
    plt.ylabel(r'$v_{implicit}(t)$')
    plt.subplot(gs[6:14,0:6])
    plt.plot(xSym-xEx,vSym-vEx,'m-',linewidth=1)
    plt.xlabel(r'$x_{symplectic}(t)-x_{explicit}(t)$')
    plt.ylabel(r'$v_{symplectic}(t)-v_{explicit}(t)$')  
    plt.subplot(gs[6:14,8:14])
    plt.plot(xSym-xIm,vSym-vIm,'m-',linewidth=1)
    plt.xlabel(r'$x_{symplectic}(t)-x_{implicit}(t)$')
    plt.ylabel(r'$v_{symplectic}(t)-v_{implicit}(t)$')

def energySymplecticPlot(t,xSym,vSym):
    plt.figure(figsize=(7,5))
    plt.title('Symplectic Euler Method')
    plt.plot(t,np.power(xSym,2)+np.power(vSym,2),'r-')
    plt.xlabel('time (t)')
    plt.ylabel('total energy (E)')
    
def vSymPlot(t,vSym):
    plt.figure(figsize=(7,5))
    plt.plot(t,vSym,'r-',label='Symplectic')
    plt.plot(t,-x0*np.sin(t)+v0*np.cos(t),'b--',label='Exact')
    plt.xlabel('time(t)')
    plt.ylabel('v(t)')
    plt.legend()

#Parts 1 and 2 Plotting

iterFunc=iterate(h0)
vstimePlots(iterFunc[0],iterFunc[1],iterFunc[2])
energyPlot(iterFunc[0],iterFunc[1],iterFunc[2])
errorPlot()
iterFunc=iterate(h0)
implicitPlot(iterFunc[0],iterFunc[3],iterFunc[4])
energyImplicitPlot(iterFunc[0],iterFunc[3],iterFunc[4])
errorImplicitPlot()
iterFunc=iterate(h0)
iterSymFunc=iterateSym(h0)
phaseSpace(iterFunc[1],iterFunc[2],iterFunc[3],iterFunc[4],iterSymFunc[0],iterSymFunc[1])
energySymplecticPlot(iterFunc[0],iterSymFunc[0],iterSymFunc[1])
vSymPlot(iterFunc[0],iterSymFunc[1])
plt.show() 
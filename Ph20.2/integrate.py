import sys
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

func = lambda x: np.e**x # define the function

a=int(sys.argv[1])
b=int(sys.argv[2])
N=int(sys.argv[3])
acc=float(sys.argv[4])

def trapInt(func,a,b,N):
    hN=(b - a)/N
    tempInt=np.append([hN*(func(a))/2],hN*func(a+hN*np.arange(1,N,dtype=float)))
    intgrl = np.append([tempInt],[hN*(func(b))/2])
    return np.sum(intgrl)
    
def simpInt(func,a,b,N):
    hN=(b - a)/(N-1)
    const=np.empty(N-2,)
    const[::2]=4/3
    const[1::2]=2/3
    tempInt = np.append([hN*(func(a))/3],hN*const*func(a+hN*np.arange(1,N-1,dtype=float)))
    intgrl = np.append([tempInt],[hN*(func(b))/3])  
    #print(np.sum(intgrl))
    return np.sum(intgrl)
    
def quadInt(func,a,b):
    #print (integrate.quad(func,a,b))
    return integrate.quad(func,a,b)
    
def rombergInt(func,a,b):
    #print (integrate.romberg(func,a,b))
    return integrate.romberg(func,a,b)
    
def convPlot(func,a,b,N,acc):
    nVal=(np.round((np.logspace(0.2,np.log10(N),1000)),0)).astype(int)
    traps=[]
    simps=[]
    #print(nVal)
    for i in nVal:
        traps.append(trapInt(func,a,b,i))
    #print(traps)
    plt.plot(nVal,abs(np.array(traps)-(np.e-1)),'r.-',label='Trapezoidal')
    plt.plot(nVal,np.power(nVal,-2.0),'m-',label='1/N^2')
    for i in nVal:
        ip=2*i+1
        simps.append(simpInt(func,a,b,ip))
    #print(simps)
    plt.plot(nVal,abs(np.array(simps)-(np.e-1)),'b.-',label='Simpson\'s')
    plt.plot(nVal,np.power(nVal,-4.0),'c-',label='1/N^4')
    plt.xlabel('Number of subintervals (N)')
    plt.ylabel(r'$\int_{'+str(a)+'}^{'+str(b)+'} f(x)$')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()

    
def simpAcc(func,a,b,N,acc):
    goal=0 # when 0, the accuracy requested has not been reached            
    k=-1
    while(goal == 0):
        k=k+1
        accInt = np.abs((simpInt(func,a,b,(2**k)*N)-simpInt(func,a,b,(2**(k+1))*N))/(simpInt(func,a,b,(2**k)*N)))
        if accInt <=acc:
            goal = 1
    return (simpInt(func,a,b,(2**k)*N), k)

print('Function: '+'e**x'+', a = '+str(a)+', b = '+str(b)+', N = '+str(N)+', accuracy = '+str(acc))    
print('Extended Trapezoidal Approximation: '+str(trapInt(func,a,b,N)))
print('Extended Simpson\'s Approximation: '+str(simpInt(func,a,b,N)))
print('Quad Integration: '+str((quadInt(func,a,b))[0]))
print('Romberg Integrations: '+str(rombergInt(func,a,b)))
accTup=(simpAcc(func,a,b,N,acc))
print('Integration to '+str(acc)+ ' accuracy: '+ str(accTup[0])+', k = '+str(accTup[1])+', N_0 = '+str(N))
convPlot(func,a,b,N,acc)

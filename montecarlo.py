import random
import matplotlib.pyplot as plt
import numpy as np
import math

k=10

#random congruencia lineal
def random1( x0, a, b, m):
    aux=(a*x0 + b) % m;
    return aux

#random Secuencia de Halton
def next_prime():
    def is_prime(num):
        "Checks if num is a prime value"
        for i in range(2,int(num**0.5)+1):
            if(num % i)==0: return False
        return True

    prime = 3
    while(1):
        if is_prime(prime):
            yield prime
        prime += 2

def vdc(n, base=2):
    vdc, denom = 0, 1
    while n:
        denom *= base
        n, remainder = divmod(n, base)
        vdc += remainder/float(denom)
    return vdc

def halton_sequence(size, dim):
    seq = []
    primeGen = next_prime()
    next(primeGen)
    for d in range(dim):
        base = next(primeGen)
        seq.append([vdc(i, base) for i in range(size)])
    return seq

#random libreria
def random3():
    x=np.random.uniform(-1,1)
    y=np.random.uniform(-1,1)
    rad=math.sqrt((x**2)+(y**2))

    return x,y,rad

#Congruencia lineal
cont=0
xs=np.array([])
ys=np.array([])
xn=np.array([])
yn=np.array([])
vpi=np.array([])
pi=0.1
x0=3
for i in range(1,k):
    #x0>=0, a>=0, b>=0, m>=x0 and  m>=a
    a=214013
    b=2531011
    m=2**32
    x=(random1(x0,a,b,m))*random.choice((-1,1))
    x0=x
    y=(random1(x0,a,b,m))*random.choice((-1,1))
    rad=math.sqrt(((x/(m-1))**2)+((y/(m-1))**2))
    if rad<=1:
        cont+=1
        xs=np.append(xs,(x/(m-1)))
        ys=np.append(ys,(y/(m-1)))
    else:
        xn=np.append(xn,(x/(m-1)))
        yn=np.append(yn,(y/(m-1)))
    pi=4*cont/i
    vpi=np.append(vpi,pi)
    x0=x

plt.subplot(2,3,1)
plt.title("Congruencia lineal como generador")
plt.scatter(xs,ys)
plt.scatter(xn,yn)
plt.xlim(-1,1)
plt.ylim(-1,1)

plt.subplot(2,3,4)
tit="Grafica de valor de pi estimado:"+str(pi)
plt.title(tit)
plt.plot(vpi,'g')
plt.hlines(y=math.pi,xmin=0,xmax=k)

#Halton sequence
cont=0
xs=np.array([])
ys=np.array([])
xn=np.array([])
yn=np.array([])
vpi=np.array([])
pi=0.1
seq=np.array(halton_sequence(k,2))
for a in range(2):
    for j in range(k):
        seq[a][j]=seq[a][j]*random.choice((-1,1))
for i in range(1,k):
    x=seq[0][i]
    y=seq[1][i]
    rad=math.sqrt((x**2)+(y**2))
    if rad<=1:
        cont+=1
        xs=np.append(xs,x)
        ys=np.append(ys,y)
    else:
        xn=np.append(xn,x)
        yn=np.append(yn,y)
    pi=4*cont/i
    vpi=np.append(vpi,pi)

plt.subplot(2,3,2)
plt.title("Secuencia de Halton como generador")
plt.scatter(xs,ys)
plt.scatter(xn,yn)
plt.xlim(-1,1)
plt.ylim(-1,1)

plt.subplot(2,3,5)
tit="Grafica de valor de pi estimado:"+str(pi)
plt.title(tit)
plt.plot(vpi,'g')
plt.hlines(y=math.pi,xmin=0,xmax=k)

#libreria python
cont=0
xs=np.array([])
ys=np.array([])
xn=np.array([])
yn=np.array([])
vpi=np.array([])
pi=0.1

for i in range(1,k):
    x,y,rad=random3()
    if rad<=1:
        cont+=1
        xs=np.append(xs,x)
        ys=np.append(ys,y)
    else:
        xn=np.append(xn,x)
        yn=np.append(yn,y)
    pi=4*cont/i
    vpi=np.append(vpi,pi)

plt.subplot(2,3,3)
plt.title("Montecarlo generador python")
plt.scatter(xs,ys)
plt.scatter(xn,yn)
plt.xlim(-1,1)
plt.ylim(-1,1)

plt.subplot(2,3,6)
tit="Grafica de valor de pi estimado:"+str(pi)
plt.title(tit)
plt.plot(vpi,'g')
plt.hlines(y=math.pi,xmin=0,xmax=k)

plt.show()
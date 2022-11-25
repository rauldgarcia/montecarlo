import random
import matplotlib.pyplot as plt
import numpy as np
import math

k=100
cont=0

xs=np.array([])
ys=np.array([])
xn=np.array([])
yn=np.array([])
vpi=np.array([])
pi=0.1

#random congruencia lineal
def random1( x0, a, b, m):
    (a*x0 + b) % m
    return (a*x0 + b) % m;


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

#Halton sequence
aux=np.array(halton_sequence(k,2))
print(np.shape(aux))
for i in range(k):
    x=aux[0][k-1]
    y=aux[1][k-1]
    rad=math.sqrt((x**2)+(y**2))
    print(x)
    if rad<=1:
        cont+=1
        xs=np.append(xs,x)
        ys=np.append(ys,y)
    else:
        xn=np.append(xn,x)
        yn=np.append(yn,y)
    oldpi=pi
    pi=4*cont/k
    vpi=np.append(vpi,pi)

print(pi)
plt.subplot(2,3,2)
plt.title("Secuencia de Halton como generador")
plt.scatter(xs,ys)
plt.scatter(xn,yn)

plt.subplot(2,3,5)
plt.title("Grafica de valor de pi estimado")
plt.plot(vpi)

#libreria python
cont=0
xs=np.array([])
ys=np.array([])
xn=np.array([])
yn=np.array([])
vpi=np.array([])
pi=0.1

for i in range(k):
    x,y,rad=random3()
    if rad<=1:
        cont+=1
        xs=np.append(xs,x)
        ys=np.append(ys,y)
    else:
        xn=np.append(xn,x)
        yn=np.append(yn,y)
    oldpi=pi
    pi=4*cont/k
    vpi=np.append(vpi,pi)

print(pi)

plt.subplot(2,3,3)
plt.title("Montecarlo generador python")
plt.scatter(xs,ys)
plt.scatter(xn,yn)

plt.subplot(2,3,6)
plt.title("Grafica de valor de pi estimado")
plt.plot(vpi)

plt.show()
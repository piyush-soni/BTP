import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')
def primes_from_2_to(n):
   
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]
def van_der_corput(n_sample, base=2):
    
    sequence = []
    for i in range(n_sample):
        n_th_number, denom = 0., 1.
        while i > 0:
            i, remainder = divmod(i, base)
            denom *= base
            n_th_number += remainder / denom
        sequence.append(n_th_number)

    return sequence
def halton(dim, n_sample):

    big_number = 10
    while 'Not enought primes':
        base = primes_from_2_to(big_number)[:dim]
        if len(base) == dim:
            break
        big_number += 1000

    # Generate a sample using a Van der Corput sequence per dimension.
    sample = [van_der_corput(n_sample + 1, dim) for dim in base]
    sample = np.stack(sample, axis=-1)[1:]

    return sample

num_of_devices = int(input("Number of devices: "))
GridDimeniton = int(input("Grid dimention :"))
a = halton(2, num_of_devices)*GridDimeniton

# splitting the inputs in different variables for better execution
x,y = [],[]
for i in a:
	x.append(i[0])
	y.append(i[1])

m1 = max(x)
m2 = max(y)

cou = 0
xval = []
yval = []

def animate(i):
    global cou
    xval.append(x[cou])
    yval.append(y[cou])
    plt.cla()
    plt.scatter(xval, yval, s=100)
    cou+=1
    plt.tight_layout()
    if(cou == num_of_devices):
        cou-=1

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
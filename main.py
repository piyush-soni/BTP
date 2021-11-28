# BTP

import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

def primes_from_2_to(n):
   
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=bool)
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
radius = int(input("Radius of device :"))
a = halton(2, num_of_devices)*GridDimeniton

x, y, status = [], [], []
for i in a:
	x.append(i[0])
	y.append(i[1])
	status.append(1)

f = open("initalDeployment.txt","w+")
f.write("Device Radius = "+str(radius)+"\n")
for i in range(num_of_devices):
	f.write("Device "+str(i+1)+" Location x="+str(int(x[i]*100)/100)+" y="+str(int(y[i]*100)/100)+"\n")
f.close()

f = open("live-status.txt","w+")
f.write(str(radius)+","+str(num_of_devices)+","+str(GridDimeniton)+",0"+"\n")
for i in range(num_of_devices):
    f.write(str(int(x[i]*100)/100)+","+str(int(y[i]*100)/100)+",1\n")
f.close()
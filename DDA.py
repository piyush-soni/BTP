import numpy as np
import matplotlib.pyplot as plt
from numpy import random
def find_frnds(i,a):
    pass
# now find friends of i in a using if dis(i,j belongs to a)<2R
         

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
#print("here the plot will be shown for 2 dimentional devices \n")

a = halton(2, num_of_devices)*GridDimeniton

config_points={}

# initialize the config_points as a int,list map 
# this will hold the supporting frnds of a particular node

for i in range(num_of_devices):
    config_points.update({i:[i+0,i+1,i+2]})
for i in range(num_of_devices):
    print(config_points[i])
# run a loop for every point to find its friends

# AFTER the upper loop we will be having a map of int and list showing the point number and its helper

# now if any device gets short we just have to check whether its friends status is 1 or 0 is it is 1 it is helping and if it is 1 then we first find the helpers of that point.
# then pass it to this function find_helper

x,y,status = [],[],[]

for i in a:
	x.append(i[0])
	y.append(i[1])
	status.append(1)
def checkstatus():
    ra = random.randint(num_of_devices,size=(5))
    for i in ra:
        if(status[i] == 1):
            status[i] = 0
        else:
            status[i] = 1


# while(True):
#     for i in range(num_of_devices):
#         r = 50
#         if(status[i] == 1):
#             plt.scatter(x[i],y[i],c="c",s=r**2)
#             plt.scatter(x[i],y[i],c="black")
#         else:
#             plt.scatter(x[i],y[i],c="r")
#             pass
#     checkstatus()
#     plt.draw()
#     plt.pause(3)
#     plt.clf()

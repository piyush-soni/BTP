import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')
def checkstatus():
    # print("Enter device number, current status")
    # n, s = map(int, input().split())
    # n-=1
    # if(n > num_of_devices or n<0 or n!=int(n)):
    #     print("invalid device number")
    # else:
    #     status[n] = s
    n = random.randrange(0,num_of_devices)
    s = random.choice([1,1,1,1,0])
    status[n] = s
    print("device",n,"status",s)

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

# requesting for all the necessary inputs in the code
num_of_devices = int(input("Number of devices: "))
GridDimeniton = int(input("Grid dimention :"))
radius = int(input("Radius of device :"))
a = halton(2, num_of_devices)*GridDimeniton

# splitting the inputs in different variables for better execution
x,y,status = [],[],[]
for i in a:
	x.append(i[0])
	y.append(i[1])
	status.append(1)

# adding device location to loc.txt
f= open("loc.txt","w+")
for i in range(num_of_devices):
    f.write("Device "+str(i+1)+" Location x="+str(int(x[i]*100)/100)+" y="+str(int(y[i]*100)/100)+"\n")
f.close()
# this connections array will be holding the friends for all then nodes
# connections = []
# for i in range(num_of_devices):
#     connections.append([])
#     pt1 = np.array((x[i],y[i]))
#     for v in range(num_of_devices):
#         if(v != i):
#             if(abs(x[i]-x[v]) <= 2*radius and abs(y[i]-y[v]) <= 2*radius):
#                 pt2 = np.array((x[v],y[v]))
#                 if(np.linalg.norm(pt1 - pt2) <= 2*radius):
#                     connections[i].append(v)

# for i in range(len(connections)):
#     print("Device Number",i+1,"connections are :",connections[i])

while(True):
    ax = plt.gca()
    for i in range(num_of_devices):
        if(status[i] == 0):
            ax.add_patch(plt.Circle((x[i],y[i]),radius,color="red"))
    for i in range(num_of_devices):
        if(status[i] == 1):
            ax.add_patch(plt.Circle((x[i],y[i]),radius))
    plt.axis("scaled")
    plt.draw()
    plt.pause(2)
    checkstatus()
    plt.clf()

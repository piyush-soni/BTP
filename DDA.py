import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')
def checkstatus():
    n = random.randrange(0,num_of_devices)
    s = random.choice([1,1,1,1,0])
    if(status[n] == s):
        return False
    status[n] = s
    con()
    print("device",n+1,"status",s)
    return True
def con():
    f = open("Connection-List.txt","w+")
    f.write("Supporting Device List \n\n")
    for i in range(num_of_devices):
        if(status[i] == 1):
            f.write("Device "+str(i+1)+" =>   ")
        else:
            f.write("Device "+str(i+1)+" =>   Disconnected \n")
            continue
        for v in connections[i]:
            if(status[v-1] == 1):
                f.write(str(v)+" ")
        f.write("\n")
    f.close()

f = open("current-device-location-list.txt","r")
l = f.readlines()
radius, num_of_devices, GridDimeniton = map(int, l[0].split(","))
temp = True
x, y, status = [], [], []
for i in l:
    if temp:
        temp = not temp
        continue
    temp1, temp2 = i.split(",")
    x.append(float(temp1))
    y.append(float(temp2[:-1]))
    status.append(1)

# this connections array will be holding the friends for all then nodes
connections = []
for i in range(num_of_devices):
    connections.append([])
for i in range(num_of_devices):
    pt1 = np.array((x[i],y[i]))
    for v in range(num_of_devices):
        if(v != i):
            if(abs(x[i]-x[v]) <= 2*radius and abs(y[i]-y[v]) <= 2*radius):
                pt2 = np.array((x[v],y[v]))
                if(np.linalg.norm(pt1 - pt2) <= 2*radius):
                    connections[i].append(v+1)

for i in range(len(connections)):
    print("Device Number",i+1,"connections are :",connections[i])
con()

t = True
while(True):
    if(t):
        plt.clf()
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
    t = checkstatus()

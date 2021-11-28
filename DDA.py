import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def readdata():
    global radius
    global num_of_devices
    global GridDimeniton
    global redplynum
    global x
    global y
    global status
    x, y, status = [], [], []
    f = open("live-status.txt","r")
    l = f.readlines()
    temp = True
    radius, num_of_devices, GridDimeniton, redplynum = map(int, l[0].split(","))
    for i in l:
        if temp:
            temp = not temp
            continue
        temp1, temp2, e = i.split(",")
        x.append(float(temp1))
        y.append(float(temp2))
        status.append(int(e))
    f.close()
def writedata():
    global radius
    global num_of_devices
    global GridDimeniton
    global redplynum
    global x
    global y
    global status
    f = open("live-status.txt","w+")
    f.write(str(radius)+","+str(num_of_devices)+","+str(GridDimeniton)+","+str(redplynum)+"\n")
    for i in range(num_of_devices):
        f.write(str(int(x[i]*100)/100)+","+str(int(y[i]*100)/100)+","+str(status[i])+"\n")
    f.close()
def checkstatus():
    global redplynum
    f = open("live-status.txt","r")
    l = f.readline()
    temp3 = int(l.split(",")[-1])
    f.close()
    if redplynum != temp3:
        redplynum = temp3
        readdata()
        return True
    n = random.randrange(0,num_of_devices)
    s = random.choice([1,1,1,1,0])
    if(status[n] == s):
        return False
    status[n] = s
    writedata()
    print("device",n+1,"status",s)
    return True

x, y, status, temp, t = [], [], [], True, True

plt.style.use('seaborn')
f = open("live-status.txt","r")
l = f.readlines()
radius, num_of_devices, GridDimeniton, redplynum = map(int, l[0].split(","))
for i in l:
    if temp:
        temp = not temp
        continue
    temp1, temp2, e = i.split(",")
    x.append(float(temp1))
    y.append(float(temp2))
    status.append(int(e))
f.close()

while(True):
    if(t):
        plt.clf()
        ax = plt.gca()
        for i in range(num_of_devices):
            if(status[i] == 2):
                ax.add_patch(plt.Circle((x[i],y[i]),radius,color="orange"))
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

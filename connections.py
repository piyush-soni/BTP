import numpy as np

arr, x, y, status, temp = [], [], [], [], True
f = open("live-status.txt","r")
l = f.readlines()
radius, num_of_devices, GridDimeniton, redplynum = map(int, l[0].split(","))
for i in l:
    if temp:
        temp = not temp
        continue
    temp1, temp2, e = i.split(",")
    x.append(float(temp1))
    y.append(float(temp2[:-1]))
    status.append(int(e))
f.close()

for i in range(num_of_devices):
    arr.append([])
    pt1 = np.array((x[i],y[i]))
    for v in range(num_of_devices):
        if v!=i:
            if(abs(x[i]-x[v]) <= 2*radius and abs(y[i]-y[v]) <= 2*radius):
                pt2 = np.array((x[v],y[v]))
                if(np.linalg.norm(pt1 - pt2) <= 2*radius):
                    arr[i].append(v+1)

for i in range(len(arr)):
    print("Device Number",i+1,"connections are :",arr[i])

f = open("Connection-List.txt","w+")
f.write("Supporting Device List \n\n")
for i in range(num_of_devices):
    if(status[i] == 0):
        f.write("Device "+str(i+1)+" =>   Disconnected \n")
        continue
    else:
        f.write("Device "+str(i+1)+" =>   ")
    for v in arr[i]:
        if(status[v-1] == 1):
            f.write(str(v)+" ")
    f.write("\n")
f.close()

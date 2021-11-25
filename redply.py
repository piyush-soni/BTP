#redeployment
# import time
# import random
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# this function will find all the disconnected devices which are not active right now for any reason
arr = set()
def find():
	global arr
	f = open("Connection-List.txt","r")
	l = f.readlines()
	for i in l:
		a = i.split()
		if len(a)<4:
			continue
		elif a[3][0] == 'D':
			arr.add(int(a[1]))
	f.close()

find()
# now we have all the device numbers saved in the arr
# we now need to get all the device locations so now we will be using the loc.txt
c = 0
d = {}
f = open("loc.txt","r")
l = f.readlines()
for i in l:
	if c == 0:
		radius = int(i)
	else:
		x, y = i.split(",")
		x = float(x)
		y = float(y[:-1])
		d[c] = [x,y]
	c+=1

# now we have the radius and loaction of all the disconnected devices
# dd is the 4 speacial points list for all the deactive devices

def fix(n):
	n = int(n*100)
	n = n/100
	return n

dd = {}
for i in arr:
	x = d[i][0]
	y = d[i][1]
	r = radius//2
	dd[i] = [(fix(x+r),fix(y+r)),(fix(x+r),fix(y-r)),(fix(x-r),fix(y+r)),(fix(x-r),fix(y-r))]
# here we have all the vertex locations 
print("deactivated devices")
print(arr)
print("------------------------")
print("redeployment needed for True cordinates")

def check(x, y):
	global arr
	global d
	global radius
	pt1 = np.array((x,y))
	for i in d:
		if i not in arr:
			pt2 = np.array((d[i][0], d[i][1]))
			if(np.linalg.norm(pt1 - pt2) <= radius):
				return False
	return True



redply = []
for i in dd:
	for v in dd[i]:
		print(v[0],v[1],check(v[0], v[1]))





while True:
	a = 1
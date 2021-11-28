# redeployment
import numpy as np


def fix(n):
	n = int(n*100)
	n = n/100
	return n

arr = set()
f = open("live-status.txt","r")
l = f.readlines()
radius, num_of_devices, GridDimeniton, redplynum = map(int, l[0].split(","))
d = {}
temp = True
c = 0
for i in l:
	if temp:
		temp = not temp
		continue
	c+=1
	temp1, temp2, a = i.split(",")
	d[c] = [float(temp1), float(temp2),int(a)]
	if d[c][-1] == 0:
		arr.add(c)
f.close()

# dd list = new potential devices
dd = {}
for i in arr:
	x = d[i][0]
	y = d[i][1]
	r = radius//2
	dd[i] = [(fix(x+r),fix(y+r)),(fix(x+r),fix(y-r)),(fix(x-r),fix(y+r)),(fix(x-r),fix(y-r))]

print(arr)
print("----------------")
print(d)
print("----------------")
print(dd)


# print("deactivated devices")
# print(arr)
# print("------------------------")
# print("redeployment needed for True cordinates")

# def check(x, y):
# 	global arr
# 	global d
# 	global radius
# 	pt1 = np.array((x,y))
# 	for i in d:
# 		if i not in arr:
# 			pt2 = np.array((d[i][0], d[i][1]))
# 			if(np.linalg.norm(pt1 - pt2) <= radius):
# 				return False
# 	return True


# redply = []
# for i in dd:
# 	for v in dd[i]:
# 		print(v[0],v[1],check(v[0], v[1]))

while True:
	a = 1

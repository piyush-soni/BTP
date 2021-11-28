# redeployment
import numpy as np


def fix(n):
	n = int(n*100)
	n = n/100
	return n
def check(x, y):
	global arr
	global radius
	pt1 = np.array((x,y))
	for i in d:
		if i not in arr:
			pt2 = np.array((d[i][0], d[i][1]))
			if(np.linalg.norm(pt1 - pt2) <= radius):
				return False
	return True

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

redply = []
for i in dd:
	c = 0
	for v in dd[i]:
		temp = check(v[0],v[1])
		if temp:
			c+=1
			redply.append((v[0],v[1]))
			print(v[0], v[1], True)
		else:
			print(False)
	if c==0:
		redply.append((d[i][0],d[i][1]))
		print(d[i][0], d[i][1], True)

command = input("press y to redploy devices  :  ")
if command == "y":
        f = open("live-status.txt", "w+")
        num_of_devices = num_of_devices - len(arr) + len(redply)
        f.write(str(radius)+","+str(num_of_devices)+","+str(GridDimeniton)+","+str(redplynum+1)+"\n")
        for i in d:
                if d[i][-1] != 0:
                        f.write(str(d[i][0])+","+str(d[i][1])+",1\n")
        for i in redply:
                f.write(str(i[0])+","+str(i[1])+",2\n")
        f.close()


while True:
	a = 1

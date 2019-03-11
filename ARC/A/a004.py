import numpy as np
N = int(input())
xys = []
for i in range(N):
    x,y = map(int,input().split())
    xys.append([x,y])

def dist(c1, c2):
    return np.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)

dist_max = 0
for i,xy1 in enumerate(xys):
    for xy2 in xys[i+1:]:
        dist_max = max(dist_max, dist(xy1,xy2))
print(dist_max)

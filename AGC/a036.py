S = int(input())
# この四角形をつくる
sqrtS = int(S**0.5)
if sqrtS**2 < S:
    sqrtS+=1

diff = sqrtS**2-S

x0,y0 = (0,0)
if diff == 0:
    x1,y1 = (0,sqrtS)
    x2,y2 = (sqrtS,0)
else:
    x1,y1 = (diff,sqrtS)
    x2,y2 = (sqrtS, 1)

print(x0,y0,x1,y1,x2,y2)

# S = sqrtS**2-x1*y2
# print(S)
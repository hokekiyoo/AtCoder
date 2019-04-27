N,M,X,Y = map(int,input().split())
xs = [int(i) for i in input().split()]
ys = [int(i) for i in input().split()]

xmax = max(xs)
ymin = min(ys)


zs = [i for i in range(X+1,Y+1)]
warflg = True
for z in zs:
    if xmax<z and z<=ymin:
        warflg = False

if warflg:
    print("War")
else:
    print("No War")


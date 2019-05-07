import numpy as np
N = int(input())
L = input().split()
npL = np.array([int(l) for l in L])
l_max = npL.max()
arg_max = np.argmax(npL)
l_deleted = np.delete(npL, arg_max)
if l_max < l_deleted.sum():
    print("Yes")
else:
    print("No")
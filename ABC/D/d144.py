import numpy as np
a,b,V = map(int, input().split())
x = V/(a*a)
if b >= 2*x:
    tan = b**2/(2*a*x)
else:
    tan = 2*(b-x)/a
ans = np.arctan(tan)
print(ans*180/np.pi)
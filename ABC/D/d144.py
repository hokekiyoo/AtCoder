import numpy as np
a,b,V = map(int, input().split())
x = V/(a*a)
"""
算数の解
"""
# if b >= 2*x:
#     tan = b**2/(2*a*x)
# else:
#     tan = 2*(b-x)/a
# ans = np.arctan(tan)
# print(ans*180/np.pi)


"""
二部探索
"""
def f(theta):
    if np.tan(theta) < (2*x)/a:
        l = x + a*np.tan(theta)/2
    else:
        l = (2*a*x*np.tan(theta))**0.5
    return l >= b


eps = 10**-12
def  binarySearch(l,r):
    while r - l > eps:
        mid = (l+r)/2
        if f(mid):
            r = mid
        else:
            l = mid
    return r

print(binarySearch(-1*np.pi/180,(np.pi/2-eps))*180/np.pi)

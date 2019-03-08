def fractorial(n):
    if n==1:
        return 1
    return fractorial(n-1)*n

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
for i in range(2,10):
    print("{:10d}{:10d}".format(fractorial(i),fibonacci(i)))


count = 0
def c114(s):
    if int(s)>N:
        return 0
    if all( s.count(c)>0 for c in "753"):
        ret = 1
    else:
        ret = 0
    ret += c114(s+"3")
    ret += c114(s+"5")
    ret += c114(s+"7")
    return ret

import numpy as np
def c119(no, a, b, c):
    if no == N:
        if min(a,b,c) >0:
            ret = abs(A-a)+abs(B-b)+abs(C-c)-10*3
            print(a,b,c,ret)
            return ret
        else:
            return 100000000
    ret0 = c119(no+1,a,b,c)         #使わない
    ret1 = c119(no+1,a+ls[no],b,c)  #Aに使う
    ret2 = c119(no+1,a,b+ls[no],c)  #Bに使う
    ret3 = c119(no+1,a,b,c+ls[no])  #Cに使う
    return min(ret0,ret1,ret2,ret3) #こいつは最後まで出てこない

if __name__ == "__main__":
    # N = 4
    # print(c119("0"))
    N = 8
    A, B, C = [1000,800,100]
    ls = [300, 333, 400, 444, 500, 555, 600, 666]
    c119(0,0,0,0)
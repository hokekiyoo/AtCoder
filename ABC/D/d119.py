# 二部探索問題

# from bisect import bisect_right as binarysearch
A, B, Q = map(int,input().split())

"""
自分で作ったやつは遅い
"""
def binarysearch(ls,x):
    n = len(ls)
    left = 0
    right = n
    pos = (right+left)//2
    while True:
        if ls[pos] < x < ls[pos+1]:
            index = pos
            break    
        elif x < ls[pos]:
            right = pos
        elif ls[pos+1] < x:
            left = pos
        pos = (right+left)//2
    return index




ss = [-10**10]+[int(input()) for _ in range(A)]+[2*10**10]
ts = [-10**10]+[int(input()) for _ in range(B)]+[2*10**10]
xs = [int(input()) for _ in range(Q)]
for x in xs:
    sind = binarysearch(ss,x)
    tind = binarysearch(ts,x)
    
    s0,s1,t0,t1 = ss[sind],ss[sind+1],ts[tind],ts[tind+1]
    # d1,d2,d3,d4 = 10**10,10**10,10**10,10**10
    # print("s",s0,x,s1)
    # print("t",t0,x,t1)
    d1 = max(x-s0,x-t0)
    d2 = min((t1-x)*2+(x-s0),(x-s0)*2+(t1-x))
    d3 = min((s1-x)*2+(x-t0),(x-t0)*2+(s1-x))
    d4 = max(s1-x, t1-x)
    print(min(d1,d2,d3,d4))

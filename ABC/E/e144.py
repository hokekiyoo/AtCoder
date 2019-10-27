N, K  = map(int, input().split())
As = sorted(list(map(int, input().split())))
Fs = sorted(list(map(int, input().split())),reverse=True)
Xs = [a*f for a,f in zip(As,Fs)]
X_M = max(Xs)

def f(x):
    K_tmp = sum([max(0,a-x//f) for a,f in zip(As,Fs)])
    return K_tmp <= K

def  binarySearch(l,r,target):
    while r - l > 1:
        mid = (l+r)//2
        if f(mid):
            r = mid
        else:
            l = mid
    return r

print(binarySearch(-1,X_M,K))

# import heapq
# q = []
# INF = 10**6
# heapq.heapify(q)
# for i,(a,f) in enumerate(zip(As,Fs)):
#     num = -(a*f*INF+i)
#     heapq.heappush(q,num)
# if K >= sum(As):
#     print(0)
#     exit()
# for k in range(K):
#     num = heapq.heappop(q)
#     i = (-num)%INF
#     n = (-num)//INF
#     # print(i,n,As[i],Fs[i])
#     As[i] -= 1
#     upd = -(As[i]*Fs[i]*INF+i)
#     heapq.heappush(q,upd)
# num = heapq.heappop(q)
# ans = (-num)//INF
# print(ans)



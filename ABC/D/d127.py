import heapq
N,M = map(int,input().split())
As = list(map(int,input().split()))

As = sorted(As)
BCs = []
heapq.heapify(BCs)
for i in range(M):
    B,C =   map(int,input().split())
    heapq.heappush(BCs,(-C,B))

ind = 0
ans = 0
flg = False
for i in range(M):
    _C,B = heapq.heappop(BCs)
    for i in range(B):
        if As[ind+i] > -_C:
            flg = True
            ind += i
            break
        else:
            ans -= _C
        if ind+i+1 > N-1:
            flg = True
            ind += i+1
            break
    if flg: break
    ind += B
print(As,As[ind:],ind,ans)
ans += sum(As[ind:])
print(ans)
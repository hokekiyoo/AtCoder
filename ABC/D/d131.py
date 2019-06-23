import heapq
N = int(input())
q = []
heapq.heapify(q)
for i in range(N):
    a,b = map(int, input().split())
    heapq.heappush(q,(b,a))

time = 0
flg = True
for i in range(N):
    b,a = heapq.heappop(q)
    time += a
    if b < time:
        flg = False
if flg:
    print("Yes")
else:
    print("No")
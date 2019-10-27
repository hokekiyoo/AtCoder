N,M = map(int, input().split())
As = list(map(int, input().split()))
import heapq
q = []
heapq.heapify(q)
for a in As:
    heapq.heappush(q,-a)
for i in range(M):
    a = heapq.heappop(q)
    a = (-a)//2*-1
    # print(a)
    heapq.heappush(q,a)

print(-1*sum(list(q)))
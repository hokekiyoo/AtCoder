import heapq
N, M  = map(int, input().split())

q = []  # 締切の小さい順に並べ替え
q1 = [] # するタスクリスト

for i in range(N):
    day, reward = map(int, input().split())
    heapq.heappush(q,(-day,-reward))
# delayは大きい順、rewardは大きい順で並べておく
while q:
    d, r = heapq.heappop(q)
    rest = M - len(q1)
    if rest >= -d:
        # できるリストに追加
        heapq.heappush(q1,-r)
    else:
        # 一番報酬が少ない奴を入れ替え
        heapq.heappush(q1,-r)
        heapq.heappop(q1)
        
print(sum(q1))
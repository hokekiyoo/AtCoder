"""
漸化式的に解く
一般性を失わない範囲をちゃんと考える。
"置き換え可能"というのをどの部分で持たせられるかを考える
今回の場合は、リスト作りの際に作ったので十分
"""

from collections import defaultdict
N, K = map(int,input().split())
# dd = defaultdict(list)
pairs = [list(map(int,input().split())) for _ in range(N)]
# 美味しい順にソート
pairs = sorted(pairs,reverse=True, key=lambda x: x[1])
kinds = set()
change = [] #変更できるもの(2個以上あるもの)



cnt = 0
for t,d in pairs[:K]: #K個上から順番に取ってみる
    if t in kinds:
        change.append(d) 
    kinds.add(t)
    cnt += d

n = len(kinds)
cnt += len(kinds)**2
ans = cnt

"""
K+1以降
Kまでに大きい順に加えたもので、2個以上あるものから順に置き換えていく。
1個のものはそのままで良い。
また、K+1以降で、2回同じものを追加する可能性はない。
なぜなら新規の追加ではないので、その場合はchangeに入ってある美味しさdiよりも
K+1以降のものは必ず低い美味しさの値になっているからである。
"""
for t,d in pairs[K:]:
    # 交換できるものがなくなったら終わり
    if len(change) == 0:
        break
    # 同じものは交換しない
    if t in kinds:
        continue
    d_min = change.pop()
    cnt = cnt - (d_min + n**2)  + (d + (n+1)**2)
    kinds.add(t)
    n += 1
    ans = max(cnt,ans)
# 集計
print(ans)

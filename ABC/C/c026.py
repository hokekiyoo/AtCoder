N = int(input())
Bs = [int(input()) for i in range(N-1)]
subs = [[] for i in range(N)]
for i,b in enumerate(Bs):
    subs[b-1].append(i+1) # 直属の部下リスト
subs = [(i,sub) for i,sub in enumerate(subs)] #インデックスと数を把握
print(subs)
money = [0] * N
for i, sub in subs[::-1]:
    if len(sub) == 0:
        money[i] = 1
    else:
        cnt = []
        for s in sub:
            cnt.append(money[s])
        money[i] = 1 + min(cnt) + max(cnt)
print(money[0])

"""制約見落としていた
番号がランダムのときが↓
subs = sorted([(len(sub),i,sub) for i,sub in enumerate(subs)]) #インデックスと数を把握
# 葉から決めていく
money = [0]*N
cnt = sum([1 for m in money if m > 0])
while cnt < N:
    for num,i,sub in subs:
        if money[i] > 0:
            continue
        if num == 0:
            money[i] = 1
        else:
            # 給与が決まっていたら決まる
            calc_flg = True
            l = []
            for s in sub:
                # まだ決まっていないときは放置
                if money[s] == 0:
                    calc_flg = False
                    break
                else:
                    l.append(money[s])
            if calc_flg:
                money[i] = min(l) + max(l) +1
        # print(money)
    # print("finish",money)
    cnt = sum([1 for m in money if m > 0])

print(money[0])

"""
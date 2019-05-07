# """
# コンプリートするものと、せざるものに分ける
# コンプリートしないものに関しては、得点の高い方から一個だけ潰す
# """

D, G = map(int, input().split())
ps_ini,cs = [], []
for i in range(D):
    p,c = map(int,input().split())
    ps_ini.append(p)
    cs.append(c)

q_min = 1000000
for i in range(2**D):
    Gtmp = G
    ps = [p for p in ps_ini]
    s = "{:010b}".format(i)[::-1]
    q_all = 0
    for j,(p,c) in enumerate(zip(ps,cs)):
        # ボーナスの考慮
        Gtmp -= (p*(j+1)*100+c)*int(s[j]) 
        q_all += p*int(s[j])
        ps[j] -= p*int(s[j])
    # print(s,ps)
    if Gtmp <= 0:
        q_min = min(q_min, q_all)
    else:
        # コンプしていない問題で一番大きいやつ
        ind = 0
        for i,p in enumerate(ps):
            if p != 0:
                ind = i
        # print(Gtmp,ind,Gtmp//((ind+1)*100))
        # 比較
        if Gtmp//((ind+1)*100) > ps[ind]:
            continue
        if Gtmp%((ind+1)*100) == 0:           #割り切れない
            q_all += (Gtmp//((ind+1)*100))
        else:                           #割り切れる
            q_all += (Gtmp//((ind+1)*100) + 1) #最大値をコンプする以外ありえん
        q_min = min(q_min, q_all)
print(q_min)


### 参考 : 再帰関数で書いているもの
# sums=[]
# for i in range(D):
#     sums.append((i+1)*100*ps_ini[i]+cs[i])
 
def ans(G,t):
    if t <= 0:
        return 100000000000
    n = min(G//(100*t),ps_ini[t-1])
    s = 100*t*n
    
    if n == ps_ini[t-1]:
        s = 100*t*n+cs[t-1]
    if G > s:
        n += ans(G-s,t-1)
    return min(n,ans(G,t-1))
 
print(ans(G,D))

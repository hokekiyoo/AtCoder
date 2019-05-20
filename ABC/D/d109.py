
"""
解法
奇数のペアを見つけ出し、ペアが重なるようにルートを敷いてやると良い？
"""

### 予め一筆書きルートを作る
H, W = map(int,input().split())
As = []
for i in range(H):
    As.append(list(map(int,input().split())))
routes = []
for i in range(H):
    for j in range(W):
        if i%2 == 0:
            routes.append((i+1,j+1))
        else:
            routes.append((i+1,W-j))
n = len(routes)
mvs = []
cnt = 0
for i in range(n-1):
    hi,wi = routes[i]
    hi2,wi2 = routes[i+1]
    if As[hi-1][wi-1] % 2 == 1:
        As[hi2-1][wi2-1] += 1
        mvs.append([hi,wi,hi2,wi2])
        cnt += 1

print(cnt)
for h1,w1,h2,w2 in mvs:
    print(h1,w1,h2,w2)


"""
失敗解法(移動回数が多すぎる)
H, W = map(int,input().split())
odds = []
for i in range(H):
    # As.append(list(map(int,input().split())))
    ls = list(map(int,input().split()))
    for j,l in enumerate(ls):
        if l%2 == 1:
            odds.append([i,j])

def make_route(odd1,odd2):
    h1,w1 = odd1
    h2,w2 = odd2
    dh = abs(h1-h2)
    dw = abs(w1-w2)
    move_list = []
    for _ in range(dh):
        if h1 < h2:
            move_list.append((h1,w1,h1+1,w1))
            h1 += 1
        else:
            move_list.append((h1,w1,h1-1,w1))
            h1 -= 1
    for _ in range(dw):
        if w1 < w2:
            move_list.append((h2,w1,h2,w1+1))
            w1 += 1
        else:
            move_list.append((h2,w1,h2,w1-1))
            w1 -= 1

    return move_list


n = len(odds)
cnt = 0
mvs = []
for i in range(0,n-1,2):
    odd1 = odds[i]
    odd2 = odds[i+1]
    routes = make_route(odd1,odd2)
    for h1,w1,h2,w2 in routes:
        mvs.append([h1,w1,h2,w2])
        cnt += 1
print(cnt)
for h1,w1,h2,w2 in mvs:
    print(h1+1,w1+1,h2+1,w2+1)

"""


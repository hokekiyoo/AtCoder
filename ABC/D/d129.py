H,W = map(int,input().split())
S = [input() for i in range(H)]

### その1
"""
# 4方向の累積和をとって計算する
Rs = [[0]*W for i in range(H)]
Ls = [[0]*W for i in range(H)]
Ds = [[0]*W for i in range(H)]
Us = [[0]*W for i in range(H)]

for i in range(H):
    tmp = 0
    # 順方向(左にどれだけ伸びてるか)
    for j in range(W):
        if S[i][j] == '#':
            tmp = 0
        else:
            tmp += 1
            Ls[i][j] = tmp
    tmp = 0
    # 逆方向(右にどれだけ伸びてるか)
    for j in reversed(range(W)):
        if S[i][j] == '#':
            tmp = 0
        else:
            tmp += 1
            Rs[i][j] = tmp

# 行列転置 順番逆にするだけ
for j in range(W):
    tmp = 0
    # 順方向 上にどれだけ伸びているか
    for i in range(H):
        if S[i][j] == '#':
            tmp = 0
        else:
            tmp += 1
            Us[i][j] = tmp
    tmp = 0
    # 順方向 下にどれだけ伸びているか
    for i in reversed(range(H)):
        if S[i][j] == '#':
            tmp = 0
        else:
            tmp += 1
            Ds[i][j] = tmp

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#': 
            continue
        # 上下左右に伸びた数を重なっている部分引く
        tmp = Rs[i][j] + Ls[i][j] + Ds[i][j] + Us[i][j] - 3
        ans = max(ans, tmp)
print(ans)
"""

# その2
"""
左・上からゴリゴリ攻めていくパターン
一回通ったかどうかのフラグが必要
"""

cnt = [[0] * (W+1) for i in range(H+1)]
# 横
for i in range(H):
    done = [False] * (W+1)
    for j in range(W):
        l = 0
        if done[j]: continue
        if S[i][j] == ".":
            while j+l < W:
                if S[i][j+l] == ".":
                    l += 1
                else:
                    break
        for k in range(j,j+l):
            cnt[i][k] += l
            done[k] = True

print(cnt)
# 縦
for j in range(W):
    done = [False] * (H+1)
    for i in range(H):
        l = 0
        if done[i]: continue
        if S[i][j] == ".":
            while i+l < H:
                if S[i+l][j] == ".":
                    l += 1
                else:
                    break
        for k in range(i,i+l):
            cnt[k][j] += l
            done[k] = True

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans,cnt[i][j])
print(ans-1)
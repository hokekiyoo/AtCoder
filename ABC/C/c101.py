N, K = map(int,input().split())
X = list(map(int,input().split()))

# Kのwindowを持っている
# 移動幅が決まっている⇨スライディングウィンドウ
# 正負で挙動が少し変わる
# +方向に進むか、-方向に進むか
ans = 10**10
for i in range(N-K+1):
    plus =  abs(X[i]) + abs(X[i+K-1]-X[i])
    minus = abs(X[i+K-1]) + abs(X[i+K-1]-X[i])
    ans = min(ans,plus,minus)
print(ans)
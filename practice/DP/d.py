"""
TLEのやつ
"""
# ws, vs = [], []
# for i in range(N):
#     w,v = map(int,input().split())
#     ws.append(w)
#     vs.append(v)
# 重さの総和の値を固定して、その値の最大値を求める組み合わせを
# dp[i][sum_wN]とする
# dp = [[0 for i in range(W+1)] for j in range(N)]
# for i in range(N):
#     for j in range(W+1):
#         # あるWについて
#         # i番目をknapsacに加える場合
#         if j - ws[i] >= 0:
#             dp[i][j] = max(dp[i-1][j],dp[i-1][j-ws[i]] + vs[i])
#         else:
#             dp[i][j] = max(dp[i][j],dp[i-1][j])


"""
うまく行ったやつ
"""
import numpy as np
N,W = map(int, input().split())
# np.maximum https://www.sejuku.net/blog/69175
# 第一引数と第二引数の大小関係を要素ごとに比較して、大きい方を格納した配列を返します。
dp = np.zeros(W+1, dtype=np.int64)
for _ in range(N):
    w,v = map(int,input().split())
    # w以下ならvを足したもの、w以上ならそのままの値で、最大値を求める
    # 出力はw以上の配列として返す(それ以下は重さwなので関与しない)
    # 足す場合が前者、足さない場合が後者。その重さでの最大valueが保存されている
    np.maximum(dp[:-w]+v,dp[w:],out=dp[w:]) 
print(dp)
# print(dp[-1])
# XOR嫌い
# https://qiita.com/kuuso1/items/778acaa7011d98a3ff3a


"""
# 1. 激ナイーブ。当然ムリ。
# しかも間違っているらしい
N, K = map(int,input().split())
As = list(map(int,input().split()))
ans = sum([0^a for a in As])
for i in range(K):
    ans = max(ans, sum([i^a for a in As]))
print(ans)
"""

"""
#2.桁数で判断して探索範囲を狭める作戦⇨失敗
import numpy as np
N, k = map(int,input().split())
As = list(map(int,input().split()))
if k == 0:
    ans = sum([a^k for a in As])
elif max(As) == 0:
    ans = N
else:
    n2_amax = int(np.log(max(As)))+1
    n2_k = int(np.log(k))+1
    ans = 0
    if n2_amax == n2_k:
        for X in range(2**(n2_k-1),k):
            ans = max(ans, sum([a^X for a in As]))
    else:
        for X in range(2**(n2_k),k):
            ans = max(ans, sum([a^X for a in As]))
print(ans)
"""
# 順序関係をうまく変えたい。
# 各ビットの立っている数を数えるんだ！
# xorは各桁独立して考えることで、和との順序を逆に考えられる
# bit演算 : https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361

N, K = map(int,input().split())
As = list(map(int,input().split()))
bit_length = max(len(bin(K)), len(bin(max(As))))-2 #0bの除去
ans = 0
for i in range(bit_length,-1,-1): #上から順番に
    bit = 2**i 
    #iビット目の立っている数を数える
    n_bit = sum([1 for a in As if a & bit]) 
    # 0のほうが大きい場合
    # Xのビットは立っているのが望ましいが、Kを超えては駄目
    if n_bit < N - n_bit and K-bit >= 0:
        n_bit = N - n_bit
        K -= bit
    ans += bit * n_bit
print(ans)
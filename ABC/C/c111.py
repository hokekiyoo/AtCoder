import numpy as np
from collections import Counter
n = int(input())
As = input().split()
As = [int(A) for A in As]

A_odd = As[::2]         #奇数列
A_even = As[1:][::2]    #偶数列

# 最頻の要素を並べる
odd_pair = Counter(A_odd).most_common(2)
even_pair = Counter(A_even).most_common(2)

if odd_pair[0][0] != even_pair[0][0]:               # TOPの数字が違う
    N = n-odd_pair[0][1]-even_pair[0][1]
else:                                               # TOPの数字が一緒
    if len(odd_pair) == 1 and len(even_pair) == 1:  # 文字列がそもそも1種類
        N = n/2
    elif len(odd_pair) == 1:                        # oddが1種類
        N = n-even_pair[1][1]
    elif len(even_pair) == 1:                       # evenが1種類
        N = n-odd_pair[1][1] 
    elif odd_pair[1][1] > even_pair[1][1]:          # oddの2番目のが多い
        N = n-even_pair[0][1]-odd_pair[1][1]
    else:
        N = n-odd_pair[0][1]-even_pair[1][1]        # oddの1番目のが多い
print(int(N))
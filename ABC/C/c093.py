As = sorted(list(map(int, input().split())))
"""
2つ選んで両方を1増やす
1つ選んで2増やす

2 5 4
2 6 3
偶奇が一致しているものを選ぶ
・全部一致している -> 差の総数を2で割る
・1つだけ異なる -> 一回、1つ選んで2増やす

"""
amari = [a%2 for a in As]
# すべての偶機が一致
if sum(amari) == 0 or sum(amari) == 3:
    print(((As[2]-As[1])+(As[2]-As[0]))//2)
# 一箇所だけ奇数
elif sum(amari) == 1:
    Bs = [a+1 if a%2==0 else a for a in As]
    print(((Bs[2]-Bs[1])+(Bs[2]-Bs[0]))//2 + 1)
# 一箇所だけ偶数
elif sum(amari) == 2:
    Bs = [a+1 if a%2==1 else a for a in As]
    print(((Bs[2]-Bs[1])+(Bs[2]-Bs[0]))//2 + 1)
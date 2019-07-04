"""
import numpy as np

N, A, B, C = map(int,input().split())
goals = [A,B,C]
ls = []
for i in range(N):
    ls.append(int(input()))

# goals = [1000,800,100]
# ls = [300,333,400,444,500,555,600,666]

def count(x,ls):
    try:
        x.index(0)
        x.index(1)
        x.index(2)        
    except:
        return False
    A = np.zeros(len(goals))
    for i,l in enumerate(ls):
        add_ind = x[i]
        if add_ind==3:
            pass
        else:
            A[add_ind] += l
    combine_MP = 0
    for i in range(3):
        combine_MP += 10*(x.count(i)-1)
    return A, combine_MP
    
    
score_min = 100000
for N in range(4**8):
    x = []
    for j in range(len(ls)):
        x.append(N % 4)
        N = N // 4 
    try:
        A, combine_MP = count(x,ls)
        score = np.abs(A-np.array(goals)).sum() + combine_MP
        if score_min >= score:
            score_min = score
    except:
        pass
print(score_min)
"""

"""
20190704とき直し
l1,l2,...,lN
N は max8本
A,B,Cの3本の竹にしたい

延長 : 1MP  +1
短縮 : 1MP  -1
合成 : 10MP li + lj
A, B, Cを達成するための最小MP
"""


N,A,B,C = map(int, input().split())
ls = [int(input()) for i in range(N)]

import sys
sys.setrecursionlimit(100000)
"""
Gを作りながら探索するパターン
"""

minMP = 10**9 + 7
def dfs(i,MP,a,b,c):
    global minMP
    # 探索打ち切り条件->計算してしまう
    if i+1  >= N:
        if a>0 and b>0 and c>0:
            cnt = MP + abs(A-a)+abs(B-b)+abs(C-c) - 30 
            minMP = min(cnt,minMP)
        return 0
    l = ls[i+1]
    # 再帰的に探索
    dfs(i+1,MP,a,b,c)   # なんもしない
    dfs(i+1,MP+10,a+l,b,c) # aに
    dfs(i+1,MP+10,a,b+l,c) # bに
    dfs(i+1,MP+10,a,b,c+l) # cに

dfs(-1,0,0,0,0)
print(minMP)
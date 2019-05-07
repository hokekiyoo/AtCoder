"""
配列をソート
差を取って、最も大きいところから切っていく
K個塊になるまで切っていく
塊の端っこから端っこまでを足していく
"""
import numpy as np

N, M  = map(int,input().split())
A = input().split()
A = np.array([int(a) for a in A])

def count(A):
    A_sorted = np.sort(A)
    delta = np.abs(A_sorted[:-1] - A_sorted[1:])
    delta_ind = delta.argsort()[::-1]
    delta_ind_sort = np.sort(delta_ind[:N-1]) #昇順
    if len(delta_ind_sort) == 0:
        return 0 
    N_all = np.abs(A_sorted[0] - A_sorted[delta_ind_sort[0]]) #初期
    for i in range(len(delta_ind_sort)-1):
        # print(A_sorted[delta_ind_sort[i]+1],  A_sorted[delta_ind_sort[i+1]])
        N_all += np.abs(A_sorted[delta_ind_sort[i]+1] - A_sorted[delta_ind_sort[i+1]])
    
    N_all += np.abs(A_sorted[-1]-A_sorted[delta_ind_sort[-1]+1])
    return N_all


if N == 1:
    print(A.max()-A.min())
else:
    print(count(A))
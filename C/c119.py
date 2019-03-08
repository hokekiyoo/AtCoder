"""
間違った。全探索でおｋ
"""

import numpy as np
point = 0

# N, A, B, C = map(int,input().split())
# goals = [A,B,C]
# for i in range(N):
#     ls.append(int(input()))
# goals = [1000,800,100]
# ls = [300,333,400,444,500,555,600,666]
goals = [100,90,80]
ls = [98,40,30,21,80]



while len(goals) > 0:
    # 最小ペアの探索(単体)
    diff_min_single = 1000
    for i,l in enumerate(ls):
        diffs = np.array([np.abs(l-goal) for goal in goals])
        if diffs.min() < diff_min_single:
            diff_min_single = diffs.min()
            l_single = l
            goal_single = goals[np.argmin(diffs)]

    # print(l_single, goal_single, diff_min_single)

    l_mat = np.zeros((len(ls),len(ls)))
    diff_min_double = 1000
    for goal in goals:
        for i in range(len(ls)):
            for j in range(len(ls)):
                if i>j:
                    diff = np.abs(ls[i]+ls[j]-goal)
                    if diff_min_double >= diff:
                        diff_min_double = diff
                        l_double = ls[i]+ls[j]
                        i1, i2 = i,j
                        goal_double = goal
                        # print(i,j,diff_min_double)
    # print(l_double, goal_double, diff_min_double)

    if (diff_min_single <= diff_min_double + 10) or len(ls)==len(goals):
        point += diff_min_single
        ls.remove(l_single)
        goals.remove(goal_single)
    else:
        ls[i1] = ls[i1] + ls[i2]
        ls.remove(ls[i2])
        point += 10
    print(goals, ls, point)

print(point)
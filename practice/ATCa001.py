# H = 4
# W = 5
# route = [["s","#",".",".","."],
#          [".",".",".","#","."],
#          [".","#",".","#","."],
#          [".",".",".","#","g"]]

import numpy as np
def dfs(i,j):
    if route[i][j] == "#":
        return False
    if route[i][j] == "g":
        return True
    if route[i][j] == "." or route[i][j] == "s":
        route[i][j] = "#" #一度通った道を使わない
        a = dfs(i-1,j)
        b = dfs(i+1,j)
        c = dfs(i,j+1)
        d = dfs(i,j-1)
    return a or b or c or d


H,W = map(int,input().split())
# 端を#でパディング
route = [["#"]*(W+2)]
for i in range(H):
    route.append(list("#"+input()+"#"))
route.append(["#"]*(W+2))
sind = []
# スタート位置の探索
for j,routeh in enumerate(route):
    try:
        sind= [j,routeh.index("s")]
    except:
        continue   
# 判定 
if dfs(sind[0],sind[1]):
    print("Yes")
else:
    print("No")


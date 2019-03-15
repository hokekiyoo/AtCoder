import numpy as np
from copy import deepcopy

def dfs(maps,i,j):
    if i < 0 or i>=10 or j < 0 or j>=10:
        return 0
    if maps[i][j] == "x":
        return 0
    if maps[i][j] == "o":        
        ret = 1
        maps[i][j] = "x"
    ret += dfs(maps,i-1,j)
    ret += dfs(maps,i+1,j)
    ret += dfs(maps,i,j-1)
    ret += dfs(maps,i,j+1)
    return ret

def main():
    # maps = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], 
    #         ['x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'x'], 
    #         ['x', 'x', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'x'],
    #         ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x', 'x'], 
    #         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], 
    #         ['x', 'x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x'], 
    #         ['x', 'x', 'x', 'x', 'o', 'o', 'x', 'x', 'x', 'x'], 
    #         ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x', 'x'], 
    #         ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'x'], 
    #         ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'x']]
    maps = []
    for i in range(10):
        maps.append(list(input()))
    maps = np.array(maps)
    N = np.sum(maps=="o")
    ind = np.where(maps=="x")

    success = False
    for i,j in zip(ind[0],ind[1]):
        maps_new = deepcopy(maps) #initialize
        maps_new[i][j] = "o"
        ind_o = np.where(maps_new=="o")
        # n = dfs(maps_new,ind_o[0][0],ind_o[1][0])
        n = dfs(maps_new,i,j)
        if n == N+1:
            success = True
            break
    if success:
        print("YES")
    else:
        print("NO")

main()
    


"""
失敗作
ややこしくしすぎた。
"""
def dfs1(count,i,j):
    if i < 0 or i>=10 or j < 0 or j>=10 or count>=2 or maps[i][j]==".":
        return False
    if N == np.sum(maps==".")+np.sum(maps=="-"):
        return True
    if count == 0:
        # "-"は先回りして塗り潰している可能性があるので
        if maps[i][j] == "o" or maps[i][j] == "-":
            # print(count,i,j,maps[i][j])
            maps[i][j] = "."
            a = dfs(count,i-1,j) 
            b = dfs(count,i+1,j)     
            c = dfs(count,i,j-1)     
            d = dfs(count,i,j+1)
            return a or b or c or d
    elif count == 1:
        # print(count,i,j,maps[i][j])
        if maps[i][j] == "o":
            maps[i][j] = "-"
            a = dfs(count+1,i-1,j) 
            b = dfs(count+1,i+1,j)     
            c = dfs(count+1,i,j-1)     
            d = dfs(count+1,i,j+1)
            return a or b or c or d
        elif maps[i][j] == "-":
            return False
    if maps[i][j] == "x":
        # print(count,i,j,maps[i][j])
        a = dfs(count+1,i-1,j) 
        b = dfs(count+1,i+1,j)     
        c = dfs(count+1,i,j-1)     
        d = dfs(count+1,i,j+1)
        return a or b or c or d


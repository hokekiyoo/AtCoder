# N = int(input())
# import numpy as np

# def num(M):
#     return 3**M - 3*2**M + 3*1**M

# allnum = 0
# M = int(np.log10(N)) #桁数
# X = N // 10**M #最上位桁数

# keta = [3,7,5]
# strN = str(N)
# for i,c in enumerate(strN):
#     m = M-i
#     if int(c) == 3:
#         allnum += 3**(m-1)-3*2**(m-1)+3*1
#     if int(c) == 5:
#         allnum += 3**(m)-2*2**(m)+1
#     if int(c) == 7:
#         allnum += 2*(3**(m)-2*2**(m)+1)
#     else: break
# print(allnum)

N = int(input())
def dfs(s): # 文字列 s で始まる七五三数の個数
    if int(s) > N:
        print("invalid  ",s)
        return 0
    print("valid    ",s)
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0 # s 自体が七五三数なら +1
    for c in '753':
        ret += dfs(s+c) #ここに再起表現が入る
    return ret

print(dfs('0')) # 本当は dfs('') と書きたいが 4 行目でのエラーを防ぐため仕方なく

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

# 2019/5/8 とき直し(stack)
from collections import deque
N = int(input())
stack = deque(["0"])
cnt = 0
while len(stack)>0:
    c = stack.pop()
    for s in "357":
        cs = c+s
        if int(cs)<=N:
            stack.append(cs)
            if cs.count("3")*cs.count("5")*cs.count("7")>0:
                cnt += 1
print(cnt)
        

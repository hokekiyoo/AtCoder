# 文字列の一致を見る
# N 100なので全探索でよいだろう
# 端点には注意

N = int(input())
S = input()
T = input()
cnt = 0
for i in range(N,0,-1):
    if S[-i:]==T[:i]:
        cnt = i
        break
print(len(S)+len(T)-cnt)
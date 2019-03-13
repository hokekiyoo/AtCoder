# S = [int(i) for i in input()]
# val = 0
# def dfs(i,n):
#     global val
#     if i == 3:
#         if n == 7: print(True)
#         else : print(False)
#         return n
#     plus = dfs(i+1,n+S[i+1])
#     minus = dfs(i+1,n-S[i+1])
#     # print(plus,minus)
#     return n
# dfs(0,S[0])

S = input()
bits = ["---","--+","-+-","-++",
       "+--","+-+","++-","+++"]
"""
op = ["-","+"]として3回回しが主流？
"""

flg = False
for bit in bits:
    eq = S[0]+bit[0]+S[1]+bit[1]+S[2]+bit[2]+S[3]
    val = eval(eq)
    if val == 7:
        print(eq+"=7")
        flg=True
        break
if not flg:
    print("nothing")
"""
与えられた長さNのtをt'にする方法
各iについて、t'のi文字目はtのi,i+1文字目のどちらかである

単一文字のt'に持っていく最小操作回数

文字間差分の最大値が最も小さい文字が強い
"""

S = input()
# S = "whbrjpjyhsrywlqjxdbrbaomnw"
Sset = set(S)
ans = 1000
for s in Sset:
    string  = s+S+s
    diff = 0
    tmp = 0
    for i,st in enumerate(string): 
        if s == st:
            diff = max(diff, i-tmp) #差のmax
            tmp = i
    ans = min(ans,diff)
print(ans-1)

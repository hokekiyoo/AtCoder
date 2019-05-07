S = list(input())
n = len(S)
def dfs(count,s):
    if count == n:
        # 最後に数式を足す
        return eval(s)
    # + を挟むか否か
    plus = dfs(count+1, s+'+'+S[count]) #挟んだ場合
    nothing = dfs(count+1, s+S[count])  #挟まない場合
    return plus + nothing

print(dfs(1,S[0]))
N, K = map(int,input().split())
S = input()

cdict = {"A":"a","B":"b","C":"c"}
print(S[:K-1] + cdict[S[K-1]] + S[K:])
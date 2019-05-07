## DP問題
## ※桁数求めてから、数字を当てはめるほうがシンプルかも。

N,M = map(int,input().split())
As = list(map(str,input().split()))
match = {"1":2, "2":5, "3":5,
         "4":4, "5":5, "6":6,
         "7":3, "8":7, "9":6}
 
# test
# N, M = 10000, 9
# As = [str(i) for i in range(1,10)]
 
 
ws = {} #マッチの数に対しての、作れる数字の最大値を算出
for a in As:
    w = match[a] #数aに使うマッチの数
    try: 
        ws[str(w)] = max(a,ws[str(w)])
    except:
        ws[str(w)] = a
ks = list(map(int,ws.keys()))
ns = list(ws.values())
 
dp = ["0" for _ in range(N+1)]
for i in range(1,min(ks)):#最小
    dp[i] = "-1"
 
for i in range(N+1):
    # print(i)
    for a,k in zip(ns,ks):
        if i+k <= N:
            if dp[i] == "-1":
                dp[i+k] = str(max(int(dp[i]+a),int(dp[i+k])))
            elif dp[i] == "0":
                dp[i+k] = str(max(int(a),int(dp[i+k])))
            elif len(dp[i+k]) < len(dp[i])+1:
                    dp[i+k] = dp[i]+a
            elif len(dp[i+k]) == len(dp[i])+1:
                dp[i+k] = max(dp[i+k],dp[i]+a)
        else:
            continue
print(dp[N])
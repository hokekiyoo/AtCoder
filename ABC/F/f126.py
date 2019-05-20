M, K = map(int,input().split())


if M == 1 and K == 1:
    print(-1)
elif M==1 and K == 0:
    print("0 0 1 1")
elif K >= 2**M:
    print(-1)
else:
    M = [i for i in range(2**M)]
    M.remove(K)
    ans = M + [K] + M[::-1] + [K]
    anstr = ""
    for a in ans:
        anstr += str(a) + " "
    print(anstr[:-1])
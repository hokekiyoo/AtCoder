N,D = map(int, input().split())
if D < 100:
    print(D*(100**N))
else:
    print((D+1)*(100**N))
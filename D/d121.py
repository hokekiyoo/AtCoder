N,M = map(int,input().split())
def xor_sum(N):
    N+=1
    value = 0
    value += (N//2)%2 # 2^0の位
    for i in range(1,40):
        # print(N%(2**(i+1))-2**i)
        cnt = max(0,N%(2**(i+1))-2**i) #mod2^(i+1)のcnt
        value += (cnt%2) * 2**i
    return value

# print(xor_sum(3))
print(xor_sum(M)^xor_sum(N-1))

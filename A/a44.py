"""
1軒のホテルがあります。 このホテルの宿泊費は、次のようになっています。
最初の K泊までは、1泊あたり X円
K+1泊目以降は、1泊あたりY円
高橋君は、このホテルに N泊連続で宿泊することにしました。 高橋君の宿泊費は合計で何円になるか求めてください。
"""
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N <= K:
    value = N*X
else:
    value = K*X + (N-K)*Y
print(int(value))
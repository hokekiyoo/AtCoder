N = int(input())
# N = 100
# 素因数を足し合わせてみる
divisors = [0]*(N+1)
# 素因数分解(小さい方から順に割っていく)
for j in range(2,N+1):
    s = 0
    L = j
    while s == 0:
        for i in range(2,N+1):
            if L % i == 0:
                divisors[i] += 1
                L //= i
                if L == 1:
                    s = 1 #1はこれ以上素因数を産まない
                break
    # print("{}!:{}".format(j,divisors))

# 3パターン
# 75　*　1 パターン
# 25 * 3 パターン
# 5 * 15 パターン
# 5 * 5 * 3 パターン
list75 = [i for i,div in enumerate(divisors) if 74 <= div and i > 1]
list25 = [i for i,div in enumerate(divisors) if 24 <= div and i > 1]
list15 = [i for i,div in enumerate(divisors) if 14 <= div and i > 1]
list5 = [i for i,div in enumerate(divisors) if 4 <= div and i > 1]
list3 = [i for i,div in enumerate(divisors) if 2 <= div and i > 1]
# list2 = [i for i,div in enumerate(divisors) if 1 <= div and i > 1]
# print(list75)
# print(list25)
# print(list15)
# print(list5)
# print(list3)
# print(len(list75),len(list25),len(list15),len(list5),len(list3))
n75 = len(list75)
n25 = len(list25)
n15 = len(list15)
n5 = len(list5)
n3 = len(list3)
print(n75 + n25*(n3-1) + n15*(n5-1) + n5*(n5-1)//2*(n3-2))
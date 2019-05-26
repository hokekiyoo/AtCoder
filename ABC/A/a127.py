A, B = map(int,input().split())
if A >= 13:
    print(B)
elif 6<=A<13:
    print(B//2)
elif A<6:
    print(0)
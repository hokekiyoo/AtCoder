N,D = map(int, input().split())
"""
i-D i+D
2D+1個見ることができる

15 1 -> 5コずつ見られる

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
"""
if N%(2*D+1)==0:
    print(N//(2*D+1))
else:
    print(N//(2*D+1)+1)
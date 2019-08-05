import sys
N = int(input())
Hs = list(map(int, input().split()))[::-1]
# 後ろから貪欲のほうが良くない？
pre = 10**10
for h in Hs:
    # print(h)
    if pre - h  >= 0:
        pre = h
    elif pre - h == -1:
        pre = h -1 
    else:
        print("No")
        exit(0)
print("Yes")

"""
prev_h = -1
downflg = False
for h in Hs:
    # 増加中
    if not downflg:
        if  h - prev_h >= 0:
            prev_h = h
        elif h - prev_h == -1:
            downflg = True
            prev_h = h
        else:
            print("No")
            sys.exit()
    # 減少中
    else:
        if h - prev_h > 0:
            downflg = False
            prev_h = h
        if h - prev_h == 0:
            prev_h = h
        else:
            print("No")
            sys.exit()
    # print(h,prev_h,downflg)
    prev_h = h
print("Yes")
"""
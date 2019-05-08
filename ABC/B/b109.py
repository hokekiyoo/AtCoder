N = int(input())
ws = [input()]

flg = True
for i in range(N-1):
    Wi = input()
    if Wi in ws:
        flg = False
    elif ws[-1][-1] != Wi[0]:
        flg = False
    ws.append(Wi)

if flg:
    print("Yes")
else:
    print("No")
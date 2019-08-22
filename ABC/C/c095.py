"""
ピザ A,B,AB(half&half)
値段 A,B,C

A,BをX,Y用意する

20 310 160
A 3 B 2

"""

a,b,c,x,y = map(int, input().split())

if a+b <= 2*c:
    print(a*x+b*y)
else:
    min_xy = min(x,y)
    max_xy = max(x,y)
    # ハーフハーフで少ない方を穴埋め
    n_c = min_xy*2
    v = n_c*c + max(0,x-min_xy)*a+max(0,y-min_xy)*b
    # print(min_xy,n_c,max(0,x-min_xy))
    # ハーフハーフで余らせた方が安い場合
    N_c = max_xy*2
    V = N_c * c
    print(min(v,V))


sx,sy,tx,ty = map(int, input().split())

# cms =  list("UDRL")
# mvs = [(0,1),(0,-1),(1,0),(-1,0)]

dx = (tx-sx)
dy = (ty-sy)
ans = ""
# 一回目 s -> t -> s
ans += ("U")*dy+("R")*dx+("D")*dy+("L")*dx
# 二回目 一旦左に行く s->t
ans += "L"
ans += "U"*(dy+1)
ans += "R"*(dx+1)
ans += "D"
# 二回目 t->s
ans += "R"
ans += "D"*(dy+1)
ans += "L"*(dx+1)
ans += "U"

print(ans)
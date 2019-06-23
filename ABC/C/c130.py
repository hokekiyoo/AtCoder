W,H,x,y = map(int, input().split())
S = W*H/2.0 #長方形内であれば、中心からの対象点を選ぶ事により、2分割できる
flg = (W/2==x and H/2 ==y) #長方形の中心を通れば、2分割できる。そうじゃないとだめ

print(S,int(flg))
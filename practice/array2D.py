m, n = 3,2
A = [[0]*m]*n
B= [[0 for i in range(m)] for j in range(n)]
print("A\n", A)
print("B\n", B)

### AのIDを見る
print("ID 0 \n{}".format(id(0)))
print("ID A")
for i in range(n):
    for j in range(m):
        print(i,j,id(A[i][j]))
### BのIDを見る
print("ID B")
for i in range(n):
    for j in range(m):
        print(i,j,id(B[i][j]))

A[0][1] = 1
B[0][1] = 1
print("A\n", A)
print("B\n", B)

# http://delta114514.hatenablog.jp/entry/2018/01/02/233002

"""
代入後
"""

### AのIDを見る
print("ID 0 \n{}".format(id(0)))
print("ID 1 \n{}".format(id(1)))
print("ID A")
for i in range(n):
    for j in range(m):
        print(i,j,id(A[i][j]))
### BのIDを見る
print("ID B")
for i in range(n):
    for j in range(m):
        print(i,j,id(B[i][j]))



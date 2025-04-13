#https://zerojudge.tw/ShowProblem?problemid=b965
#題目要,求回去

r ,c ,m = map(int, input().split())
a = [[0]*c for i in range(r)]
for i in range(r):
    aa = list(map(int, input().split()))
    for j in range(c):
        a[i][j] = aa[j]
b = list(map(int, input().split()))
b = b[::-1]
for i in range(len(b)):
    if b[i] == 1:
        d = [[0]*c for i in range(r)]
        for k in range(r):
            for j in range(c):
                d[k][j] = a[r-k-1][j]
    else:
        d = [[0]*r for i in range(c)]
        for k in range(c):
            for j in range(r):
                d[k][j] = a[j][c-k-1]
    a=d
    r = len(a)
    c = len(a[0])
print(r,c)
for i in range(r):
    print(*a[i])
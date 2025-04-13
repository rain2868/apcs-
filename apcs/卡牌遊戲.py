#https://zerojudge.tw/ShowProblem?problemid=m371
n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append([int(x) for x in input().split()])

def find_down(x, y):
    for i in range(1, n - x):
        if a[x + i][y] == a[x][y]:
            return 1, x + i, y
        if a[x + i][y] != -1: 
            break
    return 0, 0, 0 

def find_right(x, y):
    for i in range(1, m - y):
        if a[x][y + i] == a[x][y]:
            return 1, x, y + i
        if a[x][y + i] != -1:
            break
    return 0, 0, 0 

point = 0

while True:
    c = 0
    for i in range(n):
        for j in range(m):
            check = 0
            if a[i][j] > -1:
                check,xx,yy = find_right(i, j)
                if check:
                    c += 1
                    point += a[i][j]
                    a[i][j] = a[xx][yy] = -1
                check,xx,yy = find_down(i, j)
                if check:
                    c += 1
                    point += a[i][j]
                    a[i][j] = a[xx][yy] = -1
                
    if c == 0:
        break
print(point)
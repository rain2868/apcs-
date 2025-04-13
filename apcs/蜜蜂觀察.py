#https://zerojudge.tw/ShowProblem?problemid=m932
m, n, k = map(int, input().split()) 
bee = [[0] * n for i in range(m)]     
for i in range(m):
    s = list(input())
    for j in range(n):
        bee[i][j] = s[j]
#移動
movve = list(map(int, input().split()))
#移動方式
def a(move, x, y):
    if move == 0:
        return x + 0, y - 1
    elif move == 1:
        return x + 1, y + 0
    elif move == 2:
        return x + 1, y + 1
    elif move == 3:
        return x + 0, y + 1
    elif move == 4:
        return x - 1, y + 0
    elif move == 5:
        return x - 1, y - 1
#主程式
x = 0
y = m-1
ans = []
for i in range(k):
    move = movve[i]
    xx = x
    yy = y    #暫存
    try:
        x,y = a(move, x, y)
        #這個王八蛋到負的還會跑
        if x < 0:
            raise
        if y < 0:
            raise
        ans.append(bee[y][x])
    except:
        x = xx
        y = yy
        ans.append(bee[y][x])
print(''.join(ans))
ans2 = set(ans)
print(len(ans2))

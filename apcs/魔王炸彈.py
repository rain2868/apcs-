n, m, k = map(int, input().split()) #輸入n*m的棋盤大小和魔王個數
b = [[0] * m for i in range(n)]     #棋盤
c = [[0] * 4 for i in range(k)]     #魔王
d = [0]*k                           #魔王開關
for i in range(k): 
    c[i] = list(map(int, input().split())) #寫入魔王座標和移動方式(x,y,+x,+y)
while sum(d)!=1*k:
    a = []
    for i in range(k):
        if d[i] == 0:
            b[c[i][0]][c[i][1]] = 1
            c[i][0] = c[i][0] + c[i][2]
            c[i][1] = c[i][1] + c[i][3]
            if 0 > c[i][0] or c[i][0] >= n or 0 > c[i][1] or c[i][1] >= m:   #如果腳下有炸彈或跑出棋盤，關掉i魔王開關
                d[i] = 1
            elif b[c[i][0]][c[i][1]] > 0:
                d[i] = 1
                a.append(i)  #先記著，避免多人同時採後面的沒算到
    for i in a:
        b[c[i][0]][c[i][1]] = 0 
print(n*m - sum(l.count(0) for l in b)) #剩餘格數

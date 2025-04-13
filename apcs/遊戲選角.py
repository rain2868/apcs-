#https://zerojudge.tw/ShowProblem?problemid=m931
a = int(input())
d = []
for i in range(a):
    x,y = map(int, input().split())
    d.append((x*x+y*y,x,y))
d.sort()
d = d[::-1]
print(d[1][1],d[1][2])
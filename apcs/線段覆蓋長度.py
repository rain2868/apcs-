a = int(input())
b = [[0]*a for i in range(2)]
for i in range(0,a-1):
    b[i] = map(int, input().split())
    for j in range(2):
        b[i] = {range(b[i][0], b[i][1])}
for i in range(0,a-2):
    c = list(b[i] or b[i+1])
if not c:
    print(-1)
else:
    print(len(c))
a = list(map(int, input().split()))

for i in range(len(a)-1):
    b = min(a[i:len(a)])
    a.remove(b)   #刪除b
    a.insert(i,b) #b加入到位置i
    print(a)

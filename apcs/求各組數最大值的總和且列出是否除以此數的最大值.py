m, n= map(int, input().split()) #m=組數，n=每組幾個
t = [] #每組最大值
for i in range(m):
    d = 0
    c = list(map(int, input().split()))
    d = max(c) #找出這組最大值
    t.append(d) #記錄
print(sum(t)) #總和每組最大值

t2 = [] #每組最大值能整除總和的數
e = 0
for j in range(m):
    if sum(t)%t[e] == 0: #如果可以總除
        t2.append(t[e]) #紀錄
    e = e + 1 #判斷下一組
if len(t2) == 0:
    print(-1)
else:
    for num in t2:
        print(num, end=" ") #尾末不換行，改空格(原print，end="enter")
#https://zerojudge.tw/ShowProblem?problemid=c291
a=int(input())
total=0
n=[int(x) for x in input().split()]
test=[False]*a
for i in range(a):
    if test[i]:continue
    test[i]=True
    total+=1
    if n[i]==i:continue
    q = n[i]
    while n[q]!=i:
        test[q]=True
        q=n[q]
    test[q]=True
print(total)
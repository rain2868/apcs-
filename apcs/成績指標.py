#https://zerojudge.tw/ShowProblem?problemid=b964
a = int(input())
b = list(map(int, input().split()))
print(*sorted(b))
x = []
xx = []
for i in b:
   if i < 60:
      x.append(i)
   else:
      xx.append(i)
if not x:
   print('best case')
else:
   print(max(x))
if not xx:
   print('worst case')
else:
   print(min(xx))
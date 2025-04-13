#https://zerojudge.tw/ShowProblem?problemid=m370

x ,n = map(int, input().split())
food = list(map(int, input().split()))
min_food = []
max_food = []
for i in range(n):
    if food[i] < x:
        min_food.append(food[i])
    else:
        max_food.append(food[i])

if len(max_food) > len(min_food):
    print(len(max_food) ,max(max_food))
else:
    print(len(min_food) ,min(min_food))
#https://zerojudge.tw/ShowProblem?problemid=d784
def ans(arr):
    now = max_num = arr[0]
    for i in arr[1:]:
        now = max(i, now + i)
        if now > max_num:
            max_num = now
    return max_num

a = int(input())
for i in range(a):
    b = [int(n) for n in input().split()]
    array = b[1:]
    print(ans(array))
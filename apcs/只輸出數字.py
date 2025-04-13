a = int(input())
for i in range(a):
    b = input()
    ans = []
    for j in b:
        if j.isdigit():
            ans.append(j)
    ans = sorted(set(ans))
    ans = ''.join(ans)
    if ans:
        print(ans)
    else:
        print('N')

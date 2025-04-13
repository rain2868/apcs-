# top-down DP O(n^3), 0-index
n = int(input())
s = [int(x) for x in input().split()]
oo = n*10000
def cost(i,j): # min cost of [i,j]
    if memo[i][j] >= 0: 
        return memo[i][j]
    imin = oo
    total = sum(s[i:j+1])
    lsum = 0 # sum of left part
    for k in range(i,j): # [i,k] and [k+1,j]
        lsum += s[k] 
        t = cost(i,k)+cost(k+1,j)+abs(total-lsum-lsum)
        if t<imin:
            imin = t
    memo[i][j] = imin
    return imin
#
memo = [[-1]*n for i in range(n)]
for i in range(n): 
    memo[i][i] = 0
ans = cost(0,n-1)
print(ans)
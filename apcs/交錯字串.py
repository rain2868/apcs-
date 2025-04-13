#https://zerojudge.tw/ShowProblem?problemid=c462
def checkfirst(d):
        if d.isupper() and not d.islower():
            return 1
        elif d.islower() and not d.isupper():
            return 2
        return 0

def checkupper(d):
        if  d.isupper() and not d.islower():
            return True
        return False

def checklower(d):
        if d.islower() and not d.isupper() :
            return True
        return False

a = int(input())
b = input()
anss = []
k = a
for i in range(len(b)-a+1):
    ans = 0
    d =  b[i:k]  
    c = checkfirst(d)    
    if c == 1:
        try:
            kk = k
            for j in range(len(b)):
                if checkupper(d):
                    ans += a
                    i += a
                    k += a
                    d =  b[i:k] 
                else:
                    raise
                if checklower(d):
                    ans += a
                    i += a
                    k += a
                    d =  b[i:k] 
                else:
                    raise
        except:
            k = kk  
    if c == 2:
        try:
            kk = k
            for j in range(len(b)):
                if checklower(d):
                    ans += a
                    i += a
                    k += a
                    d =  b[i:k] 
                else:
                    raise
                if checkupper(d):
                    ans += a
                    i += a
                    k += a
                    d =  b[i:k] 
                else:
                    raise
        except:
            k = kk
    k += 1
    anss.append(ans)
print(max(anss))

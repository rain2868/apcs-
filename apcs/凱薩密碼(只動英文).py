a = input()
b = ''
for i in a:
    if i.isalpha():
        b += chr((ord(i)-ord('a')+3)%26+ord('a')) #金鑰3。ord=將字符轉為ASCII碼,chr反之
    else:
        b += i
print(b)
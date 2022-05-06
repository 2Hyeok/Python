def fcmp(s, t):
    
    def numcmp():
        a=float(s)
        b=float(t)
        if (a<b):
            return -1
        elif (a>b):
            return 1
        else:
            return 0
        
    def strcmp():
        for i in range(min(len(s), len(t))):
            if (ord(s[i]) < ord(t[i])):
                return -1
            elif (ord(s[i]) < ord(t[i])):
                return 1
        if(len(s) < len(t)):
             return -1
        elif(len(s) > len(t)):
            return 1
        else:
            return 0

    NUM, CHARCT = 1, 2
    cond = NUM

    for i in range(len(s)):
        c = s[i]
        if i == 0 and c == '-':
            continue
        if c.isdigit() or c == '.':
            continue
        else:
            cond = CHARCT
            break

    if cond == NUM:
        for i in range(len(t)):
            c = t[i]
            if i == 0 and c == '-':
                continue
            if c.isdigit() or c == '.':
                continue
            else:
                cond = CHARCT
                break

    if cond == NUM:
        return numcmp
    else:
        return strcmp

s=input("첫번째 문자열 입력")
t=input("두번째 문자열 입력")

p=fcmp(s, t)
print(p())

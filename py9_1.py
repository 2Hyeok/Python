'''
하나의 레퍼런스 변수(ptr)로 두 함수(strcmp 와 numcmp) 를 다루는 프로그램 작성
-문자열을 비교 해 주는 함수 strcmp(s,t)
-실수로 변환 후 비교 해 주는 함수 numcmp(s, t)
-두 문자열을 조사한 후에 해당 되는 함수(이름)를 리턴 해주는 함수 fcmp(s, t)
'''
def numcmp(s, t):
    a = float(s)
    b = float(t)
    if(a < b):
        return -1
    elif(a > b):
        return 1
    else :
        return 0

def strcmp(s, t):
    for i in range(min(len(s), len(t))):
        if(ord(s[i]) < ord(t[i])):
            return -1
        elif(ord(s[i]) > ord(t[i])):
            return 1
    if(len(s) < len(t)):
        return -1
    elif(len(s) > len(t)):
        return 1
    else:
        return 0

def fcmp(s, t):
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
print(p(s, t))

'''
주어진 두 문자열의 사전상의 순서를 비교 해 주는 함수 strcmp(s, t) 를 만드시오
test) abcd abcde 입력  -> 1 (출력)
함수 콜은 res ult=strcmp(s, t)
출력은 print( result
함수에서
s 배열과 t 배열을 비교해서 s 배열이 먼저 나오면 return 1,
나중에 나오면 return 1, 같으면 return 0
ex) s 배열 : “abcde” t 배열 : “abcdf” 이면 return 1
s 배열 : “abcdf” t 배열 : “abcde” 이면 return 1
s 배열 : “abcde” t 배열 : “abcde” 이면 return 0
f or i in range(min(len(s), len(t))) :
한 요소씩 서로 비교
loop 에서 빠 져 나 와서 두 배열의 길이 가 다를 때 비교

'''
s=input("첫번째 문자열 입력 :")
t=input("두번째 문자열 입력 :")

def numcmp(s, t):
    if(s>t):
        return 1
    elif(s==t):
        return 0
    else:
        return -1

def strcmp(s, t):
    for i in range(min(len(s), len(t))):
        a,b = ord(s[i]), ord(t[i])
        if(a>b):
            return 1
        elif(a<b):
            return -1
        else:
            continue
    if len(s) > len(t):
        return 1
    elif len(s) < len(t):
        return -1
    else:
        return 0

def strcmp2(s, t):
    for i in range(min(len(s),len(t))):
        if(ord(s[i]) < ord(t[i])):
           return -1
        elif(ord(s[i]) > ord(t[i])):
             return 1
    if len(s) > len(t):
        return 1
    elif len(s) < len(t):
        return -1
    else:
        return 0

def strcmp3(*string):
    for i in range(min(len(string[0]),len(string[1]))):
        if(ord(string[0][i]) < ord(string[1][i])):
           return -1
        elif(ord(string[0][i]) > ord(string[1][i])):
             return 1
    if(len(string[0]) > len(string[1])):
        return 1
    elif(len(string[0]) < len(string[1])):
        return -1
    else:
        return 0
    
result=numcmp(s, t)
print(result)

result=strcmp(s, t)
print(result)

result=strcmp2(s, t)
print(result)

result=strcmp3(s, t)
print(result)

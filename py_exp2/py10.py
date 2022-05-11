def deco(func):
    def stricmp(*args, **kwargs):
        s = args[0].replace(' ', '')
        t = args[1].replace(' ', '')
        return func(s, t)
    return stricmp

@deco
def strcmp(s, t):
    for i in range(min(len(s), len(t))):
        a,b = ord(s[i]), ord(t[i])
        if a>b:
            return 1
        elif a<b :
            return -1
        
    if len(s) > len(t):
        return 1
    elif len(s) < len(t):
        return -1
    else :
        return 0


s=input("첫번째 문자열 : ")
t=input("두번째 문자열 : ")
print(strcmp(s, t))

'''
def deco(func):
    def stricmp(*args, **kwargs):
        s = args[0]
        t = args[1]
        s = s.replace(' ', '')
        t = t.replace(' ', '')
        return func(s, t)
    return stricmp

@deco
def strcmp(s, t):
    for i in range(min(len(s), len(t))):
        a,b = ord(s[i]), ord(t[i])
        if a>b:
            return 1
        elif a<b :
            return -1
        else:
            continue
        
    if len(s) > len(t):
        return 1
    elif len(s) < len(t):
        return -1
    else :
        return 0


s=input("첫번째 문자열 : ")
t=input("두번째 문자열 : ")
print(strcmp(s, t))
'''

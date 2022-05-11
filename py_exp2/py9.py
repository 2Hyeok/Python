'''
실습한 midstr(s, a, b) 에서 invalid parameter a 와 b 를 예외 처리 로 구현 하시오
midstr 함수에서 예외 발생 시킬 것 메인 루틴에서 예외 처리 할 것
'''
class InvalidA(Exception):
    def __inif__(self, text):
        super().__inif__(text)
class InvalidB(Exception):
    def __inif__(self, text):
        super().__inif__(text)

def midstr(s, a, b):   
    result = []
    if a > len(s):
        raise InvalidA("유효하지 않은 시작지점 입니다.:{0}".format(a))
    elif a+b-1 > len(s):
        raise InvalidB("유효하지 않은 취할갯수 입니다.:{0}".format(b))
    else:
        result = result + s[a-1:a+b-1]
    return result

s=list(input("대상 문자열 입력"))
a=int(input("시작 지점 입력"))
b=int(input("취할 갯수 입력"))

try:
    result = midstr(s, a, b)
except InvalidA as err:
    print("예외가 발생했습니다.{0}".format(err))
except InvalidB as err:
    print("예외가 발생했습니다.{0}".format(err))
else:
    print("결과 문자열은{0} 입니다".format(result))


'''
class InvalidA(Exception):
    def __inif__(self, text):
        super().__inif__(text)
class InvalidB(Exception):
    def __inif__(self, text):
        super().__inif__(text)

'''
'''
def midstr(s, a, b):   
    result = []
    if a > len(s):
        raise Exception("유효하지 않은 시작지점 입니다.:{0}".format(a))
    elif a+b-1 > len(s):
        raise Exception("유효하지 않은 취할갯수 입니다.:{0}".format(b))
    else:
        result = result + s[a-1:a+b-1]
    return result

s=list(input("대상 문자열 입력"))
a=int(input("시작 지점 입력"))
b=int(input("취할 갯수 입력"))

try:
    result = midstr(s, a, b)
except Exception as err:
    print("예외가 발생했습니다.{0}".format(err))
else:
    print("결과 문자열은{0}입니다".format(result))

'''

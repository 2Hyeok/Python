'''
주어진 리스트 에서 a 번째에서 b 개를 취하여 주는 함 수 midstr(s, a, b) 를 만 드 시오
ex) abcdefg 2 3 -> bcd

입력은 s=list(input("대상 문자열 입력"))
a= int ("시작 지점 입력")
b in t(input("취할 갯수 입력")
함 수 call 은 result = midstr(s, a, b)

출력은 print( 결과 문자열은 {0} 입니다 format(result # str(result)

함 수 에서
1) 슬라이싱 , extend , + 연산자 사용
교재 3 장 4, 6 page , 5 장 10page 참조
2) 완성후에 invalid parameter a & b 체크 항목 추가 할 것
-
결과 리스트 만들기 전에 잘못 된 a 와 b 를 별도로 체크 할 것
'''

s=list(input("대상 문자열 입력 :"))
a=int(input("시작 지점 입력 :"))
b=int(input("취할 갯수 입력 :"))

def midstr(s, a, b):
    s=s[a-1:a+b-1]
    return s

result = midstr(s, a, b)
print("결과 문자열은 {0} 입니다".format(result))

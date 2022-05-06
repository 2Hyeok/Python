'''
16 진수를 입력으로 받아서 10 진수로 만들어서 출력시켜 주는 프로그램을 짜시오
12 B 를 입력 하면 299 를 출력
입력은 s=input(“16 진수를 입력 하시오
for 문 사용
한자리 씩 10 진수로 변환 시키고 누적된 결과를 사용
16 진수 이외의 문자 일때는 sys.exit(0) 사용해서 강제 종료
ord( ) 함수 사용 문자의 내부표현 (A SIIC 코드 ) 값 알려 주는 함수
'''
import sys
s=input("16진수를 입력하시오.")
value= 0
v = 0
for c in s:
    if(c>='0' and c<='9'):
        v=ord(c)-ord('0')
    elif(c>='A'and c<='F'):
        v=ord(c)-ord('A') + 10
    else:
        print("16진수가 아닙니다.")
        sys.exit(0)
    value = value * 16 + v #누락된 것과 계산하는 부분
print("16진수 {0} 는 10진수 {1} 입니다".format(s, value))

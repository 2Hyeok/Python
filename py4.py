'''
실습
주어진 리스트 에서 또 다른 주어진 리스트 를 제거하고 역순화 시킨 리스트를 만들어 주는프로그램
ex) abcabc  b-> caca
입력은 s=list(input( 대상 문자열 입력))
t=list(input(“ 제거할 문자 열 입력))
출력은 print( 결과 문자열은 {0} 입니다 format(result)
1) while 사용해서 인 덱스로 접근해서 해결 len 함수 사용
2) for in 사용해서 순서열로 접근해서 해결
-
extend( 또는 append 메소드 와 reverse 메소드 사용해서 해결
'''

s=list(input("대상 문자열 입력"))
t=list(input("제거할 문자열 입력"))
result = []
i = 0

for i in s:
    if(i != t[0]):
        result.append(i)
        
result.reverse()

print("결과 문자열은 {0} 입니다".format(result))

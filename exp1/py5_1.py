s=list(input("대상 문자열 입력 :"))
a=int(input("시작 지점 입력 :"))
b=int(input("취할 갯수 입력 :"))

midstr = s[a-1:len(s)]
result = s[a-1:a+b-1]

print("결과 문자열은 {0} 입니다".format(result))

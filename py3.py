'''
주어진 정수형 데이터를 왼쪽으로 n bit circular shift 시켜주는 프로그램을 짜시오
010000…….000110 를 2 bit 왼쪽으로 circular shift 시키면 000000…….0110 01
입력은 num = int(i nput(“ number 입력
n = int(input(“n 입력
출력은 입력된 num 을 2 진수로 출력 , n bit circular shift 된 num 을 2 진수로 출력
'''

num = int(input("number 입력"))
n=int(input("n : "))

check = 0x8000000000000000
num1 = num
i=0

while (i<64):
    if((num1&check)==0):
        print("0",end="")
    else:
        print("1",end="")
    num1<<=1
    i+=1
print()

i = 0
while(i<n):
    if((num&check)==0):
       num=num<<1
    else:
        num=num<<1
        num=num|1
    i+=1
num1=num

i=0

while (i<64):
    if((num1&check)==0):
        print("0",end="")
    else:
        print("1",end="")
    num1<<=1
    i+=1

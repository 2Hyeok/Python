num = int(input())
check = 0x8000000000000000
i=0
num1 = num
while (i<64):
    if((num1&check)==0):
        print("0",end="")
    else:
        print("1",end="")
    check=check>>1
    i+=1
print()

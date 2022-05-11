'''
주어진 두 문자열이 모두 숫자 문자열이면 실수로 변환 해서 크기를 비교 하고 그렇지 않
으면 사전상의 순서로 크기를 비교 해 주는 프로그램을 짜시오

1)
부모 클래스 Compare
생성자 메소드 두 문자열 저장
추상 메소드 cmp
2)
2)
Compare 클래스의 자식 클래스 Strcmp
생성자 메소드 와 오버라이딩 메소드 c mp
생성자 메소드는 super 사용하여 초기화
cmp 메소드 는 문자로 비교하는 함수
3)
Compare 클래스의 자식 클래스 Numcmp
생성자 메소드 와 오버라이딩 메소드 c mp
생성자 메소드는 super 사용하여 초기화
cmp 메소드는 실수로 변환하여 비교 하는 함수
메인
루틴에서
입력은 s=input( 첫번째 문자열 입력
t input( 두번째 문자열 입력
-
s 와 t 를 조사 프로그램은 뒷 페이지에 해서 모두 숫자 문자열이면 Numcmp 객체 생성 , 그
게 아니면 Strcmp 객체 생성 후에 cmp( ) 메소드 실행
'''

class Compare:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def cmp(self):
        pass

class Strcmp(Compare):
    def __init__(self, s, t):
        super().__init__(s, t)
        
    def cmp(self):
        for i in range(len(self.s), len(self.t)):
            if ord(self.s[i]) > ord(self.t[i]):
                return 1
            elif ord(self.s[i]) < ord(self.t[i]):
                return -1
                
            if (len(self.s)) > (len(self.t)):
               return 1
            elif (len(self.s)) < (len(self.t)):
                return -1
            else:
                return 0

    
class Numcmp(Compare):
    def __init__(self, s, t):
        super().__init__(s, t)
        
    def cmp(self):
        num_s = float(self.s)
        num_t = float(self.t)

        if num_s > num_t:
            return 1
        elif num_s < num_t:
            return -1
        else:
            return 0

s=input("첫번째 문자열 입력")
t=input("두번째 문자열 입력")

        
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
    p=Numcmp(s, t)

else :
    p=Strcmp(s, t) #연결된 함수 실행

print(p.cmp())


'''
2개의 Time 인스턴스를 생성하여 인스턴스간의 산술연산(+, -) 결과와 비교연산 결과를 출력하는
프로그램을 짜시오

시간을 나타내는 Time 클래스를 정의한다.
- 시는 0~23, 분은 0~59, 초는 0~59 입력
1) 초기화(생성자) 특수 메소드 정의 하시오
- init 특수 메소드 정의 (day 는 기본값 매개변수 사용)
2) + , - 연산자를 중복 정의 하시오
- add, sub 특수 메소드 정의
- 초 로 변환해서 연산
- /, % 사용해서 시/분/초 로 변환해서 저장
- + 연산시 24시가 넘을 경우, - 연산시 0시 이전이 될 경우
3) < , > , == 연산자를 중복 정의 하시오
- lt, gt, eq 특수 메소드 정의
- 초 로 변환해서 연산
4) print 함수를 중복 정의 하시오
- repr 특수 메소드 정의

'''
class Time:
    def __init__ (self, hour, min, sec, day=0):
        self.hour = hour
        self.min = min
        self.sec = sec
        self.day = day
        
    def __add__ (self, other): #두 시간의 합
        result = self.total_T + other.total_T
        hour=result//3600
        min=(result%3600)//60
        sec=(result%3600)%60
        return Time(other.hour, other.min, other.sec, other.day)

    def __sub__ (self, other): #두 시간의 차
        result = self.total_T - other.total_T
        hour=result//3600
        min=(result%3600)//60
        sec=(result%3600)%60
        return Time(other.hour, other.min, other.sec, other.day)
    
    def __lt__ (self, other): # <
        return self.totla_T < other.total_T
    
    def __gt__ (self, other): # >
        return self.totla_T > other.total_T
    
    def __eq__ (self, other): # ==
        return self.totla_T == other.total_T

    def __repr__ (other):
        if(total_T >= 24*60*60):
            day=1
            total_T=total_T-24*60*60
            return Time(other.hour, other.min, other.sec, other.day)
            
        if(total_T<0):
            day=-1
            total_T = total_T+24*60*60
            return Time(other.hour, other.min, other.sec, other.day)
            

hour = int(input("시 입력"))
min = int(input("분 입력"))
sec = int(input("초 입력"))
first_time = Time(10, 10, 10) 
second_time = Time(hour, min, sec, day)
add_time = first_time + second_time
sub_time = first_time - second_time
print("두 시간의 합은")
print(add_time)
print("두 시간의 차는")
print(sub_time)
if (first_time > second_time):
 print("첫번째 시간이 늦은 시간입니다")
if (first_time < second_time):
 print("첫번째 시간이 이른 시간입니다")
if (first_time == second_time):
 print("두 시간이 같은 시간입니다")

class Time():
    def __init__ (self, hour, min, sec, day=0):
        self.hour = hour
        self.min = min
        self.sec = sec
        self.day = day
        
    def __add__ (self, other):
        h = m = s = d = 0
        total_sec = (self.hour*3600 + self.min*60 + self.sec) + (other.hour*3600 + other.min*60 + other.sec)
        if(total_sec >= 86400):
            total_sec -= 86400
            d = 1

        h = total_sec // 3600
        total_sec %= 3600
        m = total_sec // 60
        total_sec %= 60
        s = total_sec
        return Time(h, m, s, d)
    
    def __sub__ (self, other):
        h = m = s = d = 0
        total_sec = (self.hour*3600 + self.min*60 + self.sec) - (other.hour*3600 + other.min*60 + other.sec)
        if(total_sec >= 86400):
            total_sec -= 86400
            d = -1

        h = total_sec // 3600
        total_sec %= 3600
        m = total_sec // 60
        total_sec %= 60
        s = total_sec
        return Time(h, m, s, d)

    
    def __repr__ (self):
        return "%d일 %d시 %d분 %d초" %(self.day, self.hour, self.min, self.sec)

    def __lt__ (self, other): # <
        return (self.hour*3600 + self.min*60 + self.sec) < (other.hour*3600 + other.min*60 + other.sec)
    
    def __gt__ (self, other): # >
        return (self.hour*3600 + self.min*60 + self.sec) > (other.hour*3600 + other.min*60 + other.sec)
    
    def __eq__ (self, other): # ==
        return (self.hour*3600 + self.min*60 + self.sec) == (other.hour*3600 + other.min*60 + other.sec)


hour = int(input("시 입력"))
min = int(input("분 입력"))
sec = int(input("초 입력"))
first_time = Time(10, 10, 10)
second_time = Time(hour, min, sec)
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

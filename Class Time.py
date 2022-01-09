
"""
파일명: class Time
작성자: Koo-Bon-sik
Problem: 시(hour), 분(min), 초(sec)의 데이터 멤버를 가지는 class Time을 구현하라. class Time의 생성자
(initiator) 및 데이터 멤버에 대한 접근자 (accessor)와 변경자 (mutator)를 구현하라. 변경자에서는 데
이터 멤버의 값이 설정/변경될 때 정상적인 범위의 값으로 설정/변경되는지 확인하는 기능을 포함하도
록 하고, 생성자 __init__() 함수에서는 각 데이터 멤버의 변경자를 사용하여 초기값 설정을 하도록 하
라.
class Time 객체에 대하여 print() 함수로 출력할 때 사용되는 문자열을 제공하기 위한 __str__() 함수로
구현하라. 
10개의 class Time 인스탄스들을 임의로 생성하여 리스트에 포함시킨 후, 이들을 오름차순으로 정렬하
는 파이썬 프로그램을 작성하라. 
class Time을 사용하여 객체를 생성하고, 그 객체의 속성을 설정하며, 출력하는 시험 프로그램을 if 
__name__ == “__main__” 조건을 사용하여 실행하도록 구현하고, 실행 결과를 확인하라
"""

class Time:
    def __init__(self, hr, mn, sec):
        self.setHour(hr)
        self.setMinute(mn)
        self.setSecond(sec)
    def setHour(self, hr):
        if 0 <= hr <= 23:
            self.hour = hr
        else:
            print("*** Error in setting time (hour: {})".format(hr))
            self.hour = 0
    def setMinute(self, mn):
        if 0 <= mn <= 59:
            self.minute = mn
        else:
            print("*** Error in setting time (minute: {})".format(mn))
            self.minute = 0
    def setSecond(self, sec):
        if 0 <= sec <= 59:
            self.second = sec
        else:
            print("*** Error in setting time (second: {})".format(sec))
            self.second = 0
    def getHour(self):
        return self.hour
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second

    def __lt__(self, other): #비교연산자 사용시 호출
        if (self.hour, self.minute, self.second)< (other.hour, other.minute, other.second):
            return True
        else:
            return False
    def __str__(self):
        return "({:2d}:{:2d}:{:2d})".format(self.getHour(), self.getMinute(),self.getSecond())

if __name__ == "__main__":
    times = [
        Time(23, 59, 59),
        Time(9, 0, 5),
        Time(13, 30, 0),
        Time(3, 59, 59),
        Time(0, 0, 0),
        Time(1,1,1)
        ]
    print("times before sorting : ")
    for t in times:
        print(t)
    
    times.sort() #오름차순 정렬
    print("\ntimes after sorting : ")
    for t in times:
        print(t)

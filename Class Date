"""
파일명: class Date
작성자: Koo-Bon-sik
Problem: 연(year), 월(month), 일(day)의 데이터 멤버를 가지는 class Date를 구현하라. class Date의 생성자
(initiator) 및 데이터 멤버에 대한 접근자 (accessor)와 변경자 (mutator)를 구현하라. 변경자에서는 데
이터 멤버의 값이 설정/변경될 때 정상적인 범위의 값으로 설정/변경되는지 확인하는 기능을 포함하도
록 하고, 생성자 __init__() 함수에서는 각 데이터 멤버의 변경자를 사용하여 초기값 설정을 하도록 하
라.
class Date 객체에 대하여 print() 함수로 출력할 때 사용되는 문자열을 제공하기 위한 __str__() 함수로
구현하라. 
10개의 class Date 인스탄스들을 임의로 생성하여 리스트에 포함시킨 후, 이들을 오름차순으로 정렬하
는 파이썬 프로그램을 작성하라. 
class Date를 사용하여 객체를 생성하고, 그 객체의 속성을 설정하며, 출력하는 시험 프로그램을 if 
__name__ == “__main__” 조건을 사용하여 실행하도록 구현하고, 실행 결과를 확인하라.
"""

class Date:
    def __init__(self, yr, mt, dy):
        self.setYear(yr)
        self.setMonth(mt)
        self.setDay(dy)
    def __str__(self):
        return "({:2d}-{:2d}-{:2d})".format(self.getYear(),self.getMonth(), self.getDay())
    def __lt__(self, other): #비교연산자 사용시 호출
        #if self.__eq__(other):
        #    return False
        if ((self.year, self.month, self.day) < (other.year, other.month, other.day)):
            return True
        else:
            return False
    
    def getYear(self):
        return self.year
    def getMonth(self):
        return self.month
    def getDay(self):
        return self.day

    def setYear(self, yr):
        self.year = yr
    def setMonth(self, mn):
        if 1 <= mn <= 12: #정상적인 데이터 값인지 판별
            self.month = mn
        else:
            print("*** Error in date setting ({}, {})".format(self.year, mn))
            self.month =1
    def setDay(self, dy):
        daysOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear(self.year): #윤년인지 판별
            daysOfMonth[2]= 29 #윤년에 맞는 2월달의 일수로 변경
        if 1 <= dy <= daysOfMonth[self.month]:
            self.day = dy
        else:
            print("*** Error in date setting ({}, {}, {})".format(self.year, self.month, dy))
            self.day =1
    def isLeapYear(self, yr): #윤년인지 판별
        if ((yr %4 == 0) and (yr % 100 != 0)) or (yr % 400 == 0):
            return True
        else:
            return False

#def sorting(dates):
#    for i in range(len(dates)):
#        j=i+1
#        for j in range(len(dates)):
#            if(dates[i].__lt__(dates[j])):
#                dates[i],dates[j] = dates[j],dates[i]

if __name__ == "__main__":
    dates = [
        Date(2020, 9, 24),
        Date(2000, 9, 15),
        Date(2020, 2, 29),
        Date(2020, 1, 31),
        Date(1997, 2, 20),
        Date(2001, 5, 2),
        Date(2001, 5, 1),
        Date(1999, 3, 1)
        ]
    print("dates before sorting : ")
    for d in dates:
        print(d)
    #
    dates.sort() 
    print("\nstudents after sorting : ")
    for d in dates:
        print(d)

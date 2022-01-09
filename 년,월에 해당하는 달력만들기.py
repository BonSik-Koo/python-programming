"""
파일명: 달력만들기
작성자: Koo-bon-sik
<problem>
 날짜를 나타내는 연(year), 월(month), 일(day)의 3개 정수를 입력 받고, 이 달의 달력을 출력하는 파이썬 프로그램을 작성하라. 달력의 첫 줄은 요일을 의미하는 영문 약자 (SUN, MON, TUE, WED, THR, FRI, 
SAT)를 출력하고, 이 달의 1일 부터 요일에 맞추어 출력되도록 할 것.
"""

Day = [ "SUN","MON","TUE","WED","THR","FRI","SAT" ]
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
Month = [ "","January","February","March","April","May","June","July","August","September","October","Novermber","Decmber" ]

year, month, day= map(int,input("input year month day : ").split(" "))

print("{} of year {}".format(Month[month],year))
print("======================================")
#for j in range(0,7,1):  #일~월
#	print(("{:5}".format(Day[j])),end='')
for j in Day:  #일~월의 이름을 출력
	print(("{:>5}".format(j)),end='')
print()
print("--------------------------------------")

#입력받은 년,월까지 일수로 바꾸는 곳
elapsed=0 
for i in range(1,year):
    if (((i%4==0 and i%100!=0)) or (i%400==0)) :
        elapsed+=366
    else:
        elapsed+=365
for j in range(1,month):
        if (((year%4==0 and year%100!=0)) or (year%400==0)) :
            days[2]=29
        elapsed+=days[j]
weekday=elapsed%7 #총일수의 해당하는 요일을 해당하는 인덱스 값을 나머지 연산을 통해 받아옴

count=0 #7일마다 개행을 해주기 위한 변수
#처음 시작하는 1일 요일까지 공백으로 두기 위한 곳
for k in range(0,weekday+1,1): 
    print(("{:5}".format(' ')),end=(''))
    count=count+1

#실제 달력에 일수를 적는 부분
if (((year%4==0 and year%100!=0)) or (year%400==0)) :
    days[2]=29
for j in range(1,days[month]+1):
    print(("{:5d}".format(j)),end='')
    count =count+1
    if (count %7==0):
        print()
        count =0
print()
print("======================================")







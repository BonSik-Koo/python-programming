"""
파일명: 날짜에 해당하는 요일 구하기
작성자: Koo-bon-sik
<problem>
날짜를 나타내는 연(year), 월(month), 일(day)의 3개 정수를 입력 받고, 이 날이 서기 1년 1월 1일부터몇 번째 날짜인지를 계산하며, 이 날이 무슨 요일인지 계산하여 출력하는 파이썬 프로그램을 작성하라. 
참고로 서기 1년 1월 1일은 월요일이다. 프로그램은 0 0 0이 입력될 때 까지 반복하도록 할 것.
"""

#Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'August','Sep', 'Oct', 'Nov', 'Dec']
Day = [ "SUN","MON","TUE","WED","THR","FRI","SAT" ]
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
elapsed=0
while True:
    year, month, day= map(int,input("input year month day : ").split(" "))
    print("Input yr_mn_dy_strings : ['{}', '{}', '{}']".format(year,month,day))
    if(year==0 and month ==0 and year==0):
        break

    for i in range(1,year):
        if (((i%4==0 and i%100!=0)) or (i%400==0)) :
            #days[2]=29
            elapsed+=366
        else:
            #days[2]=28
            elapsed+=365

    for j in range(1,month):
        if (((year%4==0 and year%100!=0)) or (year%400==0)) :
            days[2]=29
        elapsed+=days[j]

    elapsed +=day
    print("Day (year ({}), month({}), day({})) : week_day ({}), elapsed {} days from JAN01AD01".format(year,month,day,Day[(elapsed%7)],elapsed))
    elapsed =0








        
    




    

    



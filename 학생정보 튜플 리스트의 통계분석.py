"""
파일명: 학생정보 튜플 리스트의 통계 분석
작성자: Koo-Bon_sic
problem :  학생 10명의 정보를 포함하는 튜플 (학생이름, 학과명, 학번, (연, 월, 일), 평균성적)들을 리스트에 포함시킨 후, 파이썬 내장함수
sum(), max(), min(),len()을 사용하여 학생들의 성적 분포 (최대, 최소, 평균)를 파악하여 출력하는 함수 statistics_student_GPA() 
함수를 구현하라
"""

Student_data = [("Kim","EE", 12345, (2000,12,25), 4.0), ("Lee","ME", 11234, (2019,9,1), 4.2), ("Park","ICE", 10234, (2019,3,1), 4.3), ("Hong","CE", 13123, (2021,1,1), 4.1),\
    ("Yoon","ICE", 11321, (2001,8,15), 4.2),("A","ICE", 12321, (2000,7,31), 4.2) ]

def statistics_student_GPA(student_list):
    L_GPAs=list(map(lambda x:x[4],student_list)) #map을 통해 lambda함수의 조건으로 list의 처음부터 끝까지 적용하여 결과값을 list로 생성
    print("statistic_student_GPA ::")
    print(" - L_GPAs = " ,L_GPAs)
    print(" - num_student = ",len(L_GPAs))
    print(" = Statistics of GPAs : Max ({}), Min ({}), Avg ({}) ".format(max(L_GPAs),min(L_GPAs),sum(L_GPAs)/(len(L_GPAs))))

print("students =")
print(Student_data)
statistics_student_GPA(Student_data)

"""
파일명: 딕셔너리 예제
작성자: Koo-Bon_sic
problem : 집합과 딕셔너리를 사용한 정보 검색
         - 총 10개의 국가에 대하여 문자열 (str) 자료형의 국가 이름과 수도 이름을 입력받고, 국가의 이름을 딕셔너리의 key로 사용하고, 그 국가의 수도의 이름 (문자열 자료형)을 value로 사용하는 딕셔너리 (dict_country_capital)를
           구성하라. 
         - 입력장치로 부터 국가 이름을 입력받아 해당 국가의 수도 이름을 찾아내는 파이썬 프로그램을 작성하라
"""

dic ={}
for i in range(10):
    nation, capital=input("Input nation and its capital (. to quit) : ").split(' ')
    dic[nation]=capital

while True:
    insert=input("Input nation to find its capital (. to quit) : ")
    if insert =='.':
        break
    else:
        print("The capital of {} is {}".format(insert,dic[insert]))

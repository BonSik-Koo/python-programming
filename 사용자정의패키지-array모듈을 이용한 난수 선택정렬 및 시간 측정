"""
파일명: 사용자 정의 패키지와 array모듈을 이용한 난수 선택정렬 및 시간 측정
작성자: Koo-Bon-Sik
problem:  앞의 Homework 7.1과 7.2에서 준비한 사용자 정의 모듈 MyList와 MySortings을 사용하여 중복되지 않는 50000개의 정수형 난수를 포함하는 리스트를 생성하라. 아울러, 파이썬 기본 제공 모듈인 array를 사
용하여 정수형 난수 리스트에 포함된 원소들을 배열에 포함시켜라. 다음 응용 프로그램을 사용하여 리스트와 배열에 포함된 난수들을 선택 정렬시키고, 실행시간을 측정하여 비교하라
"""

import sys,time
from array import *
myPyPackage_dir= "D:/사회인을 위한 파이썬"
sys.path.append(myPyPackage_dir)

from MyPyPackage.myModules import MyList, MySortings


Array=array('i') #array의 자료형을 int로 정의
L=[]
size = 50000
if __name__=="__main__":
    MyList.genRandList(L, size)

    #Array 모듈을 이용
    for x in L:
        Array.append(x)
    
    print("Array (size : {}) before sorting : ".format(size))
    MyList.printListsample(Array, 10, 2)
    t1 = time.time()
    MySortings.selectionSort(Array)
    t2 = time.time()
    print("Array (size : {}) after sorting : ".format(size))
    MyList.printListsample(Array, 10, 2)
    print("Selection sorting for array of {} integers took {} sec".format(size,t2-t1))

    #List를 이용
    print("\nList (size : {}) before sorting : ".format(size))
    MyList.printListsample(L, 10, 2)
    t1 = time.time()
    MySortings.selectionSort(L)
    t2 = time.time()
    print("\nList (size : {}) after sorting : ".format(size))
    MyList.printListsample(L, 10, 2)
    print("Selection sorting for list of {} integers took {} sec".format(size, t2-t1))
        


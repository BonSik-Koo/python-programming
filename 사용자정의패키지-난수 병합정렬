"""
파일명: 사용자 정의 패키지를 이용한 난수 병합정렬
작성자: Koo-Bon-Sik
problem: 앞에서 준비하였던 사용자 정의 모듈 “MySortings.py”에 병합정렬 (mergeSort) 기능을 수행하는 함수 메소드 mergeSort(L)를 추가하라. 다음 응용 프로그램을 사용하여 50000개의 중복되지 않는 정수형 난
수에 대한 선택정렬과 병합정렬을 각각 실행시키고, 실행에 걸린 경과시간을 측정하여 비교하라
"""

import sys, time
from array import *
myPyPackage_dir= "D:/사회인을 위한 파이썬"
sys.path.append(myPyPackage_dir)

from MyPyPackage.myModules import MyList, MySortings


if __name__=="__main__":
    while True:
        size = int(input("\nsize of list (0 to terminate)= "))
        if size <0:
            break
        else:
            L= []
            MyList.genRandList(L, size)

            #병합정렬
            print("List (size : {}) before merge sorting : ".format(size))
            MyList.printListsample(L, 10, 2)
            t1= time.time()
            L_result= MySortings.mergeSort(L)
            t2= time.time()
            print("\nList (size : {}) after merge sorting : ".format(size))
            MyList.printListsample(L_result, 10, 2)
            print("Merge sorting for list of {} integers took {} sec".format(size, t2-t1))

            #선택정렬
            MyList.shuffleList(L)
            print("\nList (size : {}) before selection sorting : ".format(size))
            MyList.printListsample(L, 10, 2)
            t1= time.time()
            MySortings.selectionSort(L)
            t2= time.time()
            print("\nList (size : {}) after selection sorting : ".format(size))
            MyList.printListsample(L, 10, 2)
            print("Selection sorting for list of {} integers took {} sec".format(size, t2-t1))

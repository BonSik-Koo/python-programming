"""
파일명: 사용자 정의 패키지를 이용한 난수 선택정렬
작성자: Koo-Bon-Sik
problem: 사용자 정의 패키지/서브패키지 “C:/MyPyPackage/myModules/” 에 선택 정렬 알고리즘을 구현한 selectionSort(L)을 포함하는 사용자 정의 “MySortings.py”을 구현하라. 앞에서 구현한 사용자 정의 모듈
"MyList.py”을 함께 사용하는 다음 응용 프로그램을 사용하여 정확한 동작을 확인하라.
"""

import sys
myPyPackage_dir= "D:/사회인을 위한 파이썬"
sys.path.append(myPyPackage_dir)

from MyPyPackage.myModules import MyList, MySortings


L=[]
n=100
if __name__=="__main__":
    MyList.genRandList(L, n)
    print("Before Sorting :")
    MyList.printListsample(L, 10 , 3)

    MySortings.selectionSort(L)
    print("\nAfter Sorting :")
    MyList.printListsample(L, 10 , 3)


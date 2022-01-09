"""
파일명: 사용자 정의 패키지를 이용한 난수 생성
작성자: Koo-Bon-Sik
problem: 사용자 정의 패키지/서브패키지 “C:/MyPyPackage/myModules/”를 생성하고, 중복되지 않는 정수형 난수의 리스트 생성, 샘플 출력 및 뒤섞기 기능을 제공하는 genRandList(L, size), printListSample(L, 
per_line, sample_lines) 및 shuffleList(L)를 포함하는 사용자 정의 모듈 “MyList.py”을 준비하라. 다음 응용 프로그램을 사용하여 정확한 동작을 확인할 것.
"""

import sys
myPyPackage_dir= "D:/사회인을 위한 파이썬"
sys.path.append(myPyPackage_dir)

from MyPyPackage.myModules import MyList

L=[]
n=100
if __name__=="__main__":
    MyList.genRandList(L, n)
    MyList.printListsample(L, 10 , 5)

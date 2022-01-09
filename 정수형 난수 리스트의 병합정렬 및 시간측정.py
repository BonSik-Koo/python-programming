"""
파일명: 정수형 난수 리스트의 정렬 및 경과시간 측정
작성자: Koo-Bon-Sik
problem : 정수형 난수 리스트의 정렬 및 경과시간 측정
        - 중복되지 않는 정수형 (int) 난수를 지정된 개수 (예: 10,000 ~ 1,000,000) 만큼 생성하는 함수 genBigRandList(L, n)을 구현하라. 
          이 함수에는 리스트 L과 리스트에 포함될 중복되지 않는 난수의 개수 n이 전달된다.
        - 주어진 리스트의 첫 부분 2줄 (한 줄에 10개씩)과 마지막 2줄을 출력하는 함수 printListSample(L, per_line, sample_lines)를 구현하라.
        - 주어진 리스트의 원소들을 오름차순으로 병합정렬 구조로 정렬하는 함수 mergeSort(L) 함수를 구현하라.
        - 표준입력장치로 부터 100,000 이상 크기의 정수형 난수 개수를 입력 받은 후, genBigRandList() 함수를 사용하여 중복되지 않는 정수형 난수 리스트를 생성하고, 이를 printListSample() 함수를 사용하여 출력하라. 이 정수형 난수 리스트를 mergeSort() 함수를 사
          용하여 정렬하고, 정렬된 상태를 printListSample() 함수를 사용하여 출력하라. 
        - 정렬에서 걸린 시간을 time 모듈의 time() 메소드를 사용하여 측정하고, 출력하라.
"""

import time
import random

def genBigRandList(L, n): 
    for i in range(n): 
        L.append(i)
    random.shuffle(L) #list L을 shuffle

def mergeSort(L):
    if len(L) < 2:
        return L
    else:
        middle=len(L)//2
        L_left=mergeSort(L[:middle]) #원소가 하나만 남을때 까지 분할
        L_right=mergeSort(L[middle:])
        return merge_sort(L_left, L_right) #분할 시킨 두 원소들을 차례로 병합

def merge_sort(L_left,L_right):
    i,j=0,0
    len_left,len_right = len(L_left), len(L_right)
    L_result=[]

    while i<len_left and j<len_right:
        if(L_left[i] < L_right[j]):
            L_result.append(L_left[i])
            i+=1
        else :
            L_result.append(L_right[j])
            j+=1

    while i<len_left: #남은 원소가 있으면 차례로 list에 삽입
        L_result.append(L_left[i])
        i+=1
    while j<len_right: #남은 원소가 있으면 차례로 list에 삽입
        L_result.append(L_right[j])
        j+=1
    return L_result

def printListsample (L ,per_line, sample_lines):
    count =0
    size = len(L) 
    for i in range(0, sample_lines): 
        s = ""
        for j in range(0, per_line): 
            if count > size:
                break
            s += "{0:>7} ".format(L[count]) 
            count += 1
        print(s) 
        if count >= size:   
            break

    if count < size:
        print('. . . . . .')
        if count <= (size - per_line * sample_lines):
            count = size - per_line * sample_lines 
            for i in range(0, sample_lines): 
                s = ""
                for j in range(0, per_line):
                    if count >= size:
                        break
                    s += "{0:>7} ".format(L[count])
                    count += 1
                print(s) 
                if count >= size:
                    break

L=[]
Per_line=10
Sample_lines=2
while True:
    number=int(input("Input size of rnadom list L (-1 to quit) = "))
    if(number<0):
        break
    else:
        genBigRandList(L,number)
        print("Before mergeSort of L:")
        printListsample(L, Per_line, Sample_lines)

        before_time=time.time()
        result_L=mergeSort(L)
        after_time=time.time()
        elspsed_time=after_time-before_time

        print("\nAfter mergeSort of L:")
        printListsample(result_L, Per_line, Sample_lines)

        print("mergeSort() for list L (size = {})  took {} sec".format(number,elspsed_time))

        




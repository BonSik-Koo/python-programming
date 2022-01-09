"""
파일명: 행렬의 출력, 연산 프로그램
작성자: Koo-Bon_sic
problem : 
- 행렬을 표현하는 2차원 리스트 1개를 행렬의 이름 (문자열)과 함께 전달받아 출력하는 함수 printMtrx(name, M)을 작성하라. 
- 2차원 리스트 2개를 전달받아 행렬의 덧셈을 계산하여 결과를 반환하는 함수 mtrxAdd(A, B), 뺄셈을 계산하여 결과를 반환하는 함수 mtrxSubtract(A, B), 그리고 곱셈을 계산하여 결과를 반환하는 함수 mtrxMultiply(A, B)를 작성하라. 
- 다음 기능 시험 프로그램을 사용하여 결과를 출력하라.
"""

def printMtrx (name,M):
    print("{} =".format(name))
    for i in range(len(M)):  #행렬의 행개수만큼
        s=""
        for j in range(len(M[0])): #행렬의 열 개수 만큼
            s+= "{:4}".format(M[i][j])
        print(s)
def mtrxAdd(A,B):
    L_result=[] #mtrx 덧셈 결과를 담아주는 리스트 생성
    a_row, a_col= len(A), len(A[0])
    b_row, b_col= len(B), len(B[0])
    
    if a_row!=b_row and a_col!=b_col:
        print("add: row, col not match!!!!")
        return 0
    else:
        for i in range(a_row):
            L_temp=[]
            for j in range(b_col):
                L_temp.append(A[i][j] + B[i][j]) #기준 행에 있는 열의 덧셈 결과를 list로 저장 
            L_result.append(L_temp) #list에 list을 넣어주면서 2차원 결과 list를 2차원 list로 만들어준다.

        return L_result

def mtrxSubtract(A,B):
    L_result=[] #mtrx 덧셈 결과를 담아주는 리스트 생성
    a_row, a_col= len(A), len(A[0])
    b_row, b_col= len(B), len(B[0])

    if a_row!=b_row and a_col!=b_col:
        print("sub: row, col not match!!!!")
        return 0
    else:
        for i in range(a_row):
            L_temp=[]
            for j in range(b_col):
                L_temp.append(A[i][j] - B[i][j]) #기준 행에 있는 열의 뺄셈 결과를 list로 저장 
            L_result.append(L_temp) #list에 list을 넣어주면서 2차원 결과 list를 2차원 list로 만들어준다.

        return L_result

def mtrxMultiply(A,B):
    L_result=[] #mtrx 덧셈 결과를 담아주는 리스트 생성
    a_row, a_col= len(A), len(A[0])
    b_row, b_col= len(B), len(B[0])

    if a_col!=b_row:
        print("Mult: row, col not match!!!!")
        return 0
    else:
        for i in range(a_row):
            L_temp=[]
            for j in range(b_col):
                mult_result=0
                for k in range(a_col):
                    mult_result+=A[i][k] * B[k][j]
                L_temp.append(mult_result) #기준 행에 있는 열의 곱셈 결과를 list로 저장 
            L_result.append(L_temp) #list에 list을 넣어주면서 2차원 결과 list를 2차원 list로 만들어준다.

        return L_result

A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
B = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

printMtrx("A", A)
printMtrx("B", B)

C = mtrxAdd(A, B)
printMtrx("A+B", C)

D = mtrxSubtract(A, B)
printMtrx("A-B", D)

E = mtrxMultiply(A, B)
printMtrx("A*B", E)

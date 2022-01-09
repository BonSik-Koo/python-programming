"""
파일명: class Mtrx
작성자: Koo-Bon-sik
Problem: 행렬 (matrix)의 덧셈, 뺄셈, 곱셈 연산을 연산자 오버로딩 기능으로 사용할 수 있게 하는 class Mtrx를
구현하라. class Mtrx의 생성자 (initiator) 및 덧셈, 뺄셈, 곱셈 연산을 위한 연산자 오버로딩 멤버함수를
구현하고, class Mtrx 객체에 대하여 print() 함수로 출력할 때 사용되는 문자열을 제공하기 위한
__str__() 함수로 구현하라. 
2개의 4 x 5 class Mtrx 인스탄스 m1와 m2, 1개의 5 x 4 class Mtrx 인스탄스 m3를 임의로 생성하고, m4 
= m1 + m2; m5 = m1 – m2; m6 = m1 * m3를 계산하여 시험 프로그램을 if __name__ == 
“__main__” 조건을 사용하여 실행하도록 구현하고, 실행 결과를 확인하라.
"""

class Mtrx:
    def __init__(self,name,n_row,n_col,L_date):
        self.name=name
        self.row=n_row
        self.col=n_col

        index=0
        self.mtrx=[]
        for i in range(self.row):
            L_low=[]
            for j in range(self.col):
                L_low.append(L_date[index])
                index=index+1
            self.mtrx.append(L_low)
    def setName(self, name):
        self.name = name
    def __str__(self):
        s = "{} = \n".format(self.name)
        for i in range(0, self.row):  
            for j in range(0, self.col):
                s += "{:3d}".format(self.mtrx[i][j], end=" ")
            s += "\n"
        return s

    def __add__(self, other): # operator overloading of '+'
        L_res = []
        for i in range(0, self.row):
            for j in range(0, self.col):
                r_ij= self.mtrx[i][j] + other.mtrx[i][j]
                L_res.append(r_ij)
        return Mtrx("R", self.row, self.col, L_res)
    def __sub__(self, other): # operator overloading of '-'
        L_res = []
        for i in range(0, self.row):
            for j in range(0, self.col):
                r_ij= self.mtrx[i][j] - other.mtrx[i][j]
                L_res.append(r_ij) 
        return Mtrx("R", self.row, self.col, L_res)
    def __mul__(self, other): # operator overloading of '*'
        L_res = []
        for i in range(0, self.row):
            for j in range(0, other.col):
                r_ij= 0
                for k in range(0, other.row):
                    r_ij = r_ij + self.mtrx[i][k] * other.mtrx[k][j]
                L_res.append(r_ij) 
        return Mtrx("R", self.row, other.col, L_res)

def main():
    L_1 = [ 1, 2, 3, 4, 5,6, 7, 8, 9, 10,11, 12, 13, 14, 15,16, 17, 18, 19, 20]
    L_2 = [1, 0, 0, 0, 0,0, 1, 0, 0, 0,0, 0, 1, 0, 0,0, 0, 0, 1, 0]
    L_3 = [0, 0, 0, 0,1, 0, 0, 0,0, 1, 0, 0,0, 0, 1, 0,0, 0, 0, 1 ]

    m1 = Mtrx("M1", 4, 5, L_1) 
    print(m1)
    m2 = Mtrx("M2", 4, 5, L_2) 
    print(m2)
    m3 = Mtrx("M3", 5, 4, L_3)
    print(m3)
    m4 = m1 + m2
    m4.setName("M4 = M1 + M2")
    print(m4)
    m5 = m1 - m2
    m5.setName("M5 = M1 - M2") 
    print(m5)   
    m6 = m1 * m3
    m6.setName("M6 = M1 * M3") 
    print(m6)

if __name__ == "__main__":
    main()



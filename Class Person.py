"""
파일명: class Person
작성자: Koo-Bon-sik
Problem: 문자열 자료형의 속성인 이름 (name), 정수형 속성인 주민등록번호 (reg_id)와 정수형 속성인 나이
(age)를 가지는 class Person을 구현하라. class Person의 생성자 (initiator), name, reg_id와 age의 접
근자 (accessor) 및 변경자 (mutator)를 구현하라. 변경자에서는 데이터 멤버의 값이 설정/변경될 때 정
상적인 범위의 값으로 설정/변경되는지 확인하는 기능을 포함하도록 하고, 생성자 __init__() 함수에서
는 각 데이터 멤버의 변경자를 사용하여 초기값 설정을 하도록 하라.
class Person 객체에 대하여 print() 함수로 출력할 때 사용되는 문자열을 제공하기 위한 __str__() 함수
로 구현하라. 
class Person을 사용하여 객체를 생성하고, 그 객체의 속성을 설정하며, 출력하는 시험 프로그램을 if 
__name__ == “__main__” 조건을 사용하여 실행하도록 구현하고, 실행 결과를 확인하라.
"""

class Person:
    def __init__(self,name=None,reg_id=None,age=None): #해당 클래스에서 사용할 데이터멤버를 생성 및 초기화
        self.setName(name)
        self.setid(reg_id)
        self.setAge(age)
    #def __new__(cls, *args, **kwargs):  
    #    cls.__inst=super(Person,cls).__new__(cls) #해당 person클래스의 부모의 new를 실행 시킨다.
    def getName(self):
        return self.name
    def getid(self):
        return self.id
    def getage(self):
        return self.age
    def setName(self, nm):
        self.name=nm
    def setAge(self,age):
        if 0 <= age < 250: 
            self.age = age
        else:
            print("*** Error in setting age (name:{}, age:{})".format(self.name, age))
            self.age = 0 
    def setid(self,id):
        self.id=id
    def __str__(self):
        return "Person({}, {},{})".format(self.getName(),self.getid(), self.getage())

def printPersonList(L_persons):
    for p in L_persons:
        print(" ", p)

if __name__ == "__main__":
    persons = [
    Person("Kim", 990101, 21),
    Person("Lee", 980715, 22),
    Person("Park", 101225, 20),
    Person("Hong", 110315, 19),
    Person("Yoon", 971005, 23),
    Person("Wrong", 100000, 350)
    ]
print("persons : ")
printPersonList(persons)

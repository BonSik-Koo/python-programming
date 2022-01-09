"""
파일명: class Student(Person상속)
작성자: Koo-Bon-sik
Problem: 위 문제 8.1에서 구현한 class Person을 상속받는 class Student를 구현하라. class Student는 추가
적인 속성으로 정수형의 학번 (student_id), 문자열의 전공명 (major), 실수형 (float)의 평균성적 (GPA)
를 가진다. class Student의 생성자 (initiator) 및 student_id, major, GPA의 접근자 (accessor)와 변경자
(mutator)를 구현하라. 변경자에서는 데이터 멤버의 값이 설정/변경될 때 정상적인 범위의 값으로 설정
/변경되는지 확인하는 기능을 포함하도록 하고, 생성자 __init__() 함수에서는 각 데이터 멤버의 변경자
를 사용하여 초기값 설정을 하도록 하라.
class Student 객체에 대하여 print() 함수로 출력할 때 사용되는 문자열을 제공하기 위한 __str__() 함수
로 구현하라. 
10명의 학생 정보를 class Student로 생성하여 리스트에 포함시키고, 이 학생들을 이름 순, 학번 순, 
성적 순으로 정렬하여 출력하는 시험 프로그램을 if __name__ == “__main__” 조건을 사용하여 실행하
도록 구현하고, 실행 결과를 확인하라."""

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

class Student(Person):
    def __init__(self, name,reg_id,age, st_id, major, gpa):
        Person.__init__(self, name,reg_id, age)
        self.setMajor(major)
        self.setSTID(st_id)
        self.setGPA(gpa)

    def getMajor(self):
        return self.major
    def getSTID(self):
        return self.st_id
    def getGPA(self):
        return self.gpa
    def setSTID(self,st_id):
        self.st_id=st_id
    def setGPA(self,gpa):
        self.gpa=gpa
    def setMajor(self, major):
        # checking available major
        set_majors = {"EE", "ICE", "ME", "CE"}
        if major in set_majors:
            self.major = major
        else:
            print("*** Error in setting major (name:{}, age:{})".format(self.name, major))
            self.major = None # default value
    def __str__(self):
        return "Student ( {}, {}, {}, {}, {}, {} )".format(self.getName(),self.getid(),self.getage(),self.getSTID(),self.getMajor(),self.getGPA())

def compareStudent(st1, st2, compare):
    if compare == "st_id":
        if st1.st_id < st2.st_id:   
            return True
        else:
            return False
    elif compare == "name":
        if st1.name < st2.name:
            return True
        else:
            return False
    elif compare =="GPA":
        if st1.gpa < st2.gpa:
            return False
        else:
            return True
def sortStudent(L_st, compare):
    for i in range(0, len(L_st)):
        min_idx = i
        for j in range(i+1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], compare):
                min_idx = j
        if min_idx != i:
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]
def printStudents(L_st):
    for s in range(len(L_st)):
        print(L_st[s])

if __name__ == "__main__":
    students = [
    Student("Kim",990101, 21, 12345, "EE", 4.0),
    Student("Lee",980715, 22, 11234, "ME", 4.2),
    Student("Park",101225, 20, 10234, "ICE", 4.3),
    Student("Hong",110315, 19, 13123, "CE", 4.1),
    Student("Yoon", 971005,23, 11321, "ICE", 4.2),
    Student("Wrong", 100000,23, 15321, "None", 3.2)
    ]
    print("students before sorting : ")
    printStudents(students)
    #
    sortStudent(students, "name")
    print("\nstudents after sorting by name : ")
    printStudents(students)
    #
    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudents(students)
    #
    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudents(students)


"""
파일명: 텍스트 파일에서 학생정보 분석
작성자: Koo-Bon-Sik
problem:  최소 10명의 학생 정보인 (학생 이름, 국어점수, 영어점수, 수학점수, 과학점수) 데이터를 텍스트 파일 student_records.txt에 준비하고, 이 파일을 읽어 들인 후, 각 학생의 평균점수를 계산하여 학생 정보에
추가하고, 각 과목별로 학생들의 성적을 종합하여 평균 점수를 계산한 후, 결과를 output.txt 텍스트 파일에 출력하는 파이썬 프로그램을 작성하라.
"""

def fread_text(f_name):
    data_list=[]
    f=open(f_name, 'r')
    for line in f: #readlines형태로 작동(개행까지 한번에 다 받아옴)
        name, kor, eng, math,sci = line.split()
        temp=[name, int(kor), int(eng), int(math), int(sci)]
        data_list.append(temp)
    f.close()
    return data_list

def fwrite_data(file_name, data_list):
    f = open(file_name, 'w')
    f.write(" {:<8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8} \n".format("name", "Kor", "eng","math", "sci","sum","avg"))  
    #f.write("‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐\n")
    for data in data_list:
        s = "{0:<8} :".format(data[0])
        s += "{0:>8},".format(data[1])
        s += "{0:>8},".format(data[2])
        s += "{0:>8},".format(data[3])
        s += "{0:>8},".format(data[4])
        s += "{0:8d},".format(data[5])
        s += "{0:8.2f}".format(data[6])
        s += '\n'
        f.write(s)
    f.close()

def write_data(data_list):
    print(" {:<8} {:>8} {:>8} {:>8} {:>8} {:>8} {:>8}".format("name", "Kor", "eng","math", "sci","sum","avg"))
    print("‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐--------------------------\n")
    for data in data_list:
        s = "{0:<8} :".format(data[0])
        s += "{0:>8},".format(data[1])
        s += "{0:>8},".format(data[2])
        s += "{0:>8},".format(data[3])
        s += "{0:>8},".format(data[4])
        s += "{0:8d},".format(data[5])
        s += "{0:8.2f}".format(data[6])
        s += '\n'
        print(s)

def cal_score(data):
    for i in range(len(data)):
        sum=data[i][1] + data[i][2] + data[i][3] +data[i][4]
        data[i].append(sum) #data[i][5]:sum
        data[i].append(sum/4.0) #data[i][6]:avg

def cal_each_class(data):
    each_class_avg=[]
    kor_sum=0 ; eng_sum=0; math_sum=0; sci_sum=0

    for name, kor, eng, math, sci in data:
        kor_sum+=kor; eng_sum+=eng; math_sum+=math; sci_sum+=sci
    each_class_avg.append(kor_sum/5.0)
    each_class_avg.append(eng_sum/5.0)
    each_class_avg.append(math_sum/5.0)
    each_class_avg.append(sci_sum/5.0)

    return each_class_avg

stu_data=[]
if __name__ == "__main__":
    f_st_name = "student_records.txt"
    o_st_name = "output.txt"

    stu_data=fread_text(f_st_name)
    for st in stu_data:
        print(st)

    each_class=cal_each_class(stu_data) #각각의 class의 평균값 계산

    cal_score(stu_data) #각각의 학생의 과목 합,평균을 계산
    print("\nAfter calculate_scores(students")
    write_data(stu_data) #출력창에 씀

    print("Average score of each class")
    print("Kor_avg = {:4.2f}".format(each_class[0]))
    print("Eng_avg = {:4.2f}".format(each_class[1]))
    print("Math_avg = {:4.2f}".format(each_class[2]))
    print("Sci_avg = {:4.2f}".format(each_class[3]))

    fwrite_data(o_st_name, stu_data) #텍스트 파일에 씀


<student_records.txt>
Lee 80 90 95 90
Kim 85 75 70 95
Park 70 80 90 85
Yoon 80 85 90 85
Hong 75 85 85 80

<output.txt>
 name          Kor      eng     math      sci      sum      avg 
Lee      :      80,      90,      95,      90,     355,   88.75
Kim      :      85,      75,      70,      95,     325,   81.25
Park     :      70,      80,      90,      85,     325,   81.25
Yoon     :      80,      85,      90,      85,     340,   85.00
Hong     :      75,      85,      85,      80,     325,   81.25






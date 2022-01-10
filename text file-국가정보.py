"""
파일명: 텍스트파일-국가정보
작성자: Koo-Bon-Sik
problem:  최소 10개 국가의 기본 정보 (국가 이름, 수도 이름, 인구수, 면적) 데이터를 텍스트 파일 (demography.txt)에 준비하고, 이 파일의 국가 기본 정보를 읽어 들인 후 순차적으로 화면에 출력하는 파
이썬 프로그램을 작성하라. 한 줄에 한 국가씩 출력할 것. 데이터 파일로 부터 읽어 들인 국가들의 기본정보에서 인구 수를 기준으로 내림차순 정렬을 하고, 그 순서대로 국가 기본 정보를 출력하는 파이썬 프
로그램을 작성하라.
"""

if __name__=="__main__":
    country=[]
    temp=[]
    r_file=open("demography.txt", "r")
    #size=os.path.getsize(r_file) #file의 size을 읽어온다(byte)
    while True:
        read_data=r_file.readline() #파일에서 한줄씩(개행까지)읽는다. 
        if read_data =="": #정확한 의미 보기!!!!!!!!!!!
            break

        nat, cap, peo, area = read_data.split() #공백(스페이스, 탭, 엔터등)기준으로 나눈다
        data=(nat, cap , int(peo), int(area)) #tuple형태로 저장
        country.append(data) #tuple형태로 list에 저장

    print("List of countries : ")
    for i in range(len(country)):
        print("Country[{}] : {}".format(i,country[i]))

    print("\nList of countries sorted by demography(number of people) :")
    country.sort(key=lambda x : x[2],reverse=True) #내림차순 정렬 people을 기준으로
    for i in range(len(country)):
        print("Country[{}] : {}".format(i,country[i]))


<demography.txt>
Korea Seoul 51780579 220918
USA WAS_DC 329479633 983517
Canada Ottawa 36488800 9984670
China Beijing 1402727120 9596960
India NewDelhi 1360657785 3287263
Brazil Brazilia 211349952 8515767





            
            
        


    

"""
파일명: Json, pickle 파일 비교 (정수형 난수)
작성자: Koo-Bon-Sik
problem: json 파일과 pickle 파일의 비교 100만개의 중복되지 않는 정수형 난수를 포함하는 리스트를 생성하고, 이 리스트를 json과
pickle의 dump() 함수를 사용하여 파일로 저장한 후, 각 파일의 크기를 비교하고, 왜 파일 크기의 차이가 나는지에 대하여 설명하라.
"""

import sys,json, pickle,os.path
myPyPackage_dir= "E:/사회인을 위한 파이썬"
sys.path.append(myPyPackage_dir)
from MyPyPackage.myModules import MyList, MySortings,CustomJsonEncoder

L=[]
def main():
    w_file="json_pickle.txt"
    f=open(w_file,'w')
    f.write("Generating a List of 1000000 random integer elements....\n")
    MyList.genRandList(L,1000000)
    result=MySortings.mergeSort(L)

    f.write("L (size= 1000000) =\n")
    MyList.fprintListsample(f, result , 10 ,2)

    size=sys.getsizeof(result)
    f.write("sys.getsizeof(L): {}\n".format(size))
    
    f_json = open("json.txt", "w")
    json.dump(result, f_json, indent=4, cls=CustomJsonEncoder.CustomEncoder)
    f_json.close()
    size_f_json = os.path.getsize("json.txt")
    f.write("size of json.txt = {} ".format(size_f_json))
    
    f_pickle = open("pickle.bin", "wb")
    pickle.dump(result, f_pickle)
    f_pickle.close()
    size_f_pickle = os.path.getsize("pickle.bin")
    f.write("\nsize of pickle.bin = {}".format(size_f_pickle))

    f.close()
    
if __name__=="__main__":
    main()

<json_pickle.txt>
Generating a List of 1000000 random integer elements....
L (size= 1000000) =
      0       1       2       3       4       5       6       7       8       9 
     10      11      12      13      14      15      16      17      18      19 
. . . . . .
 999980  999981  999982  999983  999984  999985  999986  999987  999988  999989 
 999990  999991  999992  999993  999994  999995  999996  999997  999998  999999 
sys.getsizeof(L): 8448728
size of json.txt = 12888893 
size of pickle.bin = 4871352


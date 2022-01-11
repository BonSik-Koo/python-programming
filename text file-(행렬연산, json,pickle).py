import json, pickle
import os,os.path
import sys, time
myPyPackage_dir= "E:/사회인을 위한 파이썬"
sys.path.append(myPyPackage_dir)
from MyPyPackage.myModules import myClassMtrx, CustomJsonEncoder

def read_text(file_name):
    L_data=[]
    f=open(file_name, 'r')

    row, col = map(int,f.readline().split())
    for i in range(row):
        data =list(map(float,f.readline().split()))
        L_data.extend(data)
    mA = myClassMtrx.Mtrx("MA", row, col, L_data) 

    L_data=[]
    data=[]
    row, col = map(int,f.readline().split())
    for i in range(row):
        data =list(map(float,f.readline().split()))
        L_data.extend(data)
    mB = myClassMtrx.Mtrx("MB", row, col, L_data) 

    L_data=[]
    data=[]
    row, col = map(int,f.readline().split())
    for i in range(row):
        data =list(map(float,f.readline().split()))
        L_data.extend(data)
    mC = myClassMtrx.Mtrx("MC", row, col, L_data) 

    f.close()
    return mA, mB ,mC

def fwrite_text(f, M):
    s = "{} = \n".format(M.name)
    for i in range(0, M.row):  
        for j in range(0, M.col):
            s += "{:5}".format(M.mtrx[i][j], end=" ")
        s += "\n"
    f.write(s)

#9.3
def main_1():
    r_file="matrix.txt"
    w_file="mtrx_output.txt"
    f=open(w_file,'w')
    
    mA,mB,mC =read_text(r_file) #파일에 있는 데이터들을 배열에 담아옴
    
    mD = mA + mB
    mD.setName("mD = mA + mB")
    mE = mA - mB
    mE.setName("mE = mA - mB") 
    mF = mA * mC
    mF.setName("mF = mA * mB") 

    fwrite_text(f,mA)
    fwrite_text(f,mB)
    fwrite_text(f,mC)
    fwrite_text(f,mD)
    fwrite_text(f,mE)
    fwrite_text(f,mF)
    f.close()

#9.4
def main_2():
    r_file="matrix.txt"
    w_file="mtrx_output.txt"
    f=open(w_file,'w')
    
    mA,mB=read_text(r_file) #파일에 있는 데이터들을 배열에 담아옴
    
    mC = mA + mB
    mC.setName("mC = mA + mB")
    mD = mA - mB
    mD.setName("mD = mA - MmB") 
    mE = mA * mB
    mE.setName("mE = mA * mB") 

    fwrite_text(f,mA)
    fwrite_text(f,mB)
    fwrite_text(f,mC)
    fwrite_text(f,mD)
    fwrite_text(f,mE)
    
    # Comparison of storage of mA in JSON text file and pickle bin file
    f_json = open("mA_json.txt", "w")
    json.dump(mA, f_json, indent=4, cls=CustomJsonEncoder.CustomEncoder)
    f_json.close()
    size_f_json = os.path.getsize("mA_json.txt")
    f.write("\nsize of mA_json.txt ={} ".format(size_f_json))
    
    f_pickle = open("mA_pickle.bin", "wb")
    pickle.dump(mA, f_pickle)
    f_pickle.close()
    size_f_pickle = os.path.getsize("mA_pickle.bin")
    f.write("\nsize of mA_pickle.bin = {} ".format(size_f_pickle))

    f.close()
if __name__=="__main__":
    main_1()
    #main_2()

<matrix.txt>
4 5
1.0 0.0 0.0 0.0 0.0
0.0 1.0 0.0 0.0 0.0
0.0 0.0 1.0 0.0 0.0  
0.0 0.0 0.0 1.0 0.0
4 5
1.0 2.0 3.0 4.0 5.0
6.0 7.0 8.0 9.0 10.0
11.0 12.0 13.0 14.0 15.0 
16.0 17.0 18.0 19.0 16.0
5 4
1.0 2.0 3.0 4.0 
6.0 7.0 8.0 9.0 
11.0 12.0 13.0 14.0  
16.0 17.0 18.0 19.0 
21.0 22.0 23.0 24.0 

<mtrx_output.txt>
MA = 
  1.0  0.0  0.0  0.0  0.0
  0.0  1.0  0.0  0.0  0.0
  0.0  0.0  1.0  0.0  0.0
  0.0  0.0  0.0  1.0  0.0
MB = 
  1.0  2.0  3.0  4.0  5.0
  6.0  7.0  8.0  9.0 10.0
 11.0 12.0 13.0 14.0 15.0
 16.0 17.0 18.0 19.0 16.0
MC = 
  1.0  2.0  3.0  4.0
  6.0  7.0  8.0  9.0
 11.0 12.0 13.0 14.0
 16.0 17.0 18.0 19.0
 21.0 22.0 23.0 24.0
mD = mA + mB = 
  2.0  2.0  3.0  4.0  5.0
  6.0  8.0  8.0  9.0 10.0
 11.0 12.0 14.0 14.0 15.0
 16.0 17.0 18.0 20.0 16.0
mE = mA - mB = 
  0.0 -2.0 -3.0 -4.0 -5.0
 -6.0 -6.0 -8.0 -9.0-10.0
-11.0-12.0-12.0-14.0-15.0
-16.0-17.0-18.0-18.0-16.0
mF = mA * mB = 
  1.0  2.0  3.0  4.0
  6.0  7.0  8.0  9.0
 11.0 12.0 13.0 14.0
 16.0 17.0 18.0 19.0


   


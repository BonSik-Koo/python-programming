"""
파일명: 동적 프로그래밍 구조의 피보나치 수열 계산
작성자: Koo-Bon_sic
problem : 
- Fibonacci 수열을 신속하게 계산할 수 있도록 memo 기능을 포함하는 재귀함수 dynFibo(n)를 구성하고, 시작 (start), 끝 (end), 간격 (stride)의 정수를 입
력 받은 후 해당 순서의 피보나치 수열을 출력하는 프로그램을 작성하라. 각 단계별 피보나치 수열 계산에서 이미 메모에 포함된 피보나치 수열 값은 별
도로 계산하지 않고 메모의 내용을 사용하며, 이전에 계산된 적이 없은 피보나치 수열 값은 재귀함수를 사용하여 계산한 후, 이를 메모에 기록하여 두고, 
계산된 결과값을 반환하도록 하라.
- 이 프로그램에서는 dynFibo(n)에서 걸린 경과 시간을 time() 함수를 사용하여 측정한 후, 계산된 피보나치 수열과 함께 출력하도록 하라. start = 50, end= 100, stride = 5로 설정하여 실행 결과를 출력하라
"""

import time

memo={} #피보나치의 계산을 저장해두는 dict
def dynFibo(n):
    if n in memo:
        return memo[n] #dict의 해당 key에 있는 valude를 return해준다.
    if n <=1 :
        memo[n]=n #dict에 해당 key에 위치에 value를 넣어준다.
        return n
    else:
        result= dynFibo(n-1) + dynFibo(n-2)
        memo[n]=result #dict에 해당 key에 위치에 value를 넣어준다.
        return result

start, stop, step = map(int , input("input start, stop, step of Fibonacci series : ").split(" "))
for i in range(start,stop+1,step):
    before_time=time.time()
    result = dynFibo(i)
    after_time=time.time()
    diff_time= after_time- before_time
    print("dynFibo ({:3} = {:30}, took {:10.2f}[milli_sec]".format(i,result,diff_time))




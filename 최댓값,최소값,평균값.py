"""파일명: 최댓값,최소값,평균값
   작성자: koo-bon-sik  """

data=[]
sum=0
count=0
for i in range(10):
    num = float(input("input {}-th float data = ".format(i)))
    data.append(num)
    sum +=num
    count =count +1

    if i==0:
        min=max=num
        continue
    if num < min:
        min=num
    if num > max:
        max=num

print("input data = ",data)
print("min = {}, max = {}, avg = {}".format(min,max,sum/count))

    

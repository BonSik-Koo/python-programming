"""
파일명: bit wise
작성자: Koo-bon-sik
<problem>
3개의 16진수 x, y, z를 각각 입력 받고, 이 16진수 x와 y의 bit-wise and, bit-wise or, bit-wise exclusive or 값을 각각 계산하여 2진수 및 16진수로 출력하며, x의 bit-wise not과 bit-wise left 
shift 2, y와 z의 bitwise right shift 2를 각각 출력하는 파이썬 프로그램을 작성하고, 실행 결과를 제출하라. 각 출력 항목들은 오른쪽으로 줄 맞춤 할 것
"""
#16진수로 입력받음 (8진수 8, 2진수 2)
x= int(input("hexadcimal x = "),16) 
y= int(input("hexadcimal y = "),16)
z= int(input("hexadcimal z = "),16)

print("x = {:6} int decimal, {:>#10b} in bits".format(x,x)) # '>'오른쪽 정렬
print("y = {:6} int decimal, {:>#10b} in bits".format(y,y))
print("z = {:6} int decimal, {:>#10b} in bits".format(z,z))

print("x & y = in hex({:#6x}), in bin({:>#10b})".format((x&y),x&y))
print("x | y = in hex({:#6x}), in bin({:>#10b})".format((x|y),x|y))
print("x ^ y = in hex({:#6x}), in bin({:>#10b})".format((x^y),x^y))
print("~x = in hex({:#6x}), in bin({:>#10b})".format((~x),~x))
print("x << 2 = in hex({:#6x}), in bin({:>#10b})".format((x<<2),x<<2))
print("x >> 2 = in hex({:#6x}), in bin({:>#10b})".format((y>>2),y>>2))
print("z >> 2 = in hex({:#6x}), in bin({:>#10b})".format((z>>2),z>>2))

"""
파일명: 16진수 비트연산
작성자: Koo-bon-sik
<problem>
2개의 16진수 데이터 문자열을 한 줄로 입력 받고, 이를 정수로 변환하여 a와 b에 저장하라. 이 두 16진수 a, b의 bit-wise AND, bit-wise OR, bit-wise XOR 값을 계산하여 출력하는 파이썬 프로그램을 작성하
라. 
"""

a,b=input("input two hexadecimal numbers (예: 0xA3 0x3A) : ").split(' ') #16진수 문자열 2개를 입력 받음

a=int(a,16) #16진수 문자열을 16진수 정수형으로 변환
b=int(b,16)#16진수 문자열을 16진수 정수형으로 변환

print("a = {} = {}".format(hex(a),bin(a))) #hex,bin->문자열이다
print("b = {} = {}".format(hex(b),bin(b)))
print("a & b = {} = {}".format(hex(a&b),bin(a&b)))
print("a | b = {} = {}".format(hex(a|b),bin(a|b)))
print("a ^ b = {} = {}".format(hex(a^b),bin(a^b)))








a = 100
b = 200
c = 500
if  a > b and not(not(a > c)):
    print(a, " a  is gratter than ", b, "and c", c)
elif b > a and b > c:
    print(b, "b  is gratter than ", a, "and c", c)
else:
    # print()
    print(c, " c is gratter than a ", a, "and b ", b)

"""
while loops will be run until condition is True, once condition reach to false it will be stop
"""
num = 5
while num>0:
    print('num is : ', num)
    num=num-2

"""
range operator
range(start, stop , increment/decrement);
by default range will start from 0 index  and decrease index by -1 stil condition will be
reach at stop point
if you want o operate for loop on number we have to convert it into number range and then  it will be 
operate
"""
print('num  is ', num)
num=5
#  k in range(num) :
nums=range(num)
for k in nums:
    print('k is ', k)


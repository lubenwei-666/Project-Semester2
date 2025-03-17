# the factorial of that number
# author: Zhang Junhao
# DATE:25/3/17

a = int(input("please input a number to caculate the factorial of it:"))
c = a
b = 1
while a>0:
   b=b*a
   a = a-1
print (f"the factorial of {c} is {b}")

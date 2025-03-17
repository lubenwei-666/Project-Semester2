# the factorial of that number
# author: zhang Junhao
# DATE:25/3/17

a = int(input("please enter the number to caculate the factorial of it:"))
c = a
b = 1
for i in range(1,a+1):
    b = b*i
print(f"the factorial of {c} is {b}")

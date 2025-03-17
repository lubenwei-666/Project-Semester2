# prompts the user for their age
# author: Zhang Junhao
# DATE: 25/3/17


age = -1
while age<0:
   age = int(input("please enter your age:"))
if age <=19:
    print("you are qualify for stedent discounts")
elif 20 <= age <= 54:
    print("you are qualify for no age discounts")
else:
    print("you can receive senior discounts")

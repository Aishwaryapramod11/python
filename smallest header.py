'''
author:Aishwarya
date:15-10-24
python file to find the smallest of three numbers
'''
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if num1<num2 and num1<num3:
    print(num1)
elif num2<num3:
    print(num2)
else:
    print(num3)
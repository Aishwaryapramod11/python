'''
author:Aishwarya
date:15-10-24
python program to check whether the given number is positive or not
'''
number=int(input("enter a number:"))
if number>0:
    print("the given number:",number,"is positive")
elif number<0:
    print("the given number:",number,"is negative")
else:
    print("the given number:",number,"is zero")
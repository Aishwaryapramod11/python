'''
 author:Aishwarya
date:15-10-24
python code to find the sum of digits of a given number
'''
num=int(input("enter your number"))
sum=0
while(num>0):
    r=num%10
    num=num//10
    sum=sum+r
print("sum of digits is:",sum)
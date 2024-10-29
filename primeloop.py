'''
author:Aishwarya
date:29-10-24
Python program to check prime number or not
'''
number=int(input("enter the number"))
isPrime=True
for i in range(2,number//2+1):
    if number % i ==0:
        isPrime = False
        break
if isPrime:
     print(f"the given number{number}is prime")
else:
     print(f"the given numbeer{number}is not prime")
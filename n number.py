'''
author:Aishwarya
date:29-10-24
Python program to print n prime numbers
'''
limit=int(input("enter the limit"))
for limit in range(2,limit+1):
    isPrime=True
    for i in range(2,(limit//2)+1):
      if limit% i==0:
        isPrime=False
      break
    if  isPrime:
        print(limit,end=" ")
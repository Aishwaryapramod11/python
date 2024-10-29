'''
author:Aishwarya
date:29-10-24
Python program to print multipi table
'''
number=int(input("enter your number"))
for i in  range(0,13):
        multipli=number*i
        print(f"{number}\t*\t{i}\t=\t{multipli}")
